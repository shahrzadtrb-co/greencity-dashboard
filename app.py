import streamlit as st
from data.fetch_data import get_air_quality

st.title("🌿 GreenCity Dashboard - Germany")

city = st.selectbox("Select a city", ["Berlin", "Munich", "Frankfurt", "Stuttgart", "Hamburg"])
data = get_air_quality(city)

st.subheader(f"Air Quality Data for {city}")

if "results" in data:
    for measurement in data["results"]:
        st.write(f"Location: {measurement['location']}")
        for m in measurement["measurements"]:
            st.write(f"{m['parameter']}: {m['value']} {m['unit']} (last updated {m['lastUpdated']})")
else:
    st.error("No data available. Try a different city.")
