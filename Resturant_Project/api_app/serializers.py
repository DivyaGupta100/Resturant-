from rest_framework import serializers
from Base_App.models import ItemList, Items, Feedback, BookTable, AboutUs

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
