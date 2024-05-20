import streamlit as st
from io import StringIO

def main():
    st.title("Análisis de Ventas")

    ventas_file = st.file_uploader("Selecciona el archivo VENTAS.txt", type='txt')

    if ventas_file is not None:
        ventas_texto = StringIO(ventas_file.getvalue().decode("utf-8"))
        fecha_max, ventas_max, fecha_min, ventas_min, ventas_totales, promedio_ventas = analizar_ventas(ventas_texto)

        st.success("Resultados del análisis:")
        st.write(f"Fecha con ventas máximas: {fecha_max} - {ventas_max}")
        st.write(f"Fecha con ventas mínimas: {fecha_min} - {ventas_min}")
        st.write(f"Ventas totales: {ventas_totales}")
        st.write(f"Promedio de ventas: {promedio_ventas}")

        st.markdown(get_download_link(fecha_max, ventas_max, fecha_min, ventas_min, ventas_totales, promedio_ventas), unsafe_allow_html=True)

def analizar_ventas(ventas_file):
    ventas_max = -1
    ventas_min = float('inf')
    suma_ventas = 0
    num_ventas = 0

    for line in ventas_file:
        parts = line.strip().split(',')
        fecha = parts[0]
        ventas = float(parts[1])
        suma_ventas += ventas
        num_ventas += 1

        if ventas > ventas_max:
            ventas_max = ventas
            fecha_max = fecha
        if ventas < ventas_min:
            ventas_min = ventas
            fecha_min = fecha

    promedio_ventas = suma_ventas / num_ventas if num_ventas > 0 else 0

    return fecha_max, ventas_max, fecha_min, ventas_min, suma_ventas, promedio_ventas

def get_download_link(fecha_max, ventas_max, fecha_min, ventas_min, ventas_totales, promedio_ventas):
    content = f"Fecha con ventas máximas: {fecha_max} - {ventas_max}\n"
    content += f"Fecha con ventas mínimas: {fecha_min} - {ventas_min}\n"
    content += f"Ventas totales: {ventas_totales}\n"
    content += f"Promedio de ventas: {promedio_ventas}"

    href = f'<a href="data:text/plain;charset=utf-8,{content}" download="datos_final_ventas.txt">Descargar resultados</a>'
    return href

if __name__ == "__main__":
    main()
