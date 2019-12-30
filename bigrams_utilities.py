import pickle
import re
import random


class BigramsUtilities:

    @staticmethod
    def fit(filepath):  # обучение
        # Считывание входных данных из файлов.

        f = open(filepath, 'r')
        text = f.read()
        f.close()

        # Очистка текстов: выкидываем неалфавитные символы, приводим к lowercase.
        # Разбиваем тексты на слова.

        reg = re.compile('[^a-zA-Z ]')
        text = reg.sub('', text)
        words = text.lower().split()

        # словарь: слово - ключ, возможные следующие слова - значение
        bigrams = dict()

        # словарь: слово - ключ, частота следующих соответствующих слов из словаря bigrams - значение
        # частоты биграмм требуются по заданию, однако по заданию и не подразумевается для использования
        # (мог неправильно интерпретировать задание)
        frequences = dict()

        # заполнение словарей
        for i in range(len(words) - 1):
            ans = bigrams.get(words[i], 0)
            if ans == 0:
                bigrams[words[i]] = [words[i + 1]]
                frequences[words[i]] = [1]

            else:
                try:
                    index_of_word = bigrams[words[i]].index(words[i + 1])
                except ValueError:
                    index_of_word = -1

                if index_of_word >= 0:
                    array = frequences[words[i]]
                    array[index_of_word] += 1
                    frequences[words[i]] = array
                else:
                    array = bigrams[words[i]]
                    array.append(words[i + 1])
                    bigrams[words[i]] = array

                    array = frequences[words[i]]
                    array.append(1)
                    frequences[words[i]] = array

        # Сохранение модели.

        with open('bigrams.pickle', 'wb') as f:
            pickle.dump(bigrams, f)

        with open('frequences.pickle', 'wb') as f:
            pickle.dump(frequences, f)

    @staticmethod
    def generate(filepath, seed, length):  # генерация
        with open('bigrams.pickle', 'rb') as f:
            bigrams = pickle.load(f)

        with open('frequences.pickle', 'rb') as f:
            frequences = pickle.load(f)

        # Инициализация сидом, указанным как аргумент
        current_word = seed
        text = current_word

        # Генерация последовательности нужной длины

        for i in range(length):
            next_word = random.choice(bigrams[current_word])
            text += ' '
            text += next_word
            current_word = next_word

        f = open(filepath, 'w')
        f.write(text)
        f.close()
