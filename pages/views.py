from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request.user)
    return HttpResponse("<h1>Hello World</h1>") # string of HTML code

def contact_view(request, * args, ** kwargs):
    #print(args, kwargs)
    return HttpResponse("<h1>Contact page</h1>")

def template_view(request, *args, ** kwargs):
    return render(request, "template.html", {})

def about_view(request, * args, ** kwargs):
    my_context = {
        "my_name":"Peter",
        "my_number":"758200181"
    }
    return render(request, 'about.html', my_context)
