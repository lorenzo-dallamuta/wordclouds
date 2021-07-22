import re
# import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS


# def plot_cloud(wordcloud):
#     plt.figure(figsize=(40, 30))
#     plt.imshow(wordcloud)
#     plt.axis("off")
#     plt.show(block='false')


if __name__ == '__main__':
    wiki = wikipedia.page('Web scraping')
    text = wiki.content
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')

    mask = np.array(Image.open('masks/upvote.png'))

    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='salmon',
                          colormap='Pastel1', collocations=False, stopwords=STOPWORDS, mask=mask).generate(text)

    # plot_cloud(wordcloud)

    wordcloud.to_file("wordclouds/upvote.png")
