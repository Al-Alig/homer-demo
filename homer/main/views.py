"""
This file contains the views for the main app.
"""

from django.shortcuts import render
from entity.models import Entity


def index(request):
    """
    This function is used to display the main page.
    """
    all_offers = Entity.objects.all()

    return render(request, 'index.html', {
        'offers': all_offers,
    })


def find_entities(request):
    """
    This function is used to search and display entities at the page.
    """

    if request.method == 'POST':
        searched_city = request.POST['searched']
        searched_type = request.POST['formType']
        offers = Entity.objects.filter(city__contains=searched_city, type=searched_type)
        context = {
            'found_offer_city': searched_city,
            'found_offer_type': searched_type,
            'offers': offers,
            'offers_count': offers.count(),
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', {})
