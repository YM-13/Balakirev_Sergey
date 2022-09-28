from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + '_@.'
    
    def __new__(cls, *args, **kwargs):
        return None


    str = ''

    @classmethod
    def get_random_email(cls):
        number = randint(10, 100)
        for n in range(number): # тк точка это тоже знак
            d = randint(0, len(cls.EMAIL_CHARS) - 3)
            if d != '@' and d != '.':
                cls.str = cls.str + cls.EMAIL_CHARS[d]

        return "".join(cls.EMAIL_CHARS[randint(0, len(cls.EMAIL_CHARS) - 1)] for i in range(number)) + "@gmail.com"




    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.EMAIL_CHARS):
            return True

        s = email.split('@')
        if len(s) != 2:
            return False

        if len(s[0]) > 100 or len(s[1]) > 50:
            return False

        if '.' not in s[1]:
            return False

        if email.count('..') > 0:
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


z = EmailValidator.get_random_email()
print(EmailValidator.check_email(z))

