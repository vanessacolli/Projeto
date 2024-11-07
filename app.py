# Importa as dependências do aplicativo
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# Cria um aplicativo Flask chamado "app"
app = Flask(__name__)

# Configurações de acesso ao MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudtrecos'

# Setup da conexão com MySQL
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = 'utf8mb4'

# Variável de conexão com o MySQL
mysql = MySQL(app)


@app.before_request
def start():

    # Setup do MySQL para corrigir acentuação
    cur = mysql.connection.cursor()
    cur.execute("SET NAMES utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    cur.execute("SET character_set_client=utf8mb4")
    cur.execute("SET character_set_results=utf8mb4")

    # Setup do MySQL para dias da semana e meses em português
    cur.execute("SET lc_time_names = 'pt_BR'")


# Cria um usuário "fake" para testes
# No futuro, isso virá de um cookie
usuario = {
    'nome': 'Joca da Silva',
    'id': '1'
}
# Extrai apenas o primeiro nome do usuário
usuario['pnome'] = usuario['nome'].split()[0]


@app.route("/")  # Rota raiz, equivalente a página inicial do site (index)
def index():  # Função executada ao acessar a rota raiz

    # Um SQL de teste para exibir todos os 'trecos' do usuário conectado
    sql = '''
        SELECT * FROM treco
        WHERE t_usuario = '1' 
            AND t_status = 'on';
    '''
    cur = mysql.connection.cursor()
    cur.execute(sql,)
    trecos = cur.fetchall()
    cur.close()

    # Teste de mesa para verificar o retorno dos dados do banco de dados
    print('\n\n\n', trecos, '\n\n\n')

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': usuario
    }

    # Renderiza o template HTML, passando valores (pagina) para ele
    return render_template('index.html', **pagina)


# Rota para a página de cadastro de novo treco
@app.route('/novo', methods=['GET', 'POST'])
def novo():  # Função executada para cadastrar novo treco

    # Se o formulário foi enviado
    if request.method == 'POST':

        # Obtém os dados preenchidos na forma de dicionário
        form = dict(request.form)

        # Teste de mesa (comente depois dos testes)
        # Verifica se os dados do formulário chegaram ao back-end
        print('\n\n\n', form, '\n\n\n')

        # Em breve: grava os dados no banco de dados e segue o fluxo

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': usuario
    }

    # Renderiza o template HTML, passaod valores para ele
    return render_template('novo.html', **pagina)


@app.route('/login', methods=['GET', 'POST'])  # Rota para login de usuário
def login():

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Login'
    }

    return render_template('login.html', **pagina)


@app.route('/cadastro', methods=['GET', 'POST'])  # Cadastro de usuário
def cadastro():

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Cadastre-se',
    }

    return render_template('cadastro.html', **pagina)


@app.route('/novasenha', methods=['GET', 'POST'])  # Pedido de senha de usuário
def novasenha():

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Nova Senha'
    }

    return render_template('novasenha.html', **pagina)


@app.route('/perfil')
def perfil():

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': usuario
    }

    # Renderiza o template HTML, passaod valores para ele
    return render_template('perfil.html', **pagina)


# Executa o servidor HTTP se estiver no modo de desenvolvimento
# Remova / comente essas linhas no modo de produção
if __name__ == '__main__':
    app.run(debug=True)
