import streamlit as st

# 1. CONFIGURACIÓN DE PESTAÑA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. DISEÑO PREMIUM (CSS ACTUALIZADO)
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

    /* --- BOTONES DEL PANEL (TODOS IGUALES) --- */
    .panel-btn>div>div>button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        height: 120px !important;
        width: 100% !important;
        font-size: 20px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
        display: block !important;
    }
    .panel-btn>div>div>button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid #ffffff !important;
        transform: translateY(-5px);
    }

    /* --- BOTÓN ACCEDER (MÁS CHICO Y CENTRADO) --- */
    .login-btn-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .login-btn-container>div>div>button {
        background-color: #ffffff !important;
        color: #002B5B !important;
        height: 45px !important;
        width: 150px !important; /* Tamaño más chico controlado */
        border-radius: 10px !important;
        font-weight: bold !important;
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
        st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed", key="email")
        st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed", key="pass")
        
        # Contenedor para achicar el botón de acceder
        st.markdown('<div class="login-btn-container">', unsafe_allow_html=True)
        if st.button("ACCEDER"):
            if st.session_state.email == "admin@csir.com" and st.session_state.pass == "1913":
                st.session_state["page"] = "home"
                st.rerun()
            else:
                st.error("Datos incorrectos")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA PRINCIPAL (DENTRO) ---
elif st.session_state["page"] == "home":
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Panel de Control</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="panel-btn">', unsafe_allow_html=True)
        if st.button("👤 Perfil"):
            st.session_state["page"] = "perfil"
            st.rerun()
        if st.button("⭐ Mejora de socio"):
            st.session_state["page"] = "mejora"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel-btn">', unsafe_allow_html=True)
        if st.button("💰 Pagos"):
            st.session_state["page"] = "pagos"
            st.rerun()
        if st.button("🎟️ Comprar entradas"):
            st.session_state["page"] = "entradas"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with st.sidebar:
        st.image("csir.png", width=80)
        if st.button("Cerrar Sesión"):
            st.session_state["page"] = "login"
            st.rerun()

# --- SUBPÁGINAS ---
elif st.session_state["page"] == "perfil":
    st.markdown("## 👤 Mi Perfil")
    st.write("Datos del socio...")
    if st.button("⬅️ Volver"):
        st.session_state["page"] = "home"
        st.rerun()
