# Ctrl+Cell

Концепт проекта состоит из трёх частей.

1. База знаний. Содержит формализованную и структурированную информацию в виде Knowledge Graphs из актуальных баз данных для считывания модулем взаимосвязи.
2. Модуль взаимосвязи. Модуль извлечения взаимосвязей из базы знаний (подграфов) для точной генерации ответов LLM.
3. LLM. Суммаризация информации и заполнение отчетов по подготовленным связям для врача и пациента.

## Содержание
- [Технологии](#технологии)
- [Pipeline](#pipiline)
- [Команда проекта](#команда-проекта)
- [Источники](#источники)

## Технологии

- LLM LLama

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

- [Семенова Елизавета](https://sysbiomed.ru/team/semenova-elizaveta-alekseevna/) — Bioinforamtics
- [Яцулевич Владимир](https://vk.com/modern_qc) — Back-End Engineer

## Источники

[1] Bae J. M. The clinical decision analysis using decision tree //Epidemiology and health. – 2014. – Т. 36. – С. e2014025.

[2] Kandula V. V., Bhattacharyya P. Decision knowledge graphs: Construction of and usage in question answering for clinical practice guidelines //arXiv preprint arXiv:2308.02984. – 2023.

[3] Zhao W, Jiang X, Wang K, Sun X, Hu G, Xie G. Construction of Guideline-Based Decision Tree for Medication Recommendation.
doi: 10.3233/SHTI200015.

[4] Тюляндин С. А. и др. Рак молочной железы //Злокачественные опухоли. – 2023. – Т. 13. – №. 3s2-1. – С. 157-200.