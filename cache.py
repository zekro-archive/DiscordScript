"""
Module for processing and saving data
for processing in the API.
"""

selected = None


class Selection:
    def __init__(self, objtype: str, data):
        self.type = objtype
        self.data = data