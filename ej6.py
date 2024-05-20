import streamlit as st
from io import StringIO

def main():
    st.title("Informe de Horas Trabajadas")

    horas_file = st.file_uploader("Selecciona el archivo horas.txt", type='txt')

    if horas_file is not None:
        horas_trabajadas = analizar_horas(horas_file)

        st.success("Resultados del informe:")
        for nombre, horas_totales in horas_trabajadas.items():
            st.write(f"{nombre}, Horas Totales: {horas_totales}")

        st.markdown(get_download_link(horas_trabajadas), unsafe_allow_html=True)

def analizar_horas(horas_file):
    horas_trabajadas = {}

    # Leer el contenido del archivo y convertirlo en una cadena de texto
    horas_texto = horas_file.getvalue().decode("utf-8")

    for line in StringIO(horas_texto):
        parts = line.strip().split(',')
        nombre = parts[0]
        horas = int(parts[1])

        if nombre in horas_trabajadas:
            horas_trabajadas[nombre] += horas
        else:
            horas_trabajadas[nombre] = horas

    return horas_trabajadas

def get_download_link(horas_trabajadas):
    content = "\n".join([f"{nombre}, Horas Totales: {horas_totales}" for nombre, horas_totales in horas_trabajadas.items()])

    href = f'<a href="data:text/plain;charset=utf-8,{content}" download="informe_horas_totales.txt">Descargar resultados</a>'
    return href

if __name__ == "__main__":
    main()
