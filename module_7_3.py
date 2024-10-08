class WordsFinder:
    def __init__(self, *names):
        self.file_names = [*names]

    def get_all_words(self):
        all_words = {}
        replace_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            words = []
            with open(name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.split()
                    for word in line:
                        for symbol in replace_symbols:
                            word = word.replace(symbol, '')
                        words.append(word.lower())
            all_words[name] = words
        return all_words

    def find(self, word):
        find_dict = {}
        for name in self.file_names:
            for key, value in self.get_all_words().items():
                for i in value:
                    if i == word.lower():
                        find_dict[key] = value.index(i) + 1
        if len(find_dict) > 0:
            return find_dict
        else:
            return f'Слово не найдено'

    def count(self, word):
        count_dict = {}
        for name in self.file_names:
            for key, value in self.get_all_words().items():
                count_ = 0
                for i in value:
                    if i == word.lower():
                        count_ += 1
                        count_dict[key] = count_
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
print()

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
