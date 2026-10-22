# Набор для GitHub

Папка содержит готовый корень репозитория V.DAILY для контрольного отчёта по архитектуре. Исходный код включён целиком, чтобы схемы можно было сверить с реализацией и запустить тесты.

## Что включено

| Путь | Зачем нужен |
|---|---|
| app/ | Реальные модули, Mini App, API и предметная модель |
| tests/ | Модульные и интеграционные проверки |
| tools/ | Запуск проверки и мониторинг |
| docs/ARCHITECTURE.md | Главный документ с архитектурными схемами |
| docs/DECISIONS.md | Обоснование решений и ограничения |
| docs/API.md | Контракты интерфейса сервера |
| docs/IMPLEMENTATION_RTM.md | Трассировка требований к коду и тестам |
| docs/requirements/ | Реестр согласованных версий PRD, SRS, User Stories и RTM. Сами PDF по прежним путям недоступны и в архив не включены |
| docs/presentation/ | Презентация и текст выступления |
| verification/ | Фактический результат локального запуска тестов |
| .github/workflows/tests.yml | Конфигурация тестов при push / pull request |
| README.md | Навигация по архитектуре и запуск |
| .gitignore, .env.example | Исключения и безопасный шаблон настроек |
| requirements*.txt, demo.py, start_demo.ps1, Caddyfile.example | Воспроизведение приложения и пример окружения |

## Что исключено

Настоящий .env, токены, личная база SQLite и WAL, аудиофайлы, кэш Python, временные скриншоты, старые версии сборок, весь рабочий каталог Codex и локальные настройки редактора. .env.example содержит только пустые значения и примеры.

## Порядок публикации

URL репозитория не задан, поэтому remote и push в этой поставке не выполнялись. Если репозиторий уже существует, скопируйте содержимое этой папки в его рабочую копию. При совпадении существующих файлов сначала просмотрите различия, не перезаписывайте чужие изменения вслепую.

Из корня нужной рабочей копии:

```bash
git status --short
git add app tests tools docs verification .github README.md GITHUB_PUSH.md .gitignore .env.example requirements.txt requirements-live.txt demo.py start_demo.ps1 Caddyfile.example
git diff --cached --stat
git diff --cached --check
git commit -m "Document V.DAILY architecture and add implementation evidence"
git push
```

`git push` предполагает уже настроенную upstream-ветку. Если её нет, используйте фактические remote и ветку вашего репозитория. Не подставляйте случайный URL.

GitHub Actions запустится после публикации. Его успешный результат пока не заявлен: локально выполнен Python unittest, а CI-конфигурация подготовлена.

Для проверки преподавателем начните с README и docs/ARCHITECTURE.md, затем покажите docs/DECISIONS.md, исходный код и результат тестов.
