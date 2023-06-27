from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input checkout_input_50', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input checkout_input_50', 'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'checkout_input', 'placeholder': 'Электронная почта'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input', 'placeholder': 'Адрес'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input', 'placeholder': 'Город'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input checkout_input_50', 'placeholder': 'Почтовый индекс'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'checkout_input checkout_input_50', 'placeholder': 'Телефон'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']