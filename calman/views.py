from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import random
from decimal import Decimal

from .models import FoodStuff


def index(request):
    template = loader.get_template('calman/index.html')
    context = {
        'test': 1,
    }
    return HttpResponse(template.render(context, request))


def view_product(request):
    food_list = FoodStuff.objects.all()
    context = {
        'food_list': food_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'calman/products.html', context)


# Create your views here.
def calculate(request):
    posted_value = request.POST.get("input_value", "")
    sent_value = Decimal(posted_value)
    food_list = list(FoodStuff.objects.all())
    result_list = []
    selected_id = random.randint(0, len(food_list) - 1)
    item = food_list[selected_id].cal100
    multiplier = -1
    while item <= sent_value:
        sent_value -= item
        multiplier += 1
        if multiplier == 6:
            break
    result = (multiplier * item).__str__() + "g " + food_list[selected_id].name
    result_list.append(result)
    new_id = random.randint(0, len(food_list) - 1)
    while new_id == selected_id:
        new_id = random.randint(0, len(food_list) - 1)
    selected_id = new_id
    item = food_list[selected_id].cal50
    multiplier = -1
    while item <= sent_value:
        sent_value -= item
        multiplier += 1
        if multiplier == 6:
            break
    if multiplier == -1:
        context = {
            'result_list': result_list,
            'posted_value': posted_value,
        }
        return render(request, 'calman/result.html', context)
    result = (multiplier * item).__str__() + "g " + food_list[selected_id].name
    result_list.append(result)
    new_id = random.randint(0, len(food_list) - 1)
    while new_id == selected_id:
        new_id = random.randint(0, len(food_list) - 1)
    selected_id = new_id
    item = food_list[selected_id].cal10
    multiplier = -1
    while item <= sent_value:
        sent_value -= item
        multiplier += 1
        if multiplier == 6:
            break
    if multiplier == -1:
        context = {
            'result_list': result_list,
            'posted_value': posted_value,
        }
        return render(request, 'calman/result.html', context)
    result = (multiplier * item).__str__() + "g " + food_list[selected_id].name
    result_list.append(result)
    context = {
        'result_list': result_list,
        'posted_value': posted_value,
    }
    return render(request, 'calman/result.html', context)
