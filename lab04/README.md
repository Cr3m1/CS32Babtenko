# Звіт до роботи

**Виконавець:** Бабтенко Демід Андрійович, група КН-32

## Тема: Знайомство з ООП

### Мета роботи: навчитись використовувати основні принципи ООП, розглянути конструкції побудови класу та створення об'єктів та навчитись працювати з ними.

---

### Виконання роботи

* Результати виконання завдання:
    1. Створили папку `lab04`, клас `MyName` у файлі [`first_class.py`](first_class.py) і ноутбук [`first_class.ipynb`](first_class.ipynb).
    1. У список імен додано `demid`. Конструктор робить першу літеру великою, тому в об'єкті ім'я стає `Demid`.
    1. Програма створює об'єкти, виводить властивості, рахує букви, пише рядок у [`users.txt`](users.txt) і відхиляє ім'я з цифрою.

* Результат запуску `first_class.py`:

```text
Розпочинаємо створювати обєкти!
This is object: MyName #1
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is static with custom text: You say: Привіт, це Демід
Letters in name: 6
Full name: User #1: Bohdan (Bohdan@itcollege.lviv.ua)
Other domain: Bohdan@student.lviv.ua
This is class variable <class 'int'>: from class 5 / from object 5

This is object: MyName #2
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is static with custom text: You say: Привіт, це Демід
Letters in name: 5
Full name: User #2: Marta (Marta@itcollege.lviv.ua)
Other domain: Marta@student.lviv.ua
This is class variable <class 'int'>: from class 5 / from object 5

This is object: MyName #4
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is static with custom text: You say: Привіт, це Демід
Letters in name: 9
Full name: User #4: Anonymous (Anonymous@itcollege.lviv.ua)
Other domain: Anonymous@student.lviv.ua
This is class variable <class 'int'>: from class 5 / from object 5

This is object: MyName #5
This is object attribute: Demid / 5
This is <class 'property'>: My name is Demid / dbabtenko2024@itcollege.lviv.ua
This is <class 'method'> call: dbabtenko2024@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is static with custom text: You say: Привіт, це Демід
Letters in name: 5
Full name: User #5: Demid (dbabtenko2024@itcollege.lviv.ua)
Other domain: dbabtenko2024@student.lviv.ua
This is class variable <class 'int'>: from class 5 / from object 5

Імен у списку names: 4
We are done. We create 5 names! ??? Why 5?
Перевірка імені: Ім'я може містити лише літери!
```

* Файл `users.txt` після запуску:

```text
User #1: Bohdan (Bohdan@itcollege.lviv.ua)
User #2: Marta (Marta@itcollege.lviv.ua)
User #4: Anonymous (Anonymous@itcollege.lviv.ua)
User #5: Demid (dbabtenko2024@itcollege.lviv.ua)
```

* Ноутбук виводить для імені `demid`: `My name is Demid`, `dbabtenko2024@itcollege.lviv.ua`, `5`, `User #1: Demid (dbabtenko2024@itcollege.lviv.ua)`, `You say: Привіт з ноутбука`, `dbabtenko2024@college.lviv.ua`. Номер у ноутбуці інший, бо файл запускається окремо і лічильник класу починається знову з нуля.

* Відповіді на питання:
    1. `None` дає ім'я `Anonymous`, бо в `__init__` є перевірка: якщо ім'я не передали, викликається метод класу `anonymous_user()`. Він створює об'єкт з ім'ям `Anonymous`, і це ім'я записується в поточний об'єкт.
    1. Текст привітання змінюється аргументом методу: `say_hello("Привіт, це Демід")`. Без аргумента лишається `Hello to everyone!`.
    1. Кількість букв рахує метод `letters_count()`. У ньому стоїть `len(self.name)`. Для `Demid` результат `5`.
    1. У списку `names` чотири елементи, а лічильник `total_names` дорівнює 5. Різниця через `None`: щоб підставити ім'я `Anonymous`, клас створює ще один тимчасовий об'єкт. Він теж збільшує лічильник, але в словник не потрапляє. Тому в виводі є об'єкти №1, №2, №4 і №5, а №3 — той тимчасовий `Anonymous`.
    1. Конструктор записує ім'я як `picked[:1].upper() + picked[1:]`, тож `demid` стає `Demid`.
    1. `create_email(domain)` підставляє переданий домен після `@`. Без аргумента лишається `itcollege.lviv.ua`.
    1. Якщо в імені є цифра або інший нелітерний символ, конструктор піднімає `ValueError("Ім'я може містити лише літери!")`. Це перевірено на `Demid1`.
    1. Властивість `full_name` повертає рядок `User #<id>: <name> (<email>)`.
    1. Метод `save_to_file()` додає цей рядок у кінець файлу `users.txt`.

---

### Висновок:

- :question: Що зроблено в роботі: створено перший клас, кілька об'єктів, властивості, метод класу, статичний метод і запис у файл.
- :question: Чи досягнуто мети роботи: так. Об'єкти створюються, ім'я і пошта читаються через властивості, додаткові пункти умови виконані.
- :question: Які нові знання отримано: чим відрізняються звичайний метод, `@property`, `@classmethod` і `@staticmethod`, і чому змінна класу `total_names` спільна для всіх об'єктів.
- :question: Чи вдалось відповісти на всі питання задані в ході роботи: так. Пояснено `Anonymous` і різницю між 4 іменами у списку та лічильником 5.
- :question: Чи вдалося виконати всі завдання: так. Ім'я додано, привітання змінюється, букви рахуються, домен змінюється, помилка для `Demid1` спрацьовує, `full_name` і `save_to_file` працюють.
- :question: Чи виникли складності у виконанні завдання: номер 3 не з'являється у списку об'єктів, бо цей об'єкт створюється лише всередині виклику `anonymous_user()`.
- :question: Чи подобається такий формат здачі роботи (Feedback): так, бо клас, вивід і відповіді лежать в одній папці.
- :question: Побажання для покращення (Suggestions): у прикладі з `None` варто окремо написати, що створюється додатковий об'єкт.

---

Повернутися на [головну сторінку репозиторію](../README.md).
