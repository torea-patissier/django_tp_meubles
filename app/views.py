from rest_framework.viewsets import ModelViewSet
from .models import Dirigeant, Magasin, Meuble
from .serializers import SerializerDirigeant, SerializerMagasin, SerializerMeuble
from rest_framework.permissions import IsAuthenticated


class DirigeantViewSet(ModelViewSet):
    serializer_class = SerializerDirigeant
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Dirigeant.objects.all()

        nomparam = self.request.GET.get('nom')
        prenomparam = self.request.GET.get('prenom')

        if nomparam is not None:
            queryset = queryset.filter(nom=nomparam)

        if prenomparam is not None:
            queryset = queryset.filter(style=prenomparam)

        return queryset


class MagasinViewSet(ModelViewSet):
    serializer_class = SerializerMagasin

    def get_queryset(self):

        queryset = Magasin.objects.all()

        nomparam = self.request.GET.get('nom')
        adresseparam = self.request.GET.get('adresse')
        dirigeant = self.request.GET.get('dirigeant')
        ca = self.request.GET.get('ca')

        if nomparam is not None:
            queryset = queryset.filter(nom=nomparam)

        if adresseparam is not None:
            queryset = queryset.filter(style=adresseparam)

        if dirigeant is not None:
            queryset = queryset.filter(style=dirigeant)

        if ca is not None:
            queryset = queryset.filter(style=ca)

        return queryset


class MeubleViewSet(ModelViewSet):
    serializer_class = SerializerMeuble

    def get_queryset(self):

        queryset = Meuble.objects.all()

        nomparam = self.request.GET.get('nom')
        etat = self.request.GET.get('etat')
        magasin = self.request.GET.get('magasin')
        prix = self.request.GET.get('prix')
        statut = self.request.GET.get('statut')

        if nomparam is not None:
            queryset = queryset.filter(nom=nomparam)

        if etat is not None:
            queryset = queryset.filter(style=etat)

        if magasin is not None:
            queryset = queryset.filter(style=magasin)

        if prix is not None:
            queryset = queryset.filter(style=prix)

        if statut is not None:
            queryset = queryset.filter(style=statut)

        return queryset
