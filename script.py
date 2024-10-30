import time
from FlightRadar24 import FlightRadar24API
from unicorn.displayCode import displayCode
from unicorn.displayCode import displayIcon

fr_api = FlightRadar24API()

def scanArea():
    
    bounds = fr_api.get_bounds_by_point(53.432, -2.112, 500)
    flights = fr_api.get_flights(bounds = bounds)
    
    if flights:
        flight = flights[0]
        flight_details = fr_api.get_flight_details(flight)
        flight.set_flight_details(flight_details)

        result = {
                "origin": flight.origin_airport_name,
                "destination": flight.destination_airport_name,
                "orig_code": flight.origin_airport_iata,
                "dest_code": flight.destination_airport_iata
            }

        print(result)
        aircode = result["orig_code"] 
        displayCode(aircode,0)
    else:
        displayIcon('plane')
        print("no flight found")

while True:
    scanArea()
    time.sleep(3)
