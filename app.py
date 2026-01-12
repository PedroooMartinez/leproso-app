import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Socio CSIR", page_icon="💙", layout="centered")

# 2. DISEÑO AVANZADO (CSS)
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp {
        background: linear-gradient(180deg, #002B5B 0%, #001a38 100%);
        color: white;
    }
    /* Estilo de las cajas de entrada */
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
        color: #002B5B;
        border-radius: 8px;
    }
    /* Botón principal estilo 'Leproso' */
    .stButton>button {
        background-color: #0056b3;
        color: white;
        border: 2px solid #ffffff;
        border-radius: 20px;
        font-weight: bold;
        transition: 0.3s;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        color: #002B5B;
    }
    /* Tarjeta informativa */
    .partido-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ffffff;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA CON LOGO
col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
with col_logo2:
    # URL de un escudo de la Lepra (podes cambiarla si tenes otra)
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2e/Escudo_de_Independiente_Rivadavia.png", width=150)

st.markdown("<h1 style='text-align: center;'>OFICINA VIRTUAL</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #a8dadc;'>Club Sportivo Independiente Rivadavia</h3>", unsafe_allow_html=True)

st.write("---")

# 4. LÓGICA DE NAVEGACIÓN
if "sesion" not in st.session_state:
    st.session_state["sesion"] = False

if not st.session_state["sesion"]:
    # FORMULARIO DE ACCESO
    st.markdown("### 🔐 Ingreso Socios")
    email = st.text_input("Correo electrónico", placeholder="ejemplo@socio.com")
    password = st.text_input("Contraseña", type="password", placeholder="****")
    
    st.write("") # Espacio
    if st.button("ACCEDER AL PORTAL"):
        if email == "azul@gmail.com" and password == "1913":
            st.session_state["sesion"] = True
            st.rerun()
        else:
            st.error("❌ Los datos no coinciden. Verificá tu número de socio.")

else:
    # MENÚ PARA SOCIOS LOGUEADOS
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/2e/Escudo_de_Independiente_Rivadavia.png", width=80)
    st.sidebar.title("Mi Perfil")
    st.sidebar.write("Socio: **Azul de Corazón**")
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["sesion"] = False
        st.rerun()

    # VENTA DE ENTRADAS
    st.markdown("## 🎟️ Compra de Entradas")
    
    # Tarjeta del próximo partido
    st.markdown("""
        <div class="partido-card">
            <h4>⚽ PRÓXIMO ENCUENTRO</h4>
            <p><b>Independiente Rivadavia vs River Plate</b><br>
            Estadio: Bautista Gargantini<br>
            Fecha: Domingo 21:00 hs</p>
        </div>
    """, unsafe_allow_html=True)

    ubicacion = st.selectbox("Seleccioná tu ubicación en el estadio:", 
                            ["Popular Salvador Iúdica", "Platea Este", "Platea Oeste (Techada)"])
    
    precios = {"Popular Salvador Iúdica": 15000, "Platea Este": 20000, "Platea Oeste (Techada)": 25000}
    monto = precios[ubicacion]

    st.markdown(f"### Importe: **${monto}**")
    
    if st.button("ADQUIRIR ENTRADA"):
        st.success(f"¡Reserva confirmada en {ubicacion}!")
        st.balloons()
