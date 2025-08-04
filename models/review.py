#!/ussr/bin/python3
"""contains class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review
    attribute:
                place_id:  it will be the Place.id
                user_id: it will be the User.id
                text: Peoples review
    """

    place_id = ""
    user_id = ""
    text = ""
