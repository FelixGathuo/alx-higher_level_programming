#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    uid = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in uid:
        print(uid['id'])
    else:
        print(None)
