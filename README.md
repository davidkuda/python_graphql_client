# python_graphql_client

Recently I worked on a project where I had to request the GitHub GraphQL API from Python. I have found it quite difficult to accomplish. There are numerous things that I have learned. I publish all my learnings in this repository.

### How to perform a basic request to a GraphQL API from Python:

```python
import json
import os

import requests


TOKEN = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')


def request_something():
    query = '''
    query get_marketplace_categories { 
      marketplaceCategories {
        name
        primaryListingCount
        description
      }
    }
    '''

    response = requests.post(url='https://api.github.com/graphql',
                             json={'query': query},
                             headers={'Authorization': f'Bearer {TOKEN}'}
                             ).json()
    
    return response


if __name__ == '__main__':
    data = request_something()
    print(json.dumps(data, indent=2))

```
