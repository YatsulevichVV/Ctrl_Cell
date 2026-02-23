# Ctrl+Cell

Здесь будет описание

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Структура проекта](#структура)
- [Pipeline](#pipiline)
- [Команда проекта](#команда-проекта)
- [Источники](#источники)

## Технологии

## Начало работы

## Структура проекта

## Pipeline

1. Запуск парсера PDF формата
```
python parser.py medicine.pdf medicine.md
```

2. Перевод документа с русского языка на английский
```
python translate.py medicine_rus.txt medicine_eng.txt 
```

3. Извлечение сущностей и связей из документа
```
python get_entities.py prompt.txt medicine_eng.txt result.json
```

4. Построение графа по извлеченным сущностям
```
python make_graph.py result.json graph.pdf
```

## Команда проекта

- [Семенова Елизавета](ССЫЛКА) — Bioinforamtics
- [Яцулевич Владимир](ССЫЛКА) — Back-End Engineer

## Источники