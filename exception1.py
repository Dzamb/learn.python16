"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

user_dict = {
  'Привет': 'И тебе шалом',
  'Что делаешь?': 'Программирую',
  'Как дела?': 'Хорошо!',
  'На каком языке программируешь': 'на Python',
  'И как успехи?': 'Хорошо',
  'Досвидос': 'Чао'
}

def ask_user():
    try:
        while True:
            user_input = input('Введите: ').capitalize()        
            if user_input in user_dict.keys():
                print(user_dict.get(user_input))
                if user_input == 'Досвидос':
                    break
    except KeyboardInterrupt:
        print('Пока!')

if __name__ == "__main__":
    ask_user()
