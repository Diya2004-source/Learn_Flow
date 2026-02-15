from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#modeSerializer automatically generate fields based on the model.
#fields specifies which model to expose via the API.
