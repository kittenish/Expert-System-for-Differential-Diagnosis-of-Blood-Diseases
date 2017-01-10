from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from my_form import Client
from expert_system import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Client()
    if form.validate_on_submit():
        session['gender'] = form.gender.data
        session['age'] = form.age.data
        session['rbc'] = form.rbc.data
        session['hb'] = form.hb.data
        session['hct'] = form.hct.data
        session['mcv'] = form.mcv.data
        session['mch'] = form.mch.data
        session['mchc'] = form.mchc.data
        session['rdw'] = form.rdw.data
        session['wbc'] = form.wbc.data
        session['neu'] = form.neu.data
        session['lym'] = form.lym.data
        session['mon'] = form.mon.data
        session['eos'] = form.eos.data
        session['bas'] = form.bas.data
        session['plt'] = form.plt.data
        session['mpv'] = form.mpv.data
        session['pct'] = form.pct.data

        #print session
        result = expert_system(session)
        print result
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug = True)
