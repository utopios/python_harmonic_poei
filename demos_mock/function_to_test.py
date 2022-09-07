### call api has attr => user_info => setted by get_user method
from demos_mock.api_module import CallApi

api = CallApi()

def get_user_from_api(user, api):

    ###Get users for api and write user's informations in file
    #result = requests.get('http://localhost/users/'+user)
    with open("user.txt", 'a') as f:
        api.get_user(user)
        f.write(api.user_info)
    pass