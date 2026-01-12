import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS PROFESIONAL Y CORRECCIÓN DE COLORES
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
    .acceder-text { font-size: 45px; font-weight: 800; margin-bottom: 0px; color: white; }
    .caudillo-text { font-size: 20px; font-weight: 300; color: #a8dadc; margin-bottom: 30px; }

    /* INPUTS (Fondo blanco, letra azul) */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 10px !important; }
    input { color: #002B5B !important; -webkit-text-fill-color: #002B5B !important; }

    /* BOTONES DEL PANEL INTERNO (IGUALES Y LEGIBLES) */
    div.stButton > button {
        width: 100% !important;
        height: 100px !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        display: block !important;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: white !important;
    }

    /* BOTÓN ACCEDER (BLANCO CON LETRA AZUL - CHICO) */
    .login-center {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    /* Forzamos el estilo específico para el botón de login */
    div.stButton > button[kind="secondaryFormSubmit"], 
    div.stButton > button:first-child:not(.panel-btn) {
        /* Este estilo se aplica al primer botón que encuentre (el de login) */
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
        
        # Botón Acceder estilizado manualmente
        st.markdown("""
            <style>
            /* Estilo específico para el botón de esta pantalla */
            div.stButton > button {
                background-color: white !important;
                color: #002B5B !important;
                height: 45px !important;
                width: 160px !important;
                margin: 0 auto !important;
                display: block !important;
            }
            </style>
        """, unsafe_allow_html=True)
        
        if st.button("ACCEDER"):
            if email_input == "admin@csir.com" and pass_input == "1913":
                st.session_state["page"] = "home"
                st.rerun()
            else:
                st.error("Datos incorrectos")

# --- PANTALLA PRINCIPAL (DENTRO) ---
elif st.session_state["page"] == "home":
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Panel de Control</h2>", unsafe_allow_html=True)
    
    # CSS específico para que los botones internos sean distintos al de login
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            height: 120px !important;
            width: 100% !important;
        }
        </style>
    """, unsafe_allow_html=True)

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

# --- SUBPÁGINAS ---
elif st.session_state["page"] == "perfil":
    st.markdown("## 👤 Mi Perfil")
    st.write("Datos del socio...")
    if st.button("⬅️ Volver"):
        st.session_state["page"] = "home"
        st.rerun()
