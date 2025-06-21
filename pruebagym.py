import streamlit as st
from datetime import datetime

# Diccionario de ejercicios por grupo muscular
ejercicios_gimnasio = {
    "Piernas": [
        "Sentadillas",
        "Prensa de piernas",
        "Zancadas con mancuernas",
        "Peso muerto rumano",
        "Elevación de talones (gemelos)"
    ],
    "Pectoral": [
        "Press banca",
        "Press inclinado con mancuernas",
        "Fondos en paralelas",
        "Aperturas con mancuernas",
        "Press en máquina"
    ],
    "Brazos": [
        "Curl bíceps con barra",
        "Curl alterno con mancuernas",
        "Extensiones de tríceps en polea",
        "Press francés",
        "Curl martillo"
    ],
    "Hombros": [
        "Press militar",
        "Elevaciones laterales",
        "Elevaciones frontales",
        "Pájaros (posterior)",
        "Remo al cuello"
    ],
    "Espalda": [
        "Dominadas",
        "Peso muerto",
        "Remo con barra",
        "Jalón al pecho",
        "Remo en máquina"
    ]
}

st.title("📋 Registro de Ejercicios de Gimnasio")

# Estado global del registro
if "registro" not in st.session_state:
    st.session_state.registro = {}

# Formulario de entrada
with st.form("formulario_entrenamiento"):
    nombre = st.text_input("Introduce tu nombre")
    fecha = st.date_input("Fecha del entrenamiento")

    grupo = st.selectbox("Grupo muscular", list(ejercicios_gimnasio.keys()))
    ejercicio = st.selectbox("Ejercicio", ejercicios_gimnasio[grupo])

    repeticiones = st.number_input("Repeticiones", min_value=1, step=1)
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5)

    enviado = st.form_submit_button("Guardar ejercicio")

    if enviado:
        fecha_str = fecha.strftime("%d/%m/%Y")
        if fecha_str not in st.session_state.registro:
            st.session_state.registro[fecha_str] = {}
        if ejercicio not in st.session_state.registro[fecha_str]:
            st.session_state.registro[fecha_str][ejercicio] = []

        st.session_state.registro[fecha_str][ejercicio].append((repeticiones, peso))
        st.success(f"✅ {nombre}, guardado: {ejercicio} - {repeticiones} reps con {peso} kg el {fecha_str}")

# Mostrar ejercicios guardados
st.markdown("---")
st.subheader("📊 Histórico de entrenamientos")

if not st.session_state.registro:
    st.info("Aún no has registrado ejercicios.")
else:
    for dia, ejercicios in st.session_state.registro.items():
        st.markdown(f"### 📅 {dia}")
        for nombre_ejercicio, series in ejercicios.items():
            st.write(f"**{nombre_ejercicio}**")
            for i, (reps, kg) in enumerate(series):
                st.write(f" - Serie {i+1}: {reps} reps con {kg} kg")
