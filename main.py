from model.Consulta import Consulta
from model.Paciente import *
from model.Profissional import Profissional
from model.Usuario import Usuario
from model.Prontuarios import Prontuario
from model.Receita import Receita
from model.Local import Unidade

from connection.connection import *
from connection.paciente_dao import *
from connection.profissional_dao import *
from connection.consulta_dao import *
from connection.local_dao import *
from connection.leito_dao import *
from connection.receita_dao import *
from connection.usuario_dao import *
from connection.prontuario_dao import *

from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template, Flask, redirect, url_for, session, make_response, send_file
from datetime import datetime
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, join_room, leave_room, emit

import logging
import pdfkit
import io

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)
app.secret_key = 'chave_secreta_super_segura_vidaplus'

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {'enable-local-file-access':None}

socketio = SocketIO(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'home'

@app.route("/", methods=["GET", "POST"])
def home():
    session.clear()
    if request.method == "POST":        
        if verificaLogin():
            #if current_user.isAdmin:
                #session['isAdmin'] = True
            logging.info(f"Login bem-sucedido para usuário: {current_user}")
            return redirect(url_for('index'))
        else:
            logging.warning(f"Falha de login para usuário: {login}")
            return render_template('login.html', erro="Usuário ou senha incorretos.")
        
    return render_template('login.html')

@app.route("/novoPaciente", methods=["GET", "POST"])
def novoPacienteRoute():
    if request.method == "POST":
        if cadastrarPaciente():
            return redirect(url_for('index'))
        else:
            return render_template('cadastro.html', tipo='paciente', erro='Erro ao cadastrar Paciente', novoUser=True)
    return render_template('cadastro.html', tipo='paciente', novoUser = True)

@login_manager.user_loader
def load_user(user_id):
    usuario = buscarUsuarioPorId(user_id)
    if usuario:
        return Usuario(id=usuario[0], login=usuario[1], senha=usuario[2], email=usuario[4], tipoUsuario=usuario[5], isAdmin=usuario[3], idPaciente=usuario[6], idProfissional=usuario[7])
    return None

@app.route("/index", methods=["GET"])
@login_required
def index():
    leito = buscarLeitos("")
    pacientes = buscarPacientes("")
    locais = buscarLocais("")
    if current_user.tipoUsuario == 'paciente':
        consultas = buscarConsulta(current_user.idPaciente)
        return render_template('index.html', consultas=consultas)
    if current_user.tipoUsuario == 'profissional':
        consultas = buscarConsultaProfissionalData(current_user.idProfissional)
        return render_template('index.html', leitos=leito, consultas=consultas, locais=locais)
    return render_template('index.html', leitos=leito, pacientes=pacientes, locais=locais)

@app.route("/cadastrar_paciente", methods=["GET", "POST"])
@login_required
def cadastrarPacienteRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        if cadastrarPaciente():
            return redirect(url_for('index'))
        else:
            return render_template('cadastro.html', tipo='paciente', usuario=usuario, erro='Erro ao cadastrar Paciente')
    return render_template('cadastro.html', tipo='paciente', usuario=usuario)

@app.route("/cadastrar_profissional", methods=["GET","POST"])
@login_required
def cadastrarProfissionalRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        if cadastrarProfissional():
            return redirect(url_for('index'))
        else:
            return render_template('cadastro.html', tipo='profissional', usuario=usuario, erro='Erro ao cadastrar Profissional')
    return render_template('cadastro.html', tipo='profissional', usuario=usuario)

@app.route("/cadastrar_usuário", methods=["GET","POST"])
@login_required
def cadastrarUsuarioRoute(): #Não esta sendo utilizado
    if request.method == "POST":
        cadastrarUsuario()
    return render_template('cadastro.html', tipo='usuario')

@app.route("/marcar_consulta", methods=["GET","POST"])
@login_required
def marcarConsultaRoute():
    usuario = session.get('usuario')
    pacientes = buscarPacientes("")
    profissionais = buscarProfissionais("")
    locais = buscarLocais("")
    if request.method == "POST":
        if cadastrarConsulta():
            return render_template('marcarConsulta.html', sucesso="Consulta marcada com sucesso!", pacientes=pacientes, profissionais=profissionais, usuario=usuario)
        else:
            return render_template('marcarConsulta.html', erro="Horário indisponível para o profissional selecionado.", pacientes=pacientes, profissionais=profissionais, usuario=usuario, locais=locais)
    return render_template('marcarConsulta.html', pacientes=pacientes, profissionais=profissionais, usuario=usuario, locais=locais)

@app.route("/marcar_consulta_paciente/<id>", methods=["GET","POST"])
@login_required
def marcarConsultaPacienteRoute(id):
    profissionais = buscarProfissionais("")
    locais = buscarLocais("")
    if request.method == "POST":
        if cadastrarConsultaPaciente(int(id)):
            return redirect(url_for('index'))
        else:
            return render_template('marcarConsulta.html', erro="Horário indisponível para o profissional selecionado.", profissionais=profissionais, locais=locais)
    return render_template('marcarConsulta.html', profissionais=profissionais, locais=locais)

@app.route("/marcar_consulta_profissional/<idProf>", methods=["GET","POST"])
@login_required
def marcarConsultaProfissionalRoute(idProf):
    paciente = buscarPacientes("")
    locais = buscarLocais("")
    if request.method == "POST":
        if cadastrarConsultaProfissional(int(idProf)):
            return redirect(url_for('index'))
        else:
            return render_template('marcarConsulta.html', erro="Horário indisponível para o profissional selecionado.", pacientes=paciente,locais=locais)
    return render_template('marcarConsulta.html', pacientes=paciente,locais=locais)

@app.route("/buscar_paciente", methods=["GET","POST"])
@login_required
def buscarPacienteRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        nome = request.form.get("nome")
        paciente = buscarPacientes(nome)
        logging.info(f"Resultado da busca por paciente: {paciente}")
        if len(paciente) == 0:
            logging.warning(f"Paciente não encontrado na busca: {nome}")
            return render_template('buscas.html', tipo='paciente', erro="Paciente não encontrado.", usuario=usuario)
        return render_template('buscaResultado.html', tipo='paciente', pacientes=paciente, usuario=usuario)
    return render_template('buscas.html', tipo='paciente', usuario=usuario)

@app.route("/selecionar_paciente/<int:id>", methods=["GET"])
@login_required
def selecionarPacienteRoute(id):
    usuario = session.get('usuario')
    paciente = buscarPacientePorId(id)
    return render_template('resultado.html', tipo='paciente', paciente=paciente, usuario=usuario)

@app.route("/buscar_profissional", methods=["GET","POST"])
@login_required
def buscarProfissionalRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        nome = request.form.get("nome")
        profissional = buscarProfissionais(nome)
        logging.info(f"Resultado da busca por profissional: {profissional}")
        if len(profissional) == 0:
            logging.warning(f"Profissional não encontrado na busca: {nome}")
            return render_template('buscas.html', tipo='profissional', erro="Profissional não encontrado.", usuario=usuario)
        return render_template('buscaResultado.html', tipo='profissional', profissionais=profissional, usuario=usuario)
    return render_template('buscas.html', tipo='profissional', usuario=usuario)

@app.route("/selecionar_profissional/<int:id>", methods=["GET"])
@login_required
def selecionarProfissionalRoute(id):
    usuario = session.get('usuario')
    profissional = buscarProfissionalPorId(id)
    return render_template('resultado.html', tipo='profissional', profissional=profissional, usuario=usuario)

@app.route("/cadastrar_local", methods=["GET","POST"])
@login_required
def cadastrarLocalRoute():
    usuario = session.get('usuario')
    if request.method == "POST":
        cadastrarLocal()
    return render_template('cadastro.html', tipo='unidade', usuario=usuario)

@app.route("/cadastrar_leito", methods=["GET","POST"])
@login_required
def cadastrarLeitoRoute():
    usuario = session.get('usuario')
    locais = buscarLocais("")
    if request.method == "POST":
        cadastrarLeito()
    return render_template('cadastro.html', tipo='leito', usuario=usuario, locais=locais)

@app.route("/consultas_profissional", methods=["GET", "POST"])
@login_required
def consultasProfissionalRoute(): #ajeitar para pegar de acordo com o usuario
    profissionais = buscarProfissionais("")
    consultas = []
    data = request.form.get("data")
    if request.method == "POST":
        if current_user.isAdmin == 1:
            profissional_id = request.form.get("profissional")

            if data != '':
                consultas = buscarConsultaProfissionalData(profissional_id, data)

            else:
                consultas = buscarConsultaProfissionalData(profissional_id)
        else:
            if data != '':
                consultas = buscarConsultaProfissionalData(current_user.idProfissional, data)

            else:
                consultas = buscarConsultaProfissionalData(current_user.idProfissional)
        return render_template('verificarConsultas.html', profissionais=profissionais, consultas=consultas)
    return render_template('verificarConsultas.html', profissionais=profissionais, consultas=consultas)

@app.route("/gerar_receita/<int:consulta_id>", methods=["GET", "POST"]) #fazer isso aqui funcionar
@login_required
def gerarReceitaRoute(consulta_id):
    usuario = session.get('usuario')
    c = buscarConsultaPorId(consulta_id)
    consulta = Consulta(id_consulta=c.id_consulta,paciente=c.paciente, medico=c.medico, data_hora=c.data_hora, motivo=c.motivo, observacoes=c.observacoes)
    paciente = buscarPacientePorId(consulta.paciente)
    prontuario = verificaProntuario(paciente.id)
    if request.method == "POST":
        if prontuario == "Não tem":
            prontuario = Prontuario(consulta.paciente, request.form.get('peso'), request.form.get('altura'), request.form.get('observacoes'))
            registrarProntuario(prontuario)
            registraAlergias(consulta.paciente,request.form.get('penicilina'),request.form.get('amoxilina'),request.form.get('ibuprofeno'),request.form.get('dipirona'),request.form.get('extra1'),request.form.get('extra2'), request.form.get('extra3'))
            registraCondicoes(consulta.paciente,request.form.get('pressao_alta'),request.form.get('diabetes'),request.form.get('asma'),request.form.get('eplepsia'), request.form.get('hiv'),request.form.get('gastrite'),request.form.get('condicao_extra1'),request.form.get('condicao_extra2'),request.form.get('condicao_extra3'))
        cadastrarReceita(consulta)
        return render_template('consulta.html', sucesso="Receita cadastrada com sucesso!", consulta=consulta, paciente=paciente, usuario=usuario, prontuario=prontuario)
    return render_template('consulta.html', consulta=consulta, paciente=paciente, usuario=usuario, prontuario=prontuario)

@app.route("/verificar_leitos" , methods=["GET", "POST"])
@login_required
def verificarLeitosRoute():
    usuario = session.get('usuario')
    leitos = buscarLeitos("")
    locais = buscarLocais("")

    if request.method == "POST":
        unidadeId = request.form.get("unidade")
        leitos = buscarLeitoPorUnidade(unidadeId)
        if len(leitos) == 0:
            return render_template('leitos.html', erro="Nenhum leito encontrado.", usuario=usuario, locais=locais)
        return render_template('leitos.html', leitos=leitos, usuario=usuario, locais=locais)
    return render_template('leitos.html', usuario=usuario, leitos=leitos, locais=locais)

@app.route("/editar_paciente/<int:id>", methods=["GET", "POST"])
@login_required
def editarPacienteRoute(id):
    paciente = buscarPacientePorId(id)
    if request.method == "POST":
        nome = request.form.get("nome")
        dataNasc = request.form.get("data_nascimento")
        endereco = request.form.get("endereco")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        paciente.nome = nome
        paciente.dataNasc = dataNasc
        paciente.endereco = endereco
        paciente.telefone = telefone
        paciente.cpf = cpf
        paciente.email = email
        try:
            alterarPaciente(paciente)
            logging.info(f"Usuário {session.get('usuario')} editou paciente {nome}")
            return redirect(url_for('selecionarPacienteRoute', id=id))
        except Exception as e:
            logging.error(f"Erro ao editar paciente: {e}")
            return render_template('editar.html', tipo='paciente', paciente=paciente, erro='Erro ao editar Paciente')
    return render_template('editar.html', tipo='paciente', paciente=paciente)

@app.route("/historico_consultas/<id>", methods=["GET"])
@login_required
def historicoConsultasRoute(id):
    consultas = buscarConsultaAntigas(id)
    return render_template('consultas.html', consultas=consultas)

@app.route("/receita/<id>", methods=["GET"])
@login_required
def gerar_pdf_receita(id):
    receita = buscarReceita(id)
    html = render_template('emitirReceita.html', receita = receita)
    pdf = pdfkit.from_string(html, False, configuration=config, options=options)  # bytes

    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'receita_{id}.pdf' 
    )


@app.route("/receitas/<id>", methods=["GET"])
@login_required
def receitasRoute(id):
    receitas = acessarReceitas(id)
    return render_template('receitas.html', receitas=receitas)

@app.route("/editar_profissional/<int:id>", methods=["GET", "POST"])
@login_required
def editarProfissionalRoute(id):
    profissional = buscarProfissionalPorId(id)
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        cargo = request.form.get("cargo")
        crm = request.form.get("crm")
        dataNasc = request.form.get("data_nascimento")
        cpf = request.form.get("cpf")
        profissional['nome'] = nome
        profissional['email'] = email
        profissional['telefone'] = telefone
        profissional['cargo'] = cargo
        profissional['crm'] = crm
        profissional['dataNasc'] = dataNasc
        profissional['cpf'] = cpf
        p = Profissional(nome,cargo,email,telefone,crm,dataNasc,cpf,profissional['id'])
        try:
            alterarProfissional(p)
            logging.info(f"Usuário {session.get('usuario')} editou profissional {nome}")
            return redirect(url_for('selecionarProfissionalRoute', id=id))
        except Exception as e:
            logging.error(f"Erro ao editar profissional: {e}")
            return render_template('editar.html', tipo='profissional', profissional=profissional, erro='Erro ao editar Profissional')
    return render_template('editar.html', tipo='profissional', profissional=profissional)

@app.route("/logout")
@login_required
def logout():
    login = current_user.login
    logout_user()
    session.clear()
    logging.info(f"Logout realizado com sucesso para {login}")
    return redirect(url_for('home'))

@app.route("/videochamadas/<chave>", methods=["POST", "GET"]) 
@login_required
def videochamadasRoute(chave):

    consulta = buscarConsultaPorChave(chave)
    prontuario = verificaProntuario(consulta.paciente)

    if current_user.tipoUsuario == 'profissional':
        
        if request.method == "POST":
            if prontuario == "Não tem":
                prontuario = Prontuario(consulta.paciente, request.form.get('peso'), request.form.get('altura'), request.form.get('observacoes'))
                registrarProntuario(prontuario)
                registraAlergias(consulta.paciente,request.form.get('penicilina'),request.form.get('amoxilina'),request.form.get('ibuprofeno'),request.form.get('dipirona'),request.form.get('extra1'),request.form.get('extra2'), request.form.get('extra3'))
                registraCondicoes(consulta.paciente,request.form.get('pressao_alta'),request.form.get('diabetes'),request.form.get('asma'),request.form.get('eplepsia'), request.form.get('hiv'),request.form.get('gastrite'),request.form.get('condicao_extra1'),request.form.get('condicao_extra2'),request.form.get('condicao_extra3'))
            cadastrarReceita(consulta)
    room = f"consulta{chave}"
    return render_template('videoConferencia.html', user=current_user.login, room=room, prontuario=prontuario)

@socketio.on("join")
def handle_join(data):
    room = data["room"]
    user = data["user"]
    join_room(room)
    emit("user_joined", {"user": user}, room=room, include_self=False)

@socketio.on("signal")
def handle_signal(data):
    room = data["room"]
    # repassa a mensagem para todos da sala (menos o emissor)
    emit("signal", data, room=room, include_self=False)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    user = data['user']
    leave_room(room)
    emit('user_left', {'user': user}, room=room, include_self=False)

@socketio.on("disconnect")
def handle_disconnect():
    """
    Quando alguém sai (opcional)
    
    """


@app.route("/verificarProntuario/paciente<id>", methods=["GET"])
@login_required
def verificarProntuarioPacienteRoute(id):
    paciente = buscarPacientePorId(id)
    consultas = buscarConsultaAntigas(id) 
    prontuario = verificaProntuario(id)
    alergias = verificaAlergias(id)
    condicoes = verificaCondicoes(id)
    return render_template('prontuarios.html', consultas = consultas, prontuario = prontuario, alergias=alergias, condicoes = condicoes, paciente=paciente)

@app.route("/gerenciarLeito/<id>" , methods=["POST", "GET"])
@login_required
def gerenciarLeitoRoute(id):
    leito = buscarLeitoPorId(id)
    pacientes = buscarPacientes("")
    leitos = buscarLeitos("")
    local = buscarLocais("")
    idsLeitos = {l['idPaciente'] for l in leitos if l.get('idPaciente')}
    pacientes_disponiveis = [p for p in pacientes if p['id'] not in idsLeitos]

    if request.method == "POST":

        ocuparLeito(leito)
        return redirect(url_for('verificarLeitoRoute', id=id))
    return render_template('leito.html', leito=leito, pacientes=pacientes_disponiveis, local=local)

@app.route("/leito<id>", methods=["POST", "GET"])
@login_required
def verificarLeitoRoute(id):
    leito = buscarLeitoPorId(id)
    paciente = buscarPacientePorId(leito['idPaciente'])
    local = buscarLocais("")

    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "atualizar":
            atualizarLeito(leito)
            return redirect(url_for('verificarLeitoRoute', id=id))
        elif acao == "desocupar":
            desocuparLeito(leito)
            return redirect(url_for('index'))
    return render_template('leito.html', leito=leito, paciente=paciente, local=local)

@app.route("/relatorio/<id>/" , methods=["POST", "GET"])
@login_required
def relatoriosRoute(id):
    pacientes = buscarPacientes("")
    suprimentos = suprimentosLocal(id)
    if suprimentos == "Não tem":
        registrarSuprimentosLocal(id)
        suprimentos = suprimentosLocal(id)
    leitos = buscarLeitoPorUnidade(id)
    localT = buscarLocalId(id)
    local = localT[0]

    if request.method=="POST":
        soro = request.form.get('quantidade_soro')
        gaze = request.form.get('quantidade_gaze')
        alcool = request.form.get('quantidade_alcool')
        medicamento = request.form.get('quantidade_medicamento')
        atualizarSuprimentos(id, soro, gaze, alcool, medicamento, suprimentos)
        return redirect(url_for('relatoriosRoute', id=id))
    return render_template('relatorios.html', pacientes=pacientes, suprimentos=suprimentos, leitos=leitos, local=local)

@app.route('/relatorio/<idPaciente>/pdf')
def gerar_pdf(idPaciente):
    paciente = buscarPacientePorId(idPaciente)
    consultas = buscarConsultaAntigas(idPaciente) # trocar para, buscar finalizadas
    prontuario = verificaProntuario(idPaciente)
    alergias = verificaAlergias(idPaciente)
    condicoes = verificaCondicoes(idPaciente)
    html = render_template('prontuarios.html', consultas = consultas, prontuario = prontuario, alergias=alergias, condicoes = condicoes, paciente=paciente)
    pdf = pdfkit.from_string(html, False, configuration=config, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=relatorio.pdf'
    return response

def cadastrarPaciente():
    #pega os dados do paciente do formulário na route  
    nome = request.form.get("nome")
    dataNasc = request.form.get("data_nascimento")
    endereco = request.form.get("endereco")
    telefone = request.form.get("telefone")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    #cria o objeto paciente
    paciente = Paciente(nome=nome, dataNasc=dataNasc, endereco=endereco, cpf=cpf, telefone=telefone, email=email)
    #cadastra o paciente no banco de dados
    try:
        registrarPaciente(paciente)
        logging.info(f"Usuário {session.get('usuario')} cadastrou paciente {nome}")
        p = buscarPacienteCPF(paciente.cpf)
        nomeUser = f'{nome.split()[0].lower()}.{nome.split()[-1].lower()}'
        senha = generate_password_hash(cpf)
        registrarUsuarioPaciente(nomeUser, senha, email, p)
        return True
    except Exception as e:
        logging.error(f"Erro ao cadastrar paciente: {e}")
        return False

def cadastrarProfissional():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    cargo = request.form.get("cargo")
    crm = request.form.get("registro")
    dataNasc = request.form.get("data_nascimento")
    cpf = request.form.get("cpf")
    #cria o objeto profissional
    profissional = Profissional(nome=nome, email=email, dataNasc=dataNasc, crm=crm,  telefone=telefone, cargo=cargo, cpf=cpf)
    try:
        registrarProfissional(profissional)
        nomeUser = f'{nome.split()[0].lower()}.{nome.split()[-1].lower()}'
        logging.info(f"Usuário {session.get('usuario')} cadastrou profissional {profissional.nome}")
        p = buscarProfissionalCPF(profissional.cpf)
        senha = generate_password_hash(cpf)
        registrarUsuarioProfissional(nomeUser, senha, email,p)
        return True
    except Exception as e:
        logging.error(f"Erro ao cadastrar profissional: {e}")
        return False

def cadastrarConsulta():
    paciente = request.form.get("paciente")
    profissional = request.form.get("profissional")
    data = request.form.get("data")
    hora = request.form.get("hora")
    motivo = request.form.get("motivo")
    observacoes = request.form.get("observacoes") #verificar se será teleconsulta
    local = request.form.get("local")
    if verificaDisponibilidade(profissional, f'{data} {hora}'):
        if local == 'online':
            try:
                registrarConsultaOnline(paciente, profissional, data, hora, motivo, observacoes)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {paciente} com profissional {profissional} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
        else:
            try:
                registrarConsulta(paciente, profissional, data, hora, motivo, observacoes, local)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {paciente} com profissional {profissional} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
    else:
        logging.warning("Horário indisponível para o profissional selecionado.")
        return False
    
def cadastrarConsultaPaciente(id):
    profissional = request.form.get("profissional")
    data = request.form.get("data")
    hora = request.form.get("hora")
    motivo = request.form.get("motivo")
    observacoes = request.form.get("observacoes") #verificar se será teleconsulta
    local = request.form.get("local")

    if verificaDisponibilidade(profissional, f'{data} {hora}'):
        if local == 'online':
            try:
                registrarConsultaOnline(id, profissional, data, hora, motivo, observacoes)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {id} com profissional {profissional} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
        else:
            try:
                registrarConsulta(id, profissional, data, hora, motivo, observacoes, local)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {id} com profissional {profissional} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
    else:
        logging.warning("Horário indisponível para o profissional selecionado.")
        return False
    
def cadastrarConsultaProfissional(id):

    paciente = request.form.get("paciente")
    data = request.form.get("data")
    hora = request.form.get("hora")
    motivo = request.form.get("motivo")
    observacoes = request.form.get("observacoes") #verificar se será teleconsulta
    local = request.form.get("local")
    if verificaDisponibilidade(id, f'{data} {hora}'):
        if local == 'online':
            try:
                registrarConsultaOnline(paciente, id, data, hora, motivo, observacoes)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {paciente} com profissional {id} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
        else:
            try:
                registrarConsulta(paciente, id, data, hora, motivo, observacoes, local)
                logging.info(f"Usuário {session.get('usuario')} marcou consulta para paciente {paciente} com profissional {id} em {data} {hora}")
            except Exception as e:
                logging.error(f"Erro ao marcar consulta: {e}")
            return True
    else:
        logging.warning("Horário indisponível para o profissional selecionado.")
        return False

def cadastrarLocal():
    nome = request.form.get("nome")
    endereco = request.form.get("endereco")
    tipo = request.form.get("tipo")
    try:
        registrarLocal(local = Unidade(nome, endereco, tipo))
        logging.info(f"Usuário {current_user.login} cadastrou unidade {nome}")
    except Exception as e:
        logging.error(f"Erro ao cadastrar unidade: {e}")

def cadastrarLeito():
    numero = request.form.get("numero")
    idUnidade = request.form.get("idUnidade")
    tipo = request.form.get("tipo")
    try:
        registrarLeito(leito = Leito(numero=numero, tipo=tipo, idUnidade=idUnidade))
        logging.info(f"Usuário {session.get('usuario')} cadastrou leito {numero}")
    except Exception as e:
        logging.error(f"Erro ao cadastrar leito: {e}")

def cadastrarUsuario(): 
    user = request.form.get("usuario")
    s = request.form.get("senha")
    email = request.form.get("email")
    senha = generate_password_hash(s)
    try:
        registrarUsuario(user, senha, email)
        logging.info(f"Usuário {user} cadastrado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao cadastrar usuário: {e}")

def cadastrarReceitaVideoChamada(consulta):
    try:
        diagnostico = request.form.get("diagnostico")
        receitas = request.form.get("receita")
        receita= Receita(consulta.id_consulta, receitas, datetime.now().strftime("%Y-%m-%d"), consulta.paciente)
        registrarDiagnostico(consulta.id_consulta, diagnostico)
        registrarReceita(receita)
        logging.info(f"Receita para consulta {consulta.id_consulta} cadastrada com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao cadastrar receita: {e}")

def cadastrarReceita(consulta : Consulta):
    try:
        diagnostico = request.form.get("diagnostico")
        receitas = request.form.get("receita")
        receita= Receita(consulta.id_consulta, receitas, datetime.now().strftime("%Y-%m-%d"), consulta.paciente)
        registrarDiagnostico(consulta.id_consulta, diagnostico)
        registrarReceita(receita)
        alterarStatus(consulta.id_consulta)
        logging.info(f"Receita para consulta {consulta.id_consulta} cadastrada com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao cadastrar receita: {e}")

def ocuparLeito(leito):
    colocarPaciente(leito['id'], request.form.get('paciente'))
    leitoDisponivel(leito['id'])

def atualizarLeito(leito):
    obs = leito['observacoes']
    if obs == None:
        obs = ''
    obs += ', '+ request.form.get('observacoes')
    atualizarObs(leito['id'], obs)

def desocuparLeito(leito):
    removerPaciente(leito['id'])
    leitoIndisponivel(leito['id'])
    apagaObs(leito['id'])

def cadastrarProntuario(consulta: Consulta, paciente: Paciente):
    novoProntuarioConsulta = Prontuario(idPaciente=paciente.id, idConsulta=consulta.id_consulta, peso=request.form.get("peso"), altura=request.form.get("altura"), observacoes=request.form.get("observacoes"))
    try:
        registrarProntuario(novoProntuarioConsulta)
        logging.info(f"Prontuário para paciente {paciente.id} e consulta {consulta.id_consulta} cadastrado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao cadastrar prontuário: {e}")

def atualizarSuprimentos(id, soro, gaze, alcool, medicamento, suprimentos):

    soro = suprimentos['soro'] + int(soro)
    gaze = suprimentos['gaze'] + int(gaze)
    alcool = suprimentos['alcool'] + int(alcool)
    medicamento = suprimentos['medicamento'] + int(medicamento)
    atualizarSuprimentosLocal(id, soro, gaze, alcool, medicamento)

def verificaLogin():
    try:
        usuario = login(usuario = request.form.get("login"))
        if check_password_hash(usuario.senha,request.form.get('senha')):
            login_user(usuario)
            session['usuario'] = {
                'id': usuario.id,
                'nome': usuario.login,
                'isAdmin': usuario.isAdmin,
                'tipoUsuario': usuario.tipoUsuario,
                'email': usuario.email
            }
            logging.info(f'Login realizado com sucesso para {request.form.get('login')}')
            return True
    except Exception as e:
        logging.error(f"Erro ao realisar login para {request.form.get('login')}: {e}")
        return False