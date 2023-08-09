from rest_framework import serializers
from .models import InputModel,lifeeazyModel


class IvinSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputModel
        fields = '__all__'

class IvinProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputModel
        fields = ['Project_Name']

class lifeeazySerializer(serializers.ModelSerializer):
    objects = None

    class Meta:
        model = lifeeazyModel
        fields = '__all__'

class lifeeazyProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = lifeeazyModel
        fields = ['Project_Name']





    # def create(self, validated_data):
    #     instances = [InputModel(**item) for item in validated_data]
    #     return InputModel.objects.bulk_create(instances)


