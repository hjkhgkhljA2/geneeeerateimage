from flask import Flask, render_template, request
from g4f.client import Client

app = Flask(__name__)  # به صورت پیش‌فرض Flask به دنبال پوشه‌ی "templates" در همان دایرکتوری است.

@app.route('/', methods=['GET', 'POST'])
def home():
    image_url = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', 'a men')
        
        client = Client()
        response = client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )
        
        image_url = response.data[0].url

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
