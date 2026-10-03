# KITT Skills

> **KITT / 沿途**  
> **读懂沿途的世界**

KITT Skills 把 KITT 从 Android 外壳中抽出来，变成可被不同 AI / Agent 复用的开放 Agent Skill。

KITT 是内部代号；当前用户产品名是 **沿途**：

> **一个会读懂你正在经过的地方的 AI 副驾驶。**

KITT 的核心不是一个 App，而是一套“如何理解正在经过的地方、如何先取得可靠本地证据、何时值得开口、怎样自由讲述、用户提问时何时查证、何时保持安静”的 AI 能力。Android、PC、网页、车机或后台 Runtime 都只是宿主。

## 一句话给 AI 安装

把下面这句话直接交给具有 GitHub / 终端能力的 AI：

> 安装 https://github.com/shimao1115/KITT-SKILLS 的 KITT Skill。先读仓库的 INSTALL.md，识别你当前所在的 AI 工具，按对应 target 安装并验证。不要修改 KITT 以外的用户配置。

AI 应自行 clone / update 本仓库并执行安装器；不需要用户手工搬文件。

## 当前 Skill

当前版本：**0.2.0**

本次同步对应 KITT 主仓库当前 V0.3.1 规则，重点包括：

- 用户产品名由“路上读山河”更新为 **沿途**；
- 镇 / 乡 / 街道成为基本地方章节；
- 具体章节事实采用 **搜索 → Local Dossier → Director 自由讲述**；
- Local Dossier 是开放素材架，不是播放清单或作文提纲；
- 撤销固定“眼前切入→提问→解释→落回眼前”的旁白模板；
- 有可靠好材料的新章节通常应开口，而不是把 SILENT 当章节默认；
- 用户明确查找、实时问题或当地依据不足时走按需搜索；
- 后台研究 pending / failed 不得让整个 KITT 失声；
- 高显著性地标可以独立形成现场机会；
- 没有真实搜索/provenance 时，不得把模型记忆说成“查到的”。

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
- `references/RUNTIME.md`：持续位置、Local Dossier 和后台事件的最小 Runtime 契约。
- `install.py`：把 canonical Skill 安装到 Codex、Claude Code、OpenCode 或通用 Agent Skills 目录。
- `plugin.json`：开放 Agent Plugin / Skill 打包入口。

## 设计原则

**AI 是 KITT；App 只是壳。**

设备负责把现场、位置、图片、搜索工具和语音能力交给 KITT；KITT 负责理解、判断、查证需求与表达。

宿主没有某项能力时自然降级，不伪装拥有持续定位、后台运行、相机或实时搜索。

## 安装目标

`install.py` 支持：

- `codex` → `~/.codex/skills/kitt`
- `claude` → `~/.claude/skills/kitt`
- `opencode` → `~/.config/opencode/skills/kitt`
- `agents` → `~/.agents/skills/kitt`
- `auto` → 只安装到本机已存在的已知 Agent 根目录；若没有检测到，则回退到通用 `.agents`

详见 [INSTALL.md](INSTALL.md)。

## 与 Android KITT 的关系

Android 主仓库继续负责手机端 GPS、语音、界面、前台服务、章节解析和设备态 Runtime。

本仓库负责跨宿主的 KITT 核心能力。

```text
Android / PC / Web / Runtime
          ↓
      KITT Skill
          ↓
    任意兼容 AI 模型
```

设备负责“把现场交给 KITT”；KITT 负责“读懂沿途的世界”。
