from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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
    RegisterSerializer,
    LoginSerializer,
    UserSerializer
)




class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'user': UserSerializer(user).data, 'token': token.key},
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({'detail': 'Chiqildi.'}, status=status.HTTP_200_OK)




class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user



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