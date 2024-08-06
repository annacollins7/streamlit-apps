import streamlit as st
from rocketpy import Environment, SolidMotor, Rocket, Flight
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt
import numpy as np

# Add a title to your app
st.title('Rocket Simulator App')

# Add a section for map click coordinates
st.header('Map Click Coordinates')
st.write('Click on the map to get the longitude and latitude.')

# Initialize the map
m = folium.Map(location=[20, 0], zoom_start=2)

# Add a click event listener to the map
click_event_js = """
    function(e) {
        var coords = e.latlng;
        var lat = coords.lat;
        var lng = coords.lng;
        var popup = L.popup()
            .setLatLng(coords)
            .setContent("Lat: " + lat + "<br>Lng: " + lng)
            .openOn(%s);
        window.parent.postMessage({lat: lat, lng: lng}, "*");
    }
""" % m.get_name()

m.add_child(folium.ClickForMarker(popup=None))

# Display the map
result = st_folium(m, width=700, height=500)

# Display coordinates when clicked
if result['last_clicked']:
    lat = result['last_clicked']['lat']
    lng = result['last_clicked']['lng']
    st.write(f'Latitude: {lat}, Longitude: {lng}')

# Create environment input section
st.header('Define Your Environment')
latitude_number = st.number_input("Insert latitude", value=0.0)
longitude_number = st.number_input("Insert longitude", value=0.0)
elevation_number = st.number_input("Insert elevation (meters)", value=0)

# Create environment object
environment = Environment(latitude=latitude_number, longitude=longitude_number, elevation=elevation_number)

# Number of motors input
st.header('Rocket Configuration')
number_of_motors = st.slider('Number of Motors:', min_value=1, max_value=20)

# Display number of motors added
for i in range(number_of_motors):
    st.write(f"Motor {i+1} added")

# Select motor type
motor_type = st.selectbox("Select the type of rocket motor:", ("Solid", "Hybrid", "Liquid"))

# Simulate weather conditions
st.header('Simulate Weather Conditions')
weather_condition = st.selectbox("Select weather condition:", ("Clear", "Windy", "Rainy"))

# Adjust environment based on weather condition
if weather_condition == "Windy":
    environment.setWind(speed=15, angle=90)  # Example values, adjust as needed
elif weather_condition == "Rainy":
    environment.setRainfall(rate=5)  # Example values, adjust as needed

# Function to simulate rocket flight and plot trajectory
def simulate_flight():
    # Create a SolidMotor object with the correct parameters
    motor = SolidMotor(
        thrust_source=lambda x: 1 / (x + 1),  # Adjust to the actual thrust data file
        dry_mass=1.815,
        dry_inertia=(0.125, 0.125, 0.002),
        center_of_dry_mass_position=0.317,
        grains_center_of_mass_position=0.397,
        burn_time=3.9,
        grain_number=5,
        grain_separation=5 / 1000,
        grain_density=1815,
        grain_outer_radius=33 / 1000,
        grain_initial_inner_radius=15 / 1000,
        grain_initial_height=120 / 1000,
        nozzle_radius=33 / 1000,
        throat_radius=11 / 1000,
        interpolation_method="linear",
        nozzle_position=0,
        coordinate_system_orientation="nozzle_to_combustion_chamber",
    )
    
    # Rocket object
    rocket = Rocket(
        radius=127 / 2000,
        mass=14.426,
        inertia=(6.321, 6.321, 0.034),
        power_off_drag="powerOffDragCurve.csv",
        power_on_drag="powerOnDragCurve.csv",
        center_of_mass_without_motor=0,
        coordinate_system_orientation="tail_to_nose",
    )
    
    # Attach motor to rocket
    rocket.add_motor(motor, position=-1.255)  # Adjust position as needed
    
    # Flight object
    flight = Flight(
        rocket=rocket,
        environment=environment,
        inclination=90,
        heading=0
    )
    
    # Get flight data
    time, altitude = flight.solution[:,0], flight.solution[:,2]
    
    # Plot trajectory
    plt.figure(figsize=(10, 5))
    plt.plot(time, altitude)
    plt.title('Rocket Flight Trajectory')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid(True)
    st.pyplot(plt)

# Simulate flight and plot trajectory button
if st.button('Simulate Flight'):
    simulate_flight()
