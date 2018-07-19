# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re
patternnamesurmane = '[A-Z][a-z]+'
patternmail = '[a-z_0-9]+@[a-z0-9]+\.(ru|com|org)'
name = str(input('Введите ваше имя: '))
name1 = name
re.search(patternnamesurmane, name1)
if re.search(patternnamesurmane, name1) is None:
    print('Неверно введено имя!!')
surname = str(input('Введите вашу фамилию: '))
surname1 = surname
re.search(patternnamesurmane, surname1)
if re.search(patternnamesurmane, surname1) is None:
    print('Неправильно введена фамилия!!')
mail = input('Введите вашу электронную почту: ')
mail1 = mail
re.search(patternmail, mail1)
if re.search(patternmail, mail1) is None:
    print('Некорректно введен e-mail!!')
