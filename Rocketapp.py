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
    environment.windSpeed = 15  # Example value, adjust as needed
    environment.windDirection = 90  # Example value, adjust as needed
elif weather_condition == "Rainy":
    environment.rainRate = 5  # Example value, adjust as needed

# Function to simulate rocket flight and plot trajectory
def simulate_flight():
    # Dummy motor for demonstration
    motor = SolidMotor(thrustSource=lambda x: 1 / (x + 1), burnOut=3.9, grainNumber=5, grainSeparation=5/1000, grainDensity=1815, grainOuterRadius=33/1000, grainInitialInnerRadius=15/1000, grainInitialHeight=120/1000, nozzleRadius=33/1000, throatRadius=11/1000, interpolationMethod='linear')
    
    # Rocket object
    rocket = Rocket(motor=motor, radius=127/2000, mass=19.2, inertiaI=6.60, inertiaZ=0.0351, distanceRocketNozzle=-1.255, distanceRocketPropellant=0.930, powerOffDrag=2.5, powerOnDrag=2.5)
    
    # Flight object
    flight = Flight(rocket=rocket, environment=environment, inclination=90, heading=0)
    
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


