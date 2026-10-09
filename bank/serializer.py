from rest_framework import serializers
from .models import Checks

class ChecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checks
        fields = '__all__'
        read_only_fields = ('id',)