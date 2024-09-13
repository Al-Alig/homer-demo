"""
This file contains the views for the user app.
"""

from secrets import compare_digest

from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404

from user.models import User
from entity.models import Entity


def profile(request):
    """
    This function is used to display the profile page.
    """
    user = request.user
    offers_by_user = Entity.objects.filter(user=user)

    empty_count = 0
    context = {
        'username': user.username,
        'profile_photo': user.profile_photo,
        'country': user.country,
        'city': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'middle_name': user.middle_name,
        'phone': user.phone,
        'email': user.email,
        'creation_date': user.creation_date,
        'offers': offers_by_user
    }

    return render(request, "profile/profile.html", context)


def signup(request):
    """
    This function is used to display the signup page.
    """

    if request.method == 'POST':
        data = request.POST

        password = data['formPassword']
        password_repeat = data['formPasswordRepeat']
        username = data['formUsername']

        if compare_digest(password, password_repeat) and username is not None:
            params = {
                'password': password,
                'username': username,
                'first_name': '',
                'middle_name': '',
                'last_name': '',
                'country': '',
                'city': '',
                'phone': '',
                'email': ''
            }
            new_user = User.objects.create_user(**params)
            login(request, new_user)
            return redirect('/')

    return render(request, 'registration/signup.html')


def profile_edit(request):
    """
    This function is used to display the profile edit page.
    """
    user = request.user

    if request.method == "POST":
        data = request.POST

        new_user = User.objects.get(username=user.username, first_name=user.first_name,
                                    last_name=user.last_name, middle_name=user.middle_name,
                                    country=user.country, city=user.city, phone=user.phone,
                                    email=user.email)

        new_user.username = data['formUsername']
        new_user.first_name = data['formFirst']
        new_user.middle_name = data['formMiddle']
        new_user.last_name = data['formLast']
        new_user.country = data['formCountry']
        new_user.city = data['formCity']
        new_user.phone = data['formPhone']
        new_user.email = data['formEmail']

        new_user.save()

        return redirect("/profile")

    return render(request, 'profile/edit.html', {
        'username': user.username,
        'profile_photo': user.profile_photo,
        'country': user.country,
        'city': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'middle_name': user.middle_name,
        'phone': user.phone,
        'email': user.email,
        'creation_date': user.creation_date
    })


def user_page(request, user_id):
    """
        This function is used to display the user page.
    """
    user_current = get_object_or_404(User, pk=user_id)
    return render(request, "profile/user.html", {
        'user_current': user_current
    })
