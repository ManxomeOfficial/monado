class Vehicle:
    """
    Base class representing a generic vehicle.
    
    This parent class contains common attributes and methods that all vehicles share.
    Child classes (Car, Boat, Plane) will inherit from this class.
    """
    
    def __init__(self, make, model, year, max_speed, fuel_capacity, passenger_capacity):
        """
        Constructor for Vehicle base class.
        
        Parameters:
        make (str): Vehicle manufacturer (e.g., "Ford", "Boeing", "Yamaha")
        model (str): Vehicle model (e.g., "Mustang", "747", "WaveRunner")
        year (int): Year manufactured
        max_speed (float): Maximum speed (units depend on vehicle type)
        fuel_capacity (float): Fuel tank capacity (gallons)
        passenger_capacity (int): Maximum number of passengers
        
        REQUIREMENTS:
        1. Store all parameters as instance attributes
        2. Initialize current_fuel to 0 (vehicle starts empty)
        3. Initialize current_speed to 0 (vehicle starts stationary)
        4. Initialize passengers to 0 (vehicle starts empty)
        5. Initialize is_running to False (vehicle starts off)
        
        DIFFICULTY: Easy
        """
        # TODO: Initialize all vehicle attributes
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.passenger_capacity = passenger_capacity
        self.current_fuel = 0
        self.current_speed = 0
        self.passengers = 0
        self.is_running = False
        self.speed_units = "mph"
    
    def start_engine(self):
        """
        Start the vehicle's engine.
        
        REQUIREMENTS:
        1. Check if vehicle is already running
        2. If already running, print: "Engine is already running!"
        3. If not running, set is_running to True
        4. Print: "[make] [model] engine started!"
        
        DIFFICULTY: Easy
        """
        # TODO: Implement engine starting logic
        if self.is_running == False:
            self.is_running = True
            print(self.make + " " + self.model + " engine started!")
        else:
            print("Engine is already running!")
    
    def stop_engine(self):
        """
        Stop the vehicle's engine.
        
        REQUIREMENTS:
        1. Check if vehicle is running
        2. If not running, print: "Engine is already off!"
        3. If running, set is_running to False and current_speed to 0
        4. Print: "[make] [model] engine stopped!"
        
        DIFFICULTY: Easy
        """
        # TODO: Implement engine stopping logic
        if self.is_running == True:
            self.is_running = False
            print(self.make + " " + self.model + " engine started!")
        else:
            "Engine is already off!"
    
    def add_fuel(self, amount):
        """
        Add fuel to the vehicle.
        
        Parameters:
        amount (float): Gallons of fuel to add
        
        REQUIREMENTS:
        1. Validate that amount is positive
        2. If negative, print error and don't add fuel
        3. Check if adding fuel would exceed capacity
        4. If so, fill to capacity and print warning
        5. Otherwise, add the fuel amount
        6. Print current fuel level after adding
        
        ERROR: "Cannot add negative fuel!"
        WARNING: "Tank full! Added only [actual_amount] gallons."
        SUCCESS: "Added [amount] gallons. Current fuel: [current_fuel]/[fuel_capacity]"
        
        DIFFICULTY: Medium
        """
        # TODO: Implement fuel adding with validation
        if amount < 0:
            print("ERROR: Cannot add negative fuel!")
        elif amount + self.current_fuel > self.fuel_capacity:
            print("WARNING: Tank full! Added only " + str(self.fuel_capacity - self.current_fuel) + " gallons.")
            self.current_fuel = self.fuel_capacity
        else:
            self.current_fuel += amount
            print("SUCCESS: Added " + str(amount) + " gallons. Current fuel: " + str(self.current_fuel) + "/" + str(self.fuel_capacity))
    
    def accelerate(self, speed_increase):
        """
        Increase the vehicle's speed.
        
        Parameters:
        speed_increase (float): Amount to increase speed
        
        REQUIREMENTS:
        1. Check if engine is running - if not, print error and return
        2. Check if there's fuel - if not, print error and return
        3. Validate speed_increase is positive
        4. Don't exceed max_speed
        5. Update current_speed
        6. Print new speed
        
        ERRORS:
        - "Cannot accelerate: Engine is not running!"
        - "Cannot accelerate: No fuel!"
        - "Cannot accelerate: Speed increase must be positive!"
        
        SUCCESS: "Speed increased to [current_speed] [speed_units]"
        Note: speed_units should be "mph" (will be overridden in child classes)
        
        DIFFICULTY: Hard
        """
        # TODO: Implement acceleration with all validations
        if self.is_running == False:
            print("Cannot accelerate: Engine is not running")
        elif self.current_fuel <= 0:
            print("Cannot accelerate: No fuel!")
        elif speed_increase < 0: # Maybe allow for car to decelerate?
            print("Cannot accelerate: Speed increase must be positive!")
        else:
            self.current_speed += speed_increase
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
            print("Speed increased to " + str(self.current_speed) + " " + self.speed_units)
            return True

    
    
    def get_info(self):
        """
        Return formatted information about the vehicle.
        
        Returns:
        str: Formatted vehicle information
        
        REQUIREMENTS:
        1. Include make, model, year
        2. Include current status (running/stopped)
        3. Include current speed and max speed
        4. Include fuel level and passenger count
        5. Format nicely with proper labels
        
        EXAMPLE OUTPUT:
        "2020 Ford Mustang
         Status: Running
         Speed: 45/120 mph
         Fuel: 8.5/16.0 gallons
         Passengers: 2/4"
        
        DIFFICULTY: Easy
        """
        # TODO: Create and return formatted vehicle info
        run_stat = "Running" if self.is_running == True else "Stopped"
        print(str(self.year) + " " + str(self.make) + " " + str(self.model) + "\n" + "Status: " + run_stat + "\n" + "Speed: " + str(self.current_speed) + "/" + str(self.max_speed) + " " + self.speed_units + "\n" + 
              "Fuel: " + str(self.current_fuel) + "/" + str(self.fuel_capacity) + " gallons \n" + "Passengers: " + str(self.passengers) + "/" + str(self.passenger_capacity))

class Car(Vehicle):
    """
    Car class that inherits from Vehicle.
    
    Demonstrates inheritance and method overriding.
    Cars have unique features like doors and drive types.
    """
    
    def __init__(self, make, model, year, max_speed, fuel_capacity, passenger_capacity, 
                 num_doors, drive_type):
        """
        Constructor for Car class.
        
        Parameters:
        (inherits all Vehicle parameters, plus:)
        num_doors (int): Number of doors (2, 4, etc.)
        drive_type (str): "FWD", "RWD", "AWD", etc.
        
        REQUIREMENTS:
        1. Call parent constructor using super()
        2. Store num_doors and drive_type as additional attributes
        3. Set speed_units to "mph"
        
        DIFFICULTY: Medium
        """
        # TODO: Call super().__init__() and add car-specific attributes
        super().__init__(make, model, year, max_speed, fuel_capacity, passenger_capacity)
        self.num_doors = num_doors
        self.drive_type = drive_type
        self.speed_units = "mph"
    
    def honk(self):
        """
        Car-specific method for honking horn.
        
        REQUIREMENTS:
        1. Check if engine is running
        2. If not running, print: "Cannot honk: Engine is off!"
        3. If running, print: "BEEP BEEP! [make] [model] honking!"
        
        DIFFICULTY: Easy
        """
        # TODO: Implement honking with engine check
        if self.is_running == True:
            print("BEEP BEEP! " + self.make + " " + self.model + " is honking!")
    
    def accelerate(self, speed_increase):
        """
        Override parent accelerate method for cars.
        
        Parameters:
        speed_increase (float): Speed increase in mph
        
        REQUIREMENTS:
        1. Call parent accelerate method using super()
        2. If acceleration was successful (engine running, has fuel, etc.):
           - Print additional message: "Car accelerating on road..."
        
        This demonstrates method overriding while still using parent functionality.
        
        DIFFICULTY: Medium
        """
        # TODO: Call super().accelerate() and add car-specific behavior
        if super().accelerate(speed_increase):
            print("Car accelerating on road")

    
    def get_info(self):
        """
        Override parent get_info to include car-specific details.
        
        Returns:
        str: Enhanced vehicle info with car details
        
        REQUIREMENTS:
        1. Call parent get_info() using super()
        2. Add car-specific information:
           - Number of doors
           - Drive type
        3. Return the combined information
        
        EXAMPLE OUTPUT:
        "2020 Ford Mustang
         Status: Running
         Speed: 45/120 mph
         Fuel: 8.5/16.0 gallons
         Passengers: 2/4
         Doors: 2
         Drive Type: RWD"
        
        DIFFICULTY: Medium
        """
        # TODO: Call super().get_info() and add car details
        super().get_info()
        print("Doors: " + str(self.num_doors) + "\nDrive Type: " + self.drive_type)

class Boat(Vehicle):
    """
    Boat class that inherits from Vehicle.
    
    Boats have unique features like hull types and anchoring.
    Speed is measured in knots instead of mph.
    """
    
    def __init__(self, make, model, year, max_speed, fuel_capacity, passenger_capacity,
                 hull_type, length):
        """
        Constructor for Boat class.
        
        Parameters:
        (inherits all Vehicle parameters, plus:)
        hull_type (str): "Catamaran", "Monohull", "Pontoon", etc.
        length (float): Boat length in feet
        
        REQUIREMENTS:
        1. Call parent constructor using super()
        2. Store hull_type and length as additional attributes
        3. Set speed_units to "knots"
        4. Initialize is_anchored to True (boats start anchored)
        
        DIFFICULTY: Medium
        """
        # TODO: Call super().__init__() and add boat-specific attributes
        super().__init__(make, model, year, max_speed, fuel_capacity, passenger_capacity)
        self.hull_type = hull_type
        self.length = length
        self.speed_units = "knots"
        self.is_anchored = True
    
    def raise_anchor(self):
        """
        Boat-specific method for raising anchor.
        
        REQUIREMENTS:
        1. Check if engine is running
        2. If not running, print: "Cannot raise anchor: Engine must be running!"
        3. If already anchor is raised, print: "Anchor is already raised!"
        4. If conditions met, set is_anchored to False
        5. Print: "Anchor raised! [make] [model] ready to sail!"
        
        DIFFICULTY: Medium
        """
        # TODO: Implement anchor raising with validations
        if self.is_running == False:
            print("Cannot raise anchor: Engine must be running!")
        elif self.is_anchored == True:
            print("Anchor is already raised!")
        else:
            self.is_anchored = False
            print("Anchor raised! " + str(self.make) + " " + str(self.model) + " ready to sail!")
    
    def drop_anchor(self):
        """
        Boat-specific method for dropping anchor.
        
        REQUIREMENTS:
        1. If already anchored, print: "Anchor is already dropped!"
        2. If moving (current_speed > 0), print: "Cannot drop anchor while moving!"
        3. If conditions met, set is_anchored to True
        4. Print: "Anchor dropped! [make] [model] is now anchored!"
        
        DIFFICULTY: Easy
        """
        # TODO: Implement anchor dropping with validations
        if self.is_anchored == True:
            print("Anchor is already dropped!")
        elif self.current_speed > 0:
            print("Cannot drop anchor while moving!")
        else:
            self.is_anchored = True
            print("Anchor dropped! "+ str(self.make) + " " + str(self.model) + " is now anchored!")
    
    def accelerate(self, speed_increase):
        """
        Override parent accelerate method for boats.
        
        Parameters:
        speed_increase (float): Speed increase in knots
        
        REQUIREMENTS:
        1. Check if anchor is raised - if not, print error and return
        2. Call parent accelerate method using super()
        3. If acceleration was successful:
           - Print additional message: "Boat cruising on water..."
        
        ERROR: "Cannot accelerate: Anchor is down!"
        
        DIFFICULTY: Medium
        """
        # TODO: Check anchor, call super().accelerate(), add boat message
        if self.is_anchored == True:
            print("Cannot accelerate: Anchor is down!")
        else:
            if super().accelerate(speed_increase):
                print("Boat cruising on water...")

class Plane(Vehicle):
    """
    Plane class that inherits from Vehicle.
    
    Planes have unique features like altitude and landing gear.
    Speed is measured in mph but planes can also climb.
    """
    
    def __init__(self, make, model, year, max_speed, fuel_capacity, passenger_capacity,
                 wing_type, max_altitude):
        """
        Constructor for Plane class.
        
        Parameters:
        (inherits all Vehicle parameters, plus:)
        wing_type (str): "Fixed", "Swept", "Delta", etc.
        max_altitude (int): Maximum altitude in feet
        
        REQUIREMENTS:
        1. Call parent constructor using super()
        2. Store wing_type and max_altitude as additional attributes
        3. Set speed_units to "mph"
        4. Initialize current_altitude to 0 (plane starts on ground)
        5. Initialize landing_gear_down to True (gear starts down)
        
        DIFFICULTY: Medium
        """
        # TODO: Call super().__init__() and add plane-specific attributes
        super().__init__(make, model, year, max_speed, fuel_capacity, passenger_capacity)
        self.wing_type = wing_type
        self.max_altitude = max_altitude
        self.speed_units = "mph"
        self.current_altitude = 0
        self.landing_gear_down = True
    
    def takeoff(self):
        """
        Plane-specific method for taking off.
        
        REQUIREMENTS:
        1. Check if engine is running - if not, print error and return
        2. Check if current_speed >= 60 - if not, print error and return
        3. Check if landing gear is down - if not, print error and return
        4. If all conditions met:
           - Set current_altitude to 1000
           - Set landing_gear_down to False
           - Print success message
        
        ERRORS:
        - "Cannot takeoff: Engine must be running!"
        - "Cannot takeoff: Need at least 60 mph for takeoff!"
        - "Cannot takeoff: Landing gear must be down!"
        
        SUCCESS: "[make] [model] taking off! Now at 1000 feet altitude."
        
        DIFFICULTY: Hard
        """
        # TODO: Implement takeoff with all validations
        if self.is_running == False:
            print("Cannot takeoff: Engine must be running!")
        elif self.current_speed < 60:
            print("Cannot takeoff: Need at least 60 mph for takeoff!")
        elif self.landing_gear_down == False:
            print("Cannot takeoff: Landing gear must be down!")
        else:
            self.current_altitude = 1000
            self.landing_gear_down = False
            print(str(self.make) + " " + str(self.model) + " taking off! Now at 1000 feet altitude.")
    
    def land(self):
        """
        Plane-specific method for landing.
        
        REQUIREMENTS:
        1. Check if current_altitude > 0 - if not, print error and return
        2. Check if current_speed <= 80 - if not, print error and return
        3. If conditions met:
           - Set current_altitude to 0
           - Set landing_gear_down to True
           - Set current_speed to 0
           - Print success message
        
        ERRORS:
        - "Cannot land: Already on ground!"
        - "Cannot land: Speed too high! Must be 80 mph or less."
        
        SUCCESS: "[make] [model] landed safely! Welcome to the ground."
        
        DIFFICULTY: Medium
        """
        # TODO: Implement landing with validations
        if self.current_altitude <= 0:
            print("Cannot land: Already on ground!")
        elif self.current_speed > 80:
            print("Cannot land: Speed too high! Must be 80 mph or less.")
        else:
            self.current_altitude = 0
            self.landing_gear_down = True
            self.current_speed = 0
            print(str(self.make) + " " + str(self.model) + " landed safely! Welcome to the ground.")

def test_inheritance_demo():
    """
    Demonstrate inheritance and polymorphism with all vehicle types.
    """
    print("TESTING INHERITANCE AND POLYMORPHISM")
    print("=" * 60)
    
    # Create different vehicle objects
    car = Car("Ford", "Mustang", 2020, 120, 16, 4, 2, "RWD")
    boat = Boat("Yamaha", "242X", 2021, 50, 40, 8, "Monohull", 24)
    plane = Plane("Cessna", "172", 2019, 140, 56, 4, "Fixed", 14000)
    
    # Store in list to demonstrate polymorphism
    vehicles = [car, boat, plane]
    
    print("CREATED VEHICLES:")
    for vehicle in vehicles:
        print(f"- {vehicle.year} {vehicle.make} {vehicle.model}")
    
    print("\n" + "="*60)
    print("DEMONSTRATING POLYMORPHISM - Same method, different behaviors:")
    
    for vehicle in vehicles:
        print(f"\n--- {vehicle.__class__.__name__} Test ---")
        vehicle.add_fuel(20)
        vehicle.start_engine()
        vehicle.accelerate(30)
        
        # Call class-specific methods
        if isinstance(vehicle, Car):
            vehicle.honk()
        elif isinstance(vehicle, Boat):
            vehicle.raise_anchor()
        elif isinstance(vehicle, Plane):
            vehicle.takeoff()
        
        print(f"Info:\n{vehicle.get_info()}")

def test_method_overriding():
    """
    Test that child classes properly override parent methods.
    """
    print("\nTESTING METHOD OVERRIDING")
    print("=" * 50)
    
    # Create one of each vehicle
    car = Car("Honda", "Civic", 2022, 110, 12, 5, 4, "FWD")
    boat = Boat("Boston Whaler", "170 Montauk", 2020, 35, 30, 6, "Monohull", 17)
    plane = Plane("Piper", "Cherokee", 2018, 125, 50, 4, "Fixed", 12000)
    
    vehicles = [car, boat, plane]
    
    # Test that get_info() is customized for each type
    print("Testing get_info() method overriding:")
    for vehicle in vehicles:
        print(f"\n{vehicle.__class__.__name__} Info:")
        print(vehicle.get_info())
    
    # Test acceleration overriding
    print("\nTesting accelerate() method overriding:")
    for vehicle in vehicles:
        print(f"\n--- {vehicle.__class__.__name__} Acceleration ---")
        vehicle.start_engine()
        vehicle.add_fuel(10)
        
        if isinstance(vehicle, Boat):
            vehicle.raise_anchor()
        
        vehicle.accelerate(20)

def test_unique_features():
    """
    Test unique features of each vehicle type.
    """
    print("\nTESTING UNIQUE VEHICLE FEATURES")
    print("=" * 50)
    
    # Test car features
    print("--- CAR UNIQUE FEATURES ---")
    car = Car("Tesla", "Model 3", 2023, 140, 0, 5, 4, "AWD")  # Electric car!
    car.start_engine()
    car.honk()
    print(f"Car details:\n{car.get_info()}")
    
    # Test boat features
    print("\n--- BOAT UNIQUE FEATURES ---")
    boat = Boat("Sea Ray", "Sundancer", 2021, 45, 80, 10, "Catamaran", 35)
    boat.start_engine()
    boat.add_fuel(30)
    boat.accelerate(20)  # Should fail - anchor down
    boat.raise_anchor()
    boat.accelerate(20)  # Should work now
    boat.drop_anchor()
    
    # Test plane features
    print("\n--- PLANE UNIQUE FEATURES ---")
    plane = Plane("Boeing", "737", 2020, 500, 6875, 180, "Swept", 37000)
    plane.start_engine()
    plane.add_fuel(1000)
    plane.takeoff()  # Should fail - not enough speed
    plane.accelerate(80)
    plane.takeoff()  # Should work now
    plane.land()

# Uncomment to run tests:
test_inheritance_demo()
test_method_overriding()
test_unique_features()