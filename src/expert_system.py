import json

class Patient(object):

    def __init__(self, session):

        self.gender = session['gender']
        self.age = int(session['age'])
        self.rbc = int(session['rbc'])
        self.hb = int(session['hb'])
        self.hct = int(session['hct'])
        self.mcv = int(session['mcv'])
        self.mch = int(session['mch'])
        self.mchc = int(session['mchc'])
        self.rdw = int(session['rdw'])
        self.wbc = int(session['wbc'])
        self.neu = int(session['neu'])
        self.lym = int(session['lym'])
        self.mon = int(session['mon'])
        self.eos = int(session['eos'])
        self.bas = int(session['bas'])
        self.plt = int(session['plt'])
        self.mpv = int(session['mpv'])
        self.pct = int(session['pct'])

        if self.age > 15:
            self.age = 'adult'
        elif self.age < 0.5:
            self.age = 'newborn'
        elif self.age < 2:
            self.age = 'baby'
        else:
            self.age = 'child'

    def normal():
        f = open('../data/rules_normal.txt','r')
        rules = f.read()
        rules = json.loads(rules)
        gender = self.gender
        age = self.age
        rbc = self.rbc
        hb = self.hb
        hct = self.hct
        mcv = self.mcv
        mch = self.mch
        mchc = self.mchc
        rdw = self.rdw
        wbc = self.wbc
        neu = self.neu
        lym = self.lym
        mon = self.mon
        eos = self.eos
        bas = self.bas
        plt = self.plt
        mpv = self.mpv
        pct = self.pct
        result = eval(rules['rbc']) and eval(rules['hb']) and eval(rules['hct']) and eval(rules['mcv']) and eval(rules['mch']) \
        and eval(rules['mchc']) and eval(rules['rdw']) and eval(rules['wbc']) and eval(rules['neu']) and eval(rules['lym']) \
        and eval(rules['mon']) and eval(rules['eos']) and eval(rules['bas']) and eval(rules['plt']) and eval(rules['mpv']) \
        and eval(rules['pct'])
        return result


def expert_system(session):

    patient = Patient(self, session)
    result = {}
    if patient.normal() == True:
        result['normal'] = True
        return result
    else:
        result['normal'] = False
