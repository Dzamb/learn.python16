'''
1. Создать список из словарей с оценками учеников разных
классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
2. Посчитать и вывести средний балл по всей школе.
3. Посчитать и вывести средний балл по каждому классу.

'''

classroom_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [2, 3, 4, 5, 5]},
    {'school_class': '4c', 'scores': [3, 3, 2, 5, 1]},
    {'school_class': '4d', 'scores': [3, 1, 2, 2, 4]}
]

classroom_sum = []
classroom_sum.append(sum(classroom_scores[0]['scores']) / len(classroom_scores[0]['scores']))


print(classroom_sum)

