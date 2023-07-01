from django.shortcuts import render
from .models import Species, Codes

# Create your views here.


def list_species(request):
    print(Codes.objects.select_related("species"))
    return render(request, "list_species.html", {
        "codes": Codes.objects.select_related("species"),
    })