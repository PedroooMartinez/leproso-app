import streamlit as st

# 1. CONFIGURACIÓN DE PESTAÑA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. DISEÑO PREMIUM (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #002B5B;
        color: #ffffff;
    }
    
    /* LOGIN */
    .main-login {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding-top: 50px;
    }
    .acceder-text { font-size: 42px; font-weight: 800; margin-bottom: 0px; }
    .caudillo-text { font-size: 20px; font-weight: 300; color: #a8dadc; margin-bottom: 40px; }

    /* INPUTS LOGIN */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 10px !important; }
    input { color: #002B5B !important; -webkit-text-fill-color: #002B5B !important; }

    /* BOTONES QUE PARECEN RECTÁNGULOS (DENTRO) */
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        height: 120px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
        margin-bottom: 10px !important;
    }
    .stButton>button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid #ffffff !important;
        transform: translateY(-5px);
    }
    
    /* Ajuste para el botón de ACCEDER que sea blanco */
    .login-btn>div>div>button {
        background-color: #ffffff !important;
        color: #002B5B !important;
        height: 50px !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE NAVEGACIÓN
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# --- PANTALLA DE LOGIN ---
if st.session_state["page"] == "login":
    st.markdown('<div class="main-login"><h1 class="acceder-text">Acceder</h1><p class="caudillo-text">Socio caudillo</p></div>', unsafe_allow_html=True)
    
    _, col_form, _ = st.columns([0.6, 2, 0.6])
    with col_form:
        email = st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed")
        password = st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed")
        st.markdown('<div class="login-btn">', unsafe_allow_html=True)
        if st.button("ACCEDER"):
            if email == "admin@csir.com" and password == "1913":
                st.session_state["page"] = "home"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA PRINCIPAL ---
elif st.session_state["page"] == "home":
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Panel de Control</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👤 Perfil"):
            st.session_state["page"] = "perfil"
            st.rerun()
            
        if st.button("⭐ Mejora de socio"):
            st.session_state["page"] = "mejora"
            st.rerun()

    with col2:
        if st.button("💰 Pagos"):
            st.session_state["page"] = "pagos"
            st.rerun()
            
        if st.button("🎟️ Comprar entradas"):
            st.session_state["page"] = "entradas"
            st.rerun()

    with st.sidebar:
        st.image("csir.png", width=80)
        if st.button("Cerrar Sesión"):
            st.session_state["page"] = "login"
            st.rerun()

# --- SUBPÁGINAS (EJEMPLO) ---
elif st.session_state["page"] == "perfil":
    st.title("👤 Mi Perfil")
    st.write("Aquí irán los datos del socio caudillo.")
    if st.button("⬅️ Volver"):
        st.session_state["page"] = "home"
        st.rerun()

elif st.session_state["page"] == "pagos":
    st.title("💰 Mis Pagos")
    st.write("Aquí se verá el estado de cuenta.")
    if st.button("⬅️ Volver"):
        st.session_state["page"] = "home"
        st.rerun()
