from rest_framework import viewsets, permissions
from .models import Webpage, Session, Viewer
from .serializers import WebpageSerializer, SessionSerializer, ViewerSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
import random
import string

class WebpageViewSet(viewsets.ModelViewSet):
    queryset = Webpage.objects.all()
    serializer_class = WebpageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Generate a unique 6-character code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        session = Session.objects.create(host=request.user, code=code)
        serializer = self.get_serializer(session)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        session = self.get_object()
        identifier = request.data.get('identifier')
        if not identifier:
            return Response({'error': 'Identifier is required'}, status=400)
        Viewer.objects.create(session=session, identifier=identifier)
        return Response({'status': 'Viewer added'})

class ViewerViewSet(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
