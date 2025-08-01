# Оптимизация работы светофоров - симулятор дорожного движения


## Описание проекта

Этот проект представляет собой симулятор дорожного движения с адаптивными светофорами, написанный на Python с использованием библиотеки Pygame.
Программа визуализирует транспортные потоки на перекрестке и позволяет исследовать работу светофоров в различных условиях.

## Основные возможности

- 🚦 Два независимых светофора с автоматическим переключением
- 🚗 Генерация машин с настраиваемой интенсивностью
- 🛑 Реалистичное поведение транспорта (остановка на красный свет)
- 🎚️ Интерактивные ползунки для управления плотностью потока
- 🖱️ Простой интерфейс с кнопками управления

## Требования

- Python 3.8+
- Pygame 2.0+
- Система с поддержкой графики (не требуется мощное железо)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/traffic-light-optimization.git
cd traffic-light-optimization
Установите зависимости:

bash
pip install pygame
Запустите программу:

bash
python main.py
Как использовать
Нажмите "Start" на стартовом экране

Используйте ползунки для регулировки интенсивности движения:

Левый ползунок - поток слева направо

Правый ползунок - поток справа налево

Наблюдайте за работой светофоров и поведением машин

Для выхода нажмите кнопку "Exit"

Особенности реализации
Класс Car: отвечает за поведение отдельных автомобилей

Функции отрисовки: отдельные модули для визуализации элементов

Система событий: обработка пользовательского ввода

Таймеры: автоматическое переключение светофоров

Структура кода
text
traffic_simulation/
│── main.py                # Основной файл программы
│── README.md              # Этот файл
