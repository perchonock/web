__author__ = 'adm'
from urllib.request import urlopen
response = urlopen('https://en.wikipedia.org/wiki/Pornography')
html = response.read()
code = response.getcode()
print(code)
print(html)
file = open("C:\Yana\porn.txt", 'w')
file.write(str(html))
file.close()