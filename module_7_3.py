class WordsFinder:
    def __init__(self, *names):
        self.__file_index = 1
        self.file_names = []
        self.file_names.append(*names)
        file = open(f'file{self.__file_index}.txt', 'x', encoding='utf-8')
        file.close()
        self.__file_index += 1
        

    def get_all_words(self):
        all_word = {}
        all_word[self] = [*open(self)]



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего