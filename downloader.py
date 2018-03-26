import requests

myBook = requests.get('http://www.gutenberg.org/files/1342/1342-0.txt')

playFile = open('PrideAndPrejudice.txt', 'wb')
#len(res.text)
#print(res.text[:250])
for i in myBook.iter_content(100000):
    playFile.write(i)
playFile.close()
