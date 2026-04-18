import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

from route_engine import find_route
from fare_engine import calculate_fare
from time_estimator import estimate_travel
from nearest_station import find_nearest_station
from service_clock import metro_service_status


st.set_page_config(
    page_title="Dhari - Hyderabad Metro Guide",
    page_icon="🚇",
    layout="wide"
)

# Load datasets
stations_df = pd.read_csv("data/stations.csv")

station_list = stations_df["station"].unique()

# Metro line colors
line_colors = {
    "Red": "red",
    "Blue": "blue",
    "Green": "green"
}


# Language selection
language = st.sidebar.selectbox(
    "Language / भाषा / భాష",
    ["English", "हिंदी", "తెలుగు"]
)

translations = {

    "English": {
        "title": "Dhari (దారి)",
        "subtitle": "Precision Hyderabad Metro Guide",
        "plan": "Plan Your Metro Journey",
        "start": "Start Station",
        "end": "Destination Station",
        "find": "Find Route",
        "stations": "Stations",
        "time": "Estimated Time",
        "fare": "Fare",
        "route": "Route",
        "map": "Hyderabad Metro Network",
        "gps": "Use My Location"
    },

    "हिंदी": {
        "title": "धारी (దారి)",
        "subtitle": "हैदराबाद मेट्रो गाइड",
        "plan": "अपनी मेट्रो यात्रा की योजना बनाएं",
        "start": "प्रारंभ स्टेशन",
        "end": "गंतव्य स्टेशन",
        "find": "मार्ग खोजें",
        "stations": "स्टेशन",
        "time": "अनुमानित समय",
        "fare": "किराया",
        "route": "मार्ग",
        "map": "हैदराबाद मेट्रो नेटवर्क",
        "gps": "मेरी लोकेशन उपयोग करें"
    },

    "తెలుగు": {
        "title": "దారి (Dhari)",
        "subtitle": "హైదరాబాద్ మెట్రో గైడ్",
        "plan": "మీ మెట్రో ప్రయాణాన్ని ప్లాన్ చేయండి",
        "start": "ప్రారంభ స్టేషన్",
        "end": "గమ్యస్థానం స్టేషన్",
        "find": "మార్గం కనుగొను",
        "stations": "స్టేషన్లు",
        "time": "అంచనా సమయం",
        "fare": "చార్జ్",
        "route": "మార్గం",
        "map": "హైదరాబాద్ మెట్రో నెట్‌వర్క్",
        "gps": "నా లొకేషన్ ఉపయోగించు"
    }
}

t = translations[language]


st.markdown(f"<h1 style='text-align:center;'>🚇 {t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:gray'>{t['subtitle']}</p>", unsafe_allow_html=True)

st.markdown("---")


# Metro service clock
if not metro_service_status():
    st.warning("Metro service currently closed (6 AM – 11 PM)")


st.subheader(t["plan"])


# Station selectors
col1, col2 = st.columns(2)

with col1:
    start_station = st.selectbox(t["start"], station_list)

with col2:
    end_station = st.selectbox(t["end"], station_list)


# Route calculation
if st.button(t["find"]):
    st.session_state["route"] = find_route(start_station, end_station)


st.markdown("### 📍 Detect Nearest Metro Station")

if st.button("Use My Location"):

    location = streamlit_geolocation()

    if location is not None:

        lat = location.get("latitude")
        lon = location.get("longitude")

        if lat is not None and lon is not None:

            station, distance = find_nearest_station(lat, lon)

            st.success(
                f"Nearest Station: {station} ({round(distance,2)} km away)"
            )

        else:
            st.info("Detecting your location... please wait")

    else:
        st.warning("Location access denied or unavailable")

# Route result
route_coords = []

if "route" in st.session_state:

    route = st.session_state["route"]

    if route:

        stations, time = estimate_travel(route)

        distance = stations * 1.2
        fare = calculate_fare(distance)

        st.markdown("---")

        st.subheader("Journey Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(t["stations"], stations)

        with c2:
            st.metric(t["time"], f"{time} min")

        with c3:
            st.metric(t["fare"], f"₹ {fare}")

        st.subheader(t["route"])

        route_text = " → ".join(route)

        st.success(route_text)

        for station in route:

            row = stations_df[stations_df["station"] == station]

            lat = row.iloc[0]["lat"]
            lon = row.iloc[0]["lon"]

            route_coords.append([lat, lon])


st.markdown("---")
st.subheader(t["map"])


# Map center
map_center = [17.3850, 78.4867]

m = folium.Map(location=map_center, zoom_start=11)


# Add station markers
for _, row in stations_df.iterrows():

    folium.Marker(
        [row["lat"], row["lon"]],
        tooltip=row["station"],
        icon=folium.Icon(color="blue", icon="train")
    ).add_to(m)


# Colored route visualization
if route_coords:

    for i in range(len(route_coords) - 1):

        station_name = route[i]

        row = stations_df[stations_df["station"] == station_name]

        line = row.iloc[0]["line"]

        color = line_colors.get(line, "red")

        folium.PolyLine(
            [route_coords[i], route_coords[i+1]],
            color=color,
            weight=6
        ).add_to(m)


st_folium(m, width=900, height=500)


st.markdown("---")

st.subheader("Hyderabad Metro Route Map")

st.image("hyderabad_metro_map.png", use_container_width=True)


st.caption("Fare values are approximate based on Hyderabad Metro fare slabs.")
