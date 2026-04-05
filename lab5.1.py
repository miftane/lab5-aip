# 5.1.py
n = int(input("Сколько слов вы хотите ввести? "))
words = []

for i in range(n):
    word = input(f"Введите слово {i+1}: ")
    words.append(word)

result = " ".join(words)
print(f"Результат: {result}")
