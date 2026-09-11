from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Chave secreta necessária para usar sessões no Flask
app.secret_key = 'sua_chave_secreta_super_segura'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Pega o nome digitado na tela de login e salva na "sessão"
        usuario = request.form.get('usuario')
        if usuario:
            session['usuario'] = usuario
            return redirect(url_for('painel_ticket'))
            
    return render_template('login.html')

@app.route('/ticket')
def painel_ticket():
    # Verifica se o usuário fez login; se não, joga ele de volta pra tela de login
    if 'usuario' not in session:
        return redirect(url_for('login'))
        
    usuario_atual = session['usuario']
    return render_template('index.html', usuario=usuario_atual)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)