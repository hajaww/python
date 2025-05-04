from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
bian_data = [] # List to store data

@app.route("/", methods=['GET'])
def index():
    return render_template('input.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    if request.method == 'POST':
        BianNama = request.form['BianNama']  # Changed () to []
        BianNik = request.form['BianNik']    # Changed () to []
        
        if BianNama and BianNik:
            bian_data.append({'BianNama': BianNama, 'BianNik': BianNik}) # ini adalah fungsi untuk menambahkan data ke dalam list bian_data
            
            
    return render_template('hasil.html', data=bian_data)

@app.route('/hasil', methods=['GET'])
def hasil_get():
    return render_template('hasil.html', data=bian_data)

if __name__ == '__main__':
    app.run(debug=True)