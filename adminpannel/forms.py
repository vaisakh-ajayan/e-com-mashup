from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class ProductForm(forms.Form):
    product_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'product name'}
            ), max_length=200, required=True
        )

    product_description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control', 'placeholder':'product description', 'rows':5}
            ), max_length=2000, required=True
        )

    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'product price'}), required=True
        )

    product_image = forms.FileField(
        widget=forms.FileInput(attrs={'class':'form-control', 'multiple':False}), required=True
        )


class EditProductForm(forms.Form):
    product_name = forms.CharField(
        max_length=200, required=True, widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'product name'}
            )
        )
    product_description = forms.CharField(
        max_length=2000, required=True, widget=forms.Textarea(
            attrs={'class':'form-control', 'placeholder':'product description', 'rows':5}
            )
        )
    price = forms.FloatField(
        required=True, widget=forms.NumberInput(
            attrs={'class':'form-control', 'placeholder':'product price'}
            )
        )
    product_image = forms.FileField(
        required=True, widget=forms.FileInput(
            attrs={'class':'form-control', 'multiple':False}
            )
        )