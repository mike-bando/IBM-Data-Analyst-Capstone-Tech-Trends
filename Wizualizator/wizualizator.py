import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Konfiguracja strony ---
st.set_page_config(
    page_title="Wizualizator Danych (Excel/CSV)",
    page_icon="📊",
    layout="wide"
)

# --- Tytuł i opis aplikacji ---
st.title("📊 Interaktywny Wizualizator Danych")
st.write("""
Przeciągnij i upuść poniżej swój plik Excela (.xlsx) lub CSV (.csv), aby zobaczyć dane i stworzyć interaktywne wizualizacje.
""")

# --- Przesyłanie pliku przez użytkownika (z obsługą CSV i XLSX) ---
uploaded_file = st.file_uploader("Wybierz plik Excel lub CSV", type=["xlsx", "csv"])

# Sprawdzenie, czy plik został przesłany
if uploaded_file is not None:
    try:
        # Sprawdzenie rozszerzenia pliku i wczytanie danych
        file_extension = os.path.splitext(uploaded_file.name)[1]
        
        if file_extension == '.csv':
            # Wczytanie pliku CSV
            df = pd.read_csv(uploaded_file)
        elif file_extension == '.xlsx':
            # Wczytanie pliku Excel
            df = pd.read_excel(uploaded_file)
        
        st.success(f"Plik {uploaded_file.name} został pomyślnie wczytany!")

        # --- Wyświetlanie interaktywnej tabeli z danymi ---
        st.header("Podgląd wczytanych danych")
        st.write("Poniżej znajduje się interaktywna tabela z Twoimi danymi. Możesz sortować kolumny klikając na nagłówki.")
        st.dataframe(df)

        # --- Sekcja do tworzenia wizualizacji ---
        st.header("Kreator interaktywnych wykresów")
        st.write("Wybierz kolumny, które chcesz zwizualizować.")

        col1, col2 = st.columns(2)

        with col1:
            chart_type = st.selectbox(
                "Wybierz typ wykresu:",
                ["Wykres słupkowy", "Wykres liniowy", "Wykres punktowy (rozrzutu)"]
            )
            x_axis = st.selectbox(
                "Wybierz kolumnę dla osi X:",
                df.columns,
                index=0
            )

        with col2:
            y_axis = st.selectbox(
                "Wybierz kolumnę dla osi Y:",
                df.columns,
                index=1 if len(df.columns) > 1 else 0
            )
            color_axis = st.selectbox(
                "Grupuj według koloru (opcjonalnie):",
                [None] + df.columns.tolist()
            )

        # --- Generowanie i wyświetlanie wykresu ---
        if st.button("Generuj wykres"):
            if x_axis and y_axis:
                try:
                    if chart_type == "Wykres słupkowy":
                        fig = px.bar(df, x=x_axis, y=y_axis, color=color_axis, title=f"Wykres słupkowy: {y_axis} vs {x_axis}")
                    elif chart_type == "Wykres liniowy":
                        fig = px.line(df, x=x_axis, y=y_axis, color=color_axis, title=f"Wykres liniowy: {y_axis} vs {x_axis}")
                    elif chart_type == "Wykres punktowy (rozrzutu)":
                        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_axis, title=f"Wykres rozrzutu: {y_axis} vs {x_axis}")

                    fig.update_layout(autosize=True)
                    st.plotly_chart(fig, use_container_width=True)

                    st.info("""
                    **Wskazówka:** Wykres jest interaktywny! Możesz najechać na punkty, aby zobaczyć wartości, przybliżać i oddalać widok oraz przesuwać wykres.
                    """)

                except Exception as e:
                    st.error(f"Wystąpił błąd podczas generowania wykresu: {e}")
            else:
                st.warning("Proszę wybrać kolumny dla osi X i Y.")

        # --- Wyświetlanie podstawowych statystyk ---
        st.header("Podstawowe statystyki opisowe")
        st.write("Automatycznie wygenerowane statystyki dla kolumn numerycznych.")
        st.write(df.describe())

    except Exception as e:
        st.error(f"Wystąpił błąd podczas wczytywania pliku: {e}")