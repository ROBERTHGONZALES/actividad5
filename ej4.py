import streamlit as st
from io import StringIO

def main():
    st.title("Análisis de Temperaturas")

    temperaturas_file = st.file_uploader("Selecciona el archivo TEMPERATURAS.txt", type='txt')

    if temperaturas_file is not None:
        # Convertir el objeto BytesIO en una cadena
        temperaturas_str = temperaturas_file.getvalue().decode("utf-8")
        
        # Convertir la cadena en un objeto StringIO
        temperaturas_io = StringIO(temperaturas_str)
        
        max_temp, fecha_max, min_temp, fecha_min = analizar_temperaturas(temperaturas_io)

        st.success("Resultados del análisis:")
        st.write(f"Fecha con temperatura máxima: {fecha_max} - {max_temp}")
        st.write(f"Fecha con temperatura mínima: {fecha_min} - {min_temp}")

        st.markdown(get_download_link(max_temp, fecha_max, min_temp, fecha_min), unsafe_allow_html=True)

def analizar_temperaturas(temperaturas_file):
    max_temp = -50
    min_temp = 200
    fecha_max = ""
    fecha_min = ""

    for line in temperaturas_file:
        parts = line.strip().split(',')
        fecha = parts[0]
        temperatura = float(parts[1])

        if temperatura > max_temp:
            max_temp = temperatura
            fecha_max = fecha
        if temperatura < min_temp:
            min_temp = temperatura
            fecha_min = fecha

    return max_temp, fecha_max, min_temp, fecha_min

def get_download_link(max_temp, fecha_max, min_temp, fecha_min):
    content = f"Fecha con temperatura máxima: {fecha_max} - {max_temp}\n"
    content += f"Fecha con temperatura mínima: {fecha_min} - {min_temp}"

    href = f'<a href="data:text/plain;charset=utf-8,{content}" download="maximo_minimo_temperatura.txt">Descargar resultados</a>'
    return href

if __name__ == "__main__":
    main()
