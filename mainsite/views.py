from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginWithCaptchaForm
from .models import Member, MemberMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, '帳號已被註冊')
        elif User.objects.filter(email=email).exists():
            messages.error(request, '信箱已被註冊')
        elif not username or not password or not email or not nickname:
            messages.error(request, '所有欄位都必填')
        elif len(password) < 6 or not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
            messages.error(request, '密碼需至少6碼，且同時包含英文字母與數字')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=nickname)
            messages.success(request, '註冊成功，請登入')
            return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        form = LoginWithCaptchaForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, "登入成功")
                return redirect('/')
            else:
                messages.error(request, "帳號或密碼錯誤")
    else:
        form = LoginWithCaptchaForm()
    return render(request, 'login.html', {'form': form})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'index.html', locals() )

@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    messages = member.messages.order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        image = request.FILES.get('image')
        if content or image:
            MemberMessage.objects.create(
                member=member,
                user=request.user,
                content=content,
                image=image
            )
            return redirect('member_detail', pk=member.pk)
    return render(request, 'member_detail.html', locals() )
