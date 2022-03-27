from django.shortcuts import render


def home_page(request):
    return render(
        request=request,
        template_name='home.html',
        context={'new_item_text': request.POST.get('item_text', '')},
    )
