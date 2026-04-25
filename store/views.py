from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Product
from blog.models import Message

def home(request):
    return render(request, 'store/home.html')

def product_list(request, residence):
    products = Product.objects.filter(residence=residence, stock__gt=0).order_by('-created_at')
    residence_names = {
        '1': 'إقامة 1',
        '2': 'إقامة 2',
        '3': 'إقامة 3',
        'outside': 'خارج الإقامة',
    }
    residence_name = residence_names.get(residence, 'إقامة')
    return render(request, 'store/product_list.html', {
        'products': products,
        'residence': residence,
        'residence_name': residence_name,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            seller=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            shipping=request.POST.get('shipping', ''),
            wilaya=request.POST.get('wilaya', ''),
            phone=request.POST.get('phone', ''),
            residence=request.POST['residence'],
            image=request.FILES.get('image'),
        )
        return redirect('home')
    return render(request, 'store/add_product.html')

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.seller == request.user:
        product.delete()
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email    = request.POST['email']
        if User.objects.filter(username=username).exists():
            error = 'اسم المستخدم موجود مسبقاً'
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')
    return render(request, 'store/register.html', {'error': error})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

@login_required
def inbox(request):
    inbox_messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'store/inbox.html', {'inbox_messages': inbox_messages})

@login_required
def profile(request):
    error   = ''
    success = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_info':
            user = request.user
            user.first_name = request.POST.get('first_name', '')
            user.last_name  = request.POST.get('last_name', '')
            user.email      = request.POST.get('email', '')
            user.save()
            success = 'تم تحديث المعلومات بنجاح! ✅'

        elif action == 'change_password':
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                success = 'تم تغيير كلمة المرور بنجاح! ✅'
            else:
                error = 'كلمة المرور القديمة خاطئة! ❌'

    return render(request, 'store/profile.html', {
        'error':   error,
        'success': success,
    })