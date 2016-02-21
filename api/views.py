from django.shortcuts import redirect, render, get_object_or_404
from .forms import UserForm
from .models import User
from django.contrib import auth


# Create your views here.
def login(request):
    return render(request, 'login.html', {})


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('loggedin')
    else:
        return redirect('invalid_login')


def loggedin(request):
    return render(request, 'loggedin.html',
                  {'full_name': request.user.username})


def invalid_login(request):
    return render(request, 'invalid_login.html', {})


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', {})


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('user', user_id=user.id)

    return render(request, 'api/create_user.html', {'form': form})


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'api/user.html', {'user': user})
