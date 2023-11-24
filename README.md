## Lillac: Uma aplicação web destinada à busca de serviços especializados para pessoas com deficiência

O projeto propõe uma aplicação web que facilita a busca e a oferta de serviços acessíveis para pessoas com deficiência (PCDs). A aplicação segue as normas de acessibilidade da W3C e permite que os usuários se cadastrem, pesquisem e divulguem serviços acessíveis. O objetivo é promover a inclusão social e digital das PCDs e promover a acessibilidade nos serviços. A motivação do projeto surge da constatação de que PCDs representam 6,7% da população brasileira e que enfrentam dificuldades para encontrar serviços adequados às suas necessidades. Para avaliar a aplicação, foi realizado um teste de usabilidade com 14 PCDs e os resultados mostraram que a maioria dos usuários concordou que a aplicação era acessível e fácil de usar. A plataforma além de gratuita, possui código livre e está disponível no Github.

### Linguagens utilizadas
#### Front-end
<p float="left">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"
        alt=“html5” width="40" height="40"/>
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"
        alt="css3" width="40" height="40" />
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"
        alt=“javascript” width="40" height="40" />
    <img src="https://jinja.palletsprojects.com/en/3.1.x/_images/jinja-logo.png"
        alt="jinja" width="90" height="40">
</p>

#### Backend
<p float = "left">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt=“python”
    width="40" height="40" />
<img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt=“mysql”
    width="40" height="40" />
<p/>

### Artigo
Para mais informações, consulte o artigo ou resumo expandido do projeto:
- [Artigo](https://drive.google.com/drive/my-drive?hl=pt-BR) 
- [Resumo expandido](https://latinoware.org/wp-content/uploads/2023/10/236538_2.pdf) 

### Projeto hospedado
- [Projeto hospedado](lillac-production.up.railway.app/)

### Como usar
Este é um guia passo a passo sobre como configurar e executar este projeto.

#### Pré-requisitos
Antes de começar, certifique-se de ter o Python e o pip instalados em seu sistema.

#### Configuração
1. **Clone o repositório**
   Primeiro, clone este repositório para a sua máquina local usando  
`git clone`.
2. **Instale as dependências**
   Navegue até a pasta do projeto e execute o seguinte comando para instalar todas as dependências necessárias que estão listadas no arquivo "requirements.txt":  
``pip install -r requirements.txt``
3. **Crie o banco de dados**
No MySql execute o arquivo  
`scripts.sql`
4. **Execute o Main**
Abra um terminal integrado na pasta do projeto e execute o comando:  
``py main.py``  
Vá até o seu navegador e acesse o servidor local com o link:  
``127.0.0.1:5000``