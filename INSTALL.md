# Install KITT Skill

This file is written for both humans and AI agents.

## Agent installation contract

If the user asks you to install KITT from this repository:

1. Identify the AI host you are currently operating in when possible.
2. Obtain this repository with Git or an equivalent GitHub tool.
3. Run the repository installer with an explicit target when the host is known.
4. Verify that the installed directory contains `SKILL.md`.
5. Do not modify unrelated user configuration, global prompts, MCP settings, model settings, or other skills.
6. Report the destination that was installed.
7. If the host caches skills, tell the user only that a reload/restart may be needed; do not invent extra setup.

Canonical repository:

```text
https://github.com/shimao1115/KITT-SKILLS
```

## Supported targets

| Target | Destination |
|---|---|
| Codex | `~/.codex/skills/kitt` |
| Claude Code | `~/.claude/skills/kitt` |
| OpenCode | `~/.config/opencode/skills/kitt` |
| Generic Agent Skills host | `~/.agents/skills/kitt` |

The repository contains only one canonical copy at `skills/kitt/`. Native host directories are installation destinations, not additional sources of truth.

## Recommended command

From a cloned checkout:

```bash
python install.py --target codex
python install.py --target claude
python install.py --target opencode
python install.py --target agents
```

If the current host is genuinely unknown:

```bash
python install.py --target auto
```

Use `--dry-run` before installation when you need to inspect the selected destination:

```bash
python install.py --target auto --dry-run
```

`--target all` is intentionally available but should not be the default. Installing the same skill into multiple global compatibility directories can make some hosts discover duplicate IDs.

## Fresh install from GitHub

An AI with terminal access may perform the equivalent of:

```bash
git clone --depth 1 https://github.com/shimao1115/KITT-SKILLS.git
cd KITT-SKILLS
python install.py --target <current-host>
```

On Windows, `py install.py ...` is also acceptable when `python` is not on PATH.

If a checkout already exists, update it rather than creating repeated copies:

```bash
git pull --ff-only
python install.py --target <current-host>
```

## Without Python

If Python is unavailable, copy the complete directory:

```text
skills/kitt/
```

to the current host's destination from the table above. Preserve `SKILL.md` and its `references/` directory together.

Do not copy only fragments from `SKILL.md` into a global prompt. KITT is intended to remain an independently versioned Skill.

## Verification

A successful installation has this shape:

```text
<host skill root>/
└── kitt/
    ├── SKILL.md
    └── references/
        └── RUNTIME.md
```

Then ask the host to list or load the `kitt` skill. A useful smoke test is:

> KITT，我现在在路上。先告诉我你需要哪些现场信息；没有必要的信息就不要瞎猜。

A correct KITT should adapt to the host's available capabilities instead of pretending it already has GPS, continuous background execution, camera access, or live web access.
