"""
blocklist.py

This file jusat contain the blocklist of the jwt tokens. It will be imported by app
and the logout resourceso that the token can be added to the blockliat when the user logs out.
"""


BLOCKLIST = set()

"""REDIS should be used to store blocklist."""