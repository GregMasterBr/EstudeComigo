# eventex-wttd
Sistema de gerenciamento de Estudos - Projeto de aprendizagem Youtube - Dennis Ivy
https://www.youtube.com/watch?v=PtQiiknWUcI

##PASSO A PASSO
* Criar uma pasta de trabalho mkdir nome-da-pasta-de-trabalho (EstudeComigo)
* git init 
* adicionado o .gitignore e adicionando pastas que devem ser ignoradas
* Navegar até o diretório criado de trabalho para criar a váriavel de ambiente
* python -m venv .venv (o . antes do nome da variável de ambiente, indica que será um diretório oculto)
  -> ** Ativar o ambiente .wttd\Scripts\activate (Prompt) ou .venv\Scripts\Activate.ps1 (PowerShell)
* Instalar o Django (mais recente)
  ** pip  install django
* Criar o projeto
  ** COMANDO: django-admin startproject studybud . (esse ponto no final indica que para instalar o projeto django eventex no diretório atual.  (o startproject receberá o diretório de trabalho))
* Para facilitar a execução do manage.py, sugere-se, usar a variável do virtual_env e criar um alias
  ** (UNIX) alias manage='python $VIRTUAL_ENV/../manage.py'
  ** (WINDOWS): Dentro do diretório scripts criar um arquivo manage.bat -> EstudeComigo\.venv\Scripts\manage.bat
  *** E insira esse código: @python "%VIRTUAL_ENV%\..\manage.py" %*
  ***Teste se o projeto está rodando: manage runserver
* Criar uma app core ou base dentro do projeto studybud com o comando manage startapp base .
*Estrutura de Pasta do Projeto:
 ** EstudeComigo - Diretório de trabalho
  *** studybud - Diretório de projeto
  *** base - APP (subdiretório)
  *** manage.py
* Adicionar a app 'studybud.base', no INSTALLED_APPS no arquivo settings.py.
* ROTAS: Criar uma rota, acessando urls.py do eventex. Esse arquivo é a raiz de todas as rotas de nossa aplicação.
* Dentro do arquivo URLS.py do eventex, vai importar o URLs (arquivo que você vai criar do CORE)
  ** URLS do BASE -> [...] path('', views.home, name='home'),
  ** URLS do STUDYBUD ->[..] path('', include('studybud.base.urls')),  path('admin/', admin.site.urls),
]
* No APS do base -> EstudeComigo\.venv\studybud\base\apps.py
**     name = 'studybud.base'
* Criar view home dentro de studybud.base.views. A View ela retorna um template.
* Dentro de CORE, cria uma nova pasta chamada TEMPLATES e cria o o arquivo .html (Criar template index.html em studybud.base.templates.)
* Executar o projeto com o comando manage runserver.


