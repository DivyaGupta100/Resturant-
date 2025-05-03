from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemListViewSet, ItemsViewSet, FeedbackViewSet, BookTableViewSet, AboutUsViewSet

router = DefaultRouter()
router.register(r'itemlists', ItemListViewSet)
router.register(r'items', ItemsViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'booktables', BookTableViewSet)
router.register(r'aboutus', AboutUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
