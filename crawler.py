import request
from bs4 import beautifulsoup

anchieta + 'https://anchieta.br'
r = request.get(anchieta)
html_anchieta = r.text

soup = beautifulsoup(html_anchieta)
for elem in soup .find_all('div', class_='elementor-widget-container'):
    print(elem.text)

