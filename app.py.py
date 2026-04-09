import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Familien-Budget Dashboard")

# Beispiel-Daten
df = pd.DataFrame({
    "Name": ["Mama", "Papa", "Kind1"],
    "Budget": [1000, 1200, 500],
    "Lebensmittel": [200, 250, 100],
    "Miete": [400, 400, 0],
    "Freizeit": [100, 150, 50],
    "Versicherungen": [50, 70, 0]
})

df["Gesamtausgaben"] = df[["Lebensmittel", "Miete", "Freizeit", "Versicherungen"]].sum(axis=1)
df["Abweichung"] = df["Budget"] - df["Gesamtausgaben"]

st.dataframe(df)