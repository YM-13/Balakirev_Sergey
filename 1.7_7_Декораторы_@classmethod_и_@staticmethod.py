from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(self.name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size=<{self.size}> />" # <p class='login'>Логин: <input type='text' size=10 />

    @classmethod
    def check_name(cls, name):
        el = [False for i in name if i not in cls.CHARS_CORRECT]
        if not 3 <= len(name) <= 50 or el != []: #not all([False for i in name if i not in cls.CHARS_CORRECT]):
            raise ValueError("некорректное поле name")

class PasswordInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='password'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls, name):
        el = [False for i in name if i not in cls.CHARS_CORRECT]
        if not 3 <= len(name) <= 50 or el != []:       #not all([False for i in name if i not in cls.CHARS_CORRECT])
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)