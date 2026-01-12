import streamlit as st

# 1. CONFIGURACIÓN DE LA PESTAÑA (LOGO Y TÍTULO)
st.set_page_config(
    page_title="CSIR | Oficina Virtual",
    page_icon="csir.png",
    layout="centered"
)

# 2. CSS PARA EL DISEÑO AZUL Y CONTRASTE DE TEXTO
st.markdown("""
    <style>
    /* Fondo Azul Independiente Rivadavia */
    .stApp {
        background-color: #002B5B;
        color: #ffffff;
    }
    
    /* Centrado de textos superiores */
    .main-login {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding-top: 50px;
    }
    .acceder-text { 
        font-size: 42px; 
        font-weight: 800; 
        margin-bottom: 0px; 
    }
    .caudillo-text { 
        font-size: 20px; 
        font-weight: 300; 
        color: #a8dadc; 
        margin-bottom: 40px; 
    }

    /* Cuadros de texto: fondo blanco y letra azul oscuro para legibilidad */
    div[data-baseweb="input"] { 
        background-color: #ffffff !important; 
        border-radius: 10px !important; 
    }
    input { 
        color: #002B5B !important; 
        -webkit-text-fill-color: #002B5B !important; 
        font-weight: 500 !important;
    }

    /* Estilo del botón de Acceder */
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

    /* Ocultar elementos innecesarios de la interfaz */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENIDO DE LA PANTALLA
st.markdown("""
    <div class="main-login">
        <h1 class="acceder-text">Acceder</h1>
        <p class="caudillo-text">Socio caudillo</p>
    </div>
""", unsafe_allow_html=True)

# Formulario centrado
_, col_form, _ = st.columns([0.6, 2, 0.6])

with col_form:
    email = st.text_input("Correo", placeholder="usuario@mail.com", label_visibility="collapsed")
    password = st.text_input("Clave", type="password", placeholder="••••••••", label_visibility="collapsed")
    
    if st.button("ACCEDER"):
        if email == "admin@csir.com" and password == "1913":
            st.success("¡Ingresando!")
        else:
            st.error("Credenciales incorrectas")
