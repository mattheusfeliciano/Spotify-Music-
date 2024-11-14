# Spotify Music App 💚▶️

Bem-vindo ao Spotify Music App! Este projeto foi desenvolvido com o objetivo de explorar e visualizar dados sobre músicas do Spotify de maneira interativa. Utilizando Streamlit, Plotly e outras ferramentas, o aplicativo oferece uma análise profunda de dados, com gráficos dinâmicos e interativos para tornar a exploração da música ainda mais divertida. 🎧

Este aplicativo foi desenvolvido por Matheus Feliciano, Anna Karolyne, Micael Souza e Claudiano Barbosa. 👨‍💻👩‍💻👨‍💻

##Tecnologias Utilizadas 🛠️
Streamlit: Para criar o front-end do aplicativo de forma simples e interativa.
Plotly: Para criar gráficos interativos e visualizações dos dados.
Pandas: Para manipulação de dados e criação dos DataFrames.
VS Code: Para o desenvolvimento local, edição de código e integração com o GitHub.
Google Colab: Para processamento de dados e execução colaborativa no ambiente de nuvem.
Funcionalidades 🔍
O projeto oferece diversas funcionalidades, incluindo a exploração de dados sobre músicas, artistas e álbuns populares. O aplicativo permite visualizar informações de forma interativa, utilizando gráficos dinâmicos criados com Plotly. Algumas das funcionalidades incluem:

##Exploração de Dados: Visualização interativa de informações sobre músicas, artistas e álbuns populares.
Gráficos Dinâmicos: Gráficos interativos para explorar dados como a popularidade de músicas, distribuição de gêneros e tendências ao longo do tempo.
Análise de Dados: Análise detalhada dos dados utilizando DataFrames (df), com colunas como artist, album, genre, track_name, popularity, entre outras.

Como Rodar o Projeto 🚀
##1. Clone o Repositório
Primeiro, faça o clone deste repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/mattheusfeliciano/Spotify-Music-.git
cd Spotify-Music-
##2. Instalar as Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. Para instalá-las, basta rodar o seguinte comando:

Copiar código
pip install -r requirements.txt
##3. Rodar o App Localmente
Para rodar o aplicativo localmente, você pode usar o Streamlit. Navegue até a pasta do projeto e execute:

arduino
Copiar código
streamlit run app.py
Isso irá abrir o aplicativo no seu navegador para você visualizar a aplicação.

##4. Rodando no Google Colab
Se preferir, você pode rodar o código diretamente no Google Colab:

Acesse o Google Colab.
Carregue o notebook do projeto ou faça upload dos arquivos para rodar o código.
Instale as dependências necessárias no ambiente do Colab:
diff
Copiar código
!pip install -r requirements.txt
Você pode acessar diretamente o notebook no Colab aqui.

##5. Deploy no Streamlit Cloud
Se você deseja hospedar o projeto na Streamlit Community Cloud para acessá-lo de qualquer lugar, basta:

Conectar seu repositório GitHub ao Streamlit (leia mais na documentação oficial).
Selecionar o repositório Spotify-Music- no painel de controle do Streamlit.
Configurar o arquivo principal (geralmente app.py) e clicar em Deploy.
6. Atualizando o Repositório
Caso faça alterações e queira atualizar o repositório no GitHub, não se esqueça de rodar os comandos para fazer commit e push:

sql
Copiar código
git add .
git commit -m "Mensagem do seu commit"
git push origin main
Visualizações 📊
O projeto utiliza gráficos interativos com Plotly para apresentar diversos insights sobre as músicas e artistas. Alguns exemplos de visualizações incluem:

Top Artistas e Músicas: Visualização da popularidade de músicas e artistas.
Distribuição de Gêneros: Gráficos de barras ou pizza mostrando a popularidade dos gêneros musicais.
Tendências ao Longo do Tempo: Análise de como a popularidade das músicas varia ao longo do tempo.
Análise de Álbum e Artistas: Gráficos que comparam a popularidade de álbuns e artistas.
Exemplo de Colunas no DataFrame (df)
Os dados utilizados no aplicativo são manipulados em DataFrames do Pandas. Algumas das principais colunas incluem:

track_name: O nome da música.
artist: O nome do artista ou banda.
album: O nome do álbum onde a música está presente.
popularity: Um índice que representa a popularidade da música (quanto maior, mais popular).
genre: O gênero musical da música (por exemplo, pop, rock, etc.).
duration_ms: A duração da música em milissegundos.
explicit: Se a música tem conteúdo explícito ou não (True/False).
Essas colunas são analisadas e apresentadas de forma interativa por meio dos gráficos.

Notas Finais 💡
O código foi organizado para facilitar futuras modificações e a inclusão de novas análises.
A manipulação de dados é feita principalmente com Pandas para garantir uma análise eficiente e precisa.
O objetivo é fornecer uma experiência interativa e educativa, utilizando as melhores práticas de análise de dados e visualização.
Contribuições 🤝
Se você quiser contribuir com o projeto, siga as etapas abaixo:

Faça um fork do repositório.
Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade).
Faça as mudanças e commit (git commit -m 'Adicionando nova funcionalidade').
Envie para o repositório remoto (git push origin feature/nova-funcionalidade).
Abra um Pull Request.
Licença 📜
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Links úteis 🌐
Documentação do Streamlit
Documentação do Pandas
Documentação do Plotly
Google Colab: Acesse o notebook do Colab aqui
Kaggle - Top Spotify Songs 2023: Baixe os dados aqui
Kaggle - Most Streamed Spotify Songs 2024: Baixe os dados aqui
Divirta-se explorando o mundo da música e dados! 🎶📊

