import random
import string
import csv
import pandas as pd

# -----------------------------
# Task 1: створити файл через context manager
# -----------------------------

# # with open("task_1.txt", "w") as file:
# #     num = random.randint(1, 100)     # генеруємо випадкове число
# #     file.write(str(num) + "\n") 
# #     print(file)  # записуємо у файл

# #------------------------------
# #Task 2: записати 10_000 рядків з випадковими літерами
# # -----------------------------
# # Функція для генерації випадкових букв

# def generate_random_letter(): # генерує випадкову літеру
#     return random.choice(string.ascii_letters) # вибирає випадкову літеру з англійського алфавіту
# N:int = 10_000 # кількість рядків для запису
# file_to_save: str = "task_2.txt"

# with open(file_to_save, "a", encoding="utf-8") as f:  
#     for _ in range(N):
#         letters = generate_random_letter()
#         f.write("\n" + letters)











# Task 1. Read first 3 rows from amazon.csv, display columns \
with open("amazon.csv", "r", encoding="utf-8") as file: # відкриваємо файл для читання
    reader = csv.reader(file, delimiter=",") # створюємо об'єкт reader для читання CSV файлу
    counter = 0 # лічильник рядків
    result = [] # список для збереження перших 3 рядків
    for row in reader: # ітеруємося по кожному рядку в файлі
        if counter < 3: # якщо лічильник менший за 3
            result.append(row) # додаємо рядок до результату
            counter += 1    
print(result)   
print("-------------------")




# Task 2. Calculate image_url and display stats