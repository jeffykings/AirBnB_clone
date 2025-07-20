#!/usr/bin/python3

import uuid
from datetime import datetime
"""
Contains the model that other classes inherits
"""


class BaseModel():
    """
    Defines all common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """It is first thing to run a class is called
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        changene the public instance attribute updated_at with the current
        datetime = self.__dict__[created_at]
        """

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values of __dict__ of the
         instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
