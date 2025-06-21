# pizzeria-dashboard
sabor supremo
%%writefile app.py
import streamlit as st
from collections import Counter

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

# Título de la app
st.title("🍕 Dashboard Pizzería")

# Calcular la pizza más vendida
pizzas_contadas = Counter(p["nombre"] for p in ventas_pizzas)
pizza_mas_vendida, total_vendida = pizzas_contadas.most_common(1)[0]

# Calcular cuántos ingredientes diferentes hay
total_ingredientes = len(ingredientes_tienda)

# Mostrar resultados
st.header("📊 Información general")
st.write(f"La **pizza más vendida** es: 🏆 **{pizza_mas_vendida}** con **{total_vendida}** ventas.")
st.write(f"Hay un total de **{total_ingredientes} ingredientes diferentes** disponibles en la tienda.")

# Mostrar ingredientes si el usuario lo desea
if st.checkbox("📋 Ver lista de ingredientes"):
    for i, ing in enumerate(ingredientes_tienda, 1):
        st.write(f"{i}. {ing}")
