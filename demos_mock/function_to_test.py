### call api has attr => user_info => setted by get_user method
from demos_mock.api_module import CallApi

api = CallApi()

def get_user_from_api(user, api):

    ###Get users for api and write user's informations in file
    #result = requests.get('http://localhost/users/'+user)

    ###Code with monckeypatch
    # with open("user.txt", 'w') as f:
    #     api.get_user(user)
    #     f.write(api.user_info)

    ###Code with magicMock
    with open("user.txt", 'w') as f:
        f.write(api.get_user_with_magic_mock(user))
    pass