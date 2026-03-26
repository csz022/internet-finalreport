from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class LoginWithCaptchaForm(AuthenticationForm):
    captcha = CaptchaField(label="請輸入下方驗證碼")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
