__author__ = 'adm'
file = open("porn.txt", 'r')

class WordCounter:
    def count_words(self, file):
        text = file.read()
        porn_position = 0
        search_position = 0
        positions_of_porn = 0
        while porn_position != -1:
            porn_position = text.find('porn',search_position)
            search_position = porn_position + 1
            if porn_position != -1:
                positions_of_porn += 1
        return positions_of_porn

#counter = WordCounter()
#print(counter.count_words(file))

file.close()