import requests
from django.conf import settings
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
'''
from .models import Recipe
from .forms import RecipeForm
'''

# Create your views here.


def home(request):
    recipe_data = []
    if request.method == 'POST':
        url = 'https://api.edamam.com/search'
        search = request.POST.get('search')
        search_params = {
            'q': search,
            'app_id': settings.DATA_API_ID,
            'app_key': settings.DATA_API_KEY,
            'to': 9,
        }

        r = requests.get(url, params=search_params)

        results = r.json()['hits']

        for result in results:

            recipe_info = {
                'recipename': result['recipe']['label'],
                'image': result['recipe']['image'],
                'ingredients': '\n'.join(result['recipe']['ingredientLines']),
                'full_recipe': result['recipe']['url'],
            }

            recipe_data.append(recipe_info)

    context = {'recipe_data': recipe_data}
    return render(request, 'home.html', context)
