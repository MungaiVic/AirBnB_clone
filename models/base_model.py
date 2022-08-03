from uuid import uuid4
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """
        __init__ initializes the base model

        This method defines the template to be used
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    time_format)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    time_format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:
        """String representation of the BaseModel Class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute `updated_at`
         with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of `__dict__`
        of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(time_format)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(time_format)
        return my_dict
