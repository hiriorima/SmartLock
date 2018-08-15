#import
from py_nifty_cloud.nifty_cloud_request import NiftyCloudRequest

# instanciate with yaml file contains APPLICATION KEY and CLIENT KEY
ncr = NiftyCloudRequest('./key/ncmb/nifty_cloud.yml')
path = '/classes/status'
method = 'POST'

def post(status, used):
    values = {'status': status, 'used': used}
    response = ncr.request(path=path, query=values, method=method)
    type(response)
    print(response.status_code)
    print(response.json())
