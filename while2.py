"""
Домашнее задание №2

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
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
    while True:
        user_input = input('Введите: ')        
        if user_input in user_dict.keys():
            print(user_dict.get(user_input))
            if user_input == 'Досвидос':
                break
    

if __name__ == "__main__":
    ask_user()