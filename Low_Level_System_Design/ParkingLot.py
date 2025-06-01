from enum import Enum
from typing import List


class VehicleSize(Enum):
    MotorCyle = 1
    Compact = 2
    Large = 3


class Vehicle:
    def __init__(self, license_plate: str, size: VehicleSize):
        self.license_plate = license_plate
        self.size = size


class MotorCyle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleSize.MotorCyle)


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleSize.Compact)


class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleSize.Large)


class ParkingSpot:
    def __init__(self, spot_id: int, size: VehicleSize):
        self.spot_id = spot_id
        self.size = size
        self.vehicle = None

    def can_fit_vehicle(self, vehicle: Vehicle):
        return self.vehicle is not None and self.size.value <= vehicle.size.value


    def park(self, vehicle: Vehicle) -> bool:
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False

    def leave(self):
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None


class ParkingLevel:
    def __init__(self, level_id : int, spots: List[ParkingSpot]):
        self.level_id = level_id
        self.spots = spots

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.spots:
            if spot.park(vehicle):
                print(f"Parker {vehicle.license_plate} in splot {spot.spot_id} on level {self.level_id}")
                return True

        print(f"No available spot for {vehicle.license_plate} on level {self.level_id}")
        return False

    def leave_vehicle(self, license_plate: str):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate:
                spot.leave()
                print(f"{license_plate} left spot {spot.spot_id} on level {self.level_id}")
                return True
        return False


class PakingLot:
    def __init__(self, levels: List[ParkingLevel]):
        self.levels = levels

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        print(f"Parking failed for {vehicle.license_plate}")
        return False

    def leave_vehicle(self, license_plate: str) -> bool:
        for level in self.levels:
            if level.leave_vehicle(license_plate):
                return True
        return False



# Setup
spots = [ParkingSpot(i, VehicleSize.Compact) for i in range(5)]
level = ParkingLevel(0, spots)
lot = PakingLot([level])


# Vehicle
car = Car("ABC123")
bike = MotorCyle("BIKE45")


# Parking
lot.park_vehicle(car)
lot.park_vehicle(bike)

#leaving
lot.leave_vehicle()