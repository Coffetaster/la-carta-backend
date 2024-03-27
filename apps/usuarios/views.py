from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from apps.usuarios.forms.register_form import CustomUserCreationForm

def register_asequible(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='asequible')
            group.user_set.add(user)
            # Redireccionar al inicio de sesión o a otra página después del registro
            return redirect('/admin/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def register_recomendado(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='recomendado')
            group.user_set.add(user)
            # Redireccionar al inicio de sesión o a otra página después del registro
            return redirect('/admin/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register2.html', {'form': form})


def register_premium(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='premium')
            group.user_set.add(user)
            # Redireccionar al inicio de sesión o a otra página después del registro
            return redirect('/admin/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register3.html', {'form': form})