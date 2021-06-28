# Script takeoff_and_land.py shows connection, takeoff and landing.

import asyncio
from mavsdk import System


async def run():

    drone = System()
    await drone.connect(system_address=“serial:///dev/serial0:921600”)

    print("Waiting for connection...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    print("Waiting for position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    print("Arming")
    await drone.action.arm()

    await drone.action.set_takeoff_altitude(10)
    await asyncio.sleep(5)
    print("Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(20)

    print("Landing")
    await drone.action.land()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
