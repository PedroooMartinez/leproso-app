import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS PROFESIONAL "BLINDADO"
st.markdown("""
    <style>
    /* Fondo Azul Club */
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
        padding-top: 20px;
    }
    .acceder-text { font-size: 45px; font-weight: 800; color: white; margin-bottom: 0px; }
    .caudillo-text { font-size: 20px; font-weight: 300; color: #a8dadc; margin-bottom: 30px; }

    /* INPUTS (Fondo blanco, letra azul) */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 10px !important; }
    input { color: #002B5B !important; -webkit-text-fill-color: #002B5B !important; }

    /* --- BOTÓN ACCEDER (BLANCO CON LETRA AZUL - CHICO) --- */
    /* Usamos un selector específico para el botón de login para no romper los otros */
    .login-container div.stButton > button {
        background-color: white !important;
        color: #002B5B !important;
        height: 45px !important;
        width: 160px !important;
        margin: 0 auto !important;
        display: block !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }

    /* --- BOTONES DEL PANEL INTERNO (RECTÁNGULOS IGUALES) --- */
    /* Esta clase obligará a que midan lo mismo */
    .panel-container div.stButton > button {
        width: 100% !important;
        height: 120px !important; /* Alto fijo para todos */
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        transition: 0.3s !important;
    }
    
    .panel-container div.stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: white !important;
        transform: translateY(-3px);
    }

    /* Ocultar basurita de Streamlit */
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
    
    _, col_form, _ = st.columns([0.5, 2, 0.5])
    with col_form:
        email_input = st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed")
        pass_input = st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        # Envolvemos en el contenedor de login
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        if st.button("ACCEDER"):
            if email_input == "admin@csir.com" and pass_input == "1913":
                st.session_state["page"] = "home"
                st.rerun()
            else:
                st.error("Datos incorrectos")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA PRINCIPAL (DENTRO) ---
elif st.session_state["page"] == "home":
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Panel de Control</h2>", unsafe_allow_html=True)
    
    # Envolvemos todo el panel en una clase para controlar el tamaño de los botones
    st.markdown('<div class="panel-container">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

    with st.sidebar:
        st.image("csir.png", width=80)
        if st.button("Cerrar Sesión"):
            st.session_state["page"] = "login"
            st.rerun()

# --- SUBPÁGINAS ---
elif st.session_state["page"] == "perfil":
    st.markdown("## 👤 Mi Perfil")
    st.write("Bienvenido, Socio Caudillo.")
    if st.button("⬅️ Volver"):
        st.session_state["page"] = "home"
        st.rerun()
