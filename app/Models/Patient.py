from app.Models.User import User

class Patient(User):
    def __init__(self, **kwargs):
        super(User,self).__init__(**kwargs, userCategoryId= 1)
