class WordsFinder:
    def __init__(self, *names):
        self.names = names
        self.file_names = []
        for name in names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        replace_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.names:
            words = []
            with open(name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.split()
                    for word in line:
                        for symbol in replace_symbols:
                            word.replace(symbol, '')
                        words.append(word.lower())
            all_words[name] = words
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    return {name: words.index(i) + 1}
            else:
                return f'Слово не найдено'

    def count(self, word):
        count_ = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    count_ += 1
        return {name: count_}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
