import json

rules = {}

rules['anemia'] = {}
rules['anemia']['male'] = {}
rules['anemia']['female'] = {}
rules['anemia']['male']['rbc'] = {'left':-1, 'right':4.5}
rules['anemia']['male']['hb'] = {'left':-1, 'right':120}
rules['anemia']['male']['hct'] = {'left':-1, 'right':0.42}
rules['anemia']['female']['rbc'] = {'left':-1, 'right':4.0}
rules['anemia']['female']['hb'] = {'left':-1, 'right':110}
rules['anemia']['female']['hct'] = {'left':-1, 'right':0.37}

rules['normacytic anemia'] = {}
rules['normacytic anemia']['mcv'] = {'left':80, 'right':100}
rules['normacytic anemia']['mch'] = {'left':26, 'right':32}
rules['normacytic anemia']['mchc'] = {'left':310, 'right':350}

rules['macrocytic anemia'] = {}
rules['macrocytic anemia']['mcv'] = {'left':100, 'right':100000}
rules['macrocytic anemia']['mch'] = {'left':32, 'right':100000}
rules['macrocytic anemia']['mchc'] = {'left':310, 'right':350}

rules['microcytic anemia'] = {}
rules['microcytic anemia']['mcv'] = {'left':-1, 'right':80}
rules['microcytic anemia']['mch'] = {'left':-1, 'right':26}
rules['microcytic anemia']['mchc'] = {'left':310, 'right':350}

rules['microcytic hypochromic anemia'] = {}
rules['microcytic hypochromic anemia']['mcv'] = {'left':-1, 'right':80}
rules['microcytic hypochromic anemia']['mch'] = {'left':-1, 'right':23}
rules['microcytic hypochromic anemia']['mchc'] = {'left':-1, 'right':310}

rules['leukocytosis'] = {}
rules['leukocytosis']['adult'] = {}
rules['leukocytosis']['baby'] = {}
rules['leukocytosis']['newborn'] = {}
rules['leukocytosis']['adult']['wbc'] = {'left':10, 'right':100000}
rules['leukocytosis']['baby']['wbc'] = {'left':12, 'right':100000}
rules['leukocytosis']['newborn']['wbc'] = {'left':20, 'right':100000}

rules['leukopenia'] = {}
rules['leukopenia']['adult'] = {}
rules['leukopenia']['baby'] = {}
rules['leukopenia']['newborn'] = {}
rules['leukopenia']['adult']['wbc'] = {'left':-1, 'right':4}
rules['leukopenia']['baby']['wbc'] = {'left':-1, 'right':11}
rules['leukopenia']['newborn']['wbc'] = {'left':-1, 'right':15}

rules['neutrophilia'] = {}
rules['neutrophilia']['neu'] = {'left':7, 'right':100000}

rules['neutropenia'] = {}
rules['neutropenia']['neu'] = {'left':-1, 'right':1.5}

rules['agranulocytosis'] = {}
rules['agranulocytosis']['neu'] = {'left':-1, 'right':0.5}

rules['lymphocytosis'] = {}
rules['lymphocytosis']['lym'] = {'left':5, 'right':100000}

rules['lymphocytopenia'] = {}
rules['lymphocytopenia']['lym'] = {'left':-1, 'right':0.8}

rules['monocytosis'] = {}
rules['monocytosis']['mon'] = {'left':0.8, 'right':100000}

rules['monocytopenia'] = {}
rules['monocytopenia']['mon'] = {'left':-1, 'right':0.12}

rules['eosinophilia'] = {}
rules['eosinophilia']['eos'] = {'left':0.5, 'right':100000}

rules['eosinopenia'] = {}
rules['eosinopenia']['eos'] = {'left':-1, 'right':0.05}

rules['basophilia'] = {}
rules['basophilia']['bas'] = {'left':0.1, 'right':100000}

rules['thrombocytosis'] = {}
rules['thrombocytosis'] = {'left':1000, 'right':100000}

rules['thrombocytopenia'] = {}
rules['thrombocytopenia'] = {'left':-1, 'right':100}

f = open('rules_diseases.json','w')
f.write(json.dumps(rules))
f.close()
