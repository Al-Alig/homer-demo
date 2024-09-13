"""
This file contains the views for the entity app.
"""

import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from entity.models import Order, Entity, EntityImages
from django.core.files.storage import FileSystemStorage


@login_required(login_url="/login/")
def booking(request, entity_id):
    """
    This function is used to book a house.
    """

    if request.method == "POST":
        data = request.POST
        curr_user = request.user.id
        name_house = entity_id
        start = data['FormStart']
        end = data['FormEnd']

        book = Order(
            user=curr_user,
            entity=name_house,
            start_date=start,
            close_date=end)

        book.save()


@login_required(login_url="/login/")
def history(request, entity_id):
    """
    This function is used to display the history of the house.
    """
    context = {}

    if request.method == "POST":
        house = entity_id
        story = Order.objects.all().filter(entity=house)
        context["history"] = story

    return render(request=request, template_name="placeholder", context=context)


@login_required(login_url="/login/")
def create_application(request):
    """
    This function is used to create an application.
    """

    if request.method == "POST":
        data = request.POST

        print(data)
        print(request.FILES)

        new_entity = Entity(
            name=data['formName'],
            type=data['formType'],
            description=data['formDescription'],
            price=data['formPrice'],
            country=data['formCountry'],
            city=data['formCity'],
            address=data['formAddress'],
            user=request.user,
            entity_image=request.FILES['formImage']
        )

        new_entity.save()

        return redirect("/")

    return render(request, "reg_house.html")


def entity_detail(request, entity_id):
    """
        This function is used to display the details of a house.
    """

    entity = get_object_or_404(Entity, pk=entity_id)

    if request.method == "POST":
        data = request.POST
        start_book_date = data['startBook']
        end_book_date = data['endBook']

        book: Order

        #print(data)

        for book in Order.objects.all():
            if book.start_date > datetime.datetime.strptime(end_book_date, "%Y-%m-%d").date() or book.close_date < datetime.datetime.strptime(start_book_date, "%Y-%m-%d").date():
                new_book = Order(
                    user=request.user,
                    entity=entity,
                    start_date=start_book_date,
                    close_date=end_book_date,
                    status=1,
                )
                #print(new_book)
                new_book.save()
            else:
                raise HttpResponseNotAllowed
        else:
            new_book = Order(
                user=request.user,
                entity=entity,
                start_date=start_book_date,
                close_date=end_book_date,
                status=1,
            )
            #print(new_book)
            new_book.save()

        return redirect("/")

    context = {
        "entity": entity,
        "images": EntityImages.objects.filter(entity=entity)
    }

    return render(request, 'house_page.html', context)


@login_required(login_url="/login/")
def reservations(request):
    """
        This function is used to display the reservations made by user
    """
    context = {}

    user = request.user
    reservations_by_user = Order.objects.filter(user=user)
    context['reservations'] = reservations_by_user

    return render(request, "reservations.html", context)
