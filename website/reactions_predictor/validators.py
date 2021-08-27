from .models import User, Page, UserPage
import numpy as np
from . import connectors


def sign_in_validation(request):
    try:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = User.objects.get(user_name=user_name)
        if user.password == password:
            # get all pages for user and save in session:
            user_pages = user.userpage_set.all()
            pages = [user_page.page.name for user_page in user_pages]
            request.session['pages'] = pages
            request.session['id'] = user.id
            request.session['user_name'] = user.user_name
            request.session['name'] = user.get_name()
            return True
        return False
    except Exception as ex:
        print('Exception in Sign-In Validation:', ex)
        return False


def register_validation(request):
    try:
        pass
    except Exception as ex:
        print('Exception in Sign-Up Validation:', ex)


def email_validation(request):
    try:
        try:
            page = Page.objects.get(email=request.POST.get('page_email', None), name=request.POST.get('page_name', None))
        except Exception as ex:
            print('Exception In get Page:', ex)
            raise ex
        user_code = np.random.randint(1000, 10000)
        data = {
            "receiver": page.email,
            "subject": "Verification Message",
            "message": "Your Code is: " + str(user_code)
        }
        connectors.send_email_to_user(data)
        request.session['page_id'] = page.id
        request.session['page_name'] = page.name
        request.session['code'] = str(user_code)
        request.session['is_verified'] = False
    except Exception as ex:
        print('Exception in Email Validation:', ex)


def code_verification_validator(request):
    try:
        if (request.POST.get('code') == request.session.get('code')) and not request.session.get('is_verified'):
            user_page = UserPage(user_id=request.session.get("id"), page_id=request.session.get("page_id"))
            user_page.save()
            request.session.get('pages').append(request.session.get('page_name'))
            request.session['is_verified'] = None
            request.session['code'] = None
            request.session['page_name'] = None
            request.session['page_id'] = None
            return True
        return False
    except Exception as ex:
        raise ex
