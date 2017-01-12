from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from my_form import Client, Modify1, Modify2, Modify3
from expert_system import *

global blood_result

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

@app.route('/expert')
def expert():
    form1 = Modify1()
    form2 = Modify2()
    form3 = Modify3()
    return render_template('expert.html', form1 = form1, form2 = form2, form3 = form3)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Client()
    global blood_result
    blood_result = {'normal':False}
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
        blood_result = expert_system(session)
        #return redirect(url_for('index'))
        if blood_result['normal'] == True:
            return render_template('normal.html')

        else:
            pass

    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug = True)
    #app.run()
