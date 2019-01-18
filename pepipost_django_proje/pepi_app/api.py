from django import forms


class ContactApi(forms.Form):
    api_key = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Enter API key'
            }
        ),
        required=True)

    sender = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Sender'
            }
        ),
        required=True)

    receiver = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Recipient'
            }
        ),
        required=True)

    message = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder':'Message'
            }
        ),
        required=True)