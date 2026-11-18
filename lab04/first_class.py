from pathlib import Path


class MyName:
    """Опис класу / Документація"""

    total_names = 0

    def __init__(self, name=None, domain="itcollege.lviv.ua", login=None) -> None:
        """Ініціалізація класу"""
        picked = name if name is not None else self.anonymous_user().name
        if not str(picked).isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        self.name = picked[:1].upper() + picked[1:]
        self.login = self.name if login is None else login
        self.domain = domain
        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        """Class property
        return: повертаємо імя
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    @property
    def full_name(self) -> str:
        """Повне представлення користувача"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain=None) -> str:
        """Instance method. domain змінює частину адреси після @."""
        chosen = self.domain if domain is None else domain
        return f"{self.login}@{chosen}"

    def letters_count(self) -> int:
        """Кількість букв в імені"""
        return len(self.name)

    def save_to_file(self, filename="users.txt") -> None:
        """Додає рядок із записом у файл"""
        path = Path(__file__).with_name(filename)
        with path.open("a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        """Classs method"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"


if __name__ == "__main__":
    print("Розпочинаємо створювати обєкти!")

    names = ("Bohdan", "Marta", None, "demid")
    all_names = {
        name: MyName(name, login="dbabtenko2024") if name == "demid" else MyName(name)
        for name in names
    }
    users_file = Path(__file__).with_name("users.txt")
    users_file.write_text("", encoding="utf-8")

    for name, me in all_names.items():
        print(f"""{">*<" * 20}
This is object: {type(me).__name__} #{me.my_id}
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()}
This is static with custom text: {me.say_hello("Привіт, це Демід")}
Letters in name: {me.letters_count()}
Full name: {me.full_name}
Other domain: {me.create_email("student.lviv.ua")}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>" * 20}""")
        me.save_to_file()

    print(f"Імен у списку names: {len(names)}")
    print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

    try:
        MyName("Demid1")
    except ValueError as error:
        print("Перевірка імені:", error)
