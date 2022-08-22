#!/usr/bin/python3 

import getpass
import bcrypt

'''
    Generate prometheus basis auth password.
'''

password = getpass.getpass("password: ")
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed_password.decode())