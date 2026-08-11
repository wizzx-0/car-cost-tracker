try:
    annual_km = float(input("Enter the annual kilometers driven:"))
    fuel_price = float(input("Enter the price of fuel per liter:"))
except ValueError:
    print(" ")
    print("Incorrect. Please enter a number.")
    print(" ")
    annual_km = 0
    fuel_price = 0

tire_life_km = 20000


cars = [
    {
        "name": "Lamborghini aventador SVJ",
        "price": 700000,
        "insurance": 5000,
        "maintenance": 4000,
        "power": 770,
        "fuel_consumption": 20,
        "tires": 3700
    },
     {
        "name": "Porsche 911 992 GT3RS",
        "price": 300000,
        "insurance": 3500,
        "maintenance": 2500,
        "power": 525,
        "fuel_consumption": 13,
        "tires": 3400
    },
     {
        "name": "Ferrari 812 superfast",
        "price": 350000,
        "insurance": 4000,
        "maintenance": 3000,
        "power": 800,
        "fuel_consumption": 16,
        "tires": 3000
    },
     {
        "name": "Mclaren 720s",
        "price": 250000,
        "insurance": 3500,
        "maintenance": 3000,
        "power": 720,
        "fuel_consumption": 12,
        "tires": 2400
    },
     {
        "name": "BMW M4 competition",
        "price": 100000,
        "insurance": 2000,
        "maintenance": 1000,
        "power": 530,
        "fuel_consumption": 10,
        "tires": 2000
    }
]

def afficher_voitures(car):
    print(car["name"],":")
    print(f"price : {car['price']}","€")
    print(f"insurance : {car['insurance']}","€")
    print(f"maintenance : {car['maintenance']}","€")
    print(f"power : {car['power']}","ch")
    print(f"fuel consumption : {car['fuel_consumption']}","L/100km")
    print(f"4 Tires : {car['tires']}","€")
    print(" ")
    
        


def annual_cost(car, annual_km, fuel_price):
    return( car["insurance"] + car["maintenance"] + (annual_km / 100) * car["fuel_consumption"] * fuel_price + tires_cost(car, annual_km))

def tires_cost(car, annual_km):
    return (annual_km / tire_life_km) * car["tires"]

def ranking():
    print("Ranking of cars based on annual cost (from lowest to highest):")
    sortede = sorted(cars, key=lambda car: annual_cost(car, annual_km, fuel_price), reverse = False)
    for index, car in enumerate(sortede, start=1):
        print(f"{index}. {car['name']} - Annual Cost: {annual_cost(car, annual_km, fuel_price):.2f} €")
      
        

annual_cost(cars[0], annual_km, fuel_price)
tires_cost(cars[0], annual_km)

print("Choose a car:")
for index, car in enumerate(cars, start=1):
    print(f"{index}. {car['name']}")
print(" ")
try:
    choice = int(input("Enter the number of the car you want to choose: "))
    if choice >= 1 and choice <= len(cars):
        selected_car = cars[choice - 1]
        print("You have selected:", selected_car["name"])
        print("Annual cost for", selected_car["name"], ":", annual_cost(selected_car, annual_km, fuel_price), "€")
        print("Details of the selected car:")
        afficher_voitures(selected_car)
    else:
        print("Invalid choice. Please select a valid car number.")
except ValueError:
    print("Please enter a number.")

print(" ")
ranking()

