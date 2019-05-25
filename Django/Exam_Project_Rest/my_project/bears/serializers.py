from rest_framework import serializers

from .models import Bear, ProfileUser


class BearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bear
        fields = ('__all__')


class BearCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bear
        fields = ('color', 'price')

    def create(self, validated_data):
        owner = ProfileUser.objects.get(user__pk=self.context['request'].user.id)
        validated_data['owner'] = owner
        validated_data['type'] = "ies"
        return super(BearCreateSerializer, self).create(validated_data)
