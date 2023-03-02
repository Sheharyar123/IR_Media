from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "md-input", "placeholder": "First Name *"}
        ),
    )
    last_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "md-input", "placeholder": "Last Name *"}
        ),
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={"class": "md-input", "placeholder": "Email *"}),
    )
    phone_no = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "md-input", "placeholder": "Phone No *"}
        ),
    )
    subject = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput({"class": "md-input", "placeholder": "Subject"}),
    )
    project_details = forms.CharField(
        max_length=5000,
        required=True,
        widget=forms.Textarea(
            attrs={"class": "md-textarea", "placeholder": "Project Details"}
        ),
    )
