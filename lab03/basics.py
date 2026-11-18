import keyword
import random
from pathlib import Path

print("=== 1. Типи даних ===")
a = "змінна з текстом"
a1 = "a"
b = 1
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]
d = {"a": "Слово", "b": 1, a: b}
e = ("a", a)
print("str:", a)
print("str з одного символу:", a1)
print("int:", b)
print("float:", b1)
print("list:", c)
print("dict:", d)
print("tuple:", e)
try:
    f = {"ss", a + b}
except TypeError as error:
    print("Рядок і число не додаються:", error)
    f = {"ss", a}
print("set:", sorted(f))

print("=== 2. Константи і зарезервовані слова ===")
print("Перша константа:", True)
print(f"Як можна так робити вивід? {False}")
print("Ще одна константа:", None)
print("Зарезервовані слова:", ", ".join(keyword.kwlist))

print("=== 3. Вбудовані функції ===")
print(abs(-12.5), f"є рівним {abs(12.5)}", "і якщо порівняти то:", abs(-12.5) == abs(12.5))
print("len:", len(c))
print("round:", round(b1))
print("min і max:", min(3, 9, 1), max(3, 9, 1))

print("=== 4. Цикли ===")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цикл for завершився")

n = 1
while n <= 3:
    print("while:", n)
    n += 1

for letter in letters:
    print("буква:", letter)

print("=== 5. Розгалуження ===")
random.seed(1)
A = random.randint(0, 1)
print(f"Значить А={A}" if A else "Але може бути що А={}".format(A))

score = 75
if score >= 90:
    print("відмінно")
elif score >= 60:
    print("зараховано")
else:
    print("не зараховано")

temperature = -2
if temperature < 0:
    print("нижче нуля")
else:
    print("нуль або вище")

print("=== 6. try, except, finally ===")
A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except Exception as e:
    print("Невже це помилка >", e)
finally:
    print("О це так на тобі!")

print("=== 7. Контекстний менеджер with ===")
sample = Path(__file__).with_name("sample.txt")
with sample.open("r", encoding="utf-8") as file:
    for number, line in enumerate(file):
        print(f"{number})>", line, end="")
print()

print("=== 8. Лямбда-функція ===")


def a_b_func(left, right):
    return left, right


this_is_lambda = lambda first, age: f"Цей код написав: {first}, приклад числа: {age}"
print("Це просто функція:", a_b_func.__name__)
print("А це лямбда:", this_is_lambda.__name__)
print("Це її виклик:", this_is_lambda("Demid", 16))
print(this_is_lambda(*a_b_func("a", 1)))

print("=== 9. Приклади для Jupyter ===")
language = "Python"
print(language, type(language).__name__)
numbers = [2, 4, 6]
total = 0
for number in numbers:
    total += number
print("сума:", total)
mark = 8
if mark >= 6:
    print("тема зарахована")
else:
    print("тему треба повторити")
