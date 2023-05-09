from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import LoginForm, SignupForm

User = get_user_model()


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=255, label="Full Name")
    phone_no = forms.CharField(max_length=20, label="Phone No")

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields[f]
            field.widget.attrs.update({"class": "form-control", "placeholder": ""})
            if field.label == "Password (again)":
                field.label = "Confirm Password"

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        try:
            user.name = self.cleaned_data["name"]
            user.phone_no = self.cleaned_data["phone_no"]
            user.save()
        except:
            pass
        return user
