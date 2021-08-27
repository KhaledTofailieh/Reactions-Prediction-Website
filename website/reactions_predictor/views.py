from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Page, Post
from . import validators

from . import mappers
import json


# Create your views here.
def start(request):
    if request.session.get('logged', False):
        return redirect('/home')
    return redirect('/login')


def login(request):
    try:
        if request.method == 'POST':
            if validators.sign_in_validation(request):
                return redirect('/home')
            return render(request, 'login.html')

        # method is GET:
        return render(request, 'login.html')
    except Exception as ex:
        print('Exception: ', ex)
        return render(request, 'error-500.html')


def register(request):
    try:
        if not request.session.get('logged', False):
            if request.method == 'POST':
                pass

            # method is GET:
            return render(request, 'register.html')
    except Exception as ex:
        print('Exception: ', ex)
        return render(request, 'error-500.html')


def home(request):
    try:
        if request.method == 'POST':
            return redirect('/results')
        # method is GET:
        data = {'pages': request.session.get('pages'),
                'name': request.session.get('name'),
                'user_name': request.session.get('user_name')}
        return render(request, 'home.html', data)
    except Exception as ex:
        print('Exception: ', ex)
        return render(request, 'error-500.html')


def results(request):
    try:
        page_name = ''
        post_text = ''
        if request.method == 'POST':
            page_name = request.POST.get('selected_page', '')
            post_text = request.POST.get('post_text', '')

        reactions = {
            "haha": 2500,
            "love": 1000,
            'sad': 100,
            'wow': 1000,
            'angry': 750
        }

        data = {
            'name': request.session.get('name', ''),
            'user_name': request.session.get('user_name', ''),
            'page_name': page_name,
            'post_text': post_text,
            'post_type': 'اجتماعي',
            'reactions': json.dumps(reactions)
        }
        return render(request, 'results.html', data)
    except Exception as ex:
        print('Exception:', ex)


def page_register(request):
    try:
        pages = Page.objects.all()
        pages = [page.name for page in pages]
        data = {
            'pages': pages
        }
        # come from ajax
        if request.is_ajax():
            # sending email or verification:
            if mappers.page_register_mapper[request.POST.get('clicked')](request):
                return JsonResponse({'success': True, 'url': '/home'})
            return JsonResponse({'success': False, 'url': '/home'})

        return render(request, 'page_register.html', data)

    except Exception as ex:
        print('Some Exception in Page-Register', ex)


def test_board(request):
    try:
        posts = Post.objects.all()

        if request.method == 'POST':
            if request.is_ajax():
                # click on post text:
                # we will send page name that matches post
                try:
                    selected = int(request.POST.get('selected'))
                    # getting page that match selected
                    return JsonResponse({'success': True, 'page_name': posts[selected].page_name})
                except Exception as ex:
                    print('Exception in ajax-Method', ex)
                    return JsonResponse({'success': True, 'page_name': ''})

            return redirect('/test_results')
        # method is GET:
        data = {
            'name': request.session.get('name', ''),
            'user_name': request.session.get('user_name', ''),
            'posts': posts,
        }
        return render(request, 'test_board.html', data)
    except Exception as ex:
        print('Exception: ', ex)
        return render(request, 'error-500.html')


def test_results(request):
    try:
        page_name = ''
        post_text = ''
        if request.method == 'POST':
            page_name = request.POST.get('selected_page', '')
            post_text = request.POST.get('selected_post', '')

        reactions = {
            "haha": 2500,
            "love": 1000,
            'sad': 100,
            'wow': 1000,
            'angry': 750
        }
        data = {
            'name': request.session.get('name', ''),
            'user_name': request.session.get('user_name', ''),
            'page_name': page_name,
            'post_text': post_text,
            'post_type': 'اجتماعي',
            'real_reactions': json.dumps(reactions),
            'model_reactions': json.dumps(reactions)
        }
        return render(request, 'test_results.html', data)
    except Exception as ex:
        print('Exception:', ex)
