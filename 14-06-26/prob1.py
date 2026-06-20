class Vehicle:
    def __init__(self,number,name,hours):
        self.vehicle_number=number
        self.owner_name=name
        self.parking_hours=hours
    def total_parking_revenue(self):
            return 0
class Car(Vehicle):
    def total_parking_revenue(self):
        return self.parking_hours*30
class Bike(Vehicle):
    def total_parking_revenue(self):
        return self.parking_hours*15
class Truck(Vehicle):
    def total_parking_revenue(self):
        return self.parking_hours*50
n=int(input())
vehicles=[]
total_revenue=0
highest_bill=0
highest_vehicle=None
for _ in range(n):
    vehicle_type,vehicle_number,owner_name,parking_hours=input().split()
    parking_hours=int(parking_hours)
    vehicle_type=vehicle_type.lower()
    if vehicle_type=="car":
        v =Car(vehicle_number,owner_name,parking_hours)
    elif vehicle_type=="bike":
        v =Bike(vehicle_number,owner_name,parking_hours)
    elif vehicle_type=="truck":
        v =Truck(vehicle_number,owner_name,parking_hours)
    vehicles.append(v)
for v in vehicles:
    bill=v.total_parking_revenue()
    print(v.vehicle_number,v.owner_name,bill)
    total_revenue+=bill
    if bill>highest_bill:
        highest_bill=bill
        highest_vehicle=v
print("total Revenue:",total_revenue)
print("Highest Bill Vehicle",highest_vehicle.vehicle_number,highest_vehicle.owner_name,highest_bill)