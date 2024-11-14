# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import re

# Criar a interface do Streamlit
st.title("App Músicas mais ouvidas no Spotify 💚")  # Define o título do aplicativo

# Exibir a logo única
st.image("logos.png", width=300)  # Ajuste o width conforme necessário

st.write("""
O gráfico abaixo representa as músicas mais ouvidas do Spotify em 2023 a 2024.
""")  # Markdown para descrição

# Carregar os arquivos CSV com encoding 'utf-8'
try:
    musica_2023 = pd.read_csv("musica2023.csv", encoding='utf-8')
    musica_2024 = pd.read_csv("musica2024.csv", encoding='utf-8')

    # Verificar se as colunas necessárias existem nos dois arquivos
    if 'nome_da_música' not in musica_2023.columns or 'reproduções_spotify' not in musica_2023.columns:
        st.error("A coluna 'nome_da_música' ou 'reproduções_spotify' está ausente no arquivo musica2023.csv")
    elif 'nome_da_música' not in musica_2024.columns or 'reproduções_spotify' not in musica_2024.columns:
        st.error("A coluna 'nome_da_música' ou 'reproduções_spotify' está ausente no arquivo musica2024.csv")

    # Função para remover números e espaços antes do nome da música
    def limpar_nome_musica(nome):
        return re.sub(r'^\d+\s*-*\s*', '', nome)  # Remove qualquer sequência de dígitos seguida por hífen ou espaço

    # Aplicar a função de limpeza nos nomes das músicas
    musica_2023['nome_da_música'] = musica_2023['nome_da_música'].apply(limpar_nome_musica)
    musica_2024['nome_da_música'] = musica_2024['nome_da_música'].apply(limpar_nome_musica)

    # Adicionando a seleção de ano na barra lateral
    st.sidebar.header("Filtros")
    ano_selecionado = st.sidebar.selectbox("Selecione o ano", ['2023', '2024'])

    # Determinar qual ano carregar baseado na seleção
    if ano_selecionado == '2023':
        musica = musica_2023
        st.subheader("🎶 Músicas mais ouvidas em 2023 🎶")
    else:
        musica = musica_2024
        st.subheader("🎶 Músicas mais ouvidas em 2024 🎶")

    # Limpeza dos dados da coluna 'reproduções_spotify'
    musica['reproduções_spotify'] = musica['reproduções_spotify'].str.replace(',', '')  # Remove as vírgulas
    musica['reproduções_spotify'] = musica['reproduções_spotify'].str.replace('|', '')  # Remove os pipes '|'
    
    # Converter a coluna para numérico
    musica['reproduções_spotify'] = pd.to_numeric(musica['reproduções_spotify'], errors='coerce')

    # Remover músicas duplicadas, mantendo apenas a primeira ocorrência
    musica = musica.drop_duplicates(subset='nome_da_música', keep='first')

    # Exibir os dados em tabela, ordenados pelo maior número de reproduções
    musica_sorted_tabela = musica[['nome_da_música', 'reproduções_spotify']].sort_values(by='reproduções_spotify', ascending=False)
    st.dataframe(musica_sorted_tabela)

    # Plotar as 10 músicas mais reproduzidas no Spotify
    musica_sorted = musica_sorted_tabela.head(10)  # Filtra as 10 mais reproduzidas
    
    st.write("🎧 **Top 10 Músicas mais reproduzidas no Spotify**")
    st.write("Este gráfico mostra as 10 músicas mais reproduzidas no Spotify para o ano selecionado. O número de reproduções indica a popularidade das músicas entre os ouvintes.")
    fig = px.bar(musica_sorted, 
                 x='nome_da_música', 
                 y='reproduções_spotify', 
                 title=f"Top 10 músicas mais reproduzidas no Spotify ({ano_selecionado})", 
                 labels={'reproduções_spotify': 'Reproduções no Spotify'},
                 color='reproduções_spotify',  # Colorir as barras com base no número de reproduções
                 color_continuous_scale='greens'  # Usando a paleta 'greens' para um verde chamativo
                 )
    
    fig.update_layout(
        template="plotly_dark",  # Para um tema escuro
        title_font=dict(size=24, color="white"),  # Ajustar o título para ser legível
        xaxis_title_font=dict(size=18, color="white"),
        yaxis_title_font=dict(size=18, color="white"),
        xaxis=dict(tickangle=45),  # Ajusta a inclinação do eixo X para melhor visualização
        yaxis=dict(tickformat=',')  # Formatação de números para a quantidade de reproduções
    )

    st.plotly_chart(fig)

    # Adicionando Column Configuration para seleção de colunas
    colunas_disponiveis = ['nome_da_música', 'contagem_de_playlists_spotify', 'reproduções_spotify']

    # Adicionando a opção "Tudo" para selecionar todas as colunas
    colunas_selecionadas = st.sidebar.multiselect(
        "Selecione as colunas para o gráfico de playlists do Spotify",
        options=colunas_disponiveis,
        default=colunas_disponiveis  # Por padrão, todas as colunas são selecionadas
    )

    if 'contagem_de_playlists_spotify' in colunas_selecionadas:
        # Gráfico de contagem de playlists no Spotify para 2023
        st.write("📅 **Top 10 Músicas mais adicionadas em playlists (2023)**")
        st.write("Este gráfico exibe as músicas mais presentes nas playlists dos usuários no Spotify, refletindo as preferências populares e frequentes em 2023.")
        musica_sorted_playlists_2023 = musica[['nome_da_música', 'contagem_de_playlists_spotify']].sort_values(by='contagem_de_playlists_spotify', ascending=False).head(10)

        fig_playlists_spotify_2023 = px.bar(musica_sorted_playlists_2023, 
                                           x='nome_da_música', 
                                           y='contagem_de_playlists_spotify', 
                                           title=f"Top 10 músicas com mais playlists no Spotify (2023)", 
                                           labels={'contagem_de_playlists_spotify': 'Contagem de Playlists no Spotify'},
                                           color='contagem_de_playlists_spotify', 
                                           color_continuous_scale='greens')  # Usando a paleta verde

        fig_playlists_spotify_2023.update_layout(
            template="plotly_dark",
            title_font=dict(size=24, color="white"),
            xaxis_title_font=dict(size=18, color="white"),
            yaxis_title_font=dict(size=18, color="white"),
            xaxis=dict(tickangle=45),
            yaxis=dict(tickformat=',')
        )
        
        st.plotly_chart(fig_playlists_spotify_2023)

    if ano_selecionado == '2024':  # Gráfico adicional para o ano de 2024
        # Gráfico de barras horizontais de 'nome_do_artista' e 'alcance_das_playlists_spotify' para 2024
        st.write("🎧 **Alcance das Playlists no Spotify por Artista (2024)**")
        st.write("Este gráfico mostra o alcance das playlists para os artistas em 2024.")
        musica_2024_sorted = musica_2024[['nome_do_artista', 'alcance_das_playlists_spotify']].sort_values(by='alcance_das_playlists_spotify', ascending=False).head(10)

        fig_alcance_artistas = px.bar(musica_2024_sorted, 
                                      y='nome_do_artista', 
                                      x='alcance_das_playlists_spotify', 
                                      title="Alcance das Playlists no Spotify por Artista (2024)",
                                      labels={'alcance_das_playlists_spotify': 'Alcance das Playlists'},
                                      color='alcance_das_playlists_spotify',
                                      color_continuous_scale='greens', 
                                      orientation='h')  # Barra horizontal

        fig_alcance_artistas.update_layout(
            template="plotly_dark", 
            title_font=dict(size=24, color="white"),
            xaxis_title_font=dict(size=18, color="white"),
            yaxis_title_font=dict(size=18, color="white"),
            xaxis=dict(tickformat=','), 
            yaxis=dict(tickangle=0)
        ) 
        
        st.plotly_chart(fig_alcance_artistas)

except FileNotFoundError:
    st.error("Um ou ambos os arquivos CSV não foram encontrados. Verifique os arquivos.")
except pd.errors.ParserError:
    st.error("Erro ao analisar os arquivos CSV. Verifique o formato dos arquivos.")
