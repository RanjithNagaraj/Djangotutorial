from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from classification import *
from django.contrib import messages
# Create your views here.

def classify(request):
    if request.method == 'POST':
        description = request.POST['input']
        result = pipe_clf.predict([str(description)])[0]
        if result == 1:
            messages.success(request, "requested task is automatable")
        else:
            messages.success(request, "requested task is non automatable")
        return render(request, 'ideation/index.html')
    else:
        print("came inside")
        return  render(request, 'ideation/index.html')
