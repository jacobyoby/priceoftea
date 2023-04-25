import pandas as pd
import matplotlib.pyplot as plt
import imgkit

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Price of TEA in CHINA over Time</title>
</head>
<body>
    <div>
        <h1>Price of TEA in CHINA over Time</h1>
        <img src="{image_path}" alt="Price of TEA in CHINA over Time">
    </div>
</body>
</html>
"""


def generate_graph():
    df = pd.read_csv('data.csv', names=[
                     'Timestamp', 'Product Name', 'Original Price', 'Discounted Price'], parse_dates=['Timestamp'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Timestamp'], df['Discounted Price'], marker='o', linestyle='-')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price (in YEN)')
    ax.set_title('Price of TEA in CHINA over Time')

    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig('price_graph.png')


def generate_html_card():
    with open("html_card.html", "w", encoding="utf-8") as f:
        content = HTML_TEMPLATE.format(image_path="price_graph.png")
        f.write(content)


def generate_card_image():
    imgkit.from_file('html_card.html', 'card_image.png')


if __name__ == "__main__":
    generate_graph()
    generate_html_card()
    generate_card_image()
