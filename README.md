# Projeto
Sistema de gestão desenvolvido para o terceiro setor
**********

### 1. Instruções Iniciais

Vamos usar o **Oracle Database XE 18c** local para ser nosso banco, para isso configure da seguinte forma:

```
Configuração
```
Com isso temos nosso banco local configurado. Para continuar a configuração siga os seguintes passos:

**1)** Criar um **ambiente virtual** para desenvolvimento. Nossa linguagem será **Python 3.7.4 com Django 2.2.5**.
**2)** Rode `pip install -r requirements.txt`.
**3)** Verficar se o `databases.json` está correto na pasta config.
**4)** Rode `python manage.py migrate`. Se não ocorrer erros, prossiga;
**5)** Rode `python manage.py runserver`;
