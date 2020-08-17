import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from . import models

BASE_URL = 'https://mumbai.craigslist.org/search/?query={}'
BASE_IMG = "https://images.craigslist.org/{}_300x300.jpg"


# Create your views here.
def home(request):
    return render(request, 'base.html')


def temp(request):
    search = request.POST.get('Search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    final_url = BASE_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_list = soup.find_all('li', {'class': 'result-row'})

    final_post = []

    for post in post_list:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_img_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_img_url = BASE_IMG.format(post_img_id)
            print(post_img_url)
        else:
            post_img_url = 'https://www.craigslist.org/images/peace.jpg'

        final_post.append((post_title, post_url, post_price, post_img_url))


    frontend_stuff = {
        'Search': search,
        'final_post': final_post,
    }
    return render(request, 'my_app/temp.html', frontend_stuff)
