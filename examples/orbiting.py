# Script orbiting.py is used for flying and orbiting around my neighbourhood.
# It can be used as a template for other scripts, but coordinates should be adjusted.

import asyncio
from mavsdk import System
from mavsdk.action import OrbitYawBehavior

async def run():
    drone = System()
    yaw_behaviour = OrbitYawBehavior(1) 
    await drone.connect(system_address="serial:///dev/serial0:921600")

    print("Waiting to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break
            
    rint("Waiting for position estimate")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    async for terrain_info in drone.telemetry.home():
        absolute_altitude = terrain_info.absolute_altitude_m
        break

    print("Arming")
    await drone.action.arm()

    print("Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(1)
    flying_alt = absolute_altitude + 20.0 #To fly drone 20m above the ground plane
    #goto_location() takes Absolute MSL altitude
        
    await drone.action.goto_location(45.4929235, 18.0954726, flying_alt, 0)
    await asyncio.sleep(20)
    print("Orbiting")
    await drone.action.do_orbit(5, 2, yaw_behaviour, 45.4929235, 18.0954726, flying_alt)
    await asyncio.sleep(20)
    
    await drone.action.goto_location(45.4926528, 18.0940403, flying_alt, 0)
    await asyncio.sleep(20)
    print("Orbiting")
    await drone.action.do_orbit(5, 2, yaw_behaviour, 45.4926528, 18.0940403, flying_alt)
    await asyncio.sleep(20)
    
       
    await drone.action.goto_location(45.4918819, 18.0936916, flying_alt, 0)
    await asyncio.sleep(20)
    print("Orbiting")
    await drone.action.do_orbit(5, 2, yaw_behaviour, 45.4918819, 18.0936916, flying_alt)
    await asyncio.sleep(20) 
    
    print("Return to launch.")
    await drone.action.return_to_launch()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run()) 
