# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Contact
from .serializers import ContactSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
 
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        # Filter contacts by the logged-in user
        return self.queryset.filter(user=self.request.user)
 
    def perform_create(self, serializer):
        # Associate the new contact with the logged-in user
        serializer.save(user=self.request.user)
 
class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
 
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)
 
class LoginView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):
        from django.contrib.auth import authenticate
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)