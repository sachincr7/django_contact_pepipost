from django import forms

class ContactForm(forms.Form):
    hostname = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter your hostname'
            }
        ),
        required=True)

    port = forms.IntegerField(
        widget = forms.NumberInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter Port No'
            }
        ),
        required=True)


    tls = forms.CharField(
        widget = forms.CheckboxInput(
            attrs = {
                'value': True
            }
        ),
        required=True)
    

    login = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter Username'
            }
        ),
        required=True)


    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter Password'
            }
        ),
        required=True)

    sender = forms.CharField(
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter Sender email id'
            }
        ),
        required=True)

    receiver = forms.CharField(
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter Receiver email id'
            }
        ),
        required=True)

        
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'md-textarea form-control',
                'placeholder':'Enter Receiver email id',
                'rows': 3,
                'placeholder': 'Enter message'
            }
        ),
        required=True)

    