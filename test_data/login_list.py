from object_test_data.login import User


def login_positive():
    """
    Тестовые данные для гитхаба
    """
    return User(login='pochtasobaka@rambler.ru', password='!weak(pass)!3535')


def login_negative():
    """
    Тестовые данные для гитхаба
    """
    return User(login='почта', password='пароль')

