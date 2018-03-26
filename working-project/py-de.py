import requests

myFile = requests.get('http://www.gutenberg.org/files/1342/1342-0.txt')

playFile = open('PrideAndPrejudice.txt', 'wb')

len(myFile.text)
print(myFile.text[:500])

for i in myFile.iter_content(100000):
    playFile.write(i)
playFile.close()
