#!/usr/bin/env python3
"""Copy skills for chosen profiles/groups into a project's .claude/skills.

Usage: python3 -I scripts/install.py <skills-dir> <profile-or-group> [...]
Example: python3 -I scripts/install.py ~/code/app/.claude/skills backend frontend

Never deletes anything. An existing skill folder is skipped unless --force is
given, in which case only that skill folder's files are overwritten.
Writes <skills-dir>/.source with the repo commit (if git is available).
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def expand(cfg, name, seen=()):
    if name in cfg["groups"]:
        return [name]
    if name in cfg["profiles"]:
        if name in seen:
            raise SystemExit(f"profile loop at {name}")
        out = []
        for part in cfg["profiles"][name]:
            out += expand(cfg, part, seen + (name,))
        return out
    raise SystemExit(f"unknown profile or group: {name}\n"
                     f"profiles: {', '.join(cfg['profiles'])}\ngroups: {', '.join(cfg['groups'])}")


def main(argv):
    force = "--force" in argv
    args = [a for a in argv if a != "--force"]
    if len(args) < 2:
        print(__doc__)
        return 2
    cfg = json.loads((ROOT / "groups.json").read_text(encoding="utf-8"))
    target = Path(args[0]).expanduser()
    groups = []
    for name in args[1:]:
        for g in expand(cfg, name):
            if g not in groups:
                groups.append(g)
    skills = []
    for g in groups:
        for s in cfg["groups"][g]["skills"]:
            if s not in skills:
                skills.append(s)
    target.mkdir(parents=True, exist_ok=True)
    copied, skipped = [], []
    for s in skills:
        src, dst = ROOT / "skills" / s, target / s
        if dst.exists() and not force:
            skipped.append(s)
            continue
        shutil.copytree(src, dst, dirs_exist_ok=True)
        copied.append(s)
    try:
        sha = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        sha = "unknown (agent-skills is not a git repo yet)"
    (target / ".source").write_text(f"agent-skills {sha}\ngroups: {' '.join(groups)}\n", encoding="utf-8")
    print(f"groups: {', '.join(groups)}")
    print(f"copied {len(copied)}, skipped {len(skipped)} existing (use --force to overwrite)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
