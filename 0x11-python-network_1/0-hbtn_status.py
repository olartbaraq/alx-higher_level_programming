#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page_status = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(the_page_status), (the_page_status), the_page_status.decode('utf-8')))
