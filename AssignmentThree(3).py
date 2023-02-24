# list of car brands available at the dealership
carBrandsAvailable = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan','Mercedes','Volkswagen',]

# Ask the customer to enter their car brand
userCarBrand = input("Enter your car brand: ")

# Check if the customer's car brand is available at the dealership
if userCarBrand in carBrandsAvailable:
    print("Your car brand is available at the dealership.")
else:
    print("Sorry, your car brand is not available at the dealership.")
# Store the car prices and models in a dictionary named "car_dealership"
car_dealership = {'Toyota Corolla': 20000, 'Toyota Camry': 150000, 'Toyota Vitz': 30000, 'Toyota Land Cruiser': 780000,\
                  'Honda Civic': 60000, 'Honda Pilot': 365000, 'Honda CRV': 145000\
                      , 'Ford Fusion': 25000, 'Ford Escape': 235000, 'Ford Explorer': 563000,\
                          'Chevrolet Camaro': 925000, 'Chevrolet Spark': 23000,'Chevrolet Cruze': 62000,\
                              'Nissan Juke': 25000, 'Nissan Sunny': 235000, 'Nissan Almera': 55000,'Nissan Patrol': 950000,\
                                  'Mercedes C250': 127000, 'Mercedes E300': 835000, 'Mercedes S550': 7563000,'Mercedes E63': 795000, 'Mercedes E63s': 29935000, 'Mercedes A250': 543900,\
                                      'Volkswagen Passat': 325000, 'Volkswagen Jetta': 75000, 'Volkswagen Bora': 663000,'Volkswagen Tiguan': 987000, 'Volkswagen Atlas cross': 275000, 'Volkswagen Taos': 7763000,}

# Get the model of the individual's car
individual_car = input("Enter the model of your car: ")

# Check if the individual's car is available at the dealership
if individual_car in car_dealership:
    print(f"Your requested {individual_car} is available at the dealership for GH¢{car_dealership[individual_car]}.")
else:
    print(f"Sorry, the {individual_car} is not available at the dealership.")