import argparse
from bigrams_utilities import BigramsUtilities

# Путь к тексту для обучения и файлу для записи сгенерированного текста передаются в терминале
# Пример: main.py text.txt output.txt apple 10

parser = argparse.ArgumentParser(description='Provide fit and transform methods of model.')

# аргументы
parser.add_argument("filepath_train_text", type=str)  # путь к текстовому файлу для обучения
parser.add_argument("filepath_generated_text", type=str)  # путь к текстовому файлу для записи
parser.add_argument("condition", type=str)  # слово-состояние
parser.add_argument("length", type=int)  # длина генерируемого текста

args = parser.parse_args()

print('Fitting is processing...')
BigramsUtilities.fit(args.filepath_train_text)
print('Fitting is succesful')
BigramsUtilities.generate(args.filepath_generated_text, args.condition, args.length)
print('Text generated to ' + args.filepath_generated_text)
