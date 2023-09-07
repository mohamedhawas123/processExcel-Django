from rest_framework import serializers
from .models import Excel


class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excel
        fields= '__all__'