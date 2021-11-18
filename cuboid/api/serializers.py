from rest_framework import serializers

from cuboid.models import Cuboid


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
        