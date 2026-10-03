# KITT-SKILLS maintenance contract

This repository is the portable KITT capability package. Keep it small.

## Canonical source

`skills/kitt/SKILL.md` is the single canonical KITT behavior definition.

Do not commit duplicated copies under `.codex/`, `.claude/`, `.opencode/`, or `.agents/`. The installer creates those copies on a user's machine.

## Product boundary

KITT is the AI capability. Android, desktop apps, web pages, TTS/STT, GPS collectors and background services are hosts.

Do not move Android implementation details into the Skill unless they express a host-independent product principle.

Background execution belongs behind the thin contract in `skills/kitt/references/RUNTIME.md`. Do not add a server, queue, database, event bus, multi-agent graph or schema family merely because it might be useful later.

## Compatibility

Keep the core Skill compatible with the open `SKILL.md` pattern:

- lowercase kebab-case `name`;
- concrete `description` that tells a model when to load KITT;
- provider-neutral instructions;
- optional host capabilities must degrade gracefully;
- references use paths relative to the skill directory.

When behavior changes materially, update both the Skill metadata version and `plugin.json` version.

## Installation

`install.py` may only replace the exact `.../skills/kitt` destination. Never broaden deletion or configuration mutation.

New host support should normally be one additional target path, not a new Skill fork.

## Design test

Before adding structure, ask:

> If this is removed, what does the KITT user actually lose?

Prefer: do nothing → use AI capability → reuse host capability → simplify → minimal implementation.
