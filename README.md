# 🌍 Weather & Air Quality Dashboard

> 📊 A real-time **Weather, AQI & Air Pollution Monitoring Dashboard** built with Python and Streamlit.

## 🚀 Project Overview

This interactive dashboard fetches live weather and air-quality information for multiple locations and presents the results through a clean dark-themed interface, summary metrics, a detailed data table, and an interactive Folium map.

The project combines **OpenWeather API**, **Pandas**, **Streamlit**, and **Folium** to turn live environmental data into an easy-to-understand monitoring dashboard.

## ✨ Features

- 🌡️ Real-time temperature monitoring
- 💧 Humidity, pressure, wind and visibility information
- ☁️ Cloud coverage and weather description
- 🌍 Air Quality Index (AQI) monitoring
- 💨 PM2.5 and PM10 measurements
- 🧪 CO, NO, NO₂, O₃, SO₂ and NH₃ pollution data
- 📊 Interactive weather & air-quality data table
- 🗺️ Interactive district/location map with AQI-based markers
- 📈 Dashboard summary metrics
- 🎨 Professional dark UI with responsive metric cards
- ⚡ Live data retrieval using OpenWeather APIs

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Interactive web dashboard |
| 🐼 Pandas | Data processing and DataFrames |
| 🌐 Requests | API requests |
| 🗺️ Folium | Interactive maps |
| 🔗 Streamlit-Folium | Folium integration with Streamlit |
| ☁️ OpenWeather API | Weather & air-quality data |

## 📁 Project Structure

```text
Weather-Air-Quality-Dashboard/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Pareshprajapati-777/Weather-Air-Quality-Dashboard.git
cd Weather-Air-Quality-Dashboard
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure the OpenWeather API key 🔑

Create an API key from OpenWeather and configure it securely. Do **not** publish a real API key in the source code or commit it to GitHub.

For local development, the application can be configured to read the key from an environment variable or Streamlit secrets.

### 4️⃣ Run the dashboard ▶️

```bash
python -m streamlit run app.py
```

## 📊 Dashboard Includes

### 🌡️ Weather Monitoring

The dashboard displays:

- Current temperature
- Minimum temperature
- Maximum temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Visibility
- Cloud coverage
- Weather condition

### 🌍 Air Quality Monitoring

The dashboard monitors:

- AQI
- Carbon Monoxide (CO)
- Nitric Oxide (NO)
- Nitrogen Dioxide (NO₂)
- Ozone (O₃)
- Sulfur Dioxide (SO₂)
- PM2.5
- PM10
- Ammonia (NH₃)

### 🗺️ Interactive Map

Each location is displayed on an interactive dark-themed map. Marker colors represent the AQI category, making it easier to identify air-quality conditions geographically.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- 🔌 REST API integration
- 📡 Real-time data collection
- 🧹 Data processing with Pandas
- 📊 Dashboard development with Streamlit
- 🗺️ Geospatial visualization
- 🎨 Custom Streamlit CSS
- 🐍 Python application development
- 🌐 Environmental data monitoring

## 🔐 Security Note

**Never commit a real OpenWeather API key to a public GitHub repository.** Use environment variables or Streamlit secrets for credentials.

## 👨‍💻 Author

**Paresh Prajapati**

- 🐙 GitHub: [Pareshprajapati-777](https://github.com/Pareshprajapati-777)
- 💼 LinkedIn: [Paresh Prajapati](https://www.linkedin.com/in/pareshprajapati-co/)

## ⭐ Support

If this project is useful or helpful for learning, consider giving the repository a ⭐ on GitHub!

---

### 🌍 Built with Python • Streamlit • Pandas • Folium • OpenWeather API
