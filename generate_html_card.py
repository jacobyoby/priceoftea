import base64
import imgkit
from jinja2 import Template

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        font-family: Arial, sans-serif;
        text-align: center;
        width: 400px;
        height: 500px;
        margin: 0 auto;
        padding: 20px;
        box-sizing: border-box;
    }}
    img {{
        max-width: 100%;
        height: auto;
    }}
    h1 {{
        font-size: 24px;
        margin-bottom: 10px;
    }}
    p {{
        font-size: 14px;
    }}
</style>
</head>
<body>
<h1>Price of TEA in CHINA over Time</h1>
<img src="data:image/png;base64,{{-base64_img-}}">
<p>Generated on: {{- datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') -}}</p>
</body>
</html>
"""


def generate_card_image():
    with open('price_graph.png', 'rb') as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    html_content = Template(TEMPLATE).render(base64_img=img_base64)

    with open('html_card.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    imgkit.from_file('html_card.html', 'card_image.png')


if __name__ == "__main__":
    generate_card_image()
