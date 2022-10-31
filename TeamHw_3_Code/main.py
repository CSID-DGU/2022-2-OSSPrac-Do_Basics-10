from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Student Number'] = request.form.get('Student Number') #학번

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
