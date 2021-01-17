from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from classification import *
from django.contrib import messages
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import pandas as pd
# Create your views here.

def classify(request):
    if request.method == 'POST':
        description = request.POST['input']
        print("user input")
        print(description)
        result = pipe_clf.predict([str(description)])[0]
        if result == 1:
            messages.success(request, "requested task is automatable")
        else:
            messages.success(request, "requested task is non automatable")
        return render(request, 'ideation/index.html')
    else:
        print("came inside")
        return  render(request, 'ideation/index.html')

def dumpclassify(request):
    print("inside dumpclassify")
    if request.method == 'POST':
        #print(request.FILES)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage('media/classify','media/classify')
        filename = fs.save(myfile.name, myfile)
        #print(Path(filename).suffix)
        if Path(filename).suffix == '.csv' and 'ideationinputs' in Path(filename).stem:
            uploaded_file_url = fs.url(filename)
            test=pd.read_csv(fs.path(filename),encoding='latin')
            #print(test.columns)
            #print(fs.path(filename))
            result = pipe_clf.predict(test['TASK'])
            total_result = list(result)
            print(total_result.count(1))
            context ={
                'automatable' : total_result.count(1),
                'nonautomatable': total_result.count(-1),
                'total': len(total_result)
            }
            return render(request, 'ideation/index.html',context)
        else:
            messages.error(request, "please upload csv file")

    else:
        print("came inside")
        return  render(request, 'ideation/index.html')
