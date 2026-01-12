import streamlit as st

# 1. CONFIGURACIÓN DE PESTAÑA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. DISEÑO PROFESIONAL (CSS PERSONALIZADO)
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

    /* Estilo de los textos */
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

    /* Estilo de los inputs */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    input {
        color: white !important;
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
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }

    /* Tarjetas del Menú Principal (Interior) */
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: 0.3s;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
    .card:hover {
        background-color: rgba(255, 255, 255, 0.15);
        transform: translateY(-5px);
    }

    /* Ocultar elementos de Streamlit */
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
    
    # Contenedor del encabezado centrado
    st.markdown("""
        <div class="main-login">
            <h1 class="acceder-text">Acceder</h1>
            <p class="caudillo-text">Socio caudillo</p>
        </div>
    """, unsafe_allow_html=True)

    # Formulario
    _, col_form, _ = st.columns([0.6, 2, 0.6])
    
    with col_form:
        email = st.text_input("Correo electrónico", placeholder="usuario@mail.com", label_visibility="collapsed")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        if st.button("ACCEDER"):
            # Clave provisoria
            if email == "admin@csir.com" and password == "1913":
                st.session_state["logueado"] = True
                st.rerun()
            else:
                st.error("Datos incorrectos")

# --- PANTALLA DE INICIO (DENTRO) ---
else:
    # Encabezado interior
    st.markdown("<h2 style='text-align: center;'>Panel de Control</h2>", unsafe_allow_html=True)
    st.write("---")

    # Malla de Rectángulos (Tarjetas)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card"><h3>👤 Perfil</h3></div>', unsafe_allow_html=True)
        if st.button("Ver Perfil"):
            st.info("Próximamente")
            
        st.write("") # Espacio
        
        st.markdown('<div class="card"><h3>⭐ Mejora de socio</h3></div>', unsafe_allow_html=True)
        if st.button("Mejorar Plan"):
            st.info("Próximamente")

    with col2:
        st.markdown('<div class="card"><h3>💰 Pagos</h3></div>', unsafe_allow_html=True)
        if st.button("Gestionar Pagos"):
            st.info("Próximamente")
            
        st.write("") # Espacio
        
        st.markdown('<div class="card"><h3>🎟️ Comprar entradas</h3></div>', unsafe_allow_html=True)
        if st.button("Ver Entradas"):
            st.info("Próximamente")

    # Botón Salir en el Sidebar
    with st.sidebar:
        st.image("csir.png", width=80)
        st.write("Socio: **Caudillo del Parque**")
        if st.button("Cerrar Sesión"):
            st.session_state["logueado"] = False
            st.rerun()
