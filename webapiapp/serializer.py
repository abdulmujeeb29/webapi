from rest_framework import serializers
from .models import *


class buisSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model =buisnessProfile
    

    def create(self, validated_data):
        validated_data['business_name'] += " Nigeria limited "
    
        return buisnessProfile.objects.create(**validated_data)
    
    