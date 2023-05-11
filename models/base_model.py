#!/usr/bin/python3

"""Defining the BaseModel"""

import models

from uuid import uuid4

from datetime import datetime

class BaseModel:

    """Representing the BaseModel."""


    def __init__(self, *args, **kwargs):

        """Initializing the constructor

        Args:

            *args (any): Unused.

            **kwargs (dict): Key/value pairs of attributes.

        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())

        self.created_at = datetime.today()

        self.updated_at = datetime.today()

        if len(kwargs) != 0:

            for d, n in kwargs.items():

                if d == "created_at" or d == "updated_at":

                    self.__dict__[d] = datetime.strptime(n, tform)

                else:

                    self.__dict__[d] = n

        else:

            models.storage.new(self)


    def save(self):

        """Updating the updated_at with the current datetime."""

        self.updated_at = datetime.today()

        models.storage.save()


    def __str__(self):

        """The __str__ method for BaseModel"""

        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


    def to_dict(self):

        """This returns a dictionary containing all keys/values

           of __dict__ of the instance

        """

        instance_dict = self.__dict__.copy()

        instance_dict["created_at"] = self.created_at.isoformat()

        instance_dict["updated_at"] = self.updated_at.isoformat()

        instance_dict["__class__"] = self.__class__.__name__

        return instance_dict
