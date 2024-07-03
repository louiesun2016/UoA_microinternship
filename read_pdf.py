from flask import Flask, send_file
from flask import make_response

app = Flask(__name__)

@app.route('/viewer')
def viewer():
    with open('/Users/lusun/Downloads/backend_data/MockDisplayOnlyData/Operations/Restricted/Production_Spec_Sheet/Packing_Spec_000000 Something+1 FGS 11.14.pdf', 'rb') as pdf:
        pdf_content = pdf.read()
    response = make_response(pdf_content)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=sample.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)