import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS MAESTRO (Para centrar TODO)
st.markdown("""
    <style>
    /* Fondo oscuro */
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    
    /* Forzar el centrado de la imagen y el título */
    .centrado-total {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    /* Estilo de los inputs para que no sean gigantes */
    .stTextInput>div>div>input {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* Botón blanco minimalista */
    .stButton>button {
        background-color: #ffffff;
        color: #0d1117;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        height: 45px;
    }

    /* Ocultar basura de la interfaz */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# --- PANTALLA DE INICIO ---
if not st.session_state["logueado"]:
    
    # CONTENEDOR CENTRADO (Logo + Título)
    st.markdown(f"""
        <div class="centrado-total">
            <img src="https://raw.githubusercontent.com/{st.secrets.get('github_user', 'TU_USUARIO')}/leproso-app/main/csir.png" width="120" style="margin-bottom: 20px;">
            <h2 style="margin-bottom: 30px;">Socio CSIR</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Si la imagen de arriba no carga porque el link es privado, usamos esta de respaldo:
    # st.image("csir.png", width=120) 

    # FORMULARIO
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
    st.sidebar.image("csir.png", width=60)
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["logueado"] = False
        st.rerun()

    st.markdown("## Bienvenido al Portal")
    # ... resto del código igual ...
