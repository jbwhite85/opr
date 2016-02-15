from django.shortcuts import render
import io
from django.conf import settings
import os
from .forms import UserForm


# Create your views here.

def create_user(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
    	user = form.save()
    	return redirect('user', user_id=user.id)

	return render(request, 'api/create_user.html', {'form': form})
