# How to use agent-skills

## 1. Concepts

- A skill is a folder with `SKILL.md`. Only its `name` and `description` are loaded at session start (about 22,000 characters for all 67 skills). The body loads when the agent invokes the skill, so install only the groups a project needs.
- Skills are organised in 11 groups (`groups.json`, human view in `INDEX.md`). Install profiles are sets of groups.
- `skill-router` is the entry point. The project's CLAUDE.md tells the agent to call it first (BOOTSTRAP.md). It maps task types to skills.

## 2. Pick a profile

| Profile | Groups | Skills | Use for |
|---|---|---|---|
| `core` | meta, planning, build, review, testing, security-release | 32 | any project |
| `backend-stack` | core + backend + data | 43 | APIs, NestJS, Postgres |
| `frontend-stack` | core + frontend | 41 | web UI, React/Next.js |
| `fullstack` | backend-stack + frontend-stack | 52 | most product work |
| `seo-only` | seo-marketing | 14 | add on top, for sites that need search traffic |
| `everything` | all groups | 67 | rarely; costs more startup context |

You can also pass group names, for example `meta planning review`. `integrations` (Stripe) is opt-in and only in `everything`; add it by name.

## 3. Install

    python3 -I <path-to-agent-skills>/scripts/install.py <project>/.claude/skills fullstack seo-only

- Copies only; never deletes. Existing skill folders are skipped unless `--force` is given.
- Writes `.claude/skills/.source` (repo commit and groups).
- Then paste the BOOTSTRAP.md block into the project's CLAUDE.md.
- Keep `.claude/skills/` committed in the project so every agent and teammate sees the same skills.

## 4. How the AI should work with them

1. Call `skill-router` first; classify the task; invoke matching skills in order planning -> build -> review -> release.
2. Follow the skill. If the skill says to ask the user or to stop, do that.
3. If no skill matches, say so in one line and proceed.
4. Conflicts: user instruction > project CLAUDE.md > `spec-precedence` > skill text > defaults.
5. Report the skills used in the final message.

Slash-only skills: `grill-me`, `to-spec`, `handoff`, `triage` are user-invoked upstream. The agent should tell the user to run the command rather than invoke them itself.

## 5. Typical flows

- New feature: `grilling` -> `to-spec` -> `to-tickets` -> `tdd` (+ `codebase-design`, stack skills) -> `code-review` -> `pr`.
- Bug: `diagnosing-bugs` -> `tdd` for the regression test -> `code-review`.
- New screen: `ui-ux` -> `vercel-react-best-practices` / `vercel-composition-patterns` -> `accessibility-engineering` -> `web-design-guidelines`.
- Release: `security-and-hardening` -> `ci-cd-and-automation` -> `shipping-and-launch`.
- SEO: `product-marketing` (context doc) -> `seo-audit` -> `schema` / `site-architecture` -> `copywriting` / `cro`.
- Many agents: `coordinator` (+ `dispatching-parallel-agents`, `resource-hygiene`).

## 6. Maintaining the repo

- Add a skill: create `skills/<name>/SKILL.md` (frontmatter `name` equals the folder name, a description that says when to use it), add the name to one group in `groups.json`, add the task to the map in `skills/skill-router/SKILL.md`, then run `python3 -I scripts/build-index.py` (it fails on unknown, duplicate or missing skills and regenerates `INDEX.md`).
- Vendored skills: do not edit them in place without listing the edit in `NOTICE.md`. To update, diff against the pinned upstream commit, read the new body, then bump the commit in `NOTICE.md`.
- Third-party skills are instructions an agent will execute. Read the body and check the license (no LICENSE means do not vendor) before adding.
- Disable a skill for one project by deleting its folder from that project's `.claude/skills/`; do not delete it here.

## 7. Known limits

- Matching is by description. If an agent skips a skill, tighten the description or add the task to the router map.
- Only hooks enforce rules. Prose does not.
- Not covered yet: pnpm/monorepo workflows, queues (BullMQ/Kafka), mobile, GitLab MR specifics, Docker for local dev (this owner develops without Docker on a weak machine).
