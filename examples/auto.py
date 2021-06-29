# Script auto.py is used as a template for similar scripts when I want to used my drone in AUTO mode.
# 

import asyncio

from mavsdk import System
from mavsdk.mission import (MissionItem, MissionPlan)


async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/serial0:921600")

    print("Waiting to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    print_mission_progress_task = asyncio.ensure_future(print_mission_progress(drone))

    running_tasks = [print_mission_progress_task]
    termination_task = asyncio.ensure_future(observe_is_in_air(drone, running_tasks))

    mission_items = []
    mission_items.append(MissionItem(45.4929235,
				                             18.0954726,
                                     10,
                                     5,
                                     True,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.START_VIDEO,
                                     20,
                                     20))
    mission_items.append(MissionItem(45.4926528,
    				                         18.0940403,
                                     10,
                                     5,
                                     True,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.START_VIDEO,
                                     20,
                                     20))
    mission_items.append(MissionItem(45.4918819,
                                     18.0936916,
                                     10,
                                     5,
                                     True,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.START_VIDEO,
                                     20,
                                     20))

    mission_plan = MissionPlan(mission_items)

    await drone.mission.set_return_to_launch_after_mission(True)

    print("Uploading mission")
    await drone.mission.upload_mission(mission_plan)

    print("Arming")
    await drone.action.arm()

    print("Starting mission")
    await drone.mission.start_mission()

    await termination_task


async def print_mission_progress(drone):
    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: "
              f"{mission_progress.current}/"
              f"{mission_progress.total}")


async def observe_is_in_air(drone, running_tasks):
    """ Monitors whether the drone is flying or not and
    returns after landing """

    was_in_air = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            was_in_air = is_in_air

        if was_in_air and not is_in_air:
            for task in running_tasks:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            await asyncio.get_event_loop().shutdown_asyncgens()

            return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
