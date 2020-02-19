input_1 = input('Введите строку через пробел: ').lower()
input_2 = input('Введите строку через пробел: ').lower()

def string_comparing(input_1, input_2):
    '''
    первое условие пропустил так как тип input всегда бывает строкой
    '''
    if input_1 == input_2:
        return '1'
    elif input_1 != input_2:
        if len(input_1) > len(input_2):
            return '2'
        elif input_2 == 'learn':
            return '3'

print(string_comparing(input_1, input_2))