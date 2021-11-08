from rest_framework import serializers

from main.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = 'id title description cinema genres'.split()


