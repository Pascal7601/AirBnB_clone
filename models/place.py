#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """class that inherits from Basemodel
    Attr
        city_id = empty string
        user_id = empty string
        name = empty string
        description = empty string
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids =[] """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        