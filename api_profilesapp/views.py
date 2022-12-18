from django.shortcuts import render

# Create your views here.
def api_overview(request):
    data = {'1': 'API Overview',
               '2': 'API Overview',
               '3': 'API Overview',
               '4': 'API Overview',
               '5': 'API Overview',}
    return render(request, 'api_profileapp/api_overview.html', {'data': data})