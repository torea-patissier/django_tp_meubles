## Lancer l'application

`python3 manage.py runserver`

### Aller sur l'URL:

`http://127.0.0.1:8000/admin/`

### S'authentifier

`http://127.0.0.1:8000/api/token/`

- Une fois authentifier, récupérer l'access token

### Utilisation

- Check urls.py
- Pour `router.register('meuble', MeubleViewSet, basename='meuble')`
- Aller sur `http://127.0.0.1:8000/api/meuble/`


