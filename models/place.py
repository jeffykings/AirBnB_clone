#!/usr/bin/python3
"""contains class place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """contains class place

        attribute:
            city_id: it will be the City.id
            user_id: it will be the User.id
            name: na,e of places
            description: description of the place
            number_rooms: number of rooms
            number_bathrooms: number of bathroom
            max_guest: max number of guest are alllowed
            price_by_night: price per night
            latitude: latitude of the place
            longitude: longitude of the place
            amenity_ids: amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
