class WordsFinder:
    def __init__(self, *names):
        self.file_names = [*names]
        with open(self, encoding='utf-8') as file:
            for name in names:



    def get_all_words(self):
        dict_ = {}
        dict_[self] = [*open(self)]



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего