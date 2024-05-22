from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


def custom_admin_login(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse_lazy('admin:login'))
