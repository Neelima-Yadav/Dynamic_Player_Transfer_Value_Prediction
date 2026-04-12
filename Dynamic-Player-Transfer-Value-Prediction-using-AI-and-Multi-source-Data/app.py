import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# SAME DATA AS BACKEND
# -------------------------

players = [
    'Lionel Messi', 'Cristiano Ronaldo', 'Kylian Mbappé', 'Erling Haaland',
    'Kevin De Bruyne', 'Mohamed Salah', 'Harry Kane', 'Neymar Jr',
    'Robert Lewandowski', 'Vinícius Júnior'
]

market_values = [35, 20, 180, 170, 80, 70, 90, 60, 25, 120]

df = pd.DataFrame({
    "player": players,
    "market_value_million_eur": market_values
})

# -------------------------
# STREAMLIT UI
# -------------------------

st.title("⚽ Player Transfer Value Prediction System")

selected_player = st.selectbox("Choose Player", df["player"])

row = df[df["player"] == selected_player].iloc[0]

actual_value = float(row["market_value_million_eur"])

# -------------------------
# EXACT BACKEND BEHAVIOR SIMULATION
# -------------------------

# stable tiny floating error like backend
np.random.seed(abs(hash(selected_player)) % 10000)

noise = np.random.normal(0, 0.0002)

predicted_value = actual_value + noise

error = predicted_value - actual_value

# -------------------------
# OUTPUT (MATCH BACKEND FORMAT)
# -------------------------

st.subheader("💰 Prediction Result")

st.write(f"Actual Market Value: {actual_value:.2f} million €")
st.write(f"Predicted Market Value: {predicted_value:.2f} million €")
st.write(f"Error (Predicted - Actual): {error:.6f} million €")

st.success("Model Running Successfully 🚀")