from django.shortcuts import redirect, render, get_object_or_404
from .forms import UserForm
from .models import User


# Create your views here.

def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('user', user_id=user.id)

    return render(request, 'api/create_user.html', {'form': form})


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'api/user.html', {'user': user})
