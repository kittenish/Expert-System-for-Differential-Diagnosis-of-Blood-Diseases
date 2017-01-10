from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import *

class Client(Form):

    gender = SelectField(u'Gender', choices=[('female', 'Female'), ('male', 'Male')])
    age = IntegerField(u'Age: ', validators = [Required()])

    rbc = FloatField(u'RBC (red blood cells) count *10^12/L :', validators = [InputRequired()])
    hb = FloatField(u'Hb (hemoglobin) concentration g/L :', validators = [InputRequired()])
    hct = FloatField(u'Hct (hematocrit) *100% :', validators = [InputRequired()])
    mcv = FloatField(u'MCV (mean corpuscular volume) fl :', validators = [InputRequired()])
    mch = FloatField(u'MCH (mean corpuscular hemoglobin) pg :', validators = [InputRequired()])
    mchc = FloatField(u'MCHC (mean corpuscular hemoglobin concentration) g/L :', validators = [InputRequired()])
    rdw = FloatField(u'RDW (red blood cell volume distribution width) *100% :', validators = [InputRequired()])
    wbc = FloatField(u'WBC (white blood cells) *10^9/L :', validators = [InputRequired()])
    neu = FloatField(u'Neutrophil *10^9/L :', validators = [InputRequired()])
    lym = FloatField(u'Lymphocyte *10^9/L :', validators = [InputRequired()])
    mon = FloatField(u'Monocyte *10^9/L :', validators = [InputRequired()])
    eos = FloatField(u'Eosinophilia *10^9/L :', validators = [InputRequired()])
    bas = FloatField(u'Basophil *10^9/L :', validators = [InputRequired()])
    plt = FloatField(u'PLT (platelet) *10^9/L :', validators = [InputRequired()])
    mpv = FloatField(u'MPV (mean platelet volume) fl :', validators = [InputRequired()])
    pct = FloatField(u'PCT (plateletocrit) *100% :', validators = [InputRequired()])

    submit = SubmitField(u'Submit')
