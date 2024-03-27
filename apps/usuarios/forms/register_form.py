from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'movil', 'first_name', 'last_name', 'ci')