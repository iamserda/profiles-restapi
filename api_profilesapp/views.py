from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # a library for status codes: 200..., 300..., 400..., 500...

from . import serializers # helps us verify user input data.


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
    # whenever a request is made with data coming from outside the app, these serializers will be used apply restrains to the incoming data. For example, first_name and last_name are setup to 32 characters or less.
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """handles HTTP GET request any client to the api/hello endpoint"""
        data = ['GET: get data from a server', 'POST: to send data to the server to be store', 'PATCH: partially update data in the db.', 'UPDATE: updates a record completely', 'DELETE: removes a record from our db.']
        return Response({'message': 'My First API, yay!', 'data': data})
    
    def post(self, request, format=None):
        """handles HTTP POST request any client to the api/hello endpoint"""
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                first_name = serialized_data.validated_data.get('first_name')
                last_name = serialized_data.validated_data.get('last_name')    
                return Response({'message': 'validated, posted', 'data': {'first':first_name, 'last':last_name}})
            else:
                raise ValueError("User input is too long.")
            
        except Exception as e:
            print(e)
            pass