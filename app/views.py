from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def show_base(request):
    print(request)
    return render(request,"base.html",{})
    # return HttpResponse(request,"base.html")
