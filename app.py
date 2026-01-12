import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA (Minimalista)
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",  # Tu archivo de logo
    layout="centered"
)

# 2. CSS PARA DISEÑO PROFESIONAL Y MINIMALISTA
st.markdown("""
    <style>
    /* Fondo liso y oscuro profesional */
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    
    /* Estilo de los inputs */
    .stTextInput>div>div>input {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        padding: 10px;
    }

    /* Botón Minimalista */
    .stButton>button {
        background-color: #ffffff;
        color: #0d1117;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        height: 45px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }

    /* Contenedor de Login */
    .login-box {
        background-color: #161b22;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #30363d;
        text-align: center;
    }
    
    /* Quitar el menú de Streamlit para más limpieza */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE NAVEGACIÓN
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# --- PANTALLA DE INICIO (LOGIN) ---
if not st.session_state["logueado"]:
    # Centrar el logo y el login
    _, col_centrada, _ = st.columns([1, 2, 1])
    
    with col_centrada:
        st.image("csir.png", width=100)
        st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Socio CSIR</h2>", unsafe_allow_html=True)
        
        with st.container():
            email = st.text_input("Usuario", placeholder="correo@ejemplo.com")
            password = st.text_input("Contraseña", type="password", placeholder="••••••••")
            st.write("")
            if st.button("Iniciar Sesión"):
                # Por ahora, clave estática hasta conectar el Excel
                if email == "azul@gmail.com" and password == "1913":
                    st.session_state["logueado"] = True
                    st.rerun()
                else:
                    st.error("Credenciales no válidas")

# --- PANTALLA PRINCIPAL (DENTRO) ---
else:
    # Sidebar minimalista
    with st.sidebar:
        st.image("csir.png", width=60)
        st.write("### Mi Cuenta")
        st.write("ID Socio: **#1913-01**")
        if st.button("Cerrar Sesión"):
            st.session_state["logueado"] = False
            st.rerun()

    # Contenido principal
    st.markdown("## Bienvenido al Portal")
    st.write("Gestioná tus entradas y beneficios.")
    
    st.write("---")
    
    # Grid de acciones rápidas
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style='background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d;'>
            <h4 style='margin-top: 0;'>🎟️ Entradas</h4>
            <p style='color: #8b949e;'>Comprá tus tickets para el próximo partido.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ir a Entradas"):
            st.info("Función de compra activa próximamente")
            
    with c2:
        st.markdown("""
        <div style='background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d;'>
            <h4 style='margin-top: 0;'>👤 Mi Perfil</h4>
            <p style='color: #8b949e;'>Actualizá tus datos personales de socio.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ver Mi Perfil"):
            st.write("Datos del socio...")
