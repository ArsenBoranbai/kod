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
#5 def update_rating(rating, new_element):
#     index = 0
#     for i, num in enumerate(rating):
#         if new_element <= num:
#             index = i + 1
#         else:
#             break
#     rating.insert(index, new_element)
# my_rating = [7, 5, 3, 3, 2]
# print("Старый рейтинг:", my_rating)
# new_value = int(input("Введите элемент: "))
# update_rating(my_rating, new_value)
# print("Рейтинг:", my_rating)
