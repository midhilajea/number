from django.shortcuts import render
from fancynumber_app.models import FancyPhoneNumber

# Create your views here.
def fancy_phone_number(request):
    numbers = FancyPhoneNumber.objects.all()
    context = {
        "numbers":numbers,
    }

    return render(request, 'fancy_numbers.html',context)