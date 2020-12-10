from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Main_page():

    def main_page(request):
        
        url = ''
        url_string = ''
        user = authenticate(username=username, password=password)
        # return HttpResponse(f"User: {user}")
        
        if user:
            return HttpResponse(f"User passed if")
        else:
            return HttpResponse(f"Error")
        #     url = users.create_logout_uri(self.request.uri)
        #     url_string = 'Logout'
        # else:
        #     url = users.create_login_uri(self.request.uri)
        #     url_string = 'login'
            
        # template_values = {
        #     'url': url,
        #     'url_string': url_string,
        #     'user': user
        # }
        # return render(request, 'main_page.html', template_values)
