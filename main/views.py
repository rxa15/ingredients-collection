from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Tengku Laras Malahayati',
        'kelas': 'PBP D'
    }

    return render(request, "main.html", context)