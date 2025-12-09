# core/forms.py  (substitua a parte do validar_cpf_format / clean_cpf)
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

def only_digits(value: str) -> str:
    return re.sub(r'\D', '', value or '')

def validar_cpf_format(cpf: str) -> bool:
    """
    Retorna True se, após remover não-dígitos, o CPF tiver 11 dígitos.
    (não faz validação de dígito verificador, apenas formato)
    """
    digits = only_digits(cpf)
    return len(digits) == 11

class RegisterForm(forms.ModelForm):
    cpf = forms.CharField(max_length=20, required=True, help_text="000.000.000-00 ou 00000000000")
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar senha")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_cpf(self):
        cpf_raw = self.cleaned_data.get('cpf', '')
        digits = only_digits(cpf_raw)
        if len(digits) != 11:
            raise ValidationError("CPF inválido: deve conter 11 dígitos (com ou sem pontuação).")
        # usar os 11 dígitos como username
        if User.objects.filter(username=digits).exists():
            raise ValidationError("CPF já cadastrado.")
        return digits  # retornamos apenas os dígitos para save()

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Senhas não conferem.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        # aqui assumimos que clean_cpf retornou apenas dígitos
        user.username = self.cleaned_data.get('cpf')
        user.set_password(self.cleaned_data.get('password'))
        user.is_active = False  # aguardando aprovação
        if commit:
            user.save()
        return user
