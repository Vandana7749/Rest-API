from rest_framework import serializers
#from rest_framework import colstudent
from .models import colstudent

class colstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = colstudent
        fields = '__all__'