from os import path
import pandas as pd
from waiting import wait
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
