from apps.categories.models import MainCategory


def categories(request):
    selected_sub_cat_id = request.GET.get('sub_cat_id', '')
    selected_main_cat_id = request.GET.get('main_cat_id', '')

    if selected_sub_cat_id.isdigit():
        selected_sub_cat_id = int(selected_sub_cat_id)
    elif selected_main_cat_id.isdigit():
        selected_main_cat_id = int(selected_main_cat_id)

    context = {
        'selected_sub_cat_id': selected_sub_cat_id,
        'selected_main_cat_id': selected_main_cat_id,
        'categories': MainCategory.objects.all()
    }
    return context
