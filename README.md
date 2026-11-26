# agent-skills

Owner's standard skill set for AI coding agents: 67 skills in 11 groups, an entry-point router, install profiles, and the rules that make agents follow them.

Start here:
- `USAGE.md`: concepts, profiles, install, how the AI should use skills, maintenance.
- `BOOTSTRAP.md`: block to paste into a new project's CLAUDE.md.
- `INDEX.md`: generated list of every skill by group with descriptions.
- `groups.json`: groups and install profiles (source of truth).
- `NOTICE.md`: source, pinned commit, license and local edits for every vendored skill.
- `scripts/install.py`, `scripts/build-index.py`: installer and index/consistency check (Python 3 standard library only).
- `skills/<name>/SKILL.md`: the skills (flat folders). `vendor-notes/`: upstream licenses.

Quick install:

    python3 -I scripts/install.py <project>/.claude/skills fullstack

Groups: meta, planning, build, review, testing, backend, data, frontend, security-release, seo-marketing, integrations.

## Own skills (written for this owner)

`skill-router`, `coordinator`, `resource-hygiene`, `spec-precedence`. Everything else is vendored (see NOTICE.md).

## Review status

- Read in full: bodies of the mattpocock skills used, `web-design-guidelines`, `composition-patterns`, `react-best-practices` (SKILL.md only), both motion skills, `dispatching-parallel-agents`, parts of `git-workflow-and-versioning`.
- Descriptions plus a grep for risky commands only (`curl | sh`, `eval`, `base64 -d`; none in skills): all the other vendored skills, including the marketing, data, security, CI/CD, NestJS, Kubernetes, Docker, Stripe and TypeScript skills. Read each body before relying on it for real work.
- Reference files (`references/`, `rules/`) were not read line by line.
- skills.sh audit flagged `triage` (Gen Agent Trust Hub "Med Risk", reason not shown). Read it before enabling.

## Overlaps (pick one when they disagree)

- ADRs: `domain-modeling` vs `documentation-and-adrs`.
- Interfaces: `codebase-design` vs `api-and-interface-design`.
- Trunk-based advice in `git-workflow-and-versioning` may clash with the project's branching; the project CLAUDE.md wins.
- Prisma skills target Prisma 7+; `neon-postgres` is written for Neon/Lakebase. Use only if the project uses them.

## Deliberately not vendored

- obra `subagent-driven-development`: tells the controller never to pause or ask, which conflicts with `coordinator` and `resource-hygiene`.
- `better-auth/skills`: the repo has no license file.
- Deprecated or version-migration skills (`prisma-upgrade-v7`, `prisma-postgres-upgrade`, `prisma-mongodb-upgrade`), `prisma-compute`, `prisma-driver-adapter-implementation`.
- Neon platform skills other than `neon-postgres` (`neon`, `neon-auth`, `neon-functions`, `neon-realtime`, `neon-ai-gateway`, `neon-object-storage`).
- ~40 other marketing skills (ads, sales, PR, social, SMS ...). Add from `coreyhaines31/marketingskills` if needed.
- `react-native-skills` (mobile is out of scope for now).
