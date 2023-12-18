import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')[3].getText()

print(parrafo_especial)

columna_lateral = sopa.select('.widget-content a')

for a in columna_lateral:
    print(a.getText())

sitio_web = requests.get('https://www.escueladirecta.com/courses')
sopa_web = bs4.BeautifulSoup(sitio_web.text, 'lxml')
imagenes = sopa_web.select('.course-box-image')

for img in imagenes:
    imagen = requests.get(img['src'])
    f = open('mi_imagen.jpg', 'wb')
    f.write(imagen.content)
    f.close()

