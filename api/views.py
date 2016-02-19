from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                                {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')




def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('user', user_id=user.id)

    return render(request, 'api/create_user.html', {'form': form})


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'api/user.html', {'user': user})
