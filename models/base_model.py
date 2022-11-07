#!/usr/bin/env python3
""" Declare a Base Model """
import datetime
import uuid


class BaseModel:
    """ Base Model """

    def __init__(self, *args, **kwargs):
        ''' init instance '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        # if len(kwargs) != 0 or kwargs != {}:
        #     for k, v in  kwargs.items():
        #         if k == "created_at" or k == "updated_at":
        #             self.__dict__[k] =
        #         else:
        #             self.__dict__[k] = v
        # else:
        #     pass

    def __str__(self):
        ''' String Magic Method '''

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' Updates the pubic instance attribute with current datetime '''

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
        Returns a dictionary conatining all
        keys/values of __dict__ of the instance
        '''

        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = str(self.created_at.isoformat())
        new_dict['updated_at'] = str(self.updated_at.isoformat())
        return new_dict

# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# print(my_model.id)
# print(my_model)
# print(type(my_model.created_at))
# print("--")
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json
# [key]), my_model_json[key]))

# print("--")
# my_new_model = BaseModel(**my_model_json)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(my_model is my_new_model)
