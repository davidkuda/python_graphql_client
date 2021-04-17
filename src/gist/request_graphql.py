from logging import Logger
import os

import requests

from utils import pretty_print_json

github_personal_access_token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')


class GraphQLClient:
    def __init__(self, base_url: str, token: str = None, logger: Logger = None):
        """Instantiate the GraphQL client to interact with a GraphQL API.

        Args:
            base_url (str): All requests will be sent to this url.
            token (str, optional):
              The authorization token which will be sent with every request as
              a http header (bearer token).
            logger (Logger): Logs will be printed through this logger.
        """
        self.base_url = base_url
        self._logger = logger
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def request_graphql(self, operation: str, variables: dict = None,
                        error_log: bool = True) -> dict:
        """Send a post request with your operation to a GraphQL api.

        Args:
            operation (str):
              GraphQL operation, either query (to retrieve data), mutation (to
              post data) or a subscription.
            variables (dict, optional): If the operation uses variables,
              send those as a dictionary with this arg.
            error_log (bool, optional): If True, catches and logs error in the
              response body. Does not raise an error. Important: This log refers
              to a valid request with an error as a response. If the request is
              invalid, this function raises a HTTPError which is independent
              from this argument.

        Returns:
            json: The response from the api-request.

        Raises:
            HTTPError: If request to GitHub api returns anything other than
            2xx status code.
        """

        response_raw = requests.post(self.base_url,
                                     headers=self.headers,
                                     json={'query': operation,
                                           'variables': variables})
        response_raw.raise_for_status()
        response = response_raw.json()

        # Even if response was 200 and a json was returned, the response may
        # still contain an error if the query was not correct.
        if error_log:
            if response.get('errors'):
                self._logger.debug('Your request returned an error: \n')
                pretty_print_json(response, logger=self._logger)

        return response

    def get_marketplace_categories(self):
        query = '''
        query get_marketplace_categories { 
          marketplaceCategories {
            name
            primaryListingCount
            description
          }
        }
        '''

        data = self.request_graphql(query)
        return data
