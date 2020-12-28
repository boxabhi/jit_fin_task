  
from django.shortcuts import render
from django.http import JsonResponse
import  requests
import json
from django.views.decorators.csrf import csrf_exempt
from .helpers import return_follower_list



def index(request):
    return render(request, 'index.html')


#url = "https://api.github.com/search/users?q=boxabhi
#url = https://api.github.com/users/USERNAME/repos
#url = https://api.github.com/users/boxabhi/repos?direction=dsc
#url = https://api.github.com/users/boxabhi/followers
#url = f'https://api.github.com/users/{username}/repos'


def get_user_details(request):
    username = request.GET.get('username', None)
    if username is None:
        return JsonResponse({'error' : 'username is required'})
    
    fetch_repo_url = f'https://api.github.com/users/{username}/repos?per_page=100&sort=created'
    fetch_repo = requests.get(fetch_repo_url)
    repo_payload = []
    for fpu in fetch_repo.json():
        repo_payload.append(fpu.get('name'))
    payload = {'repositories' : repo_payload }
    return JsonResponse({'payload' : payload})
    

def get_user_followers(request):
    username = request.GET.get('username', None)
    if username is None:
        return JsonResponse({'error' : 'username is required'})
    
    fetch_followers_url = f'https://api.github.com/users/{username}/followers?per_page=100'
    fetch_followers = requests.get(fetch_followers_url)
    followers_payload = []
    for ffu in fetch_followers.json():
        followers_payload.append(ffu.get('login'))
    
    followers_payload = sorted(followers_payload,key = str.lower)            
    payload = {'followers' : followers_payload }
    
    
    

def get_highest_follower(request):
    username = request.GET.get('username', None)
    
    if username is None:
        return JsonResponse({'error': 'username is required'})
    
    list_of_user_followers = return_follower_list(username)

    if len(list_of_user_followers) <= 0:
        return JsonResponse({'message': 'user has no followers'})
    
    
    for lf in list_of_user_followers:
        lf['count'] = return_follower_list(lf['follower'] , True)
        
        
    
    max_follower = 0
    follower_name = None
    for lf in list_of_user_followers:
        if max_follower < lf['count']:
            max_follower = lf['count']
            follower_name = lf['follower']
    
    if follower_name is None:
        return JsonResponse({'message': 'every follower has zero follower'})
    
    return JsonResponse({'message' : 'person has highest number of followers' , 'name' : follower_name , 'total_follower' : max_follower})
    
    
    
    

    

@csrf_exempt
def create_new_repository(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        if data.get('token') is None:
            return JsonResponse({'error' : 'token is required' , 'message' : 'You can get your token On your Github account: go to Settings -> Developer Settings -> Personal Access Token Under OAuth Apps. Now, Generate a New Access token'})
        
        if data.get('name') is None:
            return JsonResponse({'error' : 'name is required'})
        
        url = 'https://api.github.com/user/repos'
        body = {'name' : data.get('name')}
        headers = {'Authorization': f"token {data.get('token')}"}

        result = requests.post(url , data=json.dumps(body) , headers=headers)
        payload = result.json()
        
        if payload.get('name'):
            return JsonResponse({'message' : 'github repo created' , 'url' : 'https://github.com/' + payload.get('full_name') })
        else:
            return JsonResponse({'error' : 'something went wrong','message' : 'something went wrong may be repo already exists or token error'})
            
    return JsonResponse({'error' : 'method not allowed'})
    
@csrf_exempt
def update_repository_description(request):
    
    if request.method == 'PATCH':
        data = json.loads(request.body)
        if data.get('token') is None:
            return JsonResponse({'error' : 'token is required'})
        
        if data.get('repo') is None:
            return JsonResponse({'error' : 'repo is required'})
        
        if data.get('owner') is None:
            return JsonResponse({'error' : 'owner is required'})
        
        if data.get('name') is None:
            return JsonResponse({'error' : 'name is required'})
        
        if data.get('description') is None:
            return JsonResponse({'error' : 'a short description is required'})
    

        url = f"https://api.github.com/repos/{data.get('owner')}/{data.get('repo')}"
        body = {'name' : data.get('name'), 'description' : data.get('description')}
        headers = {'Authorization': f"token {data.get('token')}"}
        
        result = requests.patch(url , data=json.dumps(body) , headers=headers)
        payload = result.json()

        return JsonResponse({'message' : 'api responded with', 'payload' : payload})


    return JsonResponse({'error' : 'method not allowed'})

    