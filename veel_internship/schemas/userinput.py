class GiveRecipeInput:
    """Class to give input while requesting for recipe"""
    def __init__(self, foodtype, summary, ingridients):
        self.foodtype = foodtype
        self.summary = summary
        self.ingridients = ingridients
    
    # def __str__(self):
    #     return "Making an input module for recipe generator"

    def give_input(self):
        """ Gives input like foodtype, summary and ingridients"""
        print("Give the food type (veg or non_veg)")
        while True:
            self.foodtype = input("Enter foodtype").lower().strip()
            if self.foodtype == "veg" or self.foodtype == "non_veg":
                break
            else:
                print("Please enter the veg or non_veg")

        self.summary = input('Enter the summary of the Item').lower().strip()

        ing = input(" Enter the ingridients separated by comma")
        self.ingridients = [i.lower().strip() for i in ing.split(',')]
        return self.foodtype, self.summary, self.ingridients