from django.shortcuts import render
from django.http import JsonResponse
import  requests
# Create your views here.


def index(request):
    return render(request, 'index.html')


#url = "https://api.github.com/search/users?q=boxabhi
#url = https://api.github.com/users/USERNAME/repos
#url = https://api.github.com/users/boxabhi/repos?direction=dsc
#url = https://api.github.com/users/boxabhi/followers
def get_user_details(request):
    username = request.GET.get('username', 'boxabhi')
    url = f'https://api.github.com/users/{username}/repos'
    
    print(url)
    data = requests.get(url)
    print(data.text)
    return JsonResponse({'payload' : data.json()})
    
    