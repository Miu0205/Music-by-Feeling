# /music_by_feeling/category_list.py

from .models import Category


def common(request):
    context = {
            'category_list': Category.objects.all(),
    }
    return context
