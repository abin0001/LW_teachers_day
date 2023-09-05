from flask import Flask, render_template,url_for
import random

app = Flask(__name__)
# add qoutes here
a="""Your tireless dedication and hard work lay the foundation for our dreams and ambitions. Your impact on our lives is immeasurable, and we are forever grateful."""
b="""You are the guiding light, illuminating the path to knowledge with your unwavering commitment and perseverance. Your hard work shapes our future"""
c="""Your relentless efforts in imparting wisdom, nurturing creativity, and fostering growth inspire us to reach greater heights. Thank you for your dedication"""
d="""Teaching is not just a profession; it's a calling, and you answer it with unwavering resolve. Your hard work molds us into responsible citizens and lifelong learners"""
e="""Every lesson you teach, every challenge you help us overcome, and every moment you invest in us is a testament to your remarkable dedication. We appreciate you"""
f="""With your passion for teaching and your relentless pursuit of excellence, you transform classrooms into havens of knowledge and inspiration."""
g="""Your selfless dedication to nurturing our minds empowers us to chase our dreams and make a difference in the world. Thank you, teachers, for your tireless work"""
h="""Through your unwavering commitment to education, you empower us to unlock our full potential and make our mark on the world. Your hard work is a gift we cherish."""
i="""Your boundless enthusiasm and dedication to our growth inspire us to become the best versions of ourselves. We are grateful for your tireless efforts"""
j="""Your hard work as educators creates a ripple effect, shaping not only our futures but also the world we will one day lead. Thank you for your unwavering commitment."""
k="""You mold the leaders, innovators, and change-makers of tomorrow with your unwavering dedication and hard work. We are grateful for your profound impact."""
l="""Your hard work is the compass that guides us through the vast sea of knowledge. Your dedication lights the way to a brighter future."""
contents=[a,b,c,d,e,f,g,h,i,j,k,l]

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/Albert_Antony_Raj')
def ind1():
    name='Albert Antony Raj Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='albert.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)
@app.route('/VenkataSubramanian')
def ind2():
    
    name='Mr.J.Venkata Subramanian Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='venkata.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)


@app.route('/Kanmani')
def ind3():
    name='Mrs.K.Kanmani Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='kanmani.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Ramla')
def ind4():
    name='Mrs.M.Ramla Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='ramla.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Jayashree')
def ind5():
    name='Dr.R.Jayashree Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='jayashree.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Sudha')
def ind6():
    name='Dr.M.R.Sudha Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='sudha.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Sivakumar')
def ind7():
    name='Dr.S.Sivakumar Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='sivakumar.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Pandiyan')
def ind8():
    name='Dr.M.Pandiyan Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='pandiyan.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Thilagavathy')
def ind9():
    name='Dr.R.Thilagavathy Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='thilagavathi.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Aruna_Rani')
def ind10():
    name='Dr.S.Aruna Rani Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='arunarani.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Helen')
def ind12():
    name='Dr.D.Helan Mam'
    theme="Happy teacher's dayr"
    qoute=random.choice(contents)
    img='helen.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Chanthini')
def ind13():
    name='Dr.P.Chanthini Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='chanthini.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Lakshmi')
def ind14():
    name='Dr.S.Lakshmi Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='lakshmi.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Selvam')
def ind15():
    name='Dr.L.Selvam Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='selvam.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Srividhya')
def ind16():
    name='Dr.B.Srividhya Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='sri.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Mothilal_Nehru')
def ind17():
    name='Mothilal Nehru Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Nehru.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Anita_Smiles')
def ind18():
    name='Dr.J.Anita Smiles Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='anitha.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Kiruthiga')
def ind20():
    name='Dr.R.Kiruthiga Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Krithika.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Shobana')
def ind21():
    name='Dr.G.Shobana Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Shobana.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)


@app.route('/Sathya')
def ind22():
    name='Dr.K.Sathya Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Unknown.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Elangovan')
def ind23():
    name='Dr.V.R.Elangovan Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Unknown.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)
@app.route('/Jhon')
def ind24():
    name='M.John Britto Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Jhon.jpg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

@app.route('/Nagarajan')
def ind19():
    name='Dr.B.Nagarajan Sir'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Unknown.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)
@app.route('/Brindha')
def ind25():
    name='Dr.B.Brindha Mam'
    theme="Happy teacher's day"
    qoute=random.choice(contents)
    img='Unknown.jpeg'
    return render_template('index.html',name=name,msg=theme, qoute=qoute,image=img)

if __name__ == '__main__':
    app.run(debug=True)
