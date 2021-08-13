from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class':"form-control username",'placeholder':"username"}
		),required=True,
	)

	firstname = forms.CharField(widget=forms.TextInput(
		attrs={'class':"form-control",'placeholder':"firstname"}
		),required=True,
	)

	lastname = forms.CharField(widget=forms.TextInput(
		attrs={'class':"form-control","placeholder":"lastname"}
		),required=True,
	)

	emailid = forms.CharField(widget=forms.EmailInput(
		attrs={'class':"form-control",'placeholder':"email id"}
		),required=True,
	)

	password = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control",'placeholder':"password"}
		),required=True,
	)

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class':"form-control", 'placeholder':"username"}
		), required=True,
	)

	password = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':'form-control', 'placeholder':"password"}
		), required=True,
	)

class CustomerCheckoutForm(forms.Form):
	phone= forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'phone number'}
		),required=True, max_length=200,
	)

	address = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control','placeholder':'address'}
		), required=True, max_length=2000,
	)