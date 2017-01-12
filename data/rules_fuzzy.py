import json

rules = {}

rules['iron deficiency anemia'] = {}
rules['iron deficiency anemia']['rbcmvc'] = [1.1, 2.9, 4.1, 5.9]
rules['iron deficiency anemia']['hb'] = [65.5,80.35,90.25,105.1]
rules['iron deficiency anemia']['rdw'] = [19.5, 21.45, 22.75, 24.7]

rules['thalassemia'] = {}
rules['thalassemia']['rbcmvc'] = [4.5, 6.9, 8.5, 10.9]
rules['thalassemia']['hb'] = [77.7,96.15,108.54,126.9]
rules['thalassemia']['rdw'] = [12.1, 16, 18.6, 22.5]

f = open('rules_fuzzy.json','w')
f.write(json.dumps(rules))
f.close()
