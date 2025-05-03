from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from Base_App.models import ItemList, Items, Feedback, BookTable, AboutUs
from .serializers import ItemListSerializer, ItemsSerializer, FeedbackSerializer, BookTableSerializer, AboutUsSerializer

class ItemListViewSet(viewsets.ModelViewSet):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookTableViewSet(viewsets.ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
