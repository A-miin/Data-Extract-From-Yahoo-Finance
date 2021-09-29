from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from yahoo_scraping.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        read_only_fields = ('id', )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not Data.objects.filter(**attrs).exists():
            Data.objects.create(**attrs)
        return attrs
