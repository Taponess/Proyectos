import streamlit as st
from datetime import datetime

st.title("📋 Registro de Ejercicios de Gimnasio")

registro = {}

nombre = st.text_input("Tu nombre")
fecha = st.date_input("Fecha del entrenamiento")
ejercicio = st.text_input("Ejercicio")
repeticiones = st.number_input("Repeticiones", min_value=1, step=1)
peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5)

if st.button("Guardar"):
    fecha_str = fecha.strftime("%d/%m/%Y")
    if fecha_str not in registro:
        registro[fecha_str] = {}
    if ejercicio not in registro[fecha_str]:
        registro[fecha_str][ejercicio] = []
    registro[fecha_str][ejercicio].append((repeticiones, peso))
    st.success(f"{nombre}, ejercicio guardado: {ejercicio} – {repeticiones} reps con {peso} kg el {fecha_str}")

# Mostrar historial
if st.checkbox("Ver historial"):
    for dia, ejercicios in registro.items():
        st.markdown(f"### 📅 {dia}")
        for nombre_ejercicio, series in ejercicios.items():
            st.write(f"**{nombre_ejercicio}**")
            for i, (reps, kg) in enumerate(series):
                st.write(f" - Serie {i+1}: {reps} reps con {kg} kg")
