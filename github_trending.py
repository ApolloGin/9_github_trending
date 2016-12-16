import requests
from datetime import timedelta, date

def get_trending_repositories(top_size):
    search_template = 'https://api.github.com/search/repositories?'\
    'q=created:>={week_ago}&sort=stars&order=desc'\
    '&access_token=98a292be015a2a4abf04dea17629c4de1f69db83'

    week_ago = date.today() - timedelta(days=7)
    response = requests.get(search_template.format(week_ago=week_ago))
    
    return response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    issues_template = 'https://api.github.com/repos/'\
    '{owner}/{repo}/issues'\
    '?access_token=98a292be015a2a4abf04dea17629c4de1f69db83'

    response = requests.get(issues_template.format(
        owner=repo_owner,
        repo=repo_name
    ))

    return response.json()


if __name__ == '__main__':
    for enum, repo in enumerate(get_trending_repositories(20), start=1):
        owner = repo['owner']['login']
        repo_name = repo['name']
        print('{0}. Repository: {1}'.format(enum, repo_name))
        print('   Owner: {0}'.format(owner))
        print('   Url: {0}'.format(repo['html_url']))
        issues = get_open_issues_amount(owner, repo_name)
        print('   Opened issues {0}:'.format(len(issues)))
        for issue in issues:
            print('    - {0}. ref: {1}'.format(
                issue['title'],
                issue['html_url']
            ))
