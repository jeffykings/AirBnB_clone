#!/usr/bin/python3
"""contains city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ class city

        attributes:
            state_id: the state id
            name: name of the city
    """

    state_id = ""
    name = ""
