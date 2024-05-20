import streamlit as st

def main():
    st.title("Calculadora de Promedios")

    notas_file = st.file_uploader("Selecciona el archivo notas.txt", type='txt')

    if notas_file is not None:
        resultados = []

        try:
            with open(notas_file.name, 'r') as input_file:
                for line in input_file:
                    parts = line.strip().split(',')
                    nombre = parts[0]
                    notas = [float(nota.split(':')[1]) for nota in parts[1:]]
                    promedio = sum(notas) / len(notas) if notas else 0
                    resultados.append((nombre, promedio))
            
            st.success("Resultados de la calculadora de promedios:")
            for nombre, promedio in resultados:
                st.write(f"Estudiante: {nombre}, Promedio: {promedio}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
