from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(max_length=50, label='Enter email')
    password = forms.CharField(widget=forms.PasswordInput, label='Enter password')    

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')

        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError('This username is already used')

        # if password != conf_password:
        #     raise forms.ValidationError('passwords must match')

        return username