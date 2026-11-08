---

### 2. `docs/architecture.md`
```markdown
# Архітектура AI-агента автоматизації розробки та CI/CD

## 1. Задачі, які автоматизує агент
Агент `build-engineer` повністю автоматизує цикл розгортання проєкту:
- перевірку та оновлення `.gitignore` (ігнорування `.venv/`, терабайтів `build/`, кешів `__pycache__`);
- створення структури каталогу `src/` і `tests/` разом із точкою входу `src/main.py`;
- конфігурацію віртуального середовища `venv`, встановлення залежностей та налаштування юніт-тесту `pytest`;
- створення кросплатформних скриптів збірки `ci.sh` та `ci.bat`, які компілюють код у виконуваний файл `hello` (`build/hello` або `build/hello.exe`);
- генерацію конвеєра GitHub Actions (`.github/workflows/ci.yml`) з матрицею для трьох ОС (`ubuntu-latest`, `windows-latest`, `macos-latest`).

## 2. Перелік Skills
- **`project-scaffold`** (`.github/skills/project-scaffold/SKILL.md`): створення каркаса проєкту, початкового `.gitignore` та `src/main.py`.
- **`build-and-test`** (`.github/skills/build-and-test/SKILL.md`): створення бізнес-логіки (`src/calculator.py`), тесту `tests/test_basic.py` (`BasicAddition`), скриптів `ci.sh`/ří.bat.
- **`github-actions`** (`.github/skills/github-actions/SKILL.md`): генерація матричного YAML-файлу CI.

## 3. Перелік Commands (у `.github/prompts/`)
1. `git-init.prompt.md` — перевірка репозиторію та оновлення `.gitignore`.
2. `create-project.prompt.md` — виклик skill `project-scaffold`.
3. `create-build.prompt.md` — виклик skill `build-and-test`.
4. `create-actions.prompt.md` — виклик skill `github-actions`.
5. `check.prompt.md` — неруйнівна валідація структури, збірки та тестів.
6. `init.prompt.md` — оркестратор, що послідовно запускає команди 1–5.

## 4. Таблиця передачі артефактів між етапами
| Послідовність | Команда | Викликаний Skill | Вхідні передумови | Вихідні файли / Артефакти |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/git-init` | — | Ініціалізований Git | Оновлений `.gitignore` |
| 2 | `/create-project` | `project-scaffold` | `.gitignore` | Каталоги `src/`, `tests/`, `src/main.py` |
| 3 | `/create-build` | `build-and-test` | `src/main.py` | `src/calculator.py`, `tests/test_basic.py`, `ci.sh`, `ci.bat` |
| 4 | `/create-actions` | `github-actions` | Скрипти збірки | `.github/workflows/ci.yml` |
| 5 | `/check` | — | Усі файли проєкту | Звіт перевірки статусів `[PASS]` / `[FAIL]` |
| 6 | `/init` | Усі через commands | Чистий репозиторій | Повністю згенерований та перевірений проєкт |

## 5. Політика зупинки оркестратора (Fail-Fast)
Оркестратор (`/init`) виконує команди чітко по черзі. Після кожної команди перевіряється код повернення (`exit code`). Якщо стається збій або очікуваний файл не створено, оркестратор **миттєво зупиняє виконання**, не переходить до наступних кроків і виводить діагностику помилки.