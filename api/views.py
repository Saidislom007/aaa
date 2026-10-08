from rest_framework import generics

from .models import (
    Conference,
    Maqola,
    AboutShoba,
    Shoba,
    WordPart,
)

from .serializers import (
    ConferenceSerializer,
    AboutSerializer,      
    MaqolaSerializer,
    WordPartSerializer,
    ShobaSerializer,
    DownloadConferenceWordFileSerializer,
)







class GetConference(generics.ListAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class GetOneConference(generics.RetrieveAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    lookup_field = 'id'


class GetMaqola(generics.ListAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer


class GetOneMaqola(generics.RetrieveAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    lookup_field = 'id'


class GetAboutShoba(generics.ListAPIView):
    queryset = AboutShoba.objects.all()
    serializer_class = AboutSerializer


class GetOneAboutShoba(generics.RetrieveAPIView):
    queryset = AboutShoba.objects.all()
    serializer_class = AboutSerializer
    lookup_field = 'id'


class GetShoba(generics.ListAPIView):
    queryset = Shoba.objects.all()
    serializer_class = ShobaSerializer


class GetOneShoba(generics.RetrieveAPIView):
    queryset = Shoba.objects.all()
    serializer_class = ShobaSerializer
    lookup_field = 'id'


class GetWordPart(generics.ListAPIView):
    queryset = WordPart.objects.all()
    serializer_class = WordPartSerializer


class GetOneWordPart(generics.RetrieveAPIView):
    queryset = WordPart.objects.all()
    serializer_class = WordPartSerializer
    lookup_field = 'id'

class DownloadConferenceWordFileView(generics.RetrieveAPIView):
    queryset = WordPart.objects.all()
    serializer_class = DownloadConferenceWordFileSerializer
    lookup_field = 'id'