from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    if "counter" not in request.session:
        request.session['counter']=-1
    request.session['counter']+= 1
    context = {
        "unique_id": get_random_string(length=14),
        "counter": request.session['counter']
    }
    return render(request, "index.html",context)
def clearing(request):
    request.session.clear()
    return redirect('/')