from django.shortcuts import render, redirect
from django.contrib import messages

from apps.comments.forms import CommentsForm
from apps.comments.models import Comment


def comment_create(request, pk):
    user = request.user

    redirect_url = request.META['HTTP_REFERER']
    if request.method != 'POST':
        return redirect(redirect_url)

    data = request.POST

    form = CommentsForm(data=data)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product_id = pk
        if user.is_authenticated:
            comment.user, comment.name, comment.email = user, user.get_full_name(), user.email
        comment.save()
        messages.success(request, 'successfully')
        return redirect(redirect_url)
    else:
        messages.error(request, form.errors)
        return redirect(redirect_url)

    # user = request.user
    #
    # name = request.POST.get('name')
    # email = request.POST.get('email')
    # rating = request.POST.get('rating')
    # message = request.POST.get('message')
    #
    # if request.user.is_authenticated:
    #     name = user.first_name
    #     email = user.email
    # elif not (email and name):
    #     messages.error(request, 'name yoki email kiritilmadi!!!')
    #     return redirect(redirect_url)
    # Comment.objects.create(name=name, email=email, message=message, rating=rating, product_id=pk)
    # messages.success(request, 'Success send')
    # return redirect(redirect_url)
