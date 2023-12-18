import bs4
import requests

# crear url sin numero de pagino
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1,51):

    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar en los libros
    for libro in libros:

        # comprobar que tengan 4 o 5 estrelas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Guardar titulo en variable
            titulo = libro.select('a')[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(titulo)


# ver los libro de 4 y 5 estrellas
for title in titulos_rating_alto:
    print(title)
