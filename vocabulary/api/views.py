from vocabulary.models import Country,Profession
from .serializers import CountrySerializer,ProfessionSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class CountryViewSet(ReadOnlyModelViewSet):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class ProfessionViewSet(ReadOnlyModelViewSet):

    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()

    