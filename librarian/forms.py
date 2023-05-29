from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from phonenumber_field.modelfields import PhoneNumberField
class SignUpForm(UserCreationForm):
    librarian_name = forms.CharField(
        label='Customer Name',
        max_length=50,

    )
    email = forms.EmailField(
        label='Email',
        max_length=254,
        required=True,
    )
    # phone_number = PhoneNumberField(max_length=13,  required=True, help_text='Enter your phone number')
    phone_number = forms.CharField(
        label='Address and Phone No. ',
        max_length=15,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Enter name you want to prefer when you login <strong>text here</strong>'

    class Meta:
        model = User
        fields = ('username', 'librarian_name', 'email', 'phone_number', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(),
            'librarian_name': forms.TextInput(),
            'email': forms.TextInput(),
            'phone_number': forms.TextInput(),
            'password1': forms.TextInput(),
            'password2': forms.TextInput()
        }


class AddBookForm(forms.Form):
    title = forms.CharField(label='product or service', required=True)
    author = forms.CharField(label='Your company', required=True)
    publication = forms.CharField(label='Description', required=True)
    category = forms.CharField(label='Category E.g:-Electronics', required=True)
    unique_id = forms.CharField(label='Price', required=True)

    class Meta:
        model = User
        fields = ('title', 'author', 'publication','category','unique_id',)
        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput(),
            'publication': forms.TextInput(),
            'category': forms.TextInput(),
            'unique_id': forms.TextInput(),
        }

