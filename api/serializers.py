from rest_framework import serializers
from .models import (
    Conference,
    WordPart,
    Shoba,
    Maqola,
    AboutShoba
)


class DownloadConferenceWordFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = ['word_fayl']




class WordPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):  
    class Meta:
        model = AboutShoba
        fields = '__all__'


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'

class AboutmoqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = 'title'


class ShobaSerializer(serializers.ModelSerializer):
    maqolalar = MaqolaSerializer(many=True, read_only=True)
    about = AboutSerializer(many=True, read_only=True)

    class Meta:
        model = Shoba
        fields = '__all__'




class ConferenceSerializer(serializers.ModelSerializer):
    word_parts = WordPartSerializer(many=True, read_only=True)
    shobalar = ShobaSerializer(many=True, read_only=True)


    
    model = Conference
    fields = '__all__'