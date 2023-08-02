from rest_framework import serializers
from .models import InputModel,lifeeazyModel


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputModel
        fields = '__all__'
class lifeSerializer(serializers.ModelSerializer):
    objects = None

    class Meta:
        model = lifeeazyModel
        fields = '__all__'

class lifeeazySerializer(serializers.ModelSerializer):

    class Meta:
        model = lifeeazyModel
        fields = ['Project_Name']

class MydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputModel
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputModel
        fields = ['Project_Name']


    # def create(self, validated_data):
    #     instances = [InputModel(**item) for item in validated_data]
    #     return InputModel.objects.bulk_create(instances)


