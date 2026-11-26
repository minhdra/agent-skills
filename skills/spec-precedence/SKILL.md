---
name: spec-precedence
description: Resolve conflicts between customer documents (SRS, URD, contracts) and earlier decisions (ADRs, chat answers, plan notes). Use when two sources disagree about behavior, scope, limits or wording.
---

# Spec precedence

Order of authority, highest first:

1. Customer-signed documents (URD, SRS, contract), newest version first.
2. ADRs and design docs.
3. Decisions made in chat or in earlier sessions.

When a lower source conflicts with a higher one, follow the higher one. Earlier decisions may have drifted from the intended design.

## How to apply

- Do not ask the owner to arbitrate each conflict. Resolve it to the document wording, then record the change as an ADR addendum (what changed, which document section decided it, date).
- List conflicts in one place (for example `docs/design/srs-gap/`) so they stay reviewable.
- Quote the document section you followed.

## Still needs an explicit go from the owner

- Legal or biometric items (for example face recognition on minors).
- Anything that needs a new paid provider or recurring cost (SMS, third-party APIs).
- Anything the owner explicitly deferred earlier (for example import/export features).
- Anything the documents mark as out of scope (another team's work, such as a mobile app or marketing site).
