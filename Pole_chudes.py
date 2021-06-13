import random 

def get_guess():
    t = True
    while t:
        x = input("Вводи: ")
        if x == "Emil is super":
            emil = input("Да здравствует повелитель! Чего вам угодно, хозяин? ")
            if emil == "Who is Boss?":
                emil1 = input("Конечно же вы Босс. Мне устроить вашу победу? ")
                if emil1 == "yes":
                    print("\nСию минуту.\n")
                    x = "emil"
                    return x
                if emil1 == "no":
                    print("Как скажете.")
                    continue 
        elif x == x.upper() or x != str(x):
            print("Хорош тупить. Вводи одну строчную букву.")
       
        elif len(x) > 1:
            print("Идиот, пиши только одну букву.")
        else:
            break
    return x

a = input("Объяснить правила игры? ")
if a == "yes" or a == "yes " or a == "ok" or a == "ok " or a == "да" or a == "да " or a == "конечно" or a == "конечно " \
or a == "Yes" or a == "Yes " or a == "Ok" or a == "Ok " or a == "Да" or a == "Да " or a == "Конечно" or a == "Конечно " \
or a == " " or a == "":
    print("Короче, мы играем Поле Чудес, только без призов и викторин.")
    print("Я дам тебе несколько попыток, чтобы угадать загаданное слово, а именно 10.")
    print("Пиши только одну букву за раз. Не надо цифр, не надо несклько букв или другой херни.")
    print("Rules are Simple.")
    print("Если угадаешь, то расскажу анекдот. Если нет, то пошлю нахрен.")

else:
    print("Ну и фиг с тобой.")



words = ["патрик", "гопник", "трансформер", "жорик", "бешбармак", "манты", "оромо", "физика", "приколдэс", "пипито", "аниме", "додик"]
secret_word = random.choice(words)

mistake = ["Лох.", "Все еще нет.", "Думай лучше.", "Включи мозги.", "Ошибка на ошибке.", "Позор тебе.", "Мимо. Якубович не одобрил бы."]
aim = ["Неплохо.", "Ох, попал. Молодчик.", "Да ты зажигаешь.", "У нас тут гений.", "Продолжай в том же духе.", "Базар жок.", "Мой сынок."]
lose = ["Лошара, ты просрал.", "Попытай удачу в следущий раз, неудачник.", "Победил компьютер. А ты просрал.", \
"Ну ничего, это игра предназначено для людей с IQ выше 60-ти, а не для тебя."]
win = ["Поздравляю, ты победил.", "Неплохо сыграл. ", "Победа. Неплохо, малыш", \
"Заслуженная победа. ", "И у нас победитель."]

secret_word = list(secret_word) 

dashes = "-"*(len(secret_word))
print(dashes)

b = input("Итак, погнали? ")
if b == "yes" or b == "yes " or b == "ok" or b == "ok " or b == "да" or b == "да " or b == "конечно" or b == "конечно " \
or b == "Yes" or a == "Yes " or b == "Ok" or b == "Ok " or b == "Да" or b == "Да " or b == "Конечно" or b == "Конечно " \
or b == " " or b == "":
    
    y = 10
    guesses_left = ('У тебя осталось ' + str(y) + ' попыток.')
    print(guesses_left)
    w = False
    while y!= 0:
        x = get_guess()
        if x == "emil":
            secret_word = ''.join(secret_word)
            print('Мои поздравления, господин. Вы как и всегда выиграли эту игру!', "Вы угадали слово:", secret_word)
            print("А теперь анекдот: \n Заходят человек и жираф в бар. Оба выпивают.\
                            \n Жираф падает, человек собирается уходить. Официант ему говорит: \
                            \n «Эй мужик не надо оставлять здесь этого пьянчугу!» А человек ему отвечает:\
                            \n «ЭТО не пьянчуга. Это Жираф!»\n")
            print("Не все анекдоты смешные.")
            w = True
            y = 0
            break
        elif x in secret_word:
            print(random.choice(aim))
            for i in range(len(secret_word)):
                if secret_word[i] == x:
                    dashes = list(dashes)
                    dashes[i] = x
                    if dashes == secret_word:
                        secret_word = ''.join(secret_word)
                        print(random.choice(win), "Ты угадал слово:", secret_word)
                        print("А теперь анекдот: \n Заходят человек и жираф в бар. Оба выпивают.\
                            \n Жираф падает, человек собирается уходить. Официант ему говорит: \
                            \n «Эй мужик не надо оставлять здесь этого пьянчугу!» А человек ему отвечает:\
                            \n «ЭТО не пьянчуга. Это Жираф!»\n")
                        print("Не все анекдоты смешные.")
                        w = True
                        y = 0
                        break
                    dashes = ''.join(dashes)
                    print(dashes)
                    
                    print('У тебя осталось ' + str(y) + ' попыток.')
                    
        elif x not in secret_word:
                print(random.choice(mistake))
                print(dashes)
                y -= 1
                print('У тебя осталось ' + str(y) + ' попыток.')
    if w == False:
        print(random.choice(lose))
        secret_word = ''.join(secret_word)
        print('Неугадал, лошара.', "Загаданное слово:", secret_word)
