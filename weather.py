# Run:
# python -m streamlit run weather.py

import requests
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Weather & Air Quality Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 45%,
            #172554 100%
        );
        color: white;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #ffffff;
    }

    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    }

    .metric-title {
        color: #94a3b8;
        font-size: 14px;
        font-weight: 600;
    }

    .metric-value {
        color: #ffffff;
        font-size: 30px;
        font-weight: 800;
        margin-top: 5px;
    }

    /* Section title */
    .section-title {
        font-size: 25px;
        font-weight: 750;
        margin-top: 30px;
        margin-bottom: 15px;
        color: white;
    }

    /* Info box */
    .info-box {
        background: rgba(59, 130, 246, 0.10);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0b1120;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌍 Weather & Air Quality Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Real-Time Weather, AQI & Air Pollution Monitoring</div>',
    unsafe_allow_html=True
)

# ============================================================
# DATA LISTS
# ============================================================

name = []
temp = []
tmin = []
tmax = []
coun = []
pre = []
des = []
clo = []
spe = []
vis = []
hum = []

aqi = []
co = []
no = []
no2 = []
o3 = []
so2 = []
pm2_5 = []
pm10 = []
nh3 = []

# ============================================================
# API
# ============================================================

# IMPORTANT: For public repositories, use an environment variable
# instead of hard-coding the OpenWeather API key.
api = "YOUR_OPENWEATHER_API_KEY"

lat = [
    "23.0225",
    "21.1702",
    "22.3072",
    "22.3039",
    "24.1721",
    "21.7514",
    "21.5222",
    "23.5976",
    "22.7554",
    "22.7112"
]

lon = [
    "72.5714",
    "72.8311",
    "73.1812",
    "70.8022",
    "72.4346",
    "72.1501",
    "70.4579",
    "72.9642",
    "73.6143",
    "72.8631"
]

# ============================================================
# API DATA FETCH
# ============================================================

with st.spinner("🌐 Fetching weather & air quality data..."):

    for i in range(len(lat)):

        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat[i]}&lon={lon[i]}&appid={api}"
        )

        air_url = (
            f"https://api.openweathermap.org/data/2.5/air_pollution"
            f"?lat={lat[i]}&lon={lon[i]}&appid={api}"
        )

        try:

            weather_response = requests.get(
                weather_url,
                timeout=10
            )

            air_response = requests.get(
                air_url,
                timeout=10
            )

            weather_response.raise_for_status()
            air_response.raise_for_status()

            z = weather_response.json()
            z1 = air_response.json()

            # ---------------- WEATHER ----------------

            name.append(z["name"])
            coun.append(z["sys"]["country"])

            temp.append(
                f"{z['main']['temp'] - 273.15:.2f}"
            )

            tmin.append(
                f"{z['main']['temp_min'] - 273.15:.2f}"
            )

            tmax.append(
                f"{z['main']['temp_max'] - 273.15:.2f}"
            )

            hum.append(z["main"]["humidity"])
            pre.append(z["main"]["pressure"])

            vis.append(
                z.get("visibility", 0)
            )

            spe.append(
                z["wind"]["speed"]
            )

            clo.append(
                z["clouds"]["all"]
            )

            des.append(
                z["weather"][0]["description"].title()
            )

            # ---------------- AIR QUALITY ----------------

            aqi.append(
                z1["list"][0]["main"]["aqi"]
            )

            components = z1["list"][0]["components"]

            co.append(components["co"])
            no.append(components["no"])
            no2.append(components["no2"])
            o3.append(components["o3"])
            so2.append(components["so2"])
            pm2_5.append(components["pm2_5"])
            pm10.append(components["pm10"])
            nh3.append(components["nh3"])

        except Exception as e:

            st.warning(
                f"⚠️ Failed to fetch data for location {i + 1}: {e}"
            )

# ============================================================
# WEATHER DATAFRAME
# ============================================================

data = {
    "City": name,
    "Country": coun,
    "Temp (°C)": temp,
    "Min Temp (°C)": tmin,
    "Max Temp (°C)": tmax,
    "Pressure (hPa)": pre,
    "Description": des,
    "Clouds (%)": clo,
    "Wind Speed (m/s)": spe,
    "Visibility (m)": vis,
    "Humidity (%)": hum
}

# ============================================================
# AIR QUALITY DATAFRAME
# ============================================================

data1 = {
    "Air Quality Index": aqi,
    "Carbon Monoxide": co,
    "Nitric Oxide": no,
    "Nitrogen Dioxide": no2,
    "Ozone": o3,
    "Sulfur Dioxide": so2,
    "Particulate Matter ≤ 2.5 µm": pm2_5,
    "Particulate Matter ≤ 10 µm": pm10,
    "Ammonia": nh3
}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

# ============================================================
# FINAL DATAFRAME
# ============================================================

final_df = pd.concat(
    [df, df1],
    axis=1
)

final_df["Latitude"] = [float(x) for x in lat[:len(final_df)]]
final_df["Longitude"] = [float(x) for x in lon[:len(final_df)]]

# ============================================================
# DASHBOARD METRICS
# ============================================================

if not final_df.empty:

    avg_temp = pd.to_numeric(
        final_df["Temp (°C)"]
    ).mean()

    avg_humidity = final_df["Humidity (%)"].mean()

    avg_aqi = final_df["Air Quality Index"].mean()

    avg_pm25 = final_df[
        "Particulate Matter ≤ 2.5 µm"
    ].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">📍 DISTRICTS</div>
                <div class="metric-value">{len(final_df)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">🌡 AVG TEMPERATURE</div>
                <div class="metric-value">{avg_temp:.1f} °C</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">🌍 AVG AQI</div>
                <div class="metric-value">{avg_aqi:.1f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">💨 AVG PM2.5</div>
                <div class="metric-value">{avg_pm25:.1f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# FULL DATA TABLE
# ============================================================

st.markdown(
    '<div class="section-title">📊 Weather & Air Quality Data</div>',
    unsafe_allow_html=True
)

st.dataframe(
    final_df,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# AQI FUNCTION
# ============================================================

def get_aqi_color(aqi_value):

    if aqi_value == 1:
        return "green"

    elif aqi_value == 2:
        return "orange"

    elif aqi_value == 3:
        return "red"

    elif aqi_value == 4:
        return "darkred"

    else:
        return "purple"


def get_aqi_text(aqi_value):

    if aqi_value == 1:
        return "Good"

    elif aqi_value == 2:
        return "Fair"

    elif aqi_value == 3:
        return "Moderate"

    elif aqi_value == 4:
        return "Poor"

    else:
        return "Very Poor"

# ============================================================
# FOLIUM MAP
# ============================================================

st.markdown(
    '<div class="section-title">🗺️ District Weather & Air Quality Map</div>',
    unsafe_allow_html=True
)

m = folium.Map(
    location=[22.5, 72.5],
    zoom_start=7,
    tiles="CartoDB dark_matter"
)

# ============================================================
# MAP MARKERS
# ============================================================

for _, row in final_df.iterrows():

    aqi_value = int(row["Air Quality Index"])

    aqi_text = get_aqi_text(aqi_value)

    marker_color = get_aqi_color(aqi_value)

    hover_data = f"""
    <div style="
        width: 330px;
        padding: 5px;
        font-family: Arial;
        color: #111827;
    ">

        <div style="
            background: #111827;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 8px;
        ">
            <b style="font-size: 17px;">
                📍 {row['City']}
            </b>
            <br>
            <span style="font-size: 12px;">
                {row['Country']}
            </span>
        </div>

        <b>🌡 Temperature:</b> {row['Temp (°C)']} °C<br>
        <b>🌡 Min:</b> {row['Min Temp (°C)']} °C<br>
        <b>🌡 Max:</b> {row['Max Temp (°C)']} °C<br>
        <b>💧 Humidity:</b> {row['Humidity (%)']} %<br>
        <b>🌤 Weather:</b> {row['Description']}<br>
        <b>☁️ Clouds:</b> {row['Clouds (%)']} %<br>
        <b>💨 Wind:</b> {row['Wind Speed (m/s)']} m/s<br>
        <b>👁 Visibility:</b> {row['Visibility (m)']} m<br>
        <b>🔵 Pressure:</b> {row['Pressure (hPa)']} hPa

        <hr>

        <b>🌍 AQI:</b>
        <span style="font-weight:bold;">
            {aqi_value} - {aqi_text}
        </span>

        <br>

        <b>CO:</b> {row['Carbon Monoxide']} μg/m³<br>
        <b>NO:</b> {row['Nitric Oxide']} μg/m³<br>
        <b>NO₂:</b> {row['Nitrogen Dioxide']} μg/m³<br>
        <b>O₃:</b> {row['Ozone']} μg/m³<br>
        <b>SO₂:</b> {row['Sulfur Dioxide']} μg/m³<br>
        <b>PM2.5:</b>
        {row['Particulate Matter ≤ 2.5 µm']} μg/m³<br>

        <b>PM10:</b>
        {row['Particulate Matter ≤ 10 µm']} μg/m³<br>

        <b>NH₃:</b> {row['Ammonia']} μg/m³

    </div>
    """

    folium.Marker(

        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        tooltip=folium.Tooltip(
            hover_data,
            sticky=True
        ),

        icon=folium.Icon(
            color=marker_color,
            icon="info-sign"
        )

    ).add_to(m)

# ============================================================
# DISPLAY MAP
# ============================================================

st_folium(
    m,
    width=None,
    height=650
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div style="
    text-align:center;
    color:#64748b;
    padding:25px;
    margin-top:25px;
">
    🌍 Weather & Air Quality Monitoring Dashboard
    <br>
    Real-time data powered by OpenWeather
</div>
""", unsafe_allow_html=True)
