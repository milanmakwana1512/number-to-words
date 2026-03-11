from django.shortcuts import render
from num2words import num2words
from .models import History

def index(request):

    result = ""

    if request.method == "POST":

        number = request.POST.get("number")

        try:
            result = num2words(int(number), lang='en_IN').upper()

            History.objects.create(number=number,words=result)
            
        except:
            result = "Invalid Number"

    history = History.objects.all().order_by('-date')[:5]

    return render(request,"index.html",{"result":result,"history":history})