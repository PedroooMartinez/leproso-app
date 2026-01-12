import streamlit as st

# 1. CONFIGURACIÓN DE PESTAÑA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. DISEÑO PROFESIONAL (CSS CORREGIDO)
st.markdown("""
    <style>
    /* Color Azul Independiente Rivadavia */
    .stApp {
        background-color: #002B5B;
        color: #ffffff;
    }
    
    /* Centrado de todo el contenido de login */
    .main-login {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding-top: 50px;
    }

    .acceder-text {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .caudillo-text {
        font-size: 20px;
        font-weight: 300;
        color: #a8dadc;
        margin-bottom: 40px;
    }

    /* --- ARREGLO DE VISIBILIDAD DE TEXTO --- */
    /* Fondo de los cuadros de texto */
    div[data-baseweb="input"] {
        background-color: #ffffff !important; 
        border-radius: 10px !important;
    }
    
    /* Color del texto que escribe el usuario (NEGRO para que se vea) */
    input {
        color: #002B5B !important; 
        -webkit-text-fill-color: #002B5B !important;
    }

    /* Color del texto de ayuda (Placeholder) */
    input::placeholder {
        color: #666666 !important;
    }

    /* Botón Acceder */
    .stButton>button {
        background-color: #ffffff;
        color: #002B5B;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        height: 50px;
        width: 100%;
        font-size: 18px;
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }

    /* Tarjetas del Menú Principal */
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE NAVEGACIÓN
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# --- PANTALLA DE LOGIN ---
if not st.session_state["logueado"]:
    
    st.markdown("""
        <div class="main-login">
            <h1 class="acceder-text">Acceder</h1>
            <p class="caudillo-text">Socio caudillo</p>
        </div>
    """, unsafe_allow_html=True)

    _, col_form, _ = st.columns([0.6, 2, 0.6])
    
    with col_form:
        # Los labels están ocultos pero existen para Streamlit
        email = st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed")
        password = st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        if st.button("ACCEDER"):
            if email == "admin@csir.com" and password == "1913":
                st.session_state["logueado"] = True
                st.rerun()
            else:
                st.error("Datos incorrectos")

# --- PANTALLA DE INICIO (DENTRO) ---
else:
    st.markdown("<h2 style='text-align: center;'>Panel de Control</h2>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><h3>👤 Perfil</h3></div>', unsafe_allow_html=True)
        if st.button("Ver Perfil", key="btn1"):
            pass
            
        st.markdown('<div class="card"><h3>⭐ Mejora de socio</h3></div>', unsafe_allow_html=True)
        if st.button("Mejorar Plan", key="btn2"):
            pass

    with col2:
        st.markdown('<div class="card"><h3>💰 Pagos</h3></div>', unsafe_allow_html=True)
        if st.button("Gestionar Pagos", key="btn3"):
            pass
            
        st.markdown('<div class="card"><h3>🎟️ Comprar entradas</h3></div>', unsafe_allow_html=True)
        if st.button("Ver Entradas", key="btn4"):
            pass

    with st.sidebar:
        st.image("csir.png", width=80)
        if st.button("Cerrar Sesión"):
            st.session_state["logueado"] = False
            st.rerun()
