# Boas-vindas ao repositório do exercício Django Clima

<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary><br />

Neste exercício, você vai colocar em prática o que aprendeu sobre Django. Você irá construir dois modelos que serão usados para gerenciar as previsões de clima em diferentes cidades. Depois, construirá templates e renderizará informações vindas do banco de dados dentro destes templates. Por fim, você implementará o redirecionamento entre os templates criados permitindo que uma pessoa navegue entre os templates criados.

</details>
  
<details>
  <summary><strong>📝 Habilidades a serem trabalhadas</strong></summary><br />

Neste exercício, verificamos se você é capaz de:

- Construir um projeto Django.
- Utilizar do ORM do Django para mapear classes em modelos de banco de dados.
- Trabalhar com as migrações do Django.
- Elaborar e utilizar _templates_ do Django.
- Implementar _views_ que renderizam _templates_ usando contextos.
- Construir os vínculos entre _views_, _templates_ e modelos.

</details>

# Orientações

<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary><br />

1. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**

```bash
brew install mysql pkg-config
```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  
O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instalar as dependências no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  Neste exercício usaremos um bando de dados MySQL.

  <strong>MySQL</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `django_clima_database`. Depois que as tabelas estiverem implementadas você poderá usar funcionalidades já implementadas para inserir registros no banco de dados.
  
  Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:

  ```bash
  docker build -t django-clima-db .
  docker run -d -p 3306:3306 --name=django-clima-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=django_clima_database django-clima-db
  ```
  
  Esses comandos irão fazer o build da imagem e subir o container
  
  Lembre-se de que o MySQL utiliza por padrão a porta 3306. Se já houver outro serviço utilizando esta porta, considere desativá-lo ou mudar a porta no comando acima.

</details>

## Requisitos

### 1 - Crie a migrate e a model `City`

Arquivo para implementação: `weather/models.py`

> <b>🍀 Dica:</b> Os Requisitos 1 e 2 solicitarão a criação de modelos. Sempre que criar/modificar um modelo, é necessário criar as migrações para espelhar as modificações para os bancos de dados, inclusive o banco de testes contam com estas modificações. Comando para gerar a migrate a partir dos modelos criados:

```bash
python3 manage.py makemigrations
```

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie a classe `City`;
- A classe `City` deve herdar os `models` do Django;
- A classe `City` deve ter uma propriedade chamada `name`;
- A propriedade `name` deve ser um campo de caracteres com um tamanho máximo de **60 caracteres**;
- A classe `City` deve ter uma propriedade chamada `latitude`;
- A propriedade `latitude` deve ser um campo de números decimais (_float_);
- A classe `City` deve ter uma propriedade chamada `longitude`;
- A propriedade `longitude` deve ser um campo de números decimais (_float_);
- A classe `City` deve conter o método `__str__` que deve retornar a propriedade `name` da cidade criada;
- A classe `City` deve conter o método `slugify` que deve retornar a propriedade `name` da cidade criada mas todo em letras minúsculas e com traços no lugar dos espaços. Exemplo: `Belo Horizonte -> belo-horizonte`;
- A classe `City` deve sobrescrever o método `save` de sua classe herdada e fazer com que, antes que ocorra o salvamento em banco, a propriedade `name` sempre tenha a primeira letra de cada palavra em maiúsculo;

</details>

### 2 - Crie a migrate e a model `DailyWeather`

Arquivo para implementação: `weather/models.py`

```bash
python3 manage.py makemigrations
```

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie a classe `DailyWeather`;
- A classe `DailyWeather` deve herdar os `models` do Django;
- A classe `DailyWeather` deve ter uma propriedade chamada `city`;
- A propriedade `city` deve se relacionar com o modelo criado anteriormente `City`;
- A propriedade `city` deve ser única para cada uma das datas, ou seja, não pode haver duas entradas de clima para a mesma cidade e data;
- A classe `DailyWeather` deve ter uma propriedade chamada `date`;
- A propriedade `date` deve ser um campo de data;
- A classe `DailyWeather` deve ter uma propriedade chamada `min_temp`;
- A propriedade `min_temp` deve ser um campo de números decimais (_float_);
- A classe `DailyWeather` deve ter uma propriedade chamada `max_temp`;
- A propriedade `max_temp` deve ser um campo de números decimais (_float_);
- A classe `DailyWeather` deve ter uma propriedade chamada `brief_description`;
- A propriedade `brief_description` deve ser um campo de caracteres com um tamanho máximo de **20 caracteres**;
- A propriedade `brief_description` deve ser escolhida a partir de algumas opções pré-estabelecidas: `Ensolarado, Nublado, Chuvoso, Parcialmente nublado, Neve, Granizo`;
- A classe `DailyWeather` deve conter o método `__str__` que deve retornar as propriedades `date` e `brief_description` no formato `DD/MM/AAAA - {brief_description}`;

</details>

### 3 - Implementar os _template_ e _view_ para renderizar a página inicial

Arquivo para implementação: `weather/templates/home.html`, `weather/views.py`, `weather/urls.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie o arquivo de template `weather/templates/home.html`;
- Crie uma função no arquivo `weather/views.py` para renderizar o template `weather/templates/home.html`;
- No template renderizado você deve passar um contexto com todas as cidades armazenadas em banco;
- Registre a rota `""` em `weather/urls.py` para usar a função criada no arquivo `weather/views.py`;
- Dentro do template será necessário percorrer o contexto com todas as cidades e exibí-las uma a uma;

</details>

---

### 4 - Implementar os _template_ e _view_ para renderizar a página com climas

Arquivo para implementação: `weather/templates/city_weather.html`, `weather/views.py`, `weather/urls.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie o arquivo de template `weather/templates/city_weather.html`;
- Crie uma função no arquivo `weather/views.py` para renderizar o template `weather/templates/city_weather.html`;
- A função criada deve receber um parâmetro, `city`, além do `request`, que é o retorno do método `slugify` do objeto cidade;
- Dentro da função, você deve manipular o parâmetro `city` para que ele volte a ser o nome da cidade e possibilite a busca em banco através do nome;
- Dentro da função, você deve resgatar todos os climas daquela cidade;
- No template renderizado você deve passar um contexto com todas os climas da cidade armazenados em banco;
- Registre a rota `"weather/<str:city>"` em `weather/urls.py` para usar a função criada no arquivo `weather/views.py`;
- Dentro do template será necessário percorrer o contexto com todos os climas e exibí-los um a um;

</details>

### 5 - Implementar os _template_ e _view_ para renderizar a página de detalhes do clima

Arquivo para implementação: `weather/templates/weather_details.html`, `weather/views.py`, `weather/urls.py`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie o arquivo de template `weather/templates/weather_details.html`;
- Crie uma função no arquivo `weather/views.py` para renderizar o template `weather/templates/weather_details.html`;
- A função criada deve receber os parâmetro, `city` e `target`, além do `request`, que são, respectivamente, o retorno do método `slugify` do objeto cidade e a data do clima no formato `AAAA-MM-DD`;
- Dentro da função, você deve manipular o parâmetro `city` para que ele volte a ser o nome da cidade e possibilite a busca em banco através do nome;
- Dentro da função, você deve manipular o parâmetro `target` para transformá-lo em um objeto do tipo data;
- Dentro da função, você deve resgatar o clima específico daquela cidade e daquele dia;
- No template renderizado você deve passar um contexto com os dados daquele clima resgatado;
- Registre a rota `"weather/<str:city>/<str:target>"` em `weather/urls.py` para usar a função criada no arquivo `weather/views.py`;
- Dentro do template será necessário exibir as propriedades do objeto clima passado no contexto;

</details>

### 6 - Implementar os redirecionamentos dos templates

Arquivo para implementação: `weather/templates/weather_details.html`, `weather/templates/city_weather.html`, `weather/templates/home.html`

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- No arquivo `weather/templates/home.html`, para cada cidade renderizada, adicione um link de redirecionamento `<a></a>` para a rota `weather/<str:city>` onde `city` é o retorno do método `slugify` do objeto cidade;
- No arquivo `weather/templates/city_weather.html`, para cada clima renderizado, adicione um link de redirecionamento `<a></a>` para a rota `weather/<str:city>/<str:target>` onde `city` é o retorno do método `slugify` do objeto cidade e `target` é a data do clima no formato `AAAA-MM-DD`;
- No arquivo `weather/templates/city_weather.html`, adicione um link de redirecionamento `<a></a>` ao final da página para retornar à página inicial (rota `""`);
- No arquivo `weather/templates/weather_details.html`, adicione um link de redirecionamento `<a></a>` ao final da página para retornar à página da cidade (rota `"weather/<str:city>"`);

</details>
