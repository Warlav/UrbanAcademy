class WordsFinder:
    def __init__(self, *names):
        self.file_names = []
        self.file_names.append(*names)
        for name in names:
            file = open(name, 'w', encoding='utf-8')
            file.close()

    def get_all_words(self):
        all_words = {}
        words = []
        replace_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                for line in file:
                    for symbol in replace_symbols:
                        line.replace(symbol, '')
                    words.append(line.lower().split())
                all_words[name] = [words]

    def find(self, word):
        return


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
