from rest_framework import serializers
from app.models import Dirigeant, Magasin, Meuble


class SerializerDirigeant(serializers.ModelSerializer):
    class Meta:
        model = Dirigeant
        fields = ['nom', 'prenom']


class SerializerMagasin(serializers.ModelSerializer):
    class Meta:
        model = Magasin
        fields = ['nom', 'adresse','dirigeant','ca']


class SerializerMeuble(serializers.ModelSerializer):
    class Meta:
        model = Meuble
        fields = ['nom', 'etat','magasin','prix','statut']

