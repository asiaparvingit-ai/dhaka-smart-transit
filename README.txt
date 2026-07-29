========================================================================
   AI-DRIVEN DHAKA TRANSIT VISUAL ANALYTICS & SIGNAL OPTIMIZATION
========================================================================
Project Name : Smart Dhaka Transit Engine
Department   : Computer Science & Engineering (Thesis Prototype)
Framework    : Python + Streamlit + SQLite3 + Plotly + Folium
========================================================================

1. OVERVIEW
------------------------------------------------------------------------
This prototype provides real-time geospatial tracking, dynamic signal 
optimization, and bus fleet demand-supply management for key traffic 
corridors in Dhaka City.

Key Features:
- Time-Aware Real-Time Traffic Congestion Sync (Peak vs Off-Peak hours)
- Interactive Geospatial Map (Intersection status: Green/Yellow/Red/Purple)
- Traffic Police Emergency Override & Intelligent Rerouting Diversions
- Predictive AI Congestion Forecasting (1-Hour Ahead)
- Bus Fleet Shortage & Active Fleet Matrix

------------------------------------------------------------------------
2. PROJECT FILE STRUCTURE
------------------------------------------------------------------------
dhaka-transit-project/
│
├── app.py                     # Main Streamlit Dashboard Application
├── dhaka_transit.db           # SQLite Database with Telemetry Logs
├── requirements.txt           # Python Dependency Package List
└── README.txt                 # Project Setup & Execution Guide

------------------------------------------------------------------------
3. PREREQUISITES & INSTALLATION
------------------------------------------------------------------------
Make sure Python 3.8+ is installed on your local machine.

Step 1: Clone or Download the project repository.
Step 2: Open Terminal / Command Prompt inside the project folder.
Step 3: Install all required Python packages using pip:

    pip install -r requirements.txt

------------------------------------------------------------------------
4. HOW TO RUN THE APPLICATION
------------------------------------------------------------------------
To launch the interactive dashboard locally, execute the following command
in your terminal:

    streamlit run app.py

Once executed, the dashboard will automatically open in your default browser 
at: http://localhost:8501

------------------------------------------------------------------------
5. DASHBOARD CONTROLS & DEMO GUIDE FOR EVALUATION
------------------------------------------------------------------------
[A] Real-Time Live Sync Mode:
    - Automatically syncs with current system time.
    - Demonstrates off-peak/night traffic conditions during late hours.

[B] Custom Date & Hour Selection:
    - Use the sidebar slider to simulate morning peak (08:00 - 10:00 AM) 
      or evening peak (17:00 - 19:00 PM) to observe high congestion.

[C] Live Traffic Police Override:
    - Select an intersection node (e.g., Farmgate).
    - Change condition to 'Road Blocked' or 'Protest / Blockade'.
    - Click 'Broadcast Traffic Advisory' to trigger dynamic map diversion 
      routes and emergency alert notices.

========================================================================
Developed for CSE Thesis Evaluation.
========================================================================