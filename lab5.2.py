# 5.2.py
words = []

while True:
    word = input("Введите слово (или 'stop' для выхода): ")
    if word.lower() == "stop":
        break
    words.append(word)

result = " ".join(words)
print(f"Результат: {result}")
