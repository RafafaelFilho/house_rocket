<h1>Projeto de Insights House Rocket</h1>

- [0. Ferramentas Utilizadas](#0-ferramentas-utilizadas)
    - [1.1. Contextualização](#11-contextualização)
    - [1.2. Necessidade](#12-necessidade)
    - [1.3. Hipóteses](#13-hipóteses)
- [2. Estratégia de Solução](#2-estratégia-de-solução)
- [3. Exploratory Data Analysis](#3-exploratory-data-analysis)
- [4. Conclusão](#4-conclusão)
- [5. Próximos Passos](#5-próximos-passos)
- [6. Agradecimento](#5-agradecimento)
<hr>
<h2>0. Ferramentas Utilizadas</h2>
<div style="display: inline_block">
  <img align="center" alt="VSCode" height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
  <img align="center" alt="Python" height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
  <img align="center" alt="Pandas" height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" />
  <img align="center" alt="Streamlit" height="40" width="60" src=https://streamlit.io/images/brand/streamlit-mark-color.png />
  <img align="center" alt="Heroku" height="55" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-original.svg" />
  <img align="center" alt="Git" height="55" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />
  <img align="center" alt="Github" height="55" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />
</div>
<hr>
<h2>1. Problemas de Negócio</h2>
<h3>1.1. Contextualização</h3>
<p>House Rocket é uma empresa de compra e venda de imóveis localizada em Seattle (EUA) utilizando plataforma digital.</p>
<p>Seu CEO quer maximizar a receita localizando as melhores oportunidades de compra de imóvel. A principal estratégia é comprar as casas mais baratas e revender no futuro, quanto maior é essa diferença entre a compra e a venda do imóvel, maior é seu lucro.</p>
<h3>1.2. Necessidade</h3>
<p>Achar boas oportunidades é uma tarefa difícil pela quantidade de características que um imóvel tem. Então, o CEO necessita de uma análise para responder à essas questões:</p>
<ul>
    <li>Quais casas o CEO deveria comprar?</li>
    <li>Verificar se as hipóteses entregues pelo CEO estão corretas</li>
    <li>Gráficos simples porém dinâmicos para o CEO fazer as próprias análises</li>
    <li>O CEO precisa passar algumas informações para a equipe de contribuintes</li>
</ul>
<h3>1.3. Hipóteses</h3>
<ol>
    <li>Imóveis com vista para água, na média, são 20% mais caros!</l1>
    <li>Imóveis com porão são mais caros, em média, do que os sem porão!</li>
    <li>Imóveis reformados recentemente tem valor mais alto</li>
    <li>Imóveis de 3 banheiros tem um crescimento de MoM de 15%</li>
    <li>O crescimento do preço dos imóveis YoY é de 10%</li>
    <li>Imóveis sem porão possuem área total 40% maiores do que os imóveis com porão</li>
</ol>
<hr>
<h2>2. Estratégia de Solução</h2>
<ul>
    <li>Utilizar o banco de dados disponibilizado pela House Rocket para fazer as análises.</li>
    <li>Validação das hipóteses por meio de Exploratory Data Analysis.</li>
    <li>Cria tabelas dos imóveis que não devem ser comprados, imóveis que podem ser comprados e imóveis que tem possibilidade de reformar após a compra.</li>
    <li>Criar plataforma utilizando o Streamlit para fazer uma visualização simples e personalizável para analisar os dados com nível de acesso.</li>
</ul>
<hr>
<h2>3. Exploratory Data Analysis</h2>
<ol>
    <li>Imóveis com vista para água, na média, são 20% mais caros!</l1>
    <ul>
        <li>Não, os imóveis com vista para a água são 212% (ou 2,12 vezes) mais caros que os imóveis sem vista para a água.</li>
    </ul>
    <li>Imóveis com construção menor de 1955, são 50% mais baratos na média!</li>
    <ul>
        <li>Não, as casa são, aproximadamente, 17% mais baratas em média.</li>
    </ul>
    <li>Imóveis com porão são mais caros, em média, do que os sem porão!</li>
    <ul>
        <li>Sim, os imóveis com porão são, aproximadamente, 30% mais caros em média do que os sem porão.</li>
    </ul>
    <li>Imóveis de 3 banheiros tem um crescimento de MoM de 15%</li>
    <ul>
        <li>Não, os imóveis tem um movimento de preço de imóvel praticamente nulo.</li>
    </ul>
    <li>Imóveis reformados recentemente tem valor mais alto</li>
    <ul>
        <li>Sim, tem uma tendencia de aumento de preço nas casas com reformas recentemente com o passar do tempo.</li>
    </ul>
    <li>Imóveis sem porão possuem área total 40% maiores do que os imóveis com porão</li>
    <ul>
        <li>Não, imóveis sem porão são, aproximadamente, 23% maiores.</li>
    </ul>
    <li>O crescimento do preço dos imóves YoY é de 10%</li>
    <ul>
        <li>Não. No geral, o crescimento YoY é de 2%, porém, para as casas em condição 5 tem um YoY de 18%.</li>
    </ul>
</ol>
<hr>
<h2>4. Conclusão</h2>
<ul>
    <li>Vizualização</li>
    <a href="https://rafael-house-rocket.herokuapp.com/">Dashboard House Rocket Web</a>
    <p>Senhas (Senha - Funcionário): 1111 - CEO ; 2222 - Gerente ; 3333 - Vendedor</p>
    <li>Comentários</li>
    <p>Com as tabelas, as escolhas de imóveis vão ser mais assertivas com as informações de compra e/ou reforma para venda trazendo um resultado maior para a empresa.</br>
    Com a visualização das análises, a empresa vai ganhar velocidade para fazer as próprias análises e na passagem de informação no Streamlit (Funcionário, Gerente, Administrador)</p>
</ul>
<hr>
<h2>5. Próximos Passos</h2>
<ul>
    <li>Utilizar a evolução dos preços para saber a movimentação individual de cada imóvel para prever o aumento/diminuição dos preços dos imóveis</li>
    <li>A partir dos gráficos simples, analisar a necessidade para fazer um relatório com as análises mais pertinentes</li>
</ul>
<hr>
<h2>6. Agradecimento</h2>
<p><b>Muito Obrigado por ter visto meu projeto</b></p>
<p>Caso queira ver mais projetos meus ou entrar em contato comigo:</p>
<a href="https://rafafaelfilho.github.io/portfolio_projetos/">Outros Projetos</a></br>
<a href="https://github.com/RafafaelFilho/portfolio_projetos">Portfólio</a></br>
<a href="https://www.linkedin.com/in/rafael-filho/">LinkedIn</a>