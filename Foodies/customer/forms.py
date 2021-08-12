from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import CharField, DecimalField, IntegerField, RegexField
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = CharField(max_length=100)
    password1 = CharField(widget=PasswordInput)
    phone = DecimalField(max_digits=12, decimal_places=1)
    password2 = CharField(widget=PasswordInput)
    USERNAME_FIELD = 'phone'
    username.widget.attrs.update({'class':'form-input',
                                 'placeholder':'Username',
                                 'name':'username',
                                 'id':'name'})
    phone.widget.attrs.update({'class':'form-input',
                                 'placeholder':'Phone Number',
                                 'name':'phone',
                                 'id':'email'})
    password1.widget.attrs.update({'class':'form-input',
                                 'placeholder':'Password',
                                 'name':'password',
                                 'id':'password'

    })
    password2.widget.attrs.update({'class':'form-input',
                                 'placeholder':'Password',
                                 'name':'password',
                                 'id':'password'

    })
    # class Meta:
    #     model = User
    #     fields = ('username','phone','password1','password2')
