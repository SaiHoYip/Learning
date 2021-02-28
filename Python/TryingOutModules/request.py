#pip install requests
import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(res.text[:500])

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
playFile = open('RomeoAndJuliet.txt', 'r')
contents = playFile.read()
print(contents)
playFile.close()