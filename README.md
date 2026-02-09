Мне не хватало Conventional Commits с сообщениями на русском языке,
поэтому я сделал вот это.

Сделано для [Commitizen на Python](https://github.com/commitizen-tools/commitizen).
Не путать с [версией на JavaScript](https://github.com/commitizen/cz-cli),
которая более популярна, но требует наличие `package.json`. Подробнее о различиях
[здесь](https://commitizen-tools.github.io/commitizen/faq/#is-this-project-affiliated-with-the-commitizen-js-project).

Установить можно так:
```bash
pip install commitizen cz-ru
```

О том как пользоваться можно почитать
[здесь](https://commitizen-tools.github.io/commitizen/).

Структура идентична [конфигу cz_conventional_commits](https://github.com/commitizen-tools/commitizen/blob/master/commitizen/cz/conventional_commits/conventional_commits.py).
Названия типов изменений вроде `fix` и `feat` решил оставить как есть.
Это не так важно, плюс не ломает генерацию списков изменений.
