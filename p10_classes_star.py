class star():
    """represent a sky object with a name, distance and size

    Attributes
    ----------
    name : str
       name of star
    distance : float
       distance from telescope
    size : float
       star size
    
    Methods
    -------
    get_visual_size():
       returns the size through the telescope
    """
    def __init__(self, name, distance, size):
        """Initialize self by name, distance and size

        keyword attributes:
        name -- (string) numerical name of star 
        distance -- (float) distance from telescope
        size -- (float) star size
        """
        self.my_name = name
        self.my_distance = distance
        self.my_size = size
    
    def __str__(self):
        """override string representation"""
        return f'Awesome star named {self.my_name} with a size of {self.my_size} at a distance of {self.my_distance}'
    
    def __repr__(self):
        """override repr representation"""
        return f"{self.__class__.__name__}('{self.my_name}', {self.my_distance}, {self.my_size})"
    
    def get_visual_size(self):
        """returns size as seen through the telescope"""
        print(self.my_name)
        print(self.my_distance)
        print(self.my_size)
        pass # do some fancyness here


my_new_object = star('alhena', 3.0, 5.3)
print(my_new_object) # Awesome star named alhena with a size of 5.3 at a distance of 3.0
print(repr(my_new_object)) # star('alhena', 3.0, 5.3)
my_new_object.get_visual_size() # alhena\n3.0\n5.3