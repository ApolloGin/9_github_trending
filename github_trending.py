import requests
from datetime import timedelta, date

NUMBER_OF_REPOSITORIES = 20
DAYS_PER_WEEK = 7
ACCESS_TOKEN = '98a292be015a2a4abf04dea17629c4de1f69db83'

def get_trending_repositories(top_size):
    search_url = 'https://api.github.com/search/repositories'

    week_ago = date.today() - timedelta(days=DAYS_PER_WEEK)

    params = {
        'q': 'created:>={week_ago}'.format(week_ago=week_ago),
        'sort': 'stars',
        'order': 'desc',
        'access_token': ACCESS_TOKEN,
        'per_page': top_size
    }    
    response = requests.get(search_url, params=params)
    return response.json()['items']

if __name__ == '__main__':
    for enum, repo in enumerate(
        get_trending_repositories(NUMBER_OF_REPOSITORIES),
        start=1):
        owner = repo['owner']['login']
        repo_name = repo['name']
        print('{0}. Repository: {1}'.format(enum, repo_name))
        print('   Owner: {0}'.format(owner))
        print('   Url: {0}'.format(repo['html_url']))
        print('   Opened issues {0}:'.format(repo['open_issues_count']))
