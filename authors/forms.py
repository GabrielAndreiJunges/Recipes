from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attr[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['email'], 'Type your e-mail')
        add_placeholder(self.fields['first_name'],
                        'Type your first name Ex.: John')
        add_placeholder(self.fields['last_name'],
                        'Type your last name Ex.: Doe')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8'
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8'
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty.',
            }
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username',
                'class': 'input text-input'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password'
            })
        }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [password_confirmation_error,],
            })
