import streamlit as st
from datetime import datetime

st.title("📋 Registro de Ejercicios de Gimnasio")

# Ejemplo de campos de entrada
nombre = st.text_input("Introduce tu nombre")
fecha = st.date_input("Fecha del entrenamiento", format="DD/MM/YYYY")
ejercicio = st.text_input("Ejercicio")
repeticiones = st.number_input("Repeticiones", min_value=1, step=1)
peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5)

if st.button("Guardar"):
    st.success(f"{nombre}, guardado: {ejercicio}, {repeticiones} reps con {peso} kg el {fecha.strftime('%d/%m/%Y')}")




from datetime import datetime

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

registro={}

prueba={"22/10/2005" : {"Dominadas":[6,12,15],
                        "Peso muerto":[7, 10, 20],
                        "Remo al cuello":[7, 20, 23] }
}


#PROGRAMA
print("--BIENVENIDO A REGISTRO DE EJERCICIOS DE GIMNASIO")
nombre=input("Introduce tu nombre ").strip().lower()
print(f"Bienvenido {nombre.capitalize()} puedes: \n Registrar día\n Ver histórico de entrenamientos \n Ver ejercicios\n Escribe 'salir' en cualquier momento para cerrar el programa")
usuario=input("Elige una opción ").lower()

def salir(usuario):
    if usuario.lower()=="salir":
        return True
    return False

def registrar_ejercicio(registro,fecha, ejercicio,repeticiones,peso):
     if ejercicio not in registro[fecha]:
          registro[fecha][ejercicio]=[]
     registro[fecha][ejercicio].append((repeticiones,peso))
     
     

while True:
    try:
        #SALIR DEL PROGRAMA
        if usuario.lower()=="salir":  
                salir(usuario)
                break
        #VER EJERCICIOS
        if usuario.lower()=="ver ejercicios" or usuario.lower()=="ejercicios": 
            print(f"{'Grupo muscular':<15} | {'Ejercicio' :<30}")
            print("-"*50)
            for grupo, ejercicios in ejercicios_gimnasio.items():
                for i, ejercicio in enumerate(ejercicios):
                        if i == 0 :
                            print("-"*50)
                            print(f"{grupo:<15} | {ejercicio:<30}")
                            
                        else:
                
                            print(f"{'':<15} | {ejercicio:<30}")
            usuario=input("Elige una opción ").lower()
            
        #VER HISTORICO ENTRENAMIENTOS
        if usuario.lower()=="ver historico de entrenamientos" or usuario.lower()=="ver historico" or usuario.lower() =="ver entrenamientos":
             if registro =={}: 
                  print("Registra al menos un día para ver el histórico de entremientos")
                  usuario=input("Elige una opción ").lower()
                  if usuario.lower()=="salir":  
                    salir(usuario)
                    break
             else:
                  for fecha,ejercicios in registro.items():
                       print(f"Ejercicios del día {fecha}")
                       print("-"*50)
                       
                       for ejercicio, p in ejercicios.items():
                               print(f"{ejercicio:<15} |")       
                               for f, (serie,repeticion,peso) in enumerate(p):
                                       print(f"{" "*16}| Series :{serie}{" "*2}| Repeticiones: {repeticion:}{" "*2}| Peso: {peso} kg")
                                       
         #REGISTRAR DÍA              
        if usuario.lower() =="registrar dia" or usuario.lower() =="entrenar":
             fecha=input("Introduce una fecha en formato dd/mm/aaaa ").strip()
             if fecha.lower()=="salir":  
                salir(usuario)
                break
             try:
                  while True:
                       
                    if fecha not in registro:
                        fecha_valida=datetime.strptime(fecha,"%d/%m/%Y")
                        registro[fecha]={}
                    else:
                        print("Fecha válida y añadida al registro.")
                        
                        ejercicio=input("Escribe un ejercicio. Si no quieres continuar pon una 'n' ")
                        if ejercicio.lower() == "n" or ejercicio.lower()=="no":
                             salir(usuario)
                             break
                        
                        else:
                            try:                                                          
                                repeticiones=input("Repeticiones")
                                peso=input("peso")
                                registrar_ejercicio(registro,fecha,ejercicio, int(repeticiones), float(peso))
                                if ejercicio.lower()=="salir" or repeticiones.lower()=="salir" or peso.lower()=="salir": 
                                    salir(usuario)
                                    break
                            except:
                                 
                                raise ValueError (f"Repeticiones y peso han de ser numéricos")
                        
                             
                
             except ValueError:
                  print("Fecha inválida. Usa el formato dd/mm/aaaa")
             
                  

        else:
             usuario=input("Elige una opción válida").lower()
             
             
    except:
         ValueError
                            
