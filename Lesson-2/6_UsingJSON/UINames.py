#!/usr/bin/env python3
#
# Client for the UINames.com service.
#
# 1. Decode the JSON data returned by the UINames.com API.
# 2. Print the fields in the specified format.
#
# Example output:
# My name is Tyler Hudson and the PIN on my card is 4840.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)
    # 1. Add a line of code here to decode JSON from the response.
    josn_response = r.json()
    
    # print(josn_response) - just to figure out what's in there
    name = josn_response["name"]
    surname = josn_response["surname"]
    pin = str(josn_response["credit_card"]["pin"])


    return "My name is {} {} and the PIN on my card is {}.".format(
        # 2. Add the correct fields from the JSON data structure.
        name, surname, pin
    )

if __name__ == '__main__':
    print(SampleRecord())
