from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from app import db
from app.models import Fechamento
from datetime import datetime
import pdfkit
import io

main = Blueprint('main', __name__)

@main.route('/')
def index():
    fechamentos = Fechamento.query.order_by(Fechamento.criado_em.desc()).all()
    return render_template('index.html', fechamentos=fechamentos)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        f = Fechamento(
            cliente=request.form['cliente'],
            data=datetime.strptime(request.form['data'], '%Y-%m-%d'),
            quantidade=float(request.form.get('quantidade', 0)),
            cor=request.form.get('cor', ''),
            descricao=request.form['descricao'],
            valor_unitario=float(request.form.get('valor_unitario', 0)),
            desconto=float(request.form.get('desconto', 0))
        )
        db.session.add(f)
        db.session.commit()
        flash('Fechamento adicionado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add.html')

@main.route('/edit/<int:fechamento_id>', methods=['GET', 'POST'])
def edit(fechamento_id):
    f = Fechamento.query.get_or_404(fechamento_id)
    if request.method == 'POST':
        f.cliente = request.form['cliente']
        f.data = datetime.strptime(request.form['data'], '%Y-%m-%d')
        f.quantidade = float(request.form.get('quantidade', 0))
        f.cor = request.form.get('cor', '')
        f.descricao = request.form['descricao']
        f.valor_unitario = float(request.form.get('valor_unitario', 0))
        f.desconto = float(request.form.get('desconto', 0))
        db.session.commit()
        flash('Fechamento atualizado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit.html', f=f)

@main.route('/delete/<int:fechamento_id>', methods=['POST'])
def delete(fechamento_id):
    f = Fechamento.query.get_or_404(fechamento_id)
    db.session.delete(f)
    db.session.commit()
    flash('Fechamento excluído com sucesso!', 'success')
    return redirect(url_for('main.index'))

@main.route('/pdf/<int:fechamento_id>')
def gerar_pdf(fechamento_id):
    f = Fechamento.query.get_or_404(fechamento_id)
    rendered = render_template('pdf_template.html', f=f)
    options = {
        'enable-local-file-access': '',
        'page-size': 'A4',
        'encoding': 'UTF-8'
    }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(rendered, False, options=options, configuration=config)

    return send_file(
        io.BytesIO(pdf),
        download_name=f"fechamento_{f.id}.pdf",
        as_attachment=True,
        mimetype='application/pdf'
    )
