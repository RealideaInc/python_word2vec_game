[toc]

# 言語距離感覚ゲーム - Word２Vec

![word2vec_game_test](https://github.com/RealideaInc/python_word2vec_game/assets/69300459/10b12c15-83ab-4de3-a7cc-98b4e172f469)

## 概要

ランダムに与えられる言葉に対して、より意味が「近い(or 遠い)」言葉を言ったほうが勝ちの対戦ゲーム！
現在二人プレイのみ対応しています。

言葉に意味が近いか遠いかはAIが判定！

## 環境・ライブラリ

- Docker
    - python3
    - gensim

## 遊び方

1. `git clone` または ZIPファイルをDL→解凍
2. `docker-compose up -d --build` でコンテナ立ち上げ
3. `docker compose exec python3 bash`でコンテナ内に入る
4. `python game.py`もしくは`python -i game.py`を実行

```
$ git clone https://github.com/RealideaInc/python_word2vec_game.git
$ cd python_word2vec_game
$ docker-compose up -d --build
$ docker compose exec python3 bash
$ python -i game.py
```
※　`-i`オプションを付与した場合、Ctrl+Dを何回か押すことで、元に戻れます。

## 仕様

- game.py
- Word2Vecを使用して、単語間の類似度を調べています。
- モデルには日本語Wikiをコーパスとして使用している「[日本語 Wikipedia エンティティベクトル(20190520 100d)](https://github.com/singletongue/WikiEntVec/releases/tag/20190520 )」を使用しています

## 参考
- [Qiita -【機械学習】Word2Vecで単語間の類似度を測定する
](https://qiita.com/DancingEnginee1/items/b10c8ef7893d99aa53be)
- [GENSIM - models.keyedvectors – Store and query word vectors](https://radimrehurek.com/gensim/models/keyedvectors.html)
- [日本語 Wikipedia エンティティベクトル](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/)

## 制作者

もやしのぶんざい
[twitter](https://twitter.com/mycspl)

#　おまけ: 単語の足し引きをしよう

## 遊び方
`python -i word_add_sub.py`

## 概要
単語の足し算、引き算をすることができます。
入力欄が現れてから
`王様+女-男`
のような式を入力してみよう。