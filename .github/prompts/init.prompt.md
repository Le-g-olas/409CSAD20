---
description: "Оркестратор: послідовний запуск git-init, create-project, create-build, create-actions та check."
agent: build-engineer
---

# Command: init (Orchestrator)

## Дії
Послідовно виконати команди за протоколом Fail-Fast:
1. `/git-init`
2. `/create-project`
3. `/create-build`
4. `/create-actions`
5. `/check`

У разі помилки на будь-якому кроці — зупинити процес та повідомити причину.
