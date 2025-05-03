from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items

# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')
        data = BookTable.objects.create(Name=name, Phone_number=phone_number,
                                  Email=email, Total_person=int(total_person),
                                  Booking_date=booking_data)  
    return render(request, 'book_table.html')


def FeedbackView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        image = request.FILES.get('image')

        if user_name and description and rating:
            feedback = Feedback(Name=user_name, Description=description, Rating=rating)
            if image:
                feedback.Image = image
            feedback.save()
            message = "Thank you for your feedback!"
            return render(request, 'feedback.html', {'message': message})
        else:
            error = "Please fill in all required fields."
            return render(request, 'feedback.html', {'error': error})
    else:
        return render(request, 'feedback.html')


def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def LogoutView(request):
    logout(request)
    return redirect('home')


# Cart views

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('menu')


def add_to_cart_and_checkout(request, item_id):
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('checkout')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for item_id, quantity in cart.items():
        try:
            item = Items.objects.get(id=item_id)
            item_total = item.price * quantity
            total_price += item_total
            cart_items.append({'item': item, 'quantity': quantity, 'total': item_total})
        except Items.DoesNotExist:
            pass
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id, None)
        request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(item_id, None)
    request.session['cart'] = cart
    return redirect('view_cart')


def checkout(request):
    if request.method == 'POST':
        payment_mode = request.POST.get('payment_mode')
        address = request.POST.get('address')
        # Here you can save payment_mode and address to database or session as needed
        request.session['payment_mode'] = payment_mode
        request.session['address'] = address
        return redirect('payment_success')
    else:
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = 0
        for item_id, quantity in cart.items():
            try:
                item = Items.objects.get(id=item_id)
                item_total = item.Price * quantity
                total_price += item_total
                cart_items.append({'item': item, 'quantity': quantity, 'total': item_total})
            except Items.DoesNotExist:
                pass
        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})


def payment_success(request):
    payment_mode = request.session.get('payment_mode', 'N/A')
    address = request.session.get('address', 'N/A')
    # Clear the cart and payment info after payment
    if 'cart' in request.session:
        del request.session['cart']
    if 'payment_mode' in request.session:
        del request.session['payment_mode']
    if 'address' in request.session:
        del request.session['address']
    return render(request, 'payment_success.html', {'payment_mode': payment_mode, 'address': address})
