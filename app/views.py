from django.shortcuts import render
from datetime import datetime
from .scripts import *

# Create your views here.
def home(request):
    g = datetime.today().strftime('%Y-%m-%d')
    data = freetips(g)
    {
        "data": data['data'][:10]
    }

    
    
   
    return render(request, 'index.html',
    {
        "data": data['data'][:10]
    })