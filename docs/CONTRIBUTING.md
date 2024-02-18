## Предложить изменения

Поучаствовать в развитии документации можно несколькими способами:

1. предлагайте изменения/дополнения в [ZEEKR Club в
   Telegram](https://t.me/zeekrclub/158198)
1. создавайте темы [на Github -
   OS-Car-Man](https://github.com/os-car-man/os-car-man/issues)
1. на интересующей вас странице нажать на иконку "внести изменения" и внести
   изменения самостоятельно.


## Режим разработчика

===! "Mac OS / Linux"
    - установить [Docker](https://docs.docker.com/engine/install/)
    - сделать форк https://github.com/os-car-man/os-car-man и склонировать его
      себе
    - запустить `make build`, чтобы собрать образ, необходимый для локальной
      работы с документацией
    - запустить `make docs`
    - открыть [http://localhost:7777](http://localhost:7777) в браузере
    - внести изменения в код
        * документация пишется на Markdown-е, используя
          [mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/)
        * навигация в `mkdocs.yml` в корне
        * сама документация в папке `docs`
    - проверить результат в браузере
    - отправить изменения на Github и создать Pull request

=== "Windows"
    - установить [Docker](https://docs.docker.com/engine/install/)
    - **TO BE CHECKED** установить `make` - [help
      link](https://stackoverflow.com/a/57042516/5387738)
    - сделать форк https://github.com/os-car-man/os-car-man и склонировать его
      себе
    - запустить `make build`, чтобы собрать образ, необходимый для локальной
      работы с документацией
    - запустить `make docs`
    - внести изменения в код
        * документация пишется на Markdown-е, используя
          [mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/)
        * навигация в `mkdocs.yml` в корне
        * сама документация в папке `docs`
    - проверить результат в браузере
    - отправить изменения на Github и создать Pull request

#### Добавление плагинов / библиотек

- `make bash`
- `cd ci-requirements/`
- `poetry add {name_of_dependency}`
- `poetry export -o requirements.txt`
- выйти из контейнера
- `make build`
- `make docs`
