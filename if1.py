age = int(input('Ведите свой возраст: '))

def main(age):
    
    if age <= 7:
      return 'Ты садикмэн'

    elif 7 < age <= 17:
      return 'Ты школота'

    elif 17 < age <= 21:
      return 'Ты студент'
    
    elif 21 < age <= 64:
      return 'Иди работать!'
    
    elif 65 <= age <= 100:
      return 'Ещё живой? Пенсия хороша(нет)'
    
    elif 100 < age < 115:
      return 'Пора на кладбище'
    
    else:
      return 'Да ты Дункан Маклауд'

print(main(age))