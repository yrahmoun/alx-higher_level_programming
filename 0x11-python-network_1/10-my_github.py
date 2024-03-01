#!/usr/bin/python3
""" takes your GitHub credentials and displays your id """


if __name__ == "__main__":
    import requests
    import sys

    auth = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
