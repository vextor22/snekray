
class PRay:
    def __init__(self, width=640, height=360) -> None:
        self.height = height
        self.width = width

    @classmethod
    def get_default_dimensions(cls):
        return(cls.width, cls.height)

    def get_dimensions(self):
        return (self.width, self.height)
        

