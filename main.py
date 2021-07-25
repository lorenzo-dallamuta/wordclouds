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

    text = " ".join(review for review in df.description)

    stopwords = set(STOPWORDS)
    stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

    # loc_mask = np.array(Image.open("masks/loc.png"))
    # star_mask = np.array(Image.open("masks/star.png"))
    wine_mask = np.array(Image.open("masks/wine_mask.png"))
    # keep it 4 bit
    transformed_wine_mask = np.ndarray(
        (wine_mask.shape[0], wine_mask.shape[1]), np.int32)
    for i in range(len(wine_mask)):
        transformed_wine_mask[i] = list(
            map(lambda x: 255 if x == 0 else 0, wine_mask[i]))
    # make it 24 bit
    # transformed_wine_mask = np.ndarray(
    #     (wine_mask.shape[0], wine_mask.shape[1], 4), np.int32)
    # for i in range(len(wine_mask)):
    #     transformed_wine_mask[i] = list(
    #         map(lambda x: (255, 255, 255, 0) if x == 0 else (0, 0, 0, 0), wine_mask[i]))

    wordcloud = WordCloud(random_state=0, width=800, height=600, mask=transformed_wine_mask, stopwords=stopwords,
                          relative_scaling=1, background_color=None, mode="RGBA")
    # processed_text = wordcloud.process_text(text)
    # image = wordcloud.generate_from_frequencies(processed_text)
    image = wordcloud.generate(text)

    image.to_file("wordclouds/wines.png")
