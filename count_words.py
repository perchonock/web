__author__ = 'adm'
file = open("C:\Yana\porn.txt", 'r')
text = file.read()
#text = 'this is porn and this is porn too'
porn_position = 0
search_position = 0
positions_of_porn = 0
while porn_position != -1:
    porn_position = text.find('porn',search_position)
    search_position = porn_position + 1
    if porn_position != -1:
        positions_of_porn += 1
print(positions_of_porn)
file.close()