import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt

# Datos simulados
ventas_pizzas = [
    {"nombre": "Pepperoni"},
    {"nombre": "Hawaiana"},
    {"nombre": "Pepperoni"},
    {"nombre": "Mexicana"},
    {"nombre": "Pepperoni"},
    {"nombre": "Hawaiana"},
    {"nombre": "Cuatro quesos"},
    {"nombre": "Pepperoni"},
    {"nombre": "Mexicana"},
    {"nombre": "Pepperoni"},
]

ingredientes_tienda = [
    "Queso mozzarella",
    "Pepperoni",
    "Jamón",
    "Piña",
    "Champiñones",
    "Chorizo",
    "Pimiento",
    "Aceitunas negras",
    "Salsa de tomate",
    "Queso cheddar",
    "Orégano",
    "Tocino"
]

# Contador de ventas
pizzas_contadas = Counter(p["nombre"] for p in ventas_pizzas)
pizza_mas_vendida, total_vendida = pizzas_contadas.most_common(1)[0]

# Interfaz
st.title("🍕 Dashboard de la Pizzería")
st.subheader("📊 Información general")

st.write(f"🥇 La pizza más vendida es: **{pizza_mas_vendida}** con **{total_vendida}** ventas.")
st.write(f"🧂 Hay un total de **{len(ingredientes_tienda)} ingredientes** en la tienda.")

if st.checkbox("📋 Mostrar lista de ingredientes"):
    st.write("### Ingredientes disponibles:")
    for i, ing in enumerate(ingredientes_tienda, 1):
        st.write(f"{i}. {ing}")

# Gráfico de ventas
st.subheader("📈 Ventas por tipo de pizza")

fig, ax = plt.subplots()
ax.bar(pizzas_contadas.keys(), pizzas_contadas.values(), color='tomato')
ax.set_ylabel("Cantidad de ventas")
ax.set_xlabel("Tipo de pizza")
ax.set_title("Ventas por pizza")
plt.xticks(rotation=45)
st.pyplot(fig)

# Opción extra: agregar más datos
st.markdown("---")
st.subheader("➕ ¿Deseas simular otra venta?")
nueva_pizza = st.selectbox("Selecciona una pizza para simular una venta:", list(pizzas_contadas.keys()))
if st.button("Registrar venta"):
    ventas_pizzas.append({"nombre": nueva_pizza})
    st.success(f"¡Venta registrada para la pizza {nueva_pizza}!")
    st.info("🔁 Recarga la página para ver los cambios en el gráfico.")
