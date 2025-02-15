from flask import Flask, render_template, request
from g4f.client import Client

app = Flask(__name__, template_folder="C:\\Users\\Afshin\\Desktop\\")


@app.route('/', methods=['GET', 'POST'])
def home():
    image_url = None
    if request.method == 'POST':
        # دریافت ورودی کاربر، با مقدار پیش‌فرض 'a men'
        prompt = request.form.get('prompt', 'a men')
        
        # ایجاد یک نمونه از Client و ارسال درخواست تولید تصویر
        client = Client()
        response = client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )
        
        # دریافت URL تصویر از پاسخ API
        image_url = response.data[0].url

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
