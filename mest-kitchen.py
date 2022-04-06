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

    def user_name(self): 
        return {self.first_name}

class MealItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''

    def available_meal(self): 
        return {self.name}

class Order():
    meal = ''
    portion = ''
    

user = User()
meal = MealItem()
order = Order()


user.first_name = "Bethel"
user.last_name = "Melariri"
user.email_address = "bethelmelariri@gmail.com"
user.allergies = "Fish"

meal.name = "Waakye & Coke"
meal.serving_size = "Large"
meal.allergens = "None"


print(user.user_name(), "the only available food is", meal.available_meal())
