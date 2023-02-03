from django.db import models


class Dirigeant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)


class Magasin(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    dirigeant = models.ForeignKey(Dirigeant, on_delete=models.CASCADE)
    ca = models.DecimalField(max_digits=10, decimal_places=2)


class Meuble(models.Model):
    NEUF = 'NEUF'
    OCCASION = 'OCCASION'
    MAUVAIS_ETAT = 'MAUVAIS ETAT'
    INUTILISABLE = 'INUTILISABLE'
    ETAT_CHOICES = [
        (NEUF, 'Neuf'),
        (OCCASION, 'Occasion'),
        (MAUVAIS_ETAT, 'Mauvais Etat'),
        (INUTILISABLE, 'Inutilisable'),
    ]

    LIBRE = 'LIBRE'
    VENDU = 'VENDU'
    STATUT_CHOICES = [
        (LIBRE, 'Libre'),
        (VENDU, 'Vendu'),
    ]

    nom = models.CharField(max_length=100)
    etat = models.CharField(max_length=100, choices=ETAT_CHOICES, default=NEUF)
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES, default=LIBRE)
