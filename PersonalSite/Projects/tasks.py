
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







def getUserRepos(userModel):
    gitUser = userModel.git_hub_account
    # Do nothing User Not Found Raise Error
    urlRestApiGit = "https://api.github.com/users/{}/repos".format(gitUser)
    try:
        url_request = Request(urlRestApiGit,
                              headers={"User-Agent": "Mozilla/5.0"})
        contents = urlopen(url_request).read()
    except:
        print(
            "Git User Couldnt Not Be Found Or Connection Erorr:{}\n".format(gitUser))
        raise Exception(
            "Git User Couldnt Not Be Found Or Connection Erorr:{}\n".format(gitUser))
    currentUserRepos = {}  # // intially empty
    jsonContentRepos = json.loads(contents)
    for reposInfo in jsonContentRepos:
        if "personalxmb" in reposInfo['name'].lower():
            continue
        oodict = {key: value
                  for key, value in reposInfo.items()
                  if key in ['id', 'description', 'html_url', 'created_at', 'updated_at', 'name']
                  }
        
        currentUserRepos[oodict['name']] = oodict
    # print(currentUserRepos)
    for key, repos in currentUserRepos.items():
        print(repos)
        repos["created_at"] = make_aware(datetime.strptime(
            repos["created_at"], "%Y-%m-%dT%H:%M:%SZ"))
        #repos["created_at"] = repos["created_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
        repos["updated_at"] = make_aware(datetime.strptime(
            repos["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
        #repos["updated_at"] = repos["updated_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
        # print(repos["updated_at"].tzinfo)
        print("Sucess Getting Project {}\n".format(key))
    # print(currentUserRepos)
    return currentUserRepos


def generateProjects(user):
    listRepos = getUserRepos(user)
    modelUser = user
    currentUserProjects = modelUser.projectUserHandlier.all()
    for key, repo in listRepos.items():
        print(repo['id'])
        project, created = currentUserProjects.get_or_create(
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



@shared_task
def populateProjectsAllUser(data=None):
    ##gets all users in the data base
    all_users = User.objects.all()
    for user in all_users:
        print(user)
        if(user.git_hub_account):
            generateProjects(user)
    return "success"