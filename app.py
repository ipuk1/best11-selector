import streamlit as st
import random

# --- Player Data ---
goalkeepers = [
    "Gianluigi Buffon", "Iker Casillas", "Manuel Neuer"
]

defenders = list(dict.fromkeys([
    "Alessandro Nesta", "Paolo Maldini", "Jaap Stam", "Lilian Thuram", "Javier Zanetti",
    "Fabio Cannavaro", "Thiago Silva", "Philipp Lahm", "Rio Ferdinand", "Cafu",
    "Roberto Carlos", "Carles Puyol", "Dani Alves", "Marcel Desailly", "Piqué",
    "Sergio Ramos", "Jaap Stam"
]))

midfielders = [
    "Zinedine Zidane", "Luis Figo", "Steven Gerrard", "Rui Costa", "Kaká", "Paul Scholes",
    "Claude Makélélé", "Andrea Pirlo", "Xavi", "Andres Iniesta", "Pavel Nedved",
    "Sergio Busquets", "Clarence Seedorf", "Edgar Davids", "David Silva",
    "Stefan Effenberg", "Luka Modrić"
]

forwards = [
    "Ronaldo Nazário", "Cristiano Ronaldo", "Lionel Messi", "Neymar", "Ronaldinho",
    "Luis Suárez", "Roberto Baggio", "Romário"
]

# --- Helper functions ---
def assign_ratings(players):
    return [{"name": p, "rating": random.randint(85, 99)} for p in players]

def select_best(players, count):
    return sorted(players, key=lambda x: x["rating"], reverse=True)[:count]

# --- Streamlit UI ---
st.title("🏆 Best 11 Football Player Selector")

st.markdown("Choose your **formation** (total of 10 outfield players):")
d = st.number_input("Defenders", min_value=1, max_value=5, value=4, step=1)
m = st.number_input("Midfielders", min_value=1, max_value=5, value=3, step=1)
f = st.number_input("Forwards", min_value=1, max_value=4, value=3, step=1)

if d + m + f != 10:
    st.warning("Total outfield players must equal 10.")
else:
    if st.button("Select Best 11"):
        gk = assign_ratings(goalkeepers)
        df = assign_ratings(defenders)
        mf = assign_ratings(midfielders)
        fw = assign_ratings(forwards)

        team = []
        team += select_best(gk, 1)
        team += select_best(df, d)
        team += select_best(mf, m)
        team += select_best(fw, f)

        st.subheader("🌟 Your Starting 11")
        for p in team:
            st.write(f"**{p['name']}** — Rating: {p['rating']}")
