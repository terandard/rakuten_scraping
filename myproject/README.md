# 楽天スクレイピングプログラム

## 概要
楽天のレビューデータを取得しデータベースに保存するプログラム  
例：https://product.rakuten.co.jp/101266/  
上記URLで表示されている商品の全レビューを取得しデータベースに保存

## 環境
言語：Python3  
フレームワーク：Scrapy  
データベース：sqlite3  

## 手順
https://product.rakuten.co.jp/  
1.上記URLからジャンルを選択（「小説・エッセイ」など）  
2.表示されたページのURLをコピー  
3. myproject/spiders/product_rakuten　内の start_url にコピーしたURLを貼り付け  
4. myproject、rakuten_scraping.db、scrapy.cfg　が見えているディレクトリで下記コマンドを実行  
　$ scrapy crawl product_rakuten  

## データベース
データベース名：review  
カラム名：  
　id → 固有id  
　user_name → ユーザー名  
　age → 年齢  
　sex → 性別  
　product_name → 商品名  
　evaluation → レビューの評価  
　date → 投稿日時  
　title → レビュータイトル  
　contents → レビュー内容  
　helpfulnum → 参考にした人数  
