from django.http import HttpResponse
from django.shortcuts import render

from . import form

def home_page(req):
    context={
        "title":"WORD COUNTER",
        # "form":form.exampleform()
    }
    return render(req,'home.html',context)


def count_page(request):
    txt=request.GET['typed_text'],
    txt=txt[0]
    txt_count = txt.split()
    return render(request, 'count.html',{"text":txt,"count":len(txt_count)})

def about_page(req):
    return render(req, 'about.html')