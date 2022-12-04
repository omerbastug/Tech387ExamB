from app.Models.User import User

class Doctor(User):
    def __init__(self, **kwargs):
        super(User,self).__init__(**kwargs, userCategoryId= 2, prefix = "Dr.")
