import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS PARA DISEÑO PROFESIONAL, MINIMALISTA Y CENTRADO
st.markdown("""
    <style>
    /* Fondo oscuro profesional */
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    
    /* TRUCO PARA CENTRAR TODAS LAS IMÁGENES */
    [data-testid="stImage"] {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Centrar títulos manualmente */
    .titulo-centrado {
        text-align: center;
        margin-bottom: 20px;
    }

    /* Estilo de los inputs */
    .stTextInput>div>div>input {
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        padding: 10px;
    }

    /* Botón Minimalista Blanco */
    .stButton>button {
        background-color: #ffffff;
        color: #0d1117;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        height: 45px;
        transition: 0.3s;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }

    /* Ocultar menús innecesarios de Streamlit */
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
    
    # Espacio superior
    st.write("")
    st.write("")
    
    # Logo centrado (Gracias al CSS de arriba)
    st.image("csir.png", width=120)
    
    # Título centrado
    st.markdown("<h2 class='titulo-centrado'>Socio CSIR</h2>", unsafe_allow_html=True)
    
    # Contenedor del formulario (usamos columnas para que no sea tan ancho en PC)
    _, col_form, _ = st.columns([0.5, 2, 0.5])
    
    with col_form:
        email = st.text_input("Usuario", placeholder="correo@ejemplo.com")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        
        if st.button("Iniciar Sesión"):
            # Datos de prueba
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
        st.write("Estado: **Socio Activo**")
        st.write("---")
        if st.button("Cerrar Sesión"):
            st.session_state["logueado"] = False
            st.rerun()

    # Contenido principal
    st.markdown("## Bienvenido al Portal")
    st.write("Seleccioná una opción para continuar:")
    
    st.write("")
    
    # Tarjetas de acciones
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; height: 150px;'>
            <h4 style='margin-top: 0;'>🎟️ Entradas</h4>
            <p style='color: #8b949e; font-size: 14px;'>Sacá tu ticket para ver a la Lepra en el Gargantini.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Comprar Tickets"):
            st.info("Módulo de ventas en mantenimiento")
            
    with col2:
        st.markdown("""
        <div style='background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; height: 150px;'>
            <h4 style='margin-top: 0;'>💳 Mi Carnet</h4>
            <p style='color: #8b949e; font-size: 14px;'>Visualizá tu carnet digital y código QR de acceso.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ver Mi Carnet"):
            st.write("Cargando carnet...")
