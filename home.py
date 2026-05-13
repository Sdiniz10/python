from flask import Flask

app = Flask(__name__)


@app.route("/")
def curriculo():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>curriculo</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
</head>
<body>
    <div class="container">
        <div class="left_side">
            <div class="profile_text">
                <div class="img_bx">
                    <!-- Substitua a imagem profile.png na pasta img e altere src para "img/NOME_DA_SUA_IMAGEM_COM_EXTENSÃO" -->
                    <img src="profile.png">
                </div>
                 <!-- Substitua Clarinha por seu nome e "Data Scientist | Data Analyst | Data Engineer" pelos seus cargos/títulos -->
                <h2>Samuel Diniz - 17 anos<br><span>Dev</span></h2>
            </div>

            <div class="contact_info">
                <h3 class="title">Informações de Contato</h3>
                <ul>
                    <li>
                        <span class="icon"><i class="fa fa-phone" aria-hidden="true"></i></span>
                        <!-- Substitua por seu DDI (código DDI do Brasil é 55), DDD e número de celular -->
                        <span class="text">+55 31 97568-0065</span>
                    </li>
                    <li>
                        <span class="icon"><i class="fa fa-envelope-o" aria-hidden="true"></i></span>
                        <!-- Substitua por seu email -->
                        <span class="text">dinizsamuel400a@gmail.com</span>
                    </li>
                    <li>
                        <span class="icon"><i class="fa fa-linkedin-square" aria-hidden="true"></i></span>
                        <!-- Coloque o link do seu linkedin em href e substitua "linkedin.com/in/clarinha/" pelo seu link sem https:// -->
                        <a href="" target="_blank"><span class="text">linkedin.com/in/S10diniz/</span></a>F
                    </li>
                    <li>
                        <span class="icon"><i class="fa fa-github" aria-hidden="true"></i></span>
                        <!-- Coloque o link do seu github em href e substitua "github.com/s10diniz" pelo seu link sem https:// -->
                        <a href="" target="_blank"><span class="text">github.com/s10diniz</span></a>
                    </li>
                    <li>
                        <span class="icon"><i class="fa fa-map-marker" aria-hidden="true"></i></span>
                        <!-- Substitua pelo estado e país na qual vive -->
                        <span class="text">Mg, Brasil</span>
                    </li>
                </ul>
            </div>

            <div class="contact_info education">
                <h3 class="title">Formação</h3>
                <ul>
                    <li>
                        <!-- Substitua pelo ano de ingresso e conclusão de curso (se estiver cursando, coloque Atual ou o ano esperado para a formação) -->
                        <h5>2024-atual</h5>
                        <h4>técnico em informática</h4>
                        <h4>Colégio Cotemig</h4>
                    </li>
                    <!-- Se precisar adicionar mais formações só copiar o trecho <li>...</li> e colar logo abaixo. Veja o exemplo-->
                    <li>
                        <h5>2024-atual</h5>
                        <h4>Graduação em TI</h4>
                        <h4>colégio cotemig</h4>
                    </li>
                    <li>
                        <h5>2011-2024</h5>
                        <h4>colégio SJT</h4>
                    </li>
                </ul>
            </div>

            <div class="contact_info language">
                <h3 class="title">Idiomas</h3>
                <ul>
                    <li>
                        <!-- Substitua "Português" pelo idioma que você quer -->
                        <span class="text">Português</span>
                        <span class="percent">
                            <!-- Altera a porcentagem de acordo com a sua proeficiência no idioma acima -->
                            <div style="width: 100%;"></div>
                        </span>
                    </li>
                    <!-- Se precisar adicionar mais idiomas só copiar o trecho <li>...</li> e colar logo abaixo. Veja o exemplo -->
                    <li>
                        <!-- Substitua "Inglês" pelo idioma que você quer -->
                        <span class="text">Inglês</span>
                        <!-- Altera a porcentagem de acordo com a sua proeficiência no idioma acima -->
                        <span class="percent">
                            <div style="width: 80%;"></div>
                        </span>
                    </li>
                    <li>
                        <!-- Substitua "Espanhol" pelo idioma que você quer -->
                        <span class="text">Espanhol</span>
                        <!-- Altera a porcentagem de acordo com a sua proeficiência no idioma acima -->
                        <span class="percent">
                            <div style="width: 70%;"></div>
                        </span>
                    </li>
                    <!-- Se precisar remover algum idioma só deletar o trecho <li>...</li> em que o idioma está inserido -->
                </ul>
            </div>

        </div>
        <div class="right_side">
            <div class="light-dark-mode">
                <div class="trilho" id="trilho">
                    <div class="indicador">
                        <i class="bi bi-brightness-high-fill" id="icone"></i>
                        <!-- <i class="bi bi-moon-fill"></i> -->
                    </div>
                </div>
            </div>
            <script src="script.js"></script>
            <div class="about">
                <h2 class="title2">Sobre</h2>
                <!-- Substitua a apresentação da clarinha pela sua, contando um pouco sobre você e sua jornada -->
                <p>Olá! Meu nome é Diniz e eu adoro progamar, possuo cursos feitos no Codedex de java, lua, e atualmente possuo 9 cursos na cisco sobre cybersegurança, cisco packet tracer e muito mais, além de 2 the bests of the class no cotemig, acompanhe mais pelo meu linkedin
                    <!-- Use <br><br> para pular linhas -->
                    <br><br>Desde que me lembro, sempre fui fascinada pela forma como números e informações podem contar histórias e revelar padrões ocultos.
                    <br><br>Como profissional na área de análise de dados, tenho o privilégio de mergulhar fundo nesse mundo todos os dias, desvendando insights valiosos e ajudando a tomar decisões informadas. 
                </div>
            <div class="about">
                <h2 class="title2">Experiência</h2>
                <div class="box">
                    <div class="year_company">
                        <!-- Substitua pelo ano de ingresso e de saída da empresa (se for seu emprego atual, coloque Atual) -->
                        <h5>ainda não trabalho</h5>
                        <h5>Cotemig</h5>
                    </div>
                    <div class="text">
                        <!-- Substitua pelo seu cargo -->
                        <h4>Estudante</h4>
                        <!-- Descreva suas funções para o cargo mencionado -->
                        <p>
                           ainda não trabalho, estou em busca de um emprego
                        </p>
                    </div>
                </div>
                <!-- Se precisar adicionar mais experiências só copiar o trecho <div class="box">...</div> e colar abaixo. Veja o exemplo -->
            <div class="about skills">
                <h2 class="title2">Habilidades Profissionais</h2>
                <div class="box">
                    <!-- Substitua "Python" pela habilidade que você quiser -->
                    <h4>Python</h4>
                    <div class="percent">
                        <!-- Altera a porcentagem de acordo com a sua proeficiência na habilidade acima  -->
                        <div style="width: 90%;"></div>
                    </div>
                </div>
                <!-- Se precisar adicionar mais habilidades só copiar o trecho <div class="box">...</div> e colar abaixo. Veja o exemplo -->
                <div class="box">
                    <!-- Substitua "Python" pela habilidade que você quiser -->
                    <h4>SQL</h4>
                    <div class="percent">
                        <!-- Altera a porcentagem de acordo com a sua proeficiência na habilidade acima  -->
                        <div style="width: 90%;"></div>
                    </div>
                </div>
                <div class="box">
                    <!-- Substitua "Python" pela habilidade que você quiser -->
                    <h4>java</h4>
                    <div class="percent">
                        <!-- Altera a porcentagem de acordo com a sua proeficiência na habilidade acima  -->
                        <div style="width: 80%;"></div>
                    </div>
                </div>
                <div class="box">
                    <!-- Substitua "Python" pela habilidade que você quiser -->
                    <h4>Lua</h4>
                    <div class="percent">
                        <!-- Altera a porcentagem de acordo com a sua proeficiência na habilidade acima  -->
                        <div style="width: 80%;"></div>
                    </div>
                </div>
                <!-- Se precisar remover alguma habilidade só deletar o trecho <div class="box">...</div> em que a habilidade está inserida -->
            </div>
        </div>
    </div>
</body>
</html> """


if __name__ == "__main__":
    app.run(debug=True)
