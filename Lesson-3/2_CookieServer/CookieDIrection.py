# use cookies in python

# To set a cookie from a Python HTTP server, all you need to do is 
# set the Set-Cookie header on an HTTP response. Similarly, to read 
# a cookie in an incoming request, you read the Cookie header. 
# However, the format of these headers is a little bit tricky;  
# I don't recommend formatting them by hand. Python's http.cookies 
# module provides handy utilities for doing so.

# To create a cookie on a Python server, use the SimpleCookie class.  
# This class is based on a dictionary, but has some special behavior once you create a key within it:


from htt[.cookies import SimpleCookie, CookieError

out_cookie = SimpleCookie()
out_cookie["bearname"] = "Smokey Bear"
out_cookie["bearname"]["max-age"] = 600
out_cookie["bearname"]["httponly"] = True

# then we can send the cookie as a header from the request handler:

self.send_header("Set-Cookie", out_cookie["bearname"].OutputString())

# To read incoming cookie, create a SimpleCookie from the Cookie header:

in_cookie = SimpleCookie(self.headers["Cookie"])
in_data = in_cookie["bearname"].value


'''
Be aware that a request might not have a cookie on it, in which case accessing the Cookie header will 
raise a KeyError exception; or the cookie might not be valid, in which case the SimpleCookie constructor 
will raise http.cookies.CookieError.
'''