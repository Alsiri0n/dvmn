# Description

This project implements putting weather from [wttr.in](https://wttr.in) and output getting the data at console.
This project provides to get weather information for some places simultaneously.

At this project implements remote server error processing.

The project needs to install requests library. Work ensures on requests version 2.28.2 and python version 3.11.3.


---
# Описание

Проект реализует получение погоды с сайта [wttr.in](https://wttr.in) и выводит в консоль всю полученную информацию.
Проект предусматривает получение информации о погоде для нескольких точек одновременно.

Реализована обработка ошибка удаленного сервера. 

Для работы проекта необходима библиотека requests.
Протестирована и гарантирована работа на версии 2.28.2 и python 3.11.3.

---
Examples

Пример запуска программы
```
$ python3 weather.py
Лондон

      \   /     Солнечно
       .-.      +10(8) °C
    ― (   ) ―   ← 5 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Чт. 27 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │      .-.     Умеренный дожд…│
│      .--.     +14(13) °C     │     (   ).    +12(10) °C     │
│   .-(    ).   ↖ 6 м/c       │    (___(__)   ↖ 3-5 м/c     │
│  (___.__)__)  10 км          │   ‚‘‚‘‚‘‚‘    7 км           │
│               0.0 мм | 0%    │   ‚’‚’‚’‚’    4.2 мм | 91%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Пт. 28 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │  _`/"".-.     Местами дождь  │
│   ,\_(   ).   16 °C          │   ,\_(   ).   12 °C          │
│    /(___(__)  → 6 м/c       │    /(___(__)  ↗ 2-3 м/c     │
│      ‘ ‘ ‘ ‘  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│     ‘ ‘ ‘ ‘   0.1 мм | 68%   │     ‘ ‘ ‘ ‘   0.1 мм | 63%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Сб. 29 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │  _`/"".-.     Местами дождь  │
│   ,\_(   ).   19 °C          │   ,\_(   ).   +11(10) °C     │
│    /(___(__)  ↙ 1 м/c       │    /(___(__)  ← 3-4 м/c     │
│      ‘ ‘ ‘ ‘  10 км          │      ‘ ‘ ‘ ‘  9 км           │
│     ‘ ‘ ‘ ‘   0.1 мм | 60%   │     ‘ ‘ ‘ ‘   0.2 мм | 61%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
...
```

# Feature
Project support add city as arguments.
```
$ python weather.py Москва
Москва

      \   /     Солнечно
       .-.      14 °C
   ― (   ) ―   ↑ 1 м/c        
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Чт. 27 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /      Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     19 °C          │      .-.      15 °C          │
│    \_(   )   ↑ 3 м/c        │  ― (   ) ―   ↖ 2-5 м/c    │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Пт. 28 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │               Пасмурно       │
│     (   ).    13 °C          │      .--.     +8(5) °C       │
│    (___(__)   ↑ 2-3 м/c     │   .-(    ).   ↓ 3-4 м/c     │
│     ‘ ‘ ‘ ‘   2 км           │  (___.__)__)  10 км          │
│    ‘ ‘ ‘ ‘    0.6 мм | 63%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Сб. 29 апр. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │     \   /     Ясно           │
│     (   ).    +8(5) °C       │      .-.      +7(6) °C       │
│    (___(__)   ↓ 5-6 м/c     │  ― (   ) ―   ↓ 1-2 м/c    │
│     ‘ ‘ ‘ ‘   2 км           │      `-’      10 км          │
│    ‘ ‘ ‘ ‘    0.3 мм | 85%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
```