# Python-MAVSDK

Script for my DIY drone written in Python. 

## Getting Started

Repository contains 3 simple scripts used on a real drone. One script is used for connection and simple takeoff and landing, just to test if everything is OK. The third one is used for flying to exact points and orbiting around my neighbourhood, but with a few adjustments, it can be used for flying anywhere. The forth is used for flying in AUTO mode.

### Prerequisites


```
Python 
mavsdk
PX4 source code
```

### Description

PX4 is the Professional Autopilot. Developed by world-class developers from industry and academia, and supported by an active world wide community, it powers all kinds of vehicles from racing and cargo drones through to ground vehicles and submersibles. MAVSDK is a collection of libraries for various programming languages to interface with MAVLink systems such as drones, cameras or ground systems. The libraries provides a simple API for managing one or more vehicles, providing programmatic access to vehicle information and telemetry, and control over missions, movement and other operations. The libraries can be used onboard a drone on a companion computer or on the ground for a ground station or mobile device. MAVSDK is cross-platform: Linux, macOS, Windows, Android and iOS. MAVSDK is primarly written in C++ with wrappers available for several programming languages, including Python.

MAVSDK is a set of libraries providing a high-level API to MAVLink, providing easy to learn programmatic access to vehicle information and telemetry, as well as control over missions, movement, and other operations.  If robot or drone is MAVLink-enabled (i.e. it “talks MAVLink”), then MAVSDK will allow you to write programs that control it. MAVSDK is primarily used by developers as a tool for integrating different components on a vehicle – the flight stack, companion computer, and MAVLink peripherals (e.g. cameras). It can also be used for implementing ground station functionality that is specific to a particular domain (that would not normally be in a generic GCS like QGroundControl).
