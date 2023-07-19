import requests
from bs4 import BeautifulSoup
import io

url = 'https://pt.wikipedia.org/wiki/Ivar,_o_Desossado'

headers = {'User-Agent': 'Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Success on retrieving the Webpage! :D')
else:
    print('Failed to retrieve the webpage! :c')

soup = BeautifulSoup(response.text, "html.parser")

heading = soup.find("h1").text
print(heading)

# links = [a["href"] for a in soup.find_all("a")]

Textao = soup.find_all("p")

with io.open("Ivar O Desossado.txt", "w", encoding="utf-8") as file:
    file.write(heading + "\n")
    file.write(Textao.get_text())
    file.close()
