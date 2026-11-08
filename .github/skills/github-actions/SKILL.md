# Skill: github-actions

## Призначення
Генерація конвеєра безперервної інтеграції GitHub Actions (`.github/workflows/ci.yml`) із матрицею для трьох операційних систем.

## Коли застосовувати
Після створення скриптів збірки за командою `/create-actions`.

## Вхідні дані
- Наявність скриптів `ci.sh` та `ci.bat`

## Очікувані результати (Виходи)
1. Файл конвеєра `.github/workflows/ci.yml`, який:
   - спрацьовує на `push` і `pull_request` для гілок `master` та `develop`;
   - містить одну `job` із матрицею `os: [ubuntu-latest, windows-latest, macos-latest]`;
   - викликає виключно `ci.sh` на Linux/macOS та `ci.bat` на Windows;
   - зберігає зібраний виконуваний файл як артефакт за допомогою `actions/upload-artifact@v4`.

## Перевірка результату
- Файл `.github/workflows/ci.yml` валідний за синтаксисом YAML і містить усі три обов'язкові платформи.