# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
import re
word = 'Архангельск'
vowels = 'Аае'
print(len([i for i in list(word) if i in list(vowels)]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = len(re.findall('\w+', sentence))
print(words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
letters = sentence.split()
for letter in letters:
    print(letter[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
word_list = sentence.split()
average = sum(len(word) for word in word_list) / len(word_list)
print(average)