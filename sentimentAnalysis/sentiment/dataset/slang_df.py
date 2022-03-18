#used to download and read the csv from github
import requests
import io
import pandas as pd

def generate_slang():
    slang_url = "https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv"
    download = requests.get(slang_url).content
    slang_df = pd.read_csv(io.StringIO(download.decode('utf-8')))

    return slang_df