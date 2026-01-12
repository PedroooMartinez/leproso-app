import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS PARA MODO OSCURO Y CENTRADO DE IMAGEN
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    /* ESTO CENTRA TODAS LAS IMÁGENES AUTOMÁTICAMENTE */
    div[data-testid="stImage"] > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    /* Estilo de inputs */
    .stTextInput>div>div>input {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    /* Botón blanco */
    .stButton>button {
        background-color: #ffffff;
        color: #0d1117;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        height: 45px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE SESIÓN
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# --- PANTALLA DE INICIO ---
if not st.session_state["logueado"]:
    
    st.write("") # Espacio arriba
    st.write("")
    
    # Ponemos la imagen directamente (El CSS de arriba la va a centrar)
    st.image("csir.png", width=120)
    
    # Título centrado usando HTML simple
    st.markdown("<h2 style='text-align: center;'>Socio CSIR</h2>", unsafe_allow_html=True)
    st.write("")

    # Formulario (usamos columnas solo para achicar el ancho, no para el logo)
    _, col_form, _ = st.columns([0.5, 2, 0.5])
    
    with col_form:
        email = st.text_input("Usuario", placeholder="correo@ejemplo.com")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        
        if st.button("Iniciar Sesión"):
            if email == "azul@gmail.com" and password == "1913":
                st.session_state["logueado"] = True
                st.rerun()
            else:
                st.error("Credenciales no válidas")

# --- PANTALLA PRINCIPAL ---
else:
    with st.sidebar:
        st.image("csir.png", width=80)
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state["logueado"] = False
            st.rerun()
    
    st.markdown("## Bienvenido al Portal")
    st.write("Gestioná tus entradas y beneficios de la Lepra.")
