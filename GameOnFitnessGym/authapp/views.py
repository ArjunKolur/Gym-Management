from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

# above code we need to call the function that is in urls.app
#Home()
    
# Create your views here.
