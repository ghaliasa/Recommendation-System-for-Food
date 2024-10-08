from Pastries import PastriesEngine
from Sweets import SweetsEngine
from AnimalFood import AnimalFoodEngine
from Starter import StarterEngine
from Sandwichs import SandwichesEngine
from vegetarins import VegetarianEngine

while True:
    print("1 _     معجنات")
    print("2 _     حلويات")
    print("3 _ أكل حيواني")
    print("4 _      مقبلات")
    print("5 _     سندويش")
    print("6 _  أكل نباتي")
    print("7 _     للخروج")
    print("______________________")
    choice = input("enter your choice :  ")
    if int(choice) == 1:
        engine = PastriesEngine()
        engine.reset()
        engine.run()
    elif int(choice) == 2:
        engine = SweetsEngine()
        engine.reset()
        engine.run()
    elif int(choice) == 3:
        engine = AnimalFoodEngine()
        engine.reset()
        engine.run()
    elif int(choice) == 4:
        engine = StarterEngine()
        engine.reset()
        engine.run()
    elif int(choice) == 5:
        engine = SandwichesEngine()
        engine.reset()
        engine.run()
    elif int(choice) == 6:
        engine = VegetarianEngine()
        engine.reset()
        engine.run()
    else:
        break
