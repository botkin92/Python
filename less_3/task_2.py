def user_data(**data):
    return data


print(user_data(
    name=input('Ваше имя: '),
    surname=input('Ваше фимилия: '),
    year_of_birth=int(input('Год рождения: ')),
    sity=input('Город проживания: '),
    email=input('Адрес эл.почты: '),
    phone=input('Номер телефона: ')
))
