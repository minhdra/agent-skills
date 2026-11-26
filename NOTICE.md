# NOTICE: third-party material

Skills below were copied from public repositories on 2026-11-26. Each keeps its upstream license. Local edits are listed.

| Skills | Source | Commit | License | Local edits |
|---|---|---|---|---|
| tdd, diagnosing-bugs, code-review, domain-modeling, research, pr, to-spec, to-tickets, triage, codebase-design, handoff, grill-me, grilling, writing-for-agents | https://github.com/mattpocock/skills (c) 2026 Matt Pocock | 6f7f7831a625f040a8e06a0e7954826b87ce775a | MIT (vendor-notes/LICENSE.mattpocock-skills) | none |
| setup-engineering-skills | same repo, skill `setup-matt-pocock-skills` | same | MIT | renamed; the name was replaced in the files that referenced it |
| vercel-react-best-practices, vercel-composition-patterns, web-design-guidelines, vercel-react-view-transitions | https://github.com/vercel-labs/agent-skills | 5a37a6329fbad3666c3207392a6a7c0110e92efb | MIT (declared in the upstream README; the repo has no LICENSE file) | directories renamed to match the skill name; no content edits |
| web-motion-auditor, motion-director | https://github.com/frankxai/awesome-motion-design-agent-skills | e7dc6e2e728c918ffcea5edb2d7c94e2a6f7785d | CC0-1.0 (vendor-notes/LICENSE.frankxai-motion) | none |

| ui-ux | https://github.com/evondev/evondevKit (c) 2026 Tuấn Trần | 5a892ceac93d1bb286391663eb01cbd011706886 | MIT (vendor-notes/LICENSE.evondevkit) | none; version 0.9.3 (scripts/check-update.mjs fetches the upstream version from GitHub when run) |
| security-and-hardening, ci-cd-and-automation, git-workflow-and-versioning, documentation-and-adrs, api-and-interface-design, deprecation-and-migration, accessibility-engineering, observability-and-instrumentation, performance-optimization, shipping-and-launch | https://github.com/addyosmani/agent-skills (c) 2025 Addy Osmani | e997ac5b9a74eab332d5e9793bb38a38c8cfdd74 | MIT (vendor-notes/LICENSE.addyosmani-agent-skills) | none; upstream hooks/ not vendored |
| architecture-patterns, e2e-testing-patterns, openapi-spec-generation | https://github.com/wshobson/agents (c) 2024 Seth Hobson, from plugins/*/skills | c96b5f6552dba32e4492307493ee613581430715 | MIT (vendor-notes/LICENSE.wshobson-agents) | none |
| nestjs-best-practices | https://github.com/kadajett/agent-nestjs-skills | 3986e0cede33958e000f959031cbee0cd83c2941 | MIT (declared in the skill frontmatter; repo has no LICENSE file) | none |
| nestjs-expert | https://github.com/jeffallan/claude-skills, plugin/skills | d98d06edb54c25cfb94017c0ef830342a34a43ba | MIT (vendor-notes/LICENSE.jeffallan-claude-skills) | none |
| dispatching-parallel-agents | https://github.com/obra/superpowers (c) 2025 Jesse Vincent | 22f0b463e7a5e579904dd6211a520321035526f7 | MIT (vendor-notes/LICENSE.obra-superpowers) | none |
| product-marketing, seo-audit, ai-seo, programmatic-seo, schema, site-architecture, link-building, content-strategy, copywriting, copy-editing, cro, analytics, conversion-tracking, launch | https://github.com/coreyhaines31/marketingskills (c) 2025 Corey Haines | 8fd2fcade2fd6629026e9dfe6d133b55b36968b9 | MIT (vendor-notes/LICENSE.coreyhaines31-marketingskills) | none |
| prisma-orm-setup, prisma-client-api, prisma-cli | https://github.com/prisma/skills (c) 2025 Prisma | b4bebffd0d0c3499c3d342f69380886a28e28880 | MIT (vendor-notes/LICENSE.prisma-skills) | none |
| neon-postgres | https://github.com/neondatabase/agent-skills | d3601d9e1f9398b96a1ee25047bafba5f04199eb | Apache-2.0 (vendor-notes/LICENSE.neon-agent-skills) | none |
| supabase-postgres-best-practices | https://github.com/supabase/agent-skills (c) 2026 Supabase | c9be0e931b7930f7d02126d04774d904c381e7d7 | MIT (vendor-notes/LICENSE.supabase-agent-skills) | none |
| multi-stage-dockerfile, next-intl-add-language | https://github.com/github/awesome-copilot (c) GitHub, Inc. | 93fc8b9ee3ef56b9b5e7261e6ce92d314cb2c1cf | MIT (vendor-notes/LICENSE.github-awesome-copilot) | none |
| kubernetes-specialist, typescript-pro | https://github.com/jeffallan/claude-skills, plugin/skills | d98d06edb54c25cfb94017c0ef830342a34a43ba | MIT (vendor-notes/LICENSE.jeffallan-claude-skills) | none |
| typescript-advanced-types | https://github.com/wshobson/agents, plugins/*/skills | c96b5f6552dba32e4492307493ee613581430715 | MIT (vendor-notes/LICENSE.wshobson-agents) | none |
| stripe-best-practices | https://github.com/stripe/ai, skills/ (c) 2024-2025 Stripe | d4b19a989bf12bdbd4d42de1f9bfd3aec56fd9da | MIT (vendor-notes/LICENSE.stripe-ai) | none |

Credits carried by upstream files:
- `pr` is based on the `show-me` skill by Dex Horthy (Humanlayer); see `skills/pr/CREDITS.md`.
- `web-design-guidelines` bundles a rules snapshot pinned to vercel-labs/web-interface-guidelines commit 434b7f91364665f2f733b310ec54809bf8f37937.

Original skills (owner's own): `skill-router`, `resource-hygiene`, `spec-precedence`, `coordinator`.

Security note: skills.sh /audits (checked 2026-11-26) lists mattpocock/skills `triage` as Gen Agent Trust Hub "Med Risk". Reason not shown on the page. Read `skills/triage` before enabling it.

To update a vendored skill: diff against the upstream commit above, read the new body, then bump the commit here.

Not vendored because no license was found: better-auth/skills (commit 20c9e88a5c007461a703f1c213572b073196113e).
