from vocabulary.models import Country,Profession
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):

    class Meta:

        model = Country
        fields = "__all__"

class  ProfessionSerializer(ModelSerializer):

    class Meta:

        model = Profession
        fields = "__all__"