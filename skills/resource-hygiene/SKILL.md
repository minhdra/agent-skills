---
name: resource-hygiene
description: Keep a low-resource dev machine healthy. Use before and after any docker build/compose, test run (jest, vitest, tsc), worktree creation, dev server, or when launching several agents in parallel.
---

# Resource hygiene

The owner's machine has limited RAM (17 GB) and nearly full disk. Clean up after every task, before reporting done. Adjust the numbers below if the project's own docs say otherwise.

## Docker

- After `docker build` / `docker compose build`: `docker builder prune -f --filter until=24h` and `docker image prune -f`.
- NEVER run `docker volume prune`, `docker system prune --volumes`, or `docker image prune -a`. Volumes hold real database data; removed images must be pulled again.
- Containers started for testing: stop them with `docker compose down` (never `-v`) when finished. Do not leave them running in the background.

## Processes and worktrees

- Remove temporary worktrees (`git worktree remove`) when the work is done.
- Leave no background process behind: dev servers, watchers, `jest --watch`, `vitest --watch`.

## Load limits for tests and builds

- jest: `--maxWorkers=2`. vitest: `--pool=forks --poolOptions.forks.maxForks=2`.
- Never run jest, vitest and tsc in parallel. Run them one after another.
- Before launching several agents in parallel, check memory pressure. If swap use is above 6 GB, wait or run sequentially.
- At most 2 agents may run tests or builds at the same time.
