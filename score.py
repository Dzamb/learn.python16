'''
ЗАДАНИЕ:
1. Создать список из словарей с оценками учеников разных
классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
2. Посчитать и вывести средний балл по всей школе.
3. Посчитать и вывести средний балл по каждому классу.

'''
# Создаём список из словарей с оценками учеников разных классов школы
classroom_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [2, 3, 4, 5, 5]},
    {'school_class': '4c', 'scores': [3, 3, 2, 5, 1]},
    {'school_class': '4d', 'scores': [3, 1, 2, 2, 4]}
]
# объявляем пуской список куда будем записывать средние баллы для каждого класса
classroom_average_score = []

# создаем цикл в котором посчитаем средний балл для каждого класса и выведем на экран
for i in classroom_scores:
    classroom_average_score.append(sum(i['scores']) / len(i['scores']))
    print(f"средняя оценка для класса {i['school_class']} является {(sum(i['scores']) / len(i['scores']))}")

# посчитаем средний балл по школе и выведем на экран
school_average_score = sum(classroom_average_score) / len(classroom_average_score)
print(f"средний бал по школе {school_average_score}")


