from verbs.models import Verb
from .serializers import VerbSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class VerbViewSet(ReadOnlyModelViewSet):

    queryset = Verb.objects.all()
    serializer_class = VerbSerializer