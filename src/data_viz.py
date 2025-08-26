import streamlit as st
import altair as alt
import duckdb
import pandas as pd


conn = duckdb.connect('lab.db')

total_population = conn.execute("SELECT * FROM marts.total_population").fetchdf()
dominant_faction = conn.execute("SELECT * FROM marts.dominant_faction").fetchdf()
faction_distribution = conn.execute("SELECT * FROM marts.faction_distribution").fetchdf()
top5_regions = conn.execute("SELECT * FROM marts.top5_most_populous_regions").fetchdf()

conn.close()

st.title("Ondoriya Data Visualizations")


st.metric("Total Population", int(total_population['total_population'][0]))


st.metric("Dominant Faction", dominant_faction['dominant_faction'][0])


st.subheader("Faction Distribution")
chart = alt.Chart(faction_distribution).mark_bar().encode(
    x='faction',
    y='percent',
    color=alt.Color('faction', legend=None)
)
st.altair_chart(chart, use_container_width=True)

# ...existing code...

# Top 5 Most Populous Regions - Visual Bar Chart
st.subheader("Top 5 Most Populous Regions")
top5_chart = alt.Chart(top5_regions).mark_bar().encode(
    x=alt.X('full_name', title='Region'),
    y=alt.Y('population', title='Population'),
    color=alt.Color('population', scale=alt.Scale(scheme='viridis'), title='Population')  # Gradient color
).properties(
    width=600,
    height=400
)
st.altair_chart(top5_chart, use_container_width=True)


