
from django.utils.timezone import make_aware
from django.conf import settings
from Users.models import User
import json
from celery import shared_task
from urllib.request import Request, urlopen
import urllib.request
from datetime import datetime
import os
import logging
from celery.utils.log import get_task_logger
from Projects.models import ProjectCategory, ProjectCategoryOrderable




"""
Insert Projects Into The Appplication VIA Git 
"""

def get_url_content_as_json(url,user):
    try:
        header = {
             "User-Agent": "Mozilla/5.0"
        }
        if (user.git_api_key):
            header['Authorization'] = 'token {}'.format(user.git_api_key)
        print(header)
        url_request = Request(url,
                              headers=header)
        contents = urlopen(url_request).read()
    except Exception as e:
        print(e)
        print("Error Getting Content From Url")
        raise Exception("Error Gettign Content From Url")
   # // intially empty
    jsonStruct  = json.loads(contents)
    return jsonStruct


def getUserRepos(userModel):
    gitUser = userModel.git_hub_account
    # Do nothing User Not Found Raise Error
    urlRestApiGit = "https://api.github.com/users/{}/repos".format(gitUser)
    
    currentUserRepos = {}  # // intially empty
    jsonContentRepos = get_url_content_as_json(urlRestApiGit,userModel)
    ##
    for reposInfo in jsonContentRepos:
        if "personalxmb" in reposInfo['name'].lower():
            continue
        oodict = {key: value
                  for key, value in reposInfo.items()
                  if key in ['id', 'description', 'html_url', 'created_at', 'updated_at',\
                       'name', 'languages_url']
                  }
        
        currentUserRepos[oodict['name']] = oodict
    #print(currentUserRepos)
    ##fill in the languages for each repo
    for key, repos in currentUserRepos.items():
        if 'languages_url' in repos:
            langs_url = repos['languages_url']
            lang_json =get_url_content_as_json(langs_url,userModel)
            languages = [language for language in lang_json]
            currentUserRepos[key]['languages'] = languages

    #print(currentUserRepos)
    for key, repos in currentUserRepos.items():
        #print(repos)
        repos["created_at"] = make_aware(datetime.strptime(
            repos["created_at"], "%Y-%m-%dT%H:%M:%SZ"))
        repos["updated_at"] = make_aware(datetime.strptime(
            repos["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
        print("Sucess Getting Project {}\n".format(key))
    return currentUserRepos


def generateProjects(user):
    listRepos = getUserRepos(user)
    modelUser = user
    currentUserProjects = modelUser.projectUserHandlier.all()
    for key, repo in listRepos.items():
        #print(repo['id'])
        project, created_project = currentUserProjects.get_or_create(
            id = repo['id'],
            defaults={
                'project_name':repo['name'],
                'id': repo['id'],
                'created': repo['created_at'],
                'last_updated': repo['updated_at'],
                'description': repo['description'] if repo['description'] is not None else " ",
                'project_link': repo['html_url'],
                'projectHandlier': modelUser,
                'image': None,
                'categories' : [],
                'tags': [],
                'show_case': True,
            }
        )
        ##check if the repos name has been updates lately and update it accordingly 

        if (project.id == repo['id']) and (project.project_name == repo['name']):
            project.project_name = repo['name']
            project.save()
        ##check if the repos has been updates lately and update it accordingly 
        if project.last_updated != repo['updated_at']:
            project.last_updated = repo['updated_at']
            project.description = repo['description'] if repo['description'] is not None else " "
            project.save()
        
        ##add categories to project from git
        for category in repo['languages']:
            saved_project_category, created_category = ProjectCategory.objects.get_or_create(
            name=category)
            if created_category:
                #print('created new category')
                if created_project:
                    project_category = saved_project_category if saved_project_category else  created_category
                    ##
                    
                    #created_project.categoies.add(project_category )
                    project_category_connect = ProjectCategoryOrderable(project=created_project, project_category=project_category)
                    project_category_connect.save()
            else:
                project_category = saved_project_category if saved_project_category else  created_category 
                current_project_catgories = project._categories.all()
                if (project_category not in current_project_catgories):
                    ##
                    ##project.categories.add(project_category)
                    project_category_connect = ProjectCategoryOrderable(project=project, project_category=project_category)
                    project_category_connect.save()
            
            

        
        
        



@shared_task
def populateProjectsAllUser(data=None):
    ##gets all users in the data base
    all_users = User.objects.all()
    for user in all_users:
        print(user)
        if(user.git_hub_account):
            generateProjects(user)
    return "success"