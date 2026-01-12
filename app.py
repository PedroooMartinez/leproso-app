import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS (MANTENIENDO TU LOGIN PERFECTO)
st.markdown("""
    <style>
    .stApp {
        background-color: #002B5B;
        color: #ffffff;
    }
    
    /* LOGIN TITULOS */
    .main-login {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding-top: 50px;
    }
    .acceder-text { font-size: 42px; font-weight: 800; margin-bottom: 0px; }
    .caudillo-text { font-size: 20px; font-weight: 300; color: #a8dadc; margin-bottom: 40px; }

    /* INPUTS LOGIN (FONDO BLANCO, LETRA AZUL) */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 10px !important; }
    input { color: #002B5B !important; -webkit-text-fill-color: #002B5B !important; }

    /* ESTILO TARJETAS INTERIOR */
    .card-interior {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* BOTÓN ACCEDER (EL QUE TE GUSTABA) */
    .stButton>button {
        border-radius: 10px;
        font-weight: bold;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGACIÓN
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# --- PANTALLA DE LOGIN ---
if st.session_state["page"] == "login":
    st.markdown('<div class="main-login"><h1 class="acceder-text">Acceder</h1><p class="caudillo-text">Socio caudillo</p></div>', unsafe_allow_html=True)
    
    _, col_form, _ = st.columns([0.6, 2, 0.6])
    with col_form:
        email = st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed")
        password = st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        # Botón de Acceder tal como lo tenías
        if st.button("ACCEDER"):
            if email == "admin@csir.com" and password == "1913":
                st.session_state["page"] = "home"
                st.rerun()
            else:
                st.error("Datos incorrectos")

# --- PANTALLA DE INICIO (NUEVO DISEÑO INTERIOR) ---
elif st.session_state["page"] == "home":
    st.markdown("<h2 style='text-align: center;'>Panel de Control</h2>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card-interior"><h3>👤</h3><h4>Mi Perfil</h4></div>', unsafe_allow_html=True)
        if st.button("Gestionar Perfil", use_container_width=True):
            st.session_state["page"] = "perfil"
            st.rerun()
        
        st.write("") 

        st.markdown('<div class="card-interior"><h3>⭐</h3><h4>Mejora</h4></div>', unsafe_allow_html=True)
        if st.button("Subir de Nivel", use_container_width=True):
            st.info("Próximamente")

    with col2:
        st.markdown('<div class="card-interior"><h3>💰</h3><h4>Pagos</h4></div>', unsafe_allow_html=True)
        if st.button("Ver Facturas", use_container_width=True):
            st.info("Próximamente")

        st.write("")

        st.markdown('<div class="card-interior"><h3>🎟️</h3><h4>Entradas</h4></div>', unsafe_allow_html=True)
        if st.button("Comprar Tickets", use_container_width=True):
            st.info("Próximamente")

    with st.sidebar:
        st.image("csir.png", width=80)
        if st.button("Cerrar Sesión"):
            st.session_state["page"] = "login"
            st.rerun()
