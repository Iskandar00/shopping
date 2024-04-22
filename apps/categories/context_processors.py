from apps.categories.models import MainCategory


def categories(request):
    return {'categories': MainCategory.objects.all()}
