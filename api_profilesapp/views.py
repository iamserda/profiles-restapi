from rest_framework.views import APIView
from rest_framework.response import Response


from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def api_overview(request):
    data = {'1': 'API Overview',
               '2': 'API Overview',
               '3': 'API Overview',
               '4': 'API Overview',
               '5': 'API Overview',}
    return render(request, 'api_profilesapp/api_overview.html', {'data': data})

def showUserProfiles(request):
    context = {'users': list(UserProfile.objects.all()),}
    return render(request, 'api_profilesapp/users-list.html', context)

class HelloApiView(APIView):
    """ Testing API View"""
    
    def get(self, request, format=None):
        data = ['GET: get data from a server', 'POST: to send data to the server to be store', 'PATCH: partially update data in the db.', 'UPDATE: updates a record completely', 'DELETE: removes a record from our db.']
        
        return Response({'message': 'My First API, yay!', 'data': data})
