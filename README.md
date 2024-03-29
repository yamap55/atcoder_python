# atcoder_python

本リポジトリは Atcoder を Python で取り組むための環境になります
※JavaScript 環境も同梱

## 内容

- devcontainer
- lint
  - black
- online-judge-tools
- atcoder-python-snippets
- atcoder-cli

## 環境詳細

- Python: 3.8.2
- JavaScript（Node）: 12

## 事前準備

- Docker インストール
- VSCode インストール
- VSCode の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone

## 使用方法

1. VSCode 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナ image の取得や作成が行われる
5. 起動したら開発可能
6. ログイン
   - `acc login`
   - `oj login https://atcoder.jp/`
7. contestID を取得
   - `https://atcoder.jp/contests/abs` の場合、 `abs`
8. ディレクトリ作成（問題を選択）
   - `acc new ${contestID}`
   - 例: `acc new abs`
9. 回答する問題のディレクトリに移動
   - `cd {contestID}/{問題}`
10. 回答を作成
    - `main.py` に回答を記載
11. 回答をテスト
    - `ojt`
12. 回答を提出
    - `acc submit`

※`ojt` は `oj t -c "python main.py"'` のエイリアス

### 使用例 1（Python の場合）

```
acc new abs
cd abs/practicea/
vi main.py
ojt
acc submit main.py
```

### 使用例 2（JavaScript の場合）

```
acc new --template js abs
cd abs/practicea/
vi main.js
oj t -c "node main.js"
acc submit
```

## 参考

- online-judge-tools
  - https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md
- atcoder-cli
  - http://tatamo.81.la/blog/2018/12/07/atcoder-cli/
- atcoder-python-snippets
  - https://github.com/hirosuzuki/atcoder-python-snippets

## memo

- サンプル以外のテストケース
  - https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0
