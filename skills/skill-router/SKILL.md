---
name: skill-router
description: Choose and apply the right skills before starting any task. Use at the start of every session and whenever the task changes kind (plan, build, debug, review, backend, database, UI, security, release, SEO, multi-agent). Read INDEX.md or this map, then invoke the matching skills.
---

# Skill router

Skills are mandatory when they match. Do this before the first edit of every task.

## Procedure

1. **Classify the task** with the map below. A task can match several groups.
2. **Invoke** each matching skill with the Skill tool and follow it. Do not replace a skill with your own approach. If a skill says "ask the user", ask.
3. **Order matters:** planning -> build -> review -> release. Do not start building a non-trivial change before the planning skills ran or the user said to skip them.
4. **Skip honestly.** If no skill matches, say so in one line and proceed. If a skill is in the map but not installed in this project, say so; do not recreate it from memory.
5. **Precedence on conflict:** the user's current instruction > the project's CLAUDE.md/AGENTS.md > `spec-precedence` (customer documents over older decisions) > skill text > your defaults. A skill never overrides a safety rule or a destructive-action confirmation.
6. **Do not load everything.** Invoke only what the task needs; reference files inside a skill are read on demand.
7. **Note the skills used** in the final message (one line) so the owner can audit adoption.

## Map: task -> skills

| Task | Skills |
|---|---|
| Idea or plan is vague | `grilling` (or `grill-me`), then `to-spec` |
| Requirements or documents conflict | `spec-precedence`, then record an ADR with `documentation-and-adrs` / `domain-modeling` |
| Break a spec into work | `to-tickets`; first use in a repo: `setup-engineering-skills` |
| Look something up in primary sources | `research` |
| New feature or behavior change | `tdd`; module/interface shape: `codebase-design`, `api-and-interface-design` |
| Bug, failing test, slow code | `diagnosing-bugs`; performance: `performance-optimization` |
| Branching, commits, versions | `git-workflow-and-versioning` |
| Remove or migrate old code/APIs | `deprecation-and-migration` |
| TypeScript typing problems | `typescript-pro`, `typescript-advanced-types` |
| NestJS service | `nestjs-best-practices`, `nestjs-expert`, `architecture-patterns` |
| REST/GraphQL/OpenAPI | `api-and-interface-design`, `openapi-spec-generation` |
| Logging, metrics, tracing | `observability-and-instrumentation` |
| Postgres / schema / queries | `supabase-postgres-best-practices`; Neon: `neon-postgres`; Prisma: `prisma-orm-setup`, `prisma-client-api`, `prisma-cli` |
| Design or redesign an app screen | `ui-ux` |
| React / Next.js code | `vercel-react-best-practices`, `vercel-composition-patterns`; transitions: `vercel-react-view-transitions` |
| Review UI for guidelines | `web-design-guidelines`; accessibility: `accessibility-engineering` |
| Add a language (next-intl) | `next-intl-add-language` |
| Animation / motion | `motion-director`, audit with `web-motion-auditor` |
| Browser / E2E tests | `e2e-testing-patterns` |
| Auth, input handling, secrets | `security-and-hardening` |
| Pipelines, Docker, Kubernetes | `ci-cd-and-automation`, `multi-stage-dockerfile`, `kubernetes-specialist` |
| Release or launch readiness | `shipping-and-launch` |
| Review a branch / PR | `code-review`; PR text: `pr` |
| SEO audit, ranking, schema markup | `product-marketing` (context first), `seo-audit`, `schema`, `site-architecture`, `ai-seo`, `programmatic-seo`, `link-building` |
| Copy, conversion, analytics | `copywriting`, `copy-editing`, `cro`, `analytics`, `conversion-tracking`, `content-strategy`, `launch` |
| Payments with Stripe | `stripe-best-practices` |
| Several agents / waves | `coordinator`; independent parallel tasks: `dispatching-parallel-agents`; machine limits: `resource-hygiene` |
| Ending with work left | `handoff` |
| Writing or editing a skill / CLAUDE.md | `writing-for-agents` |

## Notes

- `grill-me`, `to-spec`, `handoff` and `triage` are user-invoked upstream (`disable-model-invocation`). If one is needed, tell the user which slash command to run.
- SEO and marketing skills expect a product-marketing context document. Run `product-marketing` first if none exists.
- Full list with descriptions: `INDEX.md`. Groups and install profiles: `groups.json`.
