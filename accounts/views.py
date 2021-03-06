from distutils.log import error
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView


# Create your views here.

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,  # Unauthenticated users must be able to sign up
    ]
    serializer_class = UserSerializer

# class UserAccounts(generics.RetrieveUpdateDestroyAPIView):
    # queryset = CustomUser.objects.all()
    # serializer_class = CustomUserSerializer

# def sign_up(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('accounts/login.html')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect()
#     else:
#         return error('invalid login')

# def logout(request):
#     logout(request)
#     return redirect('account/login.html')