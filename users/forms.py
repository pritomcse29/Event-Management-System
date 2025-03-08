from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission, User
from django.contrib.auth.models import Group
class StyledFormMixin:
    """ Mixing to apply style to form field"""

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()

    default_classes = "w-full p-3 border rounded-md"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            label = field.label or field_name.replace("_", " ")  
            placeholder_text = f"Enter {label.lower()}"
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': placeholder_text
                })
            elif isinstance(field.widget,forms.PasswordInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder': placeholder_text
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':placeholder_text
                })
   
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })


class CustomRegistrationForm(StyledFormMixin,forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password1','confirm_password','first_name','last_name']
    def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            errors =[]

            if len(password1)<8:
                errors.append("Password must be at least 8 characters")
            if not re.search(r'[a-z]',password1):
                errors.append("Password must include at least one lowercase letter")
            if not re.search(r'[A-Z]',password1):
               errors.append("Password must include at least One Uppercase letter")
            if not re.search(r'\d',password1):
                errors.append("Password must include at least one number")
            if errors:
                raise ValidationError(errors)
            return password1

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        error = []
        if not email:
            error.append("Email field can not be empty")
        if User.objects.filter(email=email).exists():
            error.append("This email is already registered")
        if error:
            raise forms.ValidationError(error)
        return email
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')
        if password1 != confirm_password:
            raise ValidationError("password do not match")
        return cleaned_data

class loginForm (StyledFormMixin,AuthenticationForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class AssignROleForm(StyledFormMixin,forms.Form):
    role=forms.ModelChoiceField(
        queryset = Group.objects.all(),
        label="Select a Role"
    )
class CreateGroup(StyledFormMixin,forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset= Permission.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
        label='Assign Permission'
    )
    class Meta:
        model = Group
        fields = ['name','permissions']

