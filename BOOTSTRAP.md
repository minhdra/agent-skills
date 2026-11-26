# Bootstrap: make an AI agent follow these skills in a new project

Skills are only suggestions until the project instructs the agent to use them. After installing (see README), paste the block below into the new project's `CLAUDE.md` (or `AGENTS.md`).

```markdown
## Agent skills (mandatory)

Skills are in `.claude/skills/` (installed from the owner's agent-skills repo; the pinned commit and installed groups are in `.claude/skills/.source`).

1. At the start of every task, invoke the `skill-router` skill and follow its procedure and task map. Invoke every skill it says matches, with the Skill tool, and follow it instead of improvising.
2. Plan before building: for a non-trivial change run the planning skills first (`grilling` -> `to-spec` -> `to-tickets`), unless the user says to skip.
3. Precedence on conflict: the user's current instruction > this file > `spec-precedence` (customer documents over older decisions) > skill text.
4. Never edit `.claude/skills/`. Change skills in the agent-skills repo and reinstall.
5. First use in a repo: run `setup-engineering-skills` once.
6. In the final message of a task, list the skills used in one line.
```

Why this works: a skill description only makes the model likely to call it. This block, loaded every session, makes calling `skill-router` a rule, and the router then points to everything else. For hard enforcement of one specific rule (for example blocking `git push`), use a hook in `.claude/settings.json`; prose cannot enforce it.
