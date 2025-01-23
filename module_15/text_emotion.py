# Установите необходимые библиотеки
# !pip install nltk
# !pip install textblob

import nltk
from textblob import TextBlob

# Загрузка ресурсов для nltk
nltk.download('punkt')

# Пример текста для анализа
text = "I love Biden and fuck them!!!"

# Создание объекта TextBlob
blob = TextBlob(text)

# Анализ тональности текста
sentiment = blob.sentiment

# Вывод результатов
print(f"Text: {text}")
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
# Установите необходимые библиотеки
# !pip install nltk
# !pip install textblob

import nltk
from textblob import TextBlob

# Загрузка ресурсов для nltk
nltk.download('punkt')

# Пример текста для анализа
text = "I love Biden and fuck them!!!"

# Создание объекта TextBlob
blob = TextBlob(text)

# Анализ тональности текста
sentiment = blob.sentiment

# Вывод результатов
print(f"Text: {text}")
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
