from rest_framework import serializers
from .models import *


class buisSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model =buisnessProfile
