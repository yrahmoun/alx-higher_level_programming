#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the body of the response """


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
