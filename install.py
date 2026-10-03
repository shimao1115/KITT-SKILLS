#!/usr/bin/env python3
"""Install the canonical KITT Agent Skill into a supported agent home."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SKILL_NAME = "kitt"

TARGETS = {
    "codex": Path.home() / ".codex" / "skills" / SKILL_NAME,
    "claude": Path.home() / ".claude" / "skills" / SKILL_NAME,
    "opencode": Path.home() / ".config" / "opencode" / "skills" / SKILL_NAME,
    "agents": Path.home() / ".agents" / "skills" / SKILL_NAME,
}

DETECT_ROOTS = {
    "codex": Path.home() / ".codex",
    "claude": Path.home() / ".claude",
    "opencode": Path.home() / ".config" / "opencode",
}


def source_dir() -> Path:
    source = Path(__file__).resolve().parent / "skills" / SKILL_NAME
    manifest = source / "SKILL.md"
    if not manifest.is_file():
        raise SystemExit(f"KITT source skill not found: {manifest}")
    return source


def auto_targets() -> list[str]:
    detected = [name for name, root in DETECT_ROOTS.items() if root.exists()]
    return detected or ["agents"]


def validate_destination(destination: Path) -> None:
    # We only ever replace an exact .../skills/kitt directory.
    if destination.name != SKILL_NAME or destination.parent.name != "skills":
        raise SystemExit(f"Refusing unsafe destination: {destination}")


def install_one(source: Path, target_name: str, dry_run: bool) -> None:
    destination = TARGETS[target_name]
    validate_destination(destination)

    print(f"{target_name}: {source} -> {destination}")
    if dry_run:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

    installed_manifest = destination / "SKILL.md"
    if not installed_manifest.is_file():
        raise SystemExit(f"Install verification failed: {installed_manifest}")
    print(f"  verified: {installed_manifest}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install KITT as an Agent Skill for Codex, Claude Code, OpenCode, or a generic Agent Skills host."
    )
    parser.add_argument(
        "--target",
        choices=["auto", "codex", "claude", "opencode", "agents", "all"],
        default="auto",
        help="Installation target. Default: auto.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show destinations without modifying files.",
    )
    args = parser.parse_args()

    source = source_dir()
    if args.target == "auto":
        names = auto_targets()
    elif args.target == "all":
        names = list(TARGETS)
    else:
        names = [args.target]

    names = list(dict.fromkeys(names))

    for name in names:
        install_one(source, name, args.dry_run)

    if not args.dry_run:
        print("\nKITT installed. Restart or reload the host agent if it does not refresh skills automatically.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
