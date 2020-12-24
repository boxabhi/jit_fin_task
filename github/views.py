from django.shortcuts import render
from django.http import JsonResponse
import  requests
import json
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
    
    
    
    fetch_repo_url = f'https://api.github.com/users/{username}/repos?per_page=500&sort=created'
    fetch_repo = requests.get(fetch_repo_url)
    
    repo_payload = []
    for fpu in fetch_repo.json():
        repo_payload.append(fpu.get('name'))
        
    fetch_followers_url = f'https://api.github.com/users/{username}/followers?per_page=100'
    fetch_followers = requests.get(fetch_followers_url)
    followers_payload = []
    
    for ffu in fetch_followers.json():
        followers_payload.append(ffu.get('login'))
                                 
    followers_payload = sorted(followers_payload,key = str.lower)    
    #followers_payload.sort()
        
    payload = {'repositories' : repo_payload ,'followers' : followers_payload }
    return JsonResponse({'payload' : payload})
    
    