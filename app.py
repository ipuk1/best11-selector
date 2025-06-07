import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

# Player pools
goalkeepers = ["Gianluigi Buffon", "Iker Casillas", "Manuel Neuer"]

defenders = [
    "Alessandro Nesta", "Paolo Maldini", "Jaap Stam", "Lilian Thuram", "Javier Zanetti",
    "Fabio Cannavaro", "Thiago Silva", "Philipp Lahm", "Rio Ferdinand", "Cafu",
    "Roberto Carlos", "Carles Puyol", "Dani Alves", "Marcel Desailly", "Piqué",
    "Sergio Ramos"
]

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

st.title("⚽ Build Your Best XI with Visual Pitch")

formation = st.selectbox("Choose formation", ["4-3-3", "4-4-2", "3-5-2", "3-4-3", "4-5-1"])
def_count, mid_count, fwd_count = map(int, formation.split("-"))

goalkeeper = st.selectbox("Goalkeeper", goalkeepers)
defense = st.multiselect(f"Select {def_count} Defenders", defenders, max_selections=def_count)
midfield = st.multiselect(f"Select {mid_count} Midfielders", midfielders, max_selections=mid_count)
forward = st.multiselect(f"Select {fwd_count} Forwards", forwards, max_selections=fwd_count)

def draw_pitch(gk, def_players, mid_players, fwd_players):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_facecolor("green")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    ax.axis("off")

    def place_players(players, y):
        spacing = 100 / (len(players) + 1)
        for i, name in enumerate(players):
            x = spacing * (i + 1)
            ax.text(x, y, name, ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Draw players
    place_players([gk], 10)
    place_players(def_players, 30)
    place_players(mid_players, 55)
    place_players(fwd_players, 80)

    return fig

if (
    goalkeeper
    and len(defense) == def_count
    and len(midfield) == mid_count
    and len(forward) == fwd_count
):
    st.subheader("🟩 Your Team Formation")

    fig = draw_pitch(goalkeeper, defense, midfield, forward)
    st.pyplot(fig)

    # Save to BytesIO buffer
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    st.download_button(
        label="📥 Download Pitch Image",
        data=buf,
        file_name="best_11_formation.png",
        mime="image/png"
    )

else:
    st.info("Please select the full lineup to display the pitch.")
