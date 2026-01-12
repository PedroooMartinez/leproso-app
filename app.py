import streamlit as st

# Configuración de la pestaña
st.set_page_config(page_title="Socio CSIR", page_icon="💙")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .stApp {
        background-color: #002B5B;
        color: white;
    }
    .stButton>button {
        background-color: #FFFFFF;
        color: #002B5B;
        border-radius: 10px;
        font-weight: bold;
    }
    input {
        background-color: #f0f2f6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.title("⚓ Independiente Rivadavia")
st.subheader("Oficina Virtual del Socio")

st.write("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.write("💻 **Ingreso**")

with col2:
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("ENTRAR AL GARGANTINI"):
        # Por ahora usamos una clave fija para probar
        if email == "azul@gmail.com" and password == "1913":
            st.success("¡Bienvenido, Leproso!")
            st.balloons()
            st.write("### Próximo Partido")
            st.info("Independiente Rivadavia vs River Plate")
        else:
            st.error("Los datos no coinciden con nuestra base de socios.")

st.write("---")
st.caption("2024 - Sistema de Gestión de Socios CSIR")
