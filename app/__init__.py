from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='599b8f291b15419aa4293f30f62920d2')

    # top headlines
    top_headlines = newsapi.get_top_headlines(country='ca')

    # sports category
    sports_category = newsapi.get_top_headlines(category='sports')

    # technology category
    tech_category = newsapi.get_top_headlines(category='technology')

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

    sports_cat = sports_category['articles']

    news_spo = []
    desc_spo = []
    img_spo = []
    p_date_spo = []
    url_spo = []

    for j in range(len(sports_cat)):
        sports_article = sports_cat[j]

        news_spo.append(sports_article['title'])
        desc_spo.append(sports_article['description'])
        img_spo.append(sports_article['urlToImage'])
        p_date_spo.append(sports_article['publishedAt'])
        url_spo.append(sports_article['url'])

    tech_cat = tech_category['articles']

    news_tec = []
    desc_tec = []
    img_tec = []
    p_date_tec = []
    url_tec = []

    for k in range(len(tech_cat)):
        technology_article = tech_cat[k]

        news_tec.append(technology_article['title'])
        desc_tec.append(technology_article['description'])
        img_tec.append(technology_article['urlToImage'])
        p_date_tec.append(technology_article['publishedAt'])
        url_tec.append(technology_article['url'])

    contents = zip(news, desc, img, p_date, url)
    sportz = zip(news_spo, desc_spo, img_spo, p_date_spo, url_spo)
    techy = zip(news_tec, desc_tec, img_tec, p_date_tec, url_tec)

    return render_template('index.html', contents=contents, sportz=sportz, techy=techy)


if __name__ == '__main__':
    app.run(debug=True)
