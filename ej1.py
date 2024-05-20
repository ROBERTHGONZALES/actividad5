import streamlit as st
import os
def main():
    # Título de la aplicación
    st.title("Filtrar correos electrónicos")

 
    uploaded_file = st.file_uploader("Cargar archivo de datos", type=["txt"])

    if uploaded_file is not None:

        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()


        output_emails = []

        for line in file_contents:
            nombre, edad, email = line.split(",")
            edad = int(edad.strip())
            if edad > 18:
                output_emails.append(email.strip())

        st.header("Correos electrónicos filtrados:")
        for email in output_emails:
            st.write(email)

        # Descargar el archivo de salida
        output_text = "\n".join(output_emails)
        st.download_button(
            label="Descargar correos electrónicos filtrados",
            data=output_text,
            file_name="emails_filtrados.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()