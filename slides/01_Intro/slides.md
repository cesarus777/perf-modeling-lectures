---
theme: seriph
title: Моделирование вычислительных систем | Лекция 1
titleTemplate: '%s'
info: false
author: Yuly Tarasov
presenter: true
lineNumbers: true
colorSchema: light
aspectRatio: 16/9
themeConfig:
  primary: '#1E22AA'
  secondary: '#00ff00'
class: text-center
drawings:
  persist: false
mdc: true
duration: 75min
layout: center
---

**Вы** -- ведущий инженер в полупроводниковой компании

---
layout: center
---

**Вы** разработали *гениальное* улучшение

<v-clicks>

- Новый алгоритм предсказателя переходов
- Революционный протокол когерентности
- Сверх-эффективный матричный сопроцессор

</v-clicks>

---
layout: center
---

Как убедить в гениальности разработки?

---
layout: image
image: /ladno.jpeg
---

---
layout: image-right
image: /working-cat.webp
---

<v-clicks class="mt-20">

- Год напряженной работы
- Заказ отправлен на фабрику
- Прихала партия 3-нм чипов из Т@*в@ня
- Начинается брингап и ...

</v-clicks>

---
layout: two-cols
---

# Сценарий №1

<ul>
  <li v-click><i>Иногда</i> чип зависает</li>
  <li v-click="'+2'">Детальное исследование показало ошибку в логике арбитража одной из шин памяти</li>
  <li v-click>Фиксим аппаратными WA и надеемся на лучшее</li>
  <li v-click>В будущем пишем больше тестов</li>
</ul>

::right::

<div class="flex items-center justify-center h-full w-full">
  <div class="w-full">
    <img v-click="2" src="/freeze.png" class="w-full">
  </div>
</div>

---
layout: two-cols
---

# Сценарий №2

<ul>
  <li v-click="1"><span>Чип <b>абсолютно</b> корректен функционально</span><span v-click="2">, но...</span></li>
  <li v-click="3">Замеры на целевых нагрузках показывают на 15% меньше TFLOPS</li>
  <li v-click="4">... что на 7% меньше конкурентов</li>
</ul>

::right::

<div class="flex items-center justify-center h-full w-full">
  <div class="w-full">
    <v-switch>
      <template #1><img src="/Stark-triumph.jpeg" class="w-full"></template>
      <template #3-5><img src="/sloth-zootopia.gif" class="w-full"></template>
    </v-switch>
  </div>
</div>

---
layout: two-cols
---

# Сценарий №3

<ul>
  <li v-click>Чип <b>абсолютно</b> корректен функционально</li>
  <li v-click>И производительность соответствует ожидаемой</li>
  <li v-click>Но <span v-click="4">энергопотребление оказалось <b>в два раза больше</b>, что неприемлемо для целевой мобильной платформы</span></li>
</ul>

::right::

<div class="flex items-center justify-center h-full w-full">
  <div class="w-full">
    <img v-click="4" src="/pc-in-fire.jpg" class="w-full">
  </div>
</div>

---
layout: statement
---

# Во что обойдется компании подобная ошибка?

---

# Исправление ошибок проектирования и респин (re-spin)

Re-spin -- новая итерация проектирования и производства

- От 6 до 12 месяцев работы команды инженеров (от $1-2M до $10-20M)
- Изготовление новых масок для нового tapeout (~$30-50M для 3-5 нм)
- Упущенная выгода из-за увеличения time-to-market
- Репутационные потери из-за непопадания в график

---
layout: fact
---

## **Ошибка в кремнии это финансовая катастрофа**

---
layout: statement
---

## А что если ошбка была бы обнаружена на этапе разработки?

Стоимость исправления от недели до месяца работы архитектора: до $10k вместо $100M+

## На 5 порядков меньше!!!

---
layout: cover
background: /title_background.jpg
---

# Моделирование вычислительных систем

Кафедра микропроцессорных технологий в интеллектуальных системах управления

<div class="abs-b">
Москва 2026
</div>

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/cesarus777/perf-modeling-lectures" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---

# О преподавателе

<div class="m-16"/>

## Тарасов Юлий

<div class="m-16"/>

- Магистр МФТИ ФРКТ
- Старший инженер-программист
- Отдел инструментов разработки и компиляторов

---

# О курсе

Цель курса - ознакомление с технологиями моделирования вычислительных систем

Система оценивания:


$$
\begin{aligned}
Оценка = П + Д - 4
\end{aligned}
$$

где $П$ -- количество посещений, $Д$ -- дополнительные баллы.

Учет посещений:

$$
\begin{aligned}
П = П_o + 0.7П_д
\end{aligned}
$$

где $П_o$ -- количество очных посещений, а $П_д$ -- дистанционных.

<!--
Это курс не про написание кода, а про мышление системного архитектора и анализ производительности.
-->

---
layout: two-cols-header
---

# Программа курса

::left::

1. Кризис сложности и роль моделирования в жизненном цикле проекта VLSI
1. Классификация уровней абстракции моделей
1. Понятие производительности, и влияние на нее разных метрик
1. Библиотеки, инструменты и фреймворки для моделирования
1. Основы событийного моделирования (discrete-event simulation)
1. SystemC и TLM 2.0
1. Архитектура модели производительности
 
::right::

8. Моделирование конфликтов и арбитража
1. Моделирование памяти (cash, prefetcher, etc.)
1. Верификация и калибровка моделей
1. Подготовка входных данных для моделей
1. Современные вызовы (гетерогенные системы, разнородные модели и тд.)
1. Экономическая целесообразность моделирования
1. Современные тренды и перспективы в индустрии
 
<style>
.two-cols-header {
  column-gap: 3rem;
}
</style>

---
layout: section
---

# Как люди жили раньше?

---
layout: image-right
image: /Intel-8086.jpg
---

# Intel 8086

- ~29000 транзисторов
- Одно ядро
- Архитектор мог держать всю систему в голове
- Проектирование было линейным

---
layout: image
image: /ic-floor.png
backgroundSize: contain
---

---
layout: section
---

# До чего мы дошли сейчас?

---
layout: image-left
image: /M3-Ultra.jpg
---

# Apple M3 Ultra

- \>100 миллионов транзисторов
- Десятки гетерогенных ядер, сотни GPU, множество спецускорителей (NPU, ISP, кодеки и тп.)
- Сложнейшая иерархия памяти
- Сеть на кристалле (Network-on-Chip NoC)

---
layout: statement
---

# Ключевое изменение -- нелинейный рост состояния системы

<!--
Ключевое изменение — нелинейный, экспоненциальный рост состояния системы. Число возможных взаимодействий между компонентами растет как факториал. Ни один человек, ни даже команда, не может предсказать поведение такой системы «в уме».

Это и есть кризис сложности. И он приводит нас к трем фундаментальным проблемам.
-->

---

# Dark Silicon: Архитектурный тупик

Приходится делать обязательный выбор, например, добавить два CPU ядра или сделать больше LLC

Каждое решение меняет производительность, площадь и энергопотребление непредсказуемым образом

<div class="flex items-center justify-center h-70% w-full">
  <div class="w-60%">
    <img src="/various-dark-silicon-patterns.jpg" class="w-full">
  </div>
</div>

---

# Проблема прогнозирования

Допустим вы написали идеальный RTL для нового предсказателя переходов. Как он повлияет на общую производительность системы?

- Ускорит ли он целевые нагрузки?
- Не станет ли он "узким горлышком" для других блоков?
- Не вызовет ли его повышенная активность к перегреву чипа?

RTL симуляция больших СнК слишком медленна для таких оценок

---

# Проблема Co-design

На заре развития процессоров сначала разрабатывали железо, а потом ПО под него

Сегодня выпуск СнК без готового программного стека **немыслим**

Программный стек должен быть так же не только функционально корректен, но и оптимизирован под целевое железо

<div class="flex items-center justify-center h-60% w-full">
  <div class="w-60%">
    <img src="/shift-left.png" class="w-full">
  </div>
</div>

---

# Стоимость ошибки

<div class="flex items-center justify-center h-95%">
  <div class="h-full">
    <img src="/fail-cost.png" class="h-full">
  </div>
</div>

---
layout: two-cols-header
---

# Interl Pentium FDIV bug (1994)

::left::

- Широко известный ныне баг в FPU Intel
- Обнаружен бользователем
- Убытки в рамках программы отзыва и замены -- $475M

::right::

<div class="flex items-center justify-center h-full w-full">
  <div class="w-full">
    <img src="/intel-pentium.jpg" class="w-full">
  </div>
</div>

---
layout: two-cols-header
---

# Современные уязвимости: Meltdown, Spectre и др

::left::

- Не просто баги, а фундаментальные просчеты в архитектурных концепциях
- Требует изменения микроархитектуры
- Soft WA заметно снижают производительность

::right::

<div class="flex items-center justify-center h-full w-full">
  <div class="w-full">
    <img src="/meltdown-spectre.png" class="w-full">
  </div>
</div>

---

# "Бесшумные провалы"

- Провалы стартапов, проваливших очередной этап инвестирования из-за недостижения заявленных показателей
- Провалы внутренних проектов
- Работавшие проекты, не выполнившие маректинговые обещания

---
layout: fact
---

## Моделирование -- базовый минимум, а не роскошный максимум

---

# Жизненный цикл проекта: V Model

<div class="flex items-center justify-center h-60% w-full mt-20">
  <div class="w-60%">
    <img src="/v_cycle.png" class="h-full">
  </div>
</div>

---
layout: image
image: /three-whales.jpg
backgroundSize: full
---

# Три кита современного проектирования VLSI

---
layout: image
image: /question_background.jpg
---

# Кит 1: Architectural exploration

<div class="flex items-center justify-center h-90% w-full mt-0">
  <div class="h-full">
    <img src="/what_if_cache_size.png" class="h-full">
  </div>
</div>

---
layout: image
image: /question_background.jpg
---

# Кит 1: Architectural exploration

<div class="flex items-center justify-center h-90% w-full mt-0">
  <div class="h-full">
    <img src="/what_if_core_scaling.png" class="h-full">
  </div>
</div>

---
layout: image
image: /question_background.jpg
---

# Кит 1: Architectural exploration

<div class="flex items-center justify-center h-90% w-full mt-0">
  <div class="h-full">
    <img src="/what_if_freq_bus_3d.png" class="h-full">
  </div>
</div>

---
layout: image
image: /question_background.jpg
---

# Кит 1: Architectural exploration

<div class="flex items-center justify-center h-90% w-full mt-0">
  <div class="h-full">
    <img src="/what_if_power_thermal.png" class="h-full">
  </div>
</div>

---
layout: image-right
image: /whale-hat.jpg
---

# Кит 1: Architectural exploration

Максимально простые модели:
- Аналитические модели
- Высокоуровневые симуляторы
- Сбор статистики не для точных выводов, а для сравнения вариантов

Главный принцип: быстро ошибиться, чтоб отбросить 95% бесперспективных идей

---
layout: image-right
image: /whale-drums.jpg
---
# Кит 2: Software Bring-up

**На сегодняшний день любой чип будет бесполезен без поддержанного программного стека**

Time-to-software стал так же важен, как time-to-silicon

Вирутальная платформа для запуска немодифицированного ПО создается **до** готовности RTL

---
layout: image-right
image: /whale-guitar.webp
---
# Кит 3: Verification, Calibration and Post-silicon

1. Кросс верификация с RTL
1. Калибровка задержек и микроархитектурных параметров для сопоставления с RTL
1. Post-Si калибровка по данным кремния
    - Анализ аномалий
    - Увеличение точности для моделей чипов следующих поколений

---
layout: two-cols-header
---

# Место китов в V-model

::left::

Разные модели выполняют свои важные роли на разных этапах разработки
- Аналитические для архтектурных оценок
- Функциональные для SW Bring-up
- Более точные для принятия микроархитектурных решений

::right::

<div class="flex items-center justify-center h-60% w-full mt-20">
  <div class="w-full">
    <img src="/v_cycle.png" class="h-full">
  </div>
</div>

---

# Фундаментальный компромисс

Большая детализация моделирования -- меньшая скорость моделирования

<div class="flex justify-center m-6">
    <img src="/gepard-researcher.jpg" class="w-1/4 pr-8">
    <img src="/turtle-researcher.jpg" class="w-1/4 pl-8">
</div>

Главное искусство -- умение подобрать модель, оптимально решающую поставленную задачу

---

# Summary

1. Проблема: Cовременные системы чудовищно сложны, цена ошибок слишком велика
1. Решение: Принять как можно больше решений до начала дорогостоящих стадий разработки
1. Методология применения:
   - Architectural exploration
   - SW Bringup
   - Verification & Calibration
1. Инструмент: Набор моделей с разной детализацией

---

# To be continued...

<div class="flex justify-center h-60% w-full mt-20">
  <div class="h-full">
    <img src="/anonimous.jpg" class="h-1">
    <p class="text-center">
      А как <v-click>моделировать</v-click>?
    </p>
  </div>
</div>

