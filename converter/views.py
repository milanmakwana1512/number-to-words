from django.shortcuts import render
from num2words import num2words
from .models import History

def index(request):

    result = ""

    if request.method == "POST":

        number = request.POST.get("number")

        try:
            if "." in number:

                number = float(number)

                rupees = int(number)
                paise = int(round((number - rupees) * 100))

                rupees_word = num2words(rupees, lang='en_IN').upper()
                paise_word = num2words(paise, lang='en_IN').upper()

                result = rupees_word + " RUPEES AND " + paise_word + " PAISA ONLY"

            else:
                rupees_word = num2words(int(number), lang='en_IN').upper()
                result = rupees_word + " RUPEES ONLY"

     # ⭐ History save
            History.objects.create(number=number, words=result)

        except:
            result = "Invalid Number"

    history = History.objects.all().order_by('-date')[:5]

    return render(request, "index.html", {"result": result, "history": history})