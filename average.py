grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average0 = sum(grades[0]) / len(grades[0])  # средняя оценка первого студента
average1 = sum(grades[1]) / len(grades[1])  # средняя оценка второго студента
average2 = sum(grades[2]) / len(grades[2])  # средняя оценка третьего студента
average3 = sum(grades[3]) / len(grades[3])  # средняя оценка четвёртого студента
average4 = sum(grades[4]) / len(grades[4])  # средняя оценка пятого студента
students = list(students)  # перевод множества в список
students.sort()  # сортировка списка по алфавиту
dict = dict([[students[0], average0], [students[1], average1], [students[2], average2], [students[3], average3],
             [students[4], average4]])  # составление словаря
print(dict)
