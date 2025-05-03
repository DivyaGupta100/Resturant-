from django.urls import path
from .views import HomeView, AboutView, MenuView, BookTableView, FeedbackView, RegisterView, LoginView, LogoutView, add_to_cart, add_to_cart_and_checkout, view_cart, update_cart, remove_from_cart, checkout, payment_success

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('menu/', MenuView, name='menu'),
    path('booktable/', BookTableView, name='booktable'),
    path('feedback/', FeedbackView, name='feedback_form'),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),

    # Cart URLs
    path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/add_checkout/<int:item_id>/', add_to_cart_and_checkout, name='add_to_cart_and_checkout'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/update/<int:item_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    # Checkout and payment URLs
    path('checkout/', checkout, name='checkout'),
    path('payment-success/', payment_success, name='payment_success'),
]
