from django.shortcuts import render


def index(request):
    context = {
        'title':'Home',
        'heading':'headHome',
        'subheading':'subheadHome',

    }
    return render(request, 'base.html',context)