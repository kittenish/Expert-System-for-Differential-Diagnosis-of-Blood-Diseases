import json

class Patient(object):

    def __init__(self, session):

        self.gender = session['gender']
        self.age = int(session['age'])
        self.rbc = float(session['rbc'])
        self.hb = float(session['hb'])
        self.hct = float(session['hct'])
        self.mcv = float(session['mcv'])
        self.mch = float(session['mch'])
        self.mchc = float(session['mchc'])
        self.rdw = float(session['rdw'])
        self.wbc = float(session['wbc'])
        self.neu = float(session['neu'])
        self.lym = float(session['lym'])
        self.mon = float(session['mon'])
        self.eos = float(session['eos'])
        self.bas = float(session['bas'])
        self.plt = float(session['plt'])
        self.mpv = float(session['mpv'])
        self.pct = float(session['pct'])
        self.rbcmvc = 0

        if self.age > 15:
            self.age = 'adult'
        elif self.age < 0.5:
            self.age = 'newborn'
        elif self.age < 2:
            self.age = 'baby'
        else:
            self.age = 'child'

    def normal(self):
        f = open('../data/rules_normal.json','r')
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

        result = {}
        result['rbc'] = eval(rules['rbc'])
        result['hb'] = eval(rules['hb'])
        result['hct'] = eval(rules['hct'])
        result['hct'] = eval(rules['hct'])
        result['mcv'] = eval(rules['mcv'])
        result['mch'] = eval(rules['mch'])
        result['mchc'] = eval(rules['mchc'])
        result['rdw'] = eval(rules['rdw'])
        result['wbc'] = eval(rules['wbc'])
        result['neu'] = eval(rules['neu'])
        result['lym'] = eval(rules['lym'])
        result['mon'] = eval(rules['mon'])
        result['eos'] = eval(rules['eos'])
        result['bas'] = eval(rules['bas'])
        result['plt'] = eval(rules['plt'])
        result['mpv'] = eval(rules['mpv'])
        result['pct'] = eval(rules['pct'])

        return result

    def disease(self, result):

        f = open('../data/rules_diseases.json','r')
        rules = f.read()
        rules = json.loads(rules)
        abnormal = set()
        pre_diseases = set()
        diseases = set()

        for i in result.keys():
            if result[i] == False:
                if i!= 'rbc' and i!='hb' and i!='hct' and i!='normal':
                    abnormal.add(i)
                    for j in rules.keys():
                        if rules[j].has_key(i):
                            if eval('self.' + i) >= rules[j][i]['left'] and  eval('self.' + i) <= rules[j][i]['right']:
                                pre_diseases.add(j)
                elif i!= 'normal':
                    if rules['anemia'][self.gender].has_key(i):
                        if eval('self.' + i) >= rules['anemia'][self.gender][i]['left'] and \
                        eval('self.' + i) <= rules['anemia'][self.gender][i]['right']:
                            pre_diseases.add('anemia')

        diseases = pre_diseases.copy()

        for i in pre_diseases:
            if i != 'anemia':
                dis_rule = rules[i]
                for j in dis_rule.keys():
                    if eval('self.' + j) > dis_rule[j]['left'] and  eval('self.' + j) < dis_rule[j]['right']:
                        pass
                    else:
                        diseases.remove(i)
                        break
            else:
                dis_rule = rules['anemia'][self.gender]
                for j in dis_rule.keys():
                    if eval('self.' + j) > dis_rule[j]['left'] and  eval('self.' + j) < dis_rule[j]['right']:
                        pass
                    else:
                        diseases.remove(i)
                        break

        return abnormal, diseases

    def diffetential(self, result):

        p_iron = 1.0
        p_tha = 1.0

        self.rbcmvc = self.rbc / self.mcv
        f = open('../data/rules_fuzzy.json','r')
        rules = f.read()
        rules = json.loads(rules)

        x = rules['iron deficiency anemia']['rbcmvc']
        if self.rbcmvc < x[2]:
            p_iron_rbcmvc = 1
        else:
            p_iron_rbcmvc = 1#(x[3] - self.rbcmvc) / (x[3] - x[2])

        x = rules['iron deficiency anemia']['hb']
        if self.hb < x[2]:
            p_iron_hb = 1
        else:
            p_iron_hb = (x[3] - self.hb) / (x[3] - x[2])

        x = rules['iron deficiency anemia']['rdw']
        if self.rdw > x[1]:
            p_iron_rdw = 1
        else:
            p_iron_rdw = (self.rdw - x[0]/100) / (x[1]/100 - x[0]/100)

        x = rules['thalassemia']['rbcmvc']
        if self.rbcmvc > x[1]:
            p_tha_rbcmvc = 1
        else:
            p_tha_rbcmvc = 1#(self.rbcmvc - x[0]) / (x[1] - x[0])

        x = rules['thalassemia']['hb']
        if self.hb > x[1]:
            p_tha_hb = 1
        else:
            p_tha_hb = (self.hb - x[0]) / (x[1] - x[0])

        x = rules['thalassemia']['rdw']
        if self.rdw < x[2]:
            p_tha_rdw = 1
        else:
            p_tha_rdw = (x[3]/100 - self.rdw) / (x[3]/100 - x[2]/100)

        p_iron = p_iron_rdw * p_iron_hb * p_iron_rbcmvc
        p_tha = p_tha_rdw * p_tha_hb * p_tha_rbcmvc
        print p_iron_rdw,p_iron_hb,p_iron_rbcmvc
        if p_iron < 0:
            p_iron = 0
        if p_tha < 0:
            p_tha = 0
        diffetential = {}
        diffetential['p_iron'] = p_iron
        diffetential['p_tha'] = p_tha
        print diffetential
        return diffetential

def expert_system(session):

    patient = Patient(session)
    result = patient.normal()
    normal = True
    for i in result.keys():
        if result[i] == False:
            normal = False
    result['normal'] = normal
    if result['normal']:
        return result
    else:
        abnormal, diseases =  patient.disease(result)
        if 'microcytic hypochromic anemia' not in diseases:
            result['abnormal'] = abnormal
            result['diseases'] = diseases
            return result
        else:
            result['abnormal'] = abnormal
            result['diseases'] = diseases
            diffetential = patient.diffetential(result)
    return result

ss = {}
ss['gender'] = 'male'
ss['age'] = 20
ss['rbc'] = 3.8
ss['hb'] = 95
ss['hct'] = 0.4
ss['mcv'] = 70
ss['mch'] = 20
ss['mchc'] = 300
ss['rdw'] = 0.21
ss['wbc'] = 5
ss['neu'] = 5
ss['lym'] = 3.5
ss['mon'] = 0.5
ss['eos'] = 0.3
ss['bas'] = 0.05
ss['plt'] = 200
ss['mpv'] = 10
ss['pct'] = 0.002
result = expert_system(ss)
print result
