import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

DB_NAME = "dhaka_transit.db"
CSV_NAME = "dhaka_bus_gps_1month.csv"

ROUTES_DATA = {
    "Gulistan - Gazipur Corridor": [
        {"stop": "Gulistan", "lat": 23.7250, "lon": 90.4100, "base_req": 25},
        {"stop": "Shahbagh", "lat": 23.7386, "lon": 90.3958, "base_req": 30},
        {"stop": "Farmgate", "lat": 23.7561, "lon": 90.3914, "base_req": 40},
        {"stop": "Mohakhali", "lat": 23.7778, "lon": 90.4006, "base_req": 35},
        {"stop": "Airport Station", "lat": 23.8517, "lon": 90.4074, "base_req": 30},
        {"stop": "Uttara House Building", "lat": 23.8737, "lon": 90.3909, "base_req": 25},
        {"stop": "Gazipur Chowrasta", "lat": 23.9999, "lon": 90.3783, "base_req": 20}
    ],
    "Motijheel - Savar Corridor": [
        {"stop": "Motijheel C/A", "lat": 23.7328, "lon": 90.4172, "base_req": 45},
        {"stop": "Shahbagh", "lat": 23.7386, "lon": 90.3958, "base_req": 30},
        {"stop": "Farmgate", "lat": 23.7561, "lon": 90.3914, "base_req": 40},
        {"stop": "Shyamoli", "lat": 23.7719, "lon": 90.3631, "base_req": 25},
        {"stop": "Gabtoli", "lat": 23.7794, "lon": 90.3524, "base_req": 30},
        {"stop": "Savar Bus Stand", "lat": 23.8479, "lon": 90.2577, "base_req": 20}
    ],
    "Jatrabari - Mirpur 10 Corridor": [
        {"stop": "Jatrabari", "lat": 23.7104, "lon": 90.4349, "base_req": 30},
        {"stop": "Sayedabad", "lat": 23.7186, "lon": 90.4260, "base_req": 25},
        {"stop": "Motijheel C/A", "lat": 23.7328, "lon": 90.4172, "base_req": 40},
        {"stop": "Shahbagh", "lat": 23.7386, "lon": 90.3958, "base_req": 30},
        {"stop": "Farmgate", "lat": 23.7561, "lon": 90.3914, "base_req": 35},
        {"stop": "Agargaon", "lat": 23.7770, "lon": 90.3755, "base_req": 25},
        {"stop": "Mirpur 10", "lat": 23.8069, "lon": 90.3686, "base_req": 35}
    ]
}

def generate_two_months_dataset():
    print("⏳ Generating July & August 2026 Dhaka Transit Telemetry Dataset...")
    records = []
    
    start_date = datetime(2026, 7, 1, 6, 0, 0)
    end_date = datetime(2026, 8, 31, 22, 0, 0)
    
    current_time = start_date
    np.random.seed(42)
    
    while current_time <= end_date:
        hour = current_time.hour
        if 6 <= hour <= 22:
            is_morning_peak = (8 <= hour <= 10)
            is_evening_peak = (17 <= hour <= 19)
            is_peak = is_morning_peak or is_evening_peak
            
            for route_name, stops in ROUTES_DATA.items():
                for idx, node in enumerate(stops):
                    base_req = node["base_req"]
                    
                    if is_peak:
                        required_buses = int(base_req * np.random.uniform(1.2, 1.4))
                        active_buses = int(required_buses - np.random.randint(2, 7))
                        congestion = round(float(np.random.uniform(78.0, 98.0)), 1)
                        load_pct = np.random.randint(85, 100)
                        traffic_status = "Heavy Jam"
                    else:
                        required_buses = int(base_req * np.random.uniform(0.8, 1.0))
                        active_buses = required_buses + np.random.randint(0, 3)
                        congestion = round(float(np.random.uniform(20.0, 48.0)), 1)
                        load_pct = np.random.randint(30, 65)
                        traffic_status = "Free Flow"
                        
                    shortage = max(0, required_buses - active_buses)
                    
                    records.append({
                        "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "route_name": route_name,
                        "stop_name": node["stop"],
                        "latitude": node["lat"],
                        "longitude": node["lon"],
                        "active_buses": active_buses,
                        "required_buses": required_buses,
                        "bus_shortage": shortage,
                        "congestion_pct": congestion,
                        "passenger_load_pct": load_pct,
                        "traffic_status": traffic_status
                    })
        
        current_time += timedelta(minutes=5)

    df = pd.DataFrame(records)
    df.to_csv(CSV_NAME, index=False)
    
    conn = sqlite3.connect(DB_NAME, timeout=30)
    df.to_sql("telemetry", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    print("✅ SQLite Database Generated Successfully!")

if __name__ == "__main__":
    generate_two_months_dataset()
