from os import path
import numpy as np
import pandas as pd
from PIL import Image
from waiting import wait
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from kaggle_.config import api as kaggle_api

DATASET_DIR = 'datasets/'
DATASET_FILENAME = 'winemag-data-130k-v2.csv'
DATASET_PATH = path.join(DATASET_DIR, DATASET_FILENAME)

if __name__ == '__main__':
    if not path.exists(DATASET_PATH):
        kaggle_api.dataset_download_files(
            'zynicide/wine-reviews', path=DATASET_DIR, force=True, unzip=True)
        wait(lambda: path.exists(DATASET_PATH),
             timeout_seconds=120, waiting_for='dataset to download')

    df = pd.read_csv(DATASET_PATH, index_col=0)

    uk_rows = df.query("country=='England'").description
    uk_reviews = (" ".join(review for review in uk_rows))

    stopwords = set(STOPWORDS)
    stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

    uk_mask = np.array(Image.open("masks/flag.png"))

    image_colors = ImageColorGenerator(uk_mask)

    uk_wordcloud = WordCloud(random_state=0, width=800, height=600, mask=uk_mask,
                             stopwords=stopwords, background_color="white", color_func=image_colors, mode="RGBA")
    uk_image = uk_wordcloud.generate(uk_reviews)

    uk_image.to_file("wordclouds/uk_wines.png")
