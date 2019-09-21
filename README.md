# Projeto
Sistema de gestão desenvolvido para o terceiro setor
**********

### 1. Instruções Iniciais

Vamos usar o **Oracle Database XE 18c** local para ser nosso banco, para isso configure da seguinte forma:

```
Senha: 'root'
```
A unica configuração necessária durante a instalação do Oracle XE é a senha, usaremos a senha 'root' como padrão para o ambiente de desensolvimento.
Com isso temos nosso banco local configurado. Para continuar a preparação do ambiente de desenvolvimento siga os seguintes passos:

- **1)** Criar um **ambiente virtual** para desenvolvimento. Nossa linguagem será **Python 3.7.4 com Django 2.2.5**.
- **2)** Rode `pip install -r requirements.txt`.
- **3)** Verficar se o `databases.json` está correto na pasta config.
- **4)** Rode `python manage.py migrate`. Se não ocorrer erros, prossiga;
- **5)** Rode `python manage.py runserver`;

### 2. Arquitetura

**Nível 0 - Core**
* Contém os arquivos de configuração do projeto (settings, urls, wsgi)
* Contém as bibliotecas de JavaScript 
* Contém as definições de css
* Contém arquivos base de telas, forms e listas
* Contém widgets

**Nível 1 - Apps**
* Contém um app para cada módulo do sistema

Os apps(módulos) possuem pastas static e template (para telas de uso específico)

**Nível 2 - Subapps**
* Contém os subapps de cada projeto do nível 1

### 3. Menu de Navegação e Views

Na pasta templates do core temos o `base.html`, trata-se da master page do sistema. Praticamente todos os templates irão herdar (direta ou indiretamente) deste arquivo.

Para incluir o `base.html` em suas páginas, basta adicionar a linha de código `{% extends 'base.html' %}` no inicio do arquivo html.

### 4. Models

Em um mesmo app (nível 1) não podem existir modelos com nome duplicado. Todos os models precisam ter o atributo `app_label = '<nome_do_app>'` em sua `class Meta`.

### 5. Grupos e Permissões

#### Grupos
Os grupos específicos para cada App devem ser nomeados da seguinte forma `<nome_do_app>.<nome_do_grupo>`. 
Ex: `animals.admin`.

#### Permissões - Apps

As permissões devem ser referenciadas da seguinte forma: `<nome_do_app>.<nome_da_permissão>`.

Obs: não podem existir permissões com nome duplicado no mesmo app (nível 1)

### 6. Referências a templates e url's

As referências a um template devem ser feitas com o caminho absoluto. Se o template estiver no core basta utilizar o seu nome.

ex1: `template_name = "animals/register/animal_list.html"`
ex2: `{% extends "base.html" %}` (neste caso base está na pasta templates do core)

A estrutura de templates dentro dos apps deve ser:

nível1: `templates/<nome_do_app>`
nível2: `templates/<nome_do_app>/<nome_do_subapp>`

### 7. JavaScript e Css

As bibliotecas e definições de javascript e css que são de utilidade geral estão na pasta static raiz.

Para utilização de featutes específicas, deve-se implementar no nível da folha os blocos `{% block css %}` e `{% block js %}`. 

### 8. Tutorial de Criação de Novo App

- **1** - Dentro da pasta raiz do projeto, execute o comando: `./manage.py startapp [nome_do_app]`


- **2** - No arquivo `core/settings.py`, adicione na variável INSTALLED_APPS:

	`'[nome_do_app]',`
  
	`'[nome_do_app].[nome_do_subapp]',`
  
  
