from rest_framework import serializers

from cuboid.models import Cuboid

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

        
class CuboidSerializer(serializers.ModelSerializer): # forms.ModelForm
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cuboid
        fields = [
            'url',
            'id',
            'user',
            'length',
            'breadth',
            'height',
            'area',
            'volume',
            'timestamp',
        ]
        read_only_fields = ['id', 'user','area','volume']

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)
        