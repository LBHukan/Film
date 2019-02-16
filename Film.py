import requests
import json

name = input('Digite um Filme: ')

request = requests.get('http://www.omdbapi.com/?apikey=f8d7fe69&t=' + name)
js = json.loads(request.text)


print('Titulo: ' + js['Title'])
print('Ano: ' + js['Year'])
print('Duracao: ' + js['Runtime'])
print('Genero: ' + js['Genre'])
print('Idioma: ' + js['Language'])
print('Poster: ' + js['Poster'])