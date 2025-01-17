import streamlit as st
from rocketpy import Environment, SolidMotor, Rocket, Flight
from streamlit_folium import st_folium
import folium

# Add a title to your app
st.title('Rocket Simulator App')

# st.title('Map Click Coordinates')
# st.write('Click on the map to get the longitude and latitude.')

# # Initialize the map
# m = folium.Map(location=[20, 0], zoom_start=2)

# # Add a click event listener to the map
# click_event_js = """
#     function(e) {
#         var coords = e.latlng;
#         var lat = coords.lat;
#         var lng = coords.lng;
#         var popup = L.popup()
#             .setLatLng(coords)
#             .setContent("Lat: " + lat + "<br>Lng: " + lng)
#             .openOn(%s);
#         window.parent.postMessage({lat: lat, lng: lng}, "*");
#     }
# """ % m.get_name()

# m.add_child(folium.ClickForMarker(popup=None))

# # Display the map
# result = st_folium(m, width=700, height=500)

# # Display coordinates when clicked
# if result['last_clicked']:
#     lat = result['last_clicked']['lat']
#     lng = result['last_clicked']['lng']
#     st.write(f'Latitude: {lat}, Longitude: {lng}')



# We want a selection between the five locations, and then store that location in a variable called `location'


st.write("Testing")
st.write("Please define your environment:")
latitude_number = st.number_input("Insert latitude")
longitude_number = st.number_input("Insert longitude")
elevation_number = st.number_input("Insert elevation")

environment = Environment(latitude=latitude_number, longitude=longitude_number, elevation=elevation_number)



number_of_motors = st.slider('Number of Motors:', min_value=1, max_value=20)

for i in range(number_of_motors):
    st.write("new motor added")

st.write(str(number_of_motors))

motor_type = st.selectbox("What type of rocket?",
    ("Forbidden ESP", "Solid", "Hybrid", "Liquid"))


# # Solid case
# if motor_type is "Forbidden ESP":
#     st.write("MAY need to electrocute it")

# # Solid case
# if motor_type is "Solid":
#     st.write("You've selected solid")

# # Hybrid case
# if motor_type is "Hybrid":
#     st.write("You've selected hybrid")

# # Liquid case
# if motor_type is "Liquid":
#     st.write("You've selected liquid")


# st.write("Please define your environment:")
# latitude_number = st.number_input("Insert latitude")
# longitude_number = st.number_input("Insert longitude")
# elevation_number = st.number_input("Insert elevation")

# environment = Environment(latitude=latitude_number, longitude=longitude_number, elevation=elevation_number)


# def calculate_square(x):
#     return x**2

# if st.button('Calculate'):
#     st.write(calculate_square(2))
#     print(calculate_square(2))

