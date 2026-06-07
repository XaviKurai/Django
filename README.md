# Django
Repositori per Django
# Blog Django M3-UF6

## Introducció
Aquest projecte és un blog desenvolupat amb Django com a part del projecte de l'assignatura M485 Programació. 
L'objectiu principal és aprendre a crear aplicacions web amb Django, incloent models, vistes, templates i base de dades.

## Instal·lació ràpida

### Clonar el repositori
```bash
git clone https://github.com/XaviKurai/Django.git
cd Django
```

### Instal·lar dependències
```bash
pip install -r requirements.txt
```

### Executar migracions
```bash
python manage.py migrate
python manage.py loaddata blog/fixtures/initial_data.json
```

## Execució del projecte
```bash
python manage.py runserver
```
Accedeix a: http://127.0.0.1:8000

## Rutes disponibles
- `/` - Pàgina principal amb els 3 últims posts
- `/posts` - Llistat de tots els posts
- `/posts/<slug>` - Detall d'un post
- `/authors` - Llistat d'autors
- `/authors/<id>` - Detall d'un autor
- `/tags` - Llistat de tags
- `/tags/<id>` - Posts d'una tag

## Documentació Pydoc
- [blog.views](blob/main/blog.views.html)
- [blog.models](blob/main/blog.models.html)
