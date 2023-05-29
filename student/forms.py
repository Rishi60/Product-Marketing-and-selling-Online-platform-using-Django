from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
class SignUpForm(UserCreationForm):
	student_name = forms.CharField(
		label='Student Name',
		max_length=50,
		help_text='Enter your full name'
	)
	email = forms.EmailField(
		max_length=254,
		required=True,
		help_text='Please enter a valid email address.'
	)
	#phone_number = PhoneNumberField(max_length=13,  required=True, help_text='Enter your phone number')
	phone_number = forms.CharField(
		label='Phone Number',
		max_length=15,
		required=True,
		help_text='Enter your phone number'
	)
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = 'Please enter College ID <strong>Eg: 15011011C03636</strong>'

	class Meta:
		model = User
		fields = ('username', 'student_name' , 'email', 'phone_number', 'password1', 'password2', )
		widgets = {
			'username': forms.TextInput(),
			'student_name':forms.TextInput(),
			'email':forms.TextInput(),
			'phone_number':forms.TextInput(),
			'password1':forms.TextInput(),
			'password2':forms.TextInput()
		}
class SearchForm(forms.Form):
	search_item = forms.CharField(
		label='Search here',
		max_length=50,
		help_text='Enter product to search'
	)

	class Meta:
		model = User
		fields = ('search_item', )
		widgets = {
			'search_item': forms.TextInput(),
		}


class BuyForm(forms.Form):
	cnf_item = forms.CharField(
		label='ConfirmName',
		max_length=50,
	)
	use_name = forms.CharField(
		label='Your Name',
		max_length=50,
	)
	address = forms.CharField(
		label='Full Address',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('cnf_item','use_name','address', )
		widgets = {
			'cnf_item': forms.TextInput(),
			'use_name': forms.TextInput(),
			'address': forms.TextInput(),
		}


class CatForm(forms.Form):
	cat_item = forms.CharField(
		label='Category',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('cat_item', )
		widgets = {
			'cat_item': forms.TextInput(),
		}