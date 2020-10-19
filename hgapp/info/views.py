from django.shortcuts import render
from .terms import EULA, TERMS, PRIVACY

def getting_started(request):
    return render(request, 'info/getting_started.html')

def terms(request):
    context= {
        "terms": TERMS,
        "eula": EULA,
        "privacy": PRIVACY,
    }
    return render(request, 'info/terms.html', context)