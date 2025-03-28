import streamlit as st
from app.sequences import get_spin_echo_sequence
from app.simulator import signal_intensity
from app.visualizer import plot_sequence

st.title("🧲 MRI Pulse Sequence Optimizer")

TE = st.slider("Echo Time (TE, ms)", 10, 200, 90)
TR = st.slider("Repetition Time (TR, ms)", 100, 2000, 1000)
T1 = st.slider("T1 (ms)", 100, 3000, 1000)
T2 = st.slider("T2 (ms)", 20, 500, 80)

sequence = get_spin_echo_sequence(TE, TR)
plot_sequence(sequence)

signal = signal_intensity(T1, T2, TR, TE)
st.write(f"📈 Expected Signal Intensity: **{signal:.3f}**")
