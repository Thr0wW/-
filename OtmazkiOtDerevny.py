import random


Otmazki = ['деревенский климат', 'много ковров', 'скучно', 'нет компьютера', 'старый дом', 'нет покоя', 'аллергия на плесень', 'аллергия на солнце', 'аллергия на траву','аллергия на деревню']
Otveti = ['В этом же нет ничего плохого!','Пропылесось', 'Найдем чем тебе занятся', 'Зато отдохнешь от него!', 'Не такой он уж и старый', 'И ЧО?', 'Не такая она уж и большая', 'С зонтиком ходи', 'Пруфы!', 'Нет']
print("\033[31m" + '\033[1m' + 'Почему ты не хочешь ехать в деревню?')
input("\033[37m" + "\033[2m" + "\033[3m" + "Enter для продолжения")
print('\033[0m')
response = '\033[4m\033[1m\033[32mВ деревне '
a=('\n\033[0m\033[2m\033[3m')
while True:
    otmazka1 = random.choice(Otmazki)
    otvet= random.choice(Otveti)
    if otmazka1 == 'деревенский  климат':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('деревенский  климат')
    elif otmazka1 == 'много ковров':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('много ковров')
    elif otmazka1 == 'скучно':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('скучно')
    elif otmazka1 == 'нет компьютера':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('нет компьютера')
    elif otmazka1 == 'старый дом':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('старый дом')
    elif otmazka1 == 'нет покоя':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('нет покоя')
    elif otmazka1 == 'аллергия на плесень':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('аллергия на плесень')
    elif otmazka1 == 'аллергия на солнце':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('аллергия на солнце')
    elif otmazka1 == 'аллергия на траву':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('аллергия на траву')
    elif otmazka1 == 'аллергия на деревню':
        input(response + otmazka1 + '\n' + otvet)
        Otmazki.remove('аллергия на деревню')