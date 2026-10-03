# KITT Skills

> **路上读山河 · 会读山河的 AI 副驾驶**

KITT Skills 把 KITT 从 Android 外壳中抽出来，变成可被不同 AI/Agent 复用的开放 Agent Skill。

KITT 的核心不是一个 App，而是一套“在路上如何理解现场、何时开口、讲什么、怎样查证、何时保持安静、怎样接住用户”的 AI 能力。Android、PC、网页、车机或后台 Runtime 都只是它的宿主。

## 一句话给 AI 安装

把下面这句话直接交给具有 GitHub/终端能力的 AI：

> 安装 https://github.com/shimao1115/KITT-SKILLS 的 KITT Skill。先读仓库的 INSTALL.md，识别你当前所在的 AI 工具，按对应 target 安装并验证。不要修改 KITT 以外的用户配置。

AI 应自行 clone/update 本仓库并执行安装器；不需要用户手工搬文件。

## 仓库结构

```text
KITT-SKILLS/
├── plugin.json
├── install.py
├── INSTALL.md
└── skills/
    └── kitt/
        ├── SKILL.md
        └── references/
            └── RUNTIME.md
```

- `skills/kitt/SKILL.md`：KITT 的唯一行为真相源。
- `references/RUNTIME.md`：需要后台/位置流时才使用的最小 Runtime 契约。
- `install.py`：把 canonical Skill 安装到 Codex、Claude Code、OpenCode 或通用 Agent Skills 目录。
- `plugin.json`：开放 Agent Plugin/Skill 打包入口。

## 设计原则

**AI 是 KITT；App 只是壳。**

KITT 继承原 Android 项目的核心体验：

> **自动时，它读山河；你开口时，它听你的。**

它不是导航、旅游攻略或百科全书。它首先判断“此刻值不值得打破安静”，只挑一件最值得理解的事讲清楚。用户主动说话时，用户意图立即取得最高优先级。

宿主若提供位置、图片、联网搜索、语音输入/TTS，KITT 使用它们；没有某项能力时就自然降级，不伪装自己拥有持续定位、后台运行或实时信息。

## 安装目标

`install.py` 当前支持：

- `codex` → `~/.codex/skills/kitt`
- `claude` → `~/.claude/skills/kitt`
- `opencode` → `~/.config/opencode/skills/kitt`
- `agents` → `~/.agents/skills/kitt`
- `auto` → 只安装到本机已存在的已知 Agent 根目录；若没有检测到，则回退到通用 `.agents`

详见 [INSTALL.md](INSTALL.md)。

## 与 Android KITT 的关系

原 Android 仓库继续负责手机端 GPS、语音、界面、前台服务等设备能力。

本仓库负责跨宿主的 KITT 核心能力。

未来推荐关系：

```text
Android / PC / Web / Runtime
          ↓
      KITT Skill
          ↓
    任意兼容 AI 模型
```

两者不需要互相复制业务逻辑。设备负责“把现场交给 KITT”，KITT 负责理解、判断与表达。
