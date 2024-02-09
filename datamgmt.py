import requests
import json

import sys
from dotenv import load_dotenv
load_dotenv()


import os

token = os.environ.get("apiaccesstoken")



import os



def fetch_github_user_data(username):
    access_token =token
    try:
        headers = {
            'Authorization': f'token {access_token}'
        }
        response = requests.get(f'https://api.github.com/users/{username}', headers=headers)
        if response.status_code == 200:
            user_data = response.json()

            user_information = {
                'name': user_data.get('name'),
                'username': user_data.get('login'),
                'bio': user_data.get('bio'),
                'email': user_data.get('email'),
                'company': user_data.get('company'),
                'publicRepos': user_data.get('public_repos'),
                'publicGists': user_data.get('public_gists'),
                'location': user_data.get('location'),
                'followers': user_data.get('followers'),
                'following': user_data.get('following'),
                'avatarUrl': user_data.get('avatar_url'),
                'githubUrl': user_data.get('html_url')
            }

            return user_information
        else:
            print(f"Error fetching GitHub user data: Status Code {response.status_code}")
            return None
    except Exception as e:
        print('Error fetching GitHub user data:', e)
        return None

# username = input("Enter GitHub username: ")
# user_data = fetch_github_user_data(username)
# if user_data:
#     print("User Information:")
#     for key, value in user_data.items():
#         print(f"{key}: {value}")
# else:
#     print("Failed to fetch user data.")




def fetch_github_user_repos(username):
    access_token =token
    try:
        headers = {
            'Authorization': f'token {access_token}'
        }
        response = requests.get(f'https://api.github.com/users/{username}/repos', headers=headers)
        
        if response.status_code == 200:
            repos_data = response.json()
            
            repositories = []
            for repo_data in repos_data:
                languagesurl = repo_data.get("languages_url")
                languageresponse = requests.get(languagesurl, headers=headers)
                if languageresponse.status_code == 200:
                    languages = languageresponse.json()
                    languageslist = list(languages.keys())


                
                repository = {
                    'name': repo_data.get('name'),
                    'description': repo_data.get('description'),
                    'language': repo_data.get('language'),
                    'url': repo_data.get('html_url'),
                    "languages":languageslist
                }
                repositories.append(repository)

            return repositories
        else:
            print(f"Error fetching GitHub user repositories: Status Code {response.status_code}")
            return None
    except Exception as e:
        print('Error fetching GitHub user repositories:', e)
        return None

# username = 'arycodes'
# repos = fetch_github_user_repos(username)
# if repos:
#     for repo in repos:
#         print("Name:", repo['name'])
#         print("Description:", repo['description'])
#         print("Language:", repo['language'])
#         print("URL:", repo['url'])
#         print("languages :", repo['languages'])
#         print()
