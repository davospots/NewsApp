from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='599b8f291b15419aa4293f30f62920d2')

    # top headlines
    top_headlines = newsapi.get_top_headlines(country='ca')

    t_articles = top_headlines['articles']
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range(len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip(news, desc, img, p_date, url)

    return render_template('index.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
