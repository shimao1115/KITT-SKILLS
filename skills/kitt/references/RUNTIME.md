# KITT Runtime Contract

Only read this file when KITT is hosted by a process that can repeatedly provide live context, or when the user explicitly asks to build/run KITT in the background.

This is intentionally a **thin contract**, not a server architecture.

## 1. Boundary

The Skill itself cannot remain alive in the background.

A host/runtime is responsible for:

- receiving GPS or other location updates;
- receiving optional photos or user speech/text;
- deciding when there is enough new information to wake the model;
- executing timers such as quiet mode;
- playing TTS / collecting STT when available;
- persisting only the minimal session state the product actually needs.

KITT is responsible for:

- understanding the current scene;
- deciding whether to speak;
- selecting the topic;
- deciding whether verification is needed;
- explaining;
- responding to the user;
- asking one useful question when asking is better than guessing.

Do not build a large workflow engine merely to host this Skill.

## 2. Minimal Context Card

Raw sensor streams should be compressed before reaching KITT.

Use natural-language fields and omit unavailable ones:

```text
【旅程意图】
目的地/大致方向：
本次旅程临时偏好：

【当前位置】
最近已知位置：
区域/道路：
方向：
速度：
海拔：
近期变化趋势：

【附近/前方可靠线索】
...

【最近讲过】
- ...

【当前交互状态】
距上次自动旁白：
刚才是否被跳过：
是否安静：
是否刚结束主动对话：

【用户刚刚说】
...
```

Do not require every field.

Destination is an intention, not a claimed navigation route.

## 3. Four actions

When the host explicitly requests structured Runtime output, return exactly one current action:

```json
{
  "action": "SILENT | SPEAK_NOW | PREPARE | ASK_USER",
  "topic": "",
  "narration": "",
  "question": "",
  "prepare_hint": "",
  "memory_update": ""
}
```

### SILENT

Nothing is currently worth interrupting the quiet for.

### SPEAK_NOW

Speak now.

- `topic`: the single cognitive topic.
- `narration`: complete spoken text.
- `memory_update`: a very short “already covered” summary.

### PREPARE

A small number of time-sensitive upcoming subjects may deserve advance verification or organization, but should not be spoken yet.

Rules:

- at most one PREPARE at a time;
- bind it to a clear scene/target;
- `prepare_hint` describes what to re-check, not a precise countdown;
- when the scene changes, re-evaluate with fresh context;
- if passed, deviated from, invalidated by new user intent, or crossed during quiet mode, discard it;
- never replay stale “you just passed...” content because it was previously prepared.

PREPARE is a one-time scene reservation, not a speech cache.

### ASK_USER

Ask one short question because asking is materially better than guessing.

- `question` should be natural and worth answering.
- If the user does not answer, abandon it.
- Do not repeatedly prompt.

## 4. Wake-up semantics

Sensors may run frequently; the model should not.

Reasonable wake-up events include:

- materially changed location/road/environment summary;
- enough elapsed distance/time after a prior narration;
- a PREPARE target may be approaching;
- the user speaks;
- the user ends quiet mode;
- the user changes destination or session preference;
- a new photo arrives.

These are reasons to **check**, not rules that force speech.

No new information → no model call is usually the right behavior.

## 5. Priority

Highest to lowest:

1. latest explicit user action or speech;
2. explicit quiet mode;
3. active user conversation;
4. brief post-conversation breathing room;
5. a one-shot ASK_USER response window;
6. mature SPEAK_NOW / PREPARE;
7. SILENT.

Do not maintain a narration queue.

At most keep:

- what is currently being handled/spoken;
- one not-yet-mature PREPARE.

## 6. Failure semantics

Automatic model/search failure should normally degrade to **SILENT**.

Do not turn connection failures into driving events or retry storms.

For an active user request, briefly say the request could not be completed. One inexpensive retry is acceptable for an obviously transient failure.

## 7. Minimal persistent state

A Runtime may keep:

- journey intent;
- short Session Instructions;
- recent topics;
- one PREPARE;
- quiet state/timer;
- a compact recent movement summary.

Do not require:

- full GPS history;
- full transcript;
- raw recordings;
- vector database;
- RAG;
- multi-agent orchestration;
- a backend server unless the actual host requires one.

The design rule is:

> **Trust the AI capability; verify the outcome. Add deterministic machinery only where reality requires it.**
