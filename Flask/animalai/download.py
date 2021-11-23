from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報を入れる
key = ""
secret = ""
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

# データをjsonで扱う
flickr = FlickrAPI(key, secret, format='parsed-json') 
# データ数は400、sortは関連順に並べる、safe_search = 1 で有害コンテンツを除外
# extras は取得したいオプション値
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

# 写真を取得
photos = result['photos']
# pprint(photos)

# 取得したurlからダウンロードする
for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    # 既にあればスキップ
    if os.path.exists(filepath): continue
    # ダウンロード
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
