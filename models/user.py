#!/usr/bin/pyhton3

"""contains a User that inherits from BaseModel"""

from models.base_model import BaseModel



class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
