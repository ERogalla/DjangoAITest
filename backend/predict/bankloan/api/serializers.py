from rest_framework import serializers
from bankloan.models import bankloan

class bankloanSerializer(serializers.ModelSerializer):
    class Meta:
        model = bankloan
        fields = ('__all__')