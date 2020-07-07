import requests
import hashlib
# response of 400 is not great
# response 200 means ok


# SHA1 hash generator


def request_api_data(query_character):
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error  fetching : {res.status_code}, check the api and try again ')
    return res


def pwned_api_checker(password):
    # check password if it exists in API response
    # sha 1 hashing
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    return response


pwned_api_checker('123')
