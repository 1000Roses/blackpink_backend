from rest_framework import serializers
from blackpinkinfo.models import Song, Member, Prize

class SongSerializers(serializers.ModelSerializer):
    prize = serializers.StringRelatedField(many=True)
    class Meta:
        model = Song
        fields = ['name','release_date','prize']

class BlackpinkSerializers(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True)
    song = SongSerializers(many=True)
    class Meta:
        model = Member
        fields = ['name','age','description','song']
        