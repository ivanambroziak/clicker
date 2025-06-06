from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.conf import settings
from .models import ClickerImage, Comment
import json


def home(request):
    active_image = ClickerImage.objects.filter(is_active=True).first()
    comments = Comment.objects.all()[:10]  # Останні 10 коментарів

    context = {
        'image': active_image,
        'comments': comments,
        'monobank_url': settings.MONOBANK_JAR_URL,
    }
    return render(request, 'clicker/home.html', context)


@require_POST
@csrf_exempt
def click_button(request):
    active_image = ClickerImage.objects.filter(is_active=True).first()
    if active_image:
        active_image.click_count += 1
        active_image.save()
        return JsonResponse({'count': active_image.click_count})
    return JsonResponse({'error': 'No active image'}, status=400)


@require_http_methods(["POST"])
def add_comment(request):
    """
    Обробляє додавання коментарів
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        text = request.POST.get('text', '').strip()

        if name and text:
            Comment.objects.create(name=name, text=text)
            return redirect('home')
        else:
            # Якщо дані не валідні, повертаємося на головну з повідомленням
            return redirect('home')

    # Якщо це не POST запит, перенаправляємо на головну
    return redirect('home')