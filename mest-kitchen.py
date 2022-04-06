class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''
    user_type = ''

    def user_allergies(self): 
        return {self.allergies}

class MealItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''

class Order():
    meal = ''
    portion = ''
    

user = User()

user.first_name = "Bethel"
user.last_name = "Melariri"
user.email_address = "bethelmelariri@gmail.com"
user.allergies = "Fish"


print(user.user_allergies())
