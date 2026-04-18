# dhari-hyderabad-metro
# 🚇 Dhari (దారి) – Hyderabad Metro Navigation System

Dhari is a **citizen-centric metro navigation tool** designed specifically for the Hyderabad Metro network.
It focuses on **accurate structural information rather than predictions**, helping commuters plan metro journeys with clarity and reliability.

The application provides route planning, fare estimation, travel time estimation, and visual route maps using an interactive interface.

## ✨ Features

🚇 **Metro Route Planning**
Find the shortest path between metro stations using a graph-based algorithm.

💰 **Fare Calculation**
Automatically calculates the fare based on official Hyderabad Metro fare slabs.

⏱ **Travel Time Estimation**
Estimates travel time based on the number of stations.

📍 **Nearest Metro Station Detection**
Detects the nearest metro station using device GPS.

🌐 **Multilingual Interface**
Supports multiple languages:

* English
* Hindi
* Telugu

🗺 **Interactive Metro Map**
Displays all metro stations on an interactive map.

🔴🔵🟢 **Colored Route Visualization**
Shows metro routes using actual metro line colors.

⏰ **Metro Service Clock**
Warns users when metro services are closed.

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Folium (Interactive Maps)**
* **Geospatial Distance Calculation**

---

## 📂 Project Structure

```
dhari-hyderabad-metro/
│
app.py
route_engine.py
fare_engine.py
time_estimator.py
nearest_station.py
location_service.py
service_clock.py
requirements.txt
render.yaml
README.md
│
data/
    stations.csv
    fare_matrix.csv
    interchange_stations.csv
│
assets/
    hyderabad_metro_map.png

## 📊 Example Usage

Example route:

```
Start Station: Miyapur  
Destination: Ameerpet
```

Output:

```
Stations: 6
Estimated Time: 12 minutes
Fare: ₹37
Route: Miyapur → JNTU → KPHB → Kukatpally → Balanagar → Ameerpet
```

The route is also highlighted visually on the metro map.

---

## 🚀 Deployment

This project can be deployed on:

* Render
* Streamlit Community Cloud
* Railway

Example Render deployment command:

```
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 🔮 Future Improvements

* Real-time train tracking
* Station exit guidance
* Offline metro navigation mode
* Multi-city metro support

---

## 👨‍💻 Author

Rishi
