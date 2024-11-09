from rest_framework.serializers import ModelSerializer
from verbs.models import Verb,VerbCharacteristic

class VerbCharacteristicSerializer(ModelSerializer):

    class Meta:

        model = VerbCharacteristic
        fields = '__all__'


class VerbSerializer(ModelSerializer):

    characteristics = VerbCharacteristicSerializer(many=True)
    class Meta:

        model = Verb
        fields = '__all__'