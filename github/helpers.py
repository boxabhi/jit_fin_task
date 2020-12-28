import  requests
import json






def return_follower_list(username, flag=False):
    fetch_followers_url = f"https://api.github.com/users/{username}/followers?page=1"
    follower_list = []
    fetch_followers = requests.get(fetch_followers_url)
    page_count = 2
    while len(fetch_followers.json()):
        for ff in fetch_followers.json():
            follower_list.append({'follower' :ff.get('login') , 'count' : 0})
           
        fetch_followers_url  = fetch_followers_url[:-1] + str(page_count)
        page_count += 1
        fetch_followers = requests.get(fetch_followers_url)
    
    if flag:
        return len(follower_list)
    else:
        return follower_list    
    


