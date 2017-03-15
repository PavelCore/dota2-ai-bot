from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt       
from botserver.bot import helper

# Create your views here.
def index(req):
    return JsonResponse({'text': "Hello, world!"})


@csrf_exempt
def reset(request):
    bot = helper.get_bot()
    return JsonResponse(bot.on_reset(request.body))


@csrf_exempt
def select(request):
    bot = helper.get_bot()
    return JsonResponse(bot.on_select(request.body))


@csrf_exempt
def chat(request):
    bot = helper.get_bot()
    json_response = bot.on_chat_message(request.body)
    return JsonResponse(bot.on_chat_message(request.body))


@csrf_exempt
def levelup(request):
    bot = helper.get_bot()
    return JsonResponse({'abilityIndex': bot.on_level_up(request.body)})


@csrf_exempt
def update(request):
    bot = helper.get_bot()
    return JsonResponse(bot.on_update(request.body))

