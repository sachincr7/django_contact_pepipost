from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail, get_connection
from django.http import HttpRequest
import requests
import json


# Create your views here.

from .forms import ContactForm
from .api import ContactApi

def contact_us_auth(request):

    
    
    if request.method == 'POST':
        contact_auth = ContactForm(request.POST)
        contact_api = ContactApi(request.POST)
        if contact_auth.is_valid() :
            # contact_auth = ContactForm(request.POST)
            hostname = contact_auth.cleaned_data['hostname']
            portno = contact_auth.cleaned_data['port']
            sender = contact_auth.cleaned_data['sender']
            receiver = [contact_auth.cleaned_data['receiver']]
            message = contact_auth.cleaned_data['message']
            hostname = contact_auth.cleaned_data['hostname']
            user_id = contact_auth.cleaned_data['login']
            password = contact_auth.cleaned_data['password']
            tls = contact_auth.cleaned_data['tls']

            connection = get_connection(
                host = hostname,
                port = portno,
                username = user_id,
                password = password,
                tls = True
            )

            
            send_mail(
                  'Subject',
                   message,
                   sender,
                   receiver,
                   fail_silently = False,
                   connection = connection
            )

            

            return HttpResponse("thanks for contacting us")
        
        elif contact_api.is_valid():
            if contact_api.is_valid() :
                url = "https://api.pepipost.com/v2/sendEmail"

                api_key = contact_api.cleaned_data['api_key']
                receiver = contact_api.cleaned_data['receiver']
                sender = contact_api.cleaned_data['sender']
                message = contact_api.cleaned_data['message']

                payload =  {"personalizations":[{"recipient":  receiver  }],"from":{"fromEmail":sender,"fromName":"blacknova5912"},"subject":"Welcome to Pepipost","content":"Hi, this is my first trial mail"}
                
                payload = json.dumps(payload)
                headers = {
                    'content-type': "application/json",
                    'api_key': api_key
                }

                print(payload)
                response = requests.request("POST", url, data = payload, headers= headers)
        
                return HttpResponse(response)
                    
                    
                    
    else:
        contact_auth = ContactForm()
        contact_api = ContactApi()

    return render(request, 'form.htm', {
        "contact_auth": contact_auth,
        "contact_api": contact_api
        })


