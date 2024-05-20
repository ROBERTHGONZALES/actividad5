import streamlit as st

def main():
    st.title("Conversor de Precios")

    programa_file = st.file_uploader("Selecciona el archivo programa3.txt", type='txt')

    if programa_file is not None:
        conversion_results = []

        try:
            with open(programa_file.name, 'r') as input_file:
                for line in input_file:
                    parts = line.strip().split(',')
                    producto = parts[0].strip()
                    try:
                        precio = float(parts[1])
                        precio_convertido = precio * 3.8
                        conversion_results.append((producto, precio_convertido))
                    except (IndexError, ValueError):
                        st.warning(f"Advertencia: No se encontró un precio válido para el producto '{producto}'.")
            
            st.success("Resultados de la conversión:")
            for producto, precio_convertido in conversion_results:
                st.write(f"Producto: {producto}, Precio Convertido: {precio_convertido}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
