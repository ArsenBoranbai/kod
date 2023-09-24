#1 spisok = [1, "Privet", 5.34, True, [5, 2, 4], {"imya": "Arsen", "vozrast": 18}]
# for element in spisok:
#     element_type = type(element)
#     print(f"Элемент: {element}, Тип: {element_type}")
#2 my_list = input("Введите элементы списка: ").split()
# for i in range(0, len(my_list)-1, 2):
#    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
# print(my_list)
#3 s = int(input("Введите месяц (от 1 до 12): "))
# vremya = ["зима", "весна", "лето", "осень"]
# if 1 <= s <= 12:
#     print(f"Месяц {s} является: {vremya[(s % 12) // 3]}")
# else:
#     print("Ошибка.")
#4 stroka = input("Введите строку из нескольких слов, разделённых пробелами: ")
# slova = stroka.split()
# for i, word in enumerate(slova, 1):
#     print(f"{i}. {word[:10]}")
#5 def funkciya(a, value):
#     if value > max(a) or value not in a:
#         a.insert(0, value)
#     else:
#         a.insert(a.index(value), value)
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# funkciya(my_list, 3)
# print(my_list)
# funkciya(my_list, 8)
# print(my_list)
# funkciya(my_list, 1)
# print(my_list)
