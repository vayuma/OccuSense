from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

import pickle

array = []

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def data(request):
    x = 123
    array = pickle.load(open('testData.p', "rb"))
    if request.method == 'POST':
        resp = request.body
        a = json.loads(resp.decode('utf-8'))
        x = (a['timetaken'])
        array.append(x)
        pickle.dump(array,open('testData.p', "wb"))
        return HttpResponse('hi')

    elif request.method =='GET':
        x = streamAvg(array, len(array))
        return render(request, 'page2.html', {"x": x})


def getAvg(x, n, total): 
    total = total + x; 
    return float(total) / n; 
  

def streamAvg(arr, n): 
    avg = 0; 
    total = 0; 
    for i in range(n): 
        avg = getAvg(arr[i], i + 1, total); 
        total = avg * (i + 1); 
    return avg; 

