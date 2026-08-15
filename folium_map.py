"""
Real interactive Folium map for the SpaceX capstone.
Run this in your own notebook/environment (needs internet for map tiles):
    pip install folium
    python folium_map.py
Then open launch_sites_map.html in a browser and screenshot it for your slide.
"""
import folium
from folium.plugins import MarkerCluster

sites = {
    "CCAFS SLC 40": (28.5623, -80.5774, "#14b8a6"),
    "KSC LC 39A":   (28.6080, -80.6041, "#f59e0b"),
    "VAFB SLC 4E":  (34.6321, -120.6108, "#6366f1"),
}

m = folium.Map(location=[29, -95], zoom_start=4, tiles="OpenStreetMap")
cluster = MarkerCluster().add_to(m)

for name, (lat, lon, color) in sites.items():
    folium.Marker(
        [lat, lon],
        popup=f"<b>{name}</b>",
        icon=folium.Icon(color="blue", icon="rocket", prefix="fa"),
    ).add_to(cluster)
    folium.Circle(
        [lat, lon], radius=1000, color=color, fill=True, fill_opacity=0.3
    ).add_to(m)

# Example proximity line: CCAFS SLC 40 to the nearest coastline point
folium.PolyLine(
    locations=[[28.5623, -80.5774], [28.56, -80.56]],
    color="red", weight=2, dash_array="5",
    tooltip="Distance to coastline"
).add_to(m)

m.save("launch_sites_map.html")
print("Saved launch_sites_map.html — open it and screenshot for your slide.")
