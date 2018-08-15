#import
from py_nifty_cloud.nifty_cloud_request import NiftyCloudRequest

# instanciate with yaml file contains APPLICATION KEY and CLIENT KEY
ncr = NiftyCloudRequest('./nifty_cloud.yml')
path = '/classes/AccessTokens'
query = {'where' : {'accessToken': 'token'}}
method = 'GET'

# standard way to request
# get recodes which matches a query from path, with GET or POST or PUT http method
response = ncr.request(path=path, query=query, method=method)
type(response)
# >>> requests.models.Response

# show status code
print(response.status_code)
# show response as json format
print(response.json())
