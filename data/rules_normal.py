import json

rules = {}

rules['rbc'] = "(gender == 'male' and age != 'newborn' and rbc >= 4.0 and rbc <= 5.5) or \
(gender == 'female' and age != 'newborn' and rbc >= 3.5 and rbc <= 5.0) or \
(age == 'newborn' and rbc >= 6.0 and rbc <= 7.0)"

rules['hb'] = "(gender == 'male' and age != 'newborn' and hb >= 120 and hb <= 160) or \
(gender == 'female' and age != 'newborn' and hb >= 110 and hb <= 150) or \
(age == 'newborn' and hb >= 170 and hb <= 200)"

rules['hct'] = "(gender == 'male' and hct >= 0.42 and hct <= 0.49) or \
(gender == 'female' and hct >= 0.37 and hct <= 0.48)"

rules['mcv'] = "mcv >= 80 and mcv <= 100"

rules['mch'] = "mch >= 26 and mch <= 32"

rules['mchc'] = "mchc >= 310 and mchc <= 350"

rules['rdw'] = "rdw <= 0.149"

rules['wbc'] = "(age == 'adult' and wbc >= 4.0 and wbc <= 10.0) or \
(age == 'baby' and wbc >= 11.0 and wbc <= 12.0) or \
(age == 'newborn' and wbc >= 15.0 and wbc <= 20.0)"

rules['neu'] = "neu >= 2.0 and neu <= 7.0"

rules['lym'] = "lym >= 0.8 and lym <= 4.0"

rules['mon'] = "mon >= 0.12 and mon <= 0.8"

rules['eos'] = "eos >= 0.05 and eos <= 0.5"

rules['bas'] = "bas >= 0 and bas <= 0.1"

rules['plt'] = "plt >= 100.0 and plt <= 300.0"

rules['mpv'] = "mpv >= 7 and mpv <= 11"

rules['pct'] = "pct >= 0.001 and pct <= 0.003"

f = open('rules_normal.json','w')
f.write(json.dumps(rules))
f.close()

'''
Normal Example:
    gender = 'male'
    age = 'adult'
    rbc = 4.5
    hb = 120
    hct = 0.45
    mcv = 90
    mch = 30
    mchc = 320
    rdw = 0.1
    wbc = 5
    neu = 5
    lym = 3.5
    mon = 0.5
    eos = 0.3
    bas = 0.05
    plt = 200
    mpv = 10
    pct = 0.002
'''
