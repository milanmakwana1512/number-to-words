from django.shortcuts import render
from num2words import num2words
from .models import History

def index(request):

    result = ""

    if request.method == "POST":

        number = request.POST.get("number")

        try:
            if "." in number:
                rupees, paise = number.split(".")

                rupees_word = num2words(int(rupees), lang='en_IN').upper()
                paise_word = num2words(int(paise), lang='en_IN').upper()

                result = rupees_word + " and " + paise_word + " PAISA ONLY"

            else:
                rupees_word = num2words(int(number), lang='en_IN').upper()
                result = rupees_word + " ONLY"

        except:
            result = "Invalid Number"

    history = History.objects.all().order_by('-date')[:5]

    return render(request,"index.html",{"result":result,"history":history})