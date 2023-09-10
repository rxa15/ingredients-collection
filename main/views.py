from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Tengku Laras Malahayati',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)