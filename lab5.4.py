# 5.4.py
import random

errors = 0
correct = 0

while errors < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    try:
        answer = int(input(f"{a} + {b} = "))
    except ValueError:
        print("Пожалуйста, введите число.")
        errors += 1
        continue
    
    if answer == a + b:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        errors += 1

print(f"Игра окончена. Правильных ответов: {correct}")
