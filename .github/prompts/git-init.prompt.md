---
description: "Перевірка репозиторію, оновлення .gitignore та вивід стану Git."
agent: build-engineer
---

# Command: git-init

## Дії
1. Перевірити наявність каталогу `.git`.
2. Створити або доповнити `.gitignore`, щоб він обов'язково містив записи: `.venv/`, `build/`, `__pycache__/`, антикеші `.pytest_cache/`.
3. Виконати перевірку `git status --short --ignored`.
