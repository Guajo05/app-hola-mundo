from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '''
    <html>
        <head>
            <title>Hola Mundo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 50px;
                    border-radius: 20px;
                    box-shadow: 0 10px 50px rgba(0,0,0,0.3);
                }
                h1 {
                    color: #667eea;
                    font-size: 3em;
                    margin: 0;
                }
                p {
                    color: #666;
                    font-size: 1.2em;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>¡Hola Mundo! 🌍</h1>
                <p>Mi primera aplicación con Docker</p>
                <p><strong>Autor:</strong> Guajo05</p>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)