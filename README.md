# AIML-dict-ja ― オープンソースの AI (人工知能)・ML (機械学習) 英日用語辞典

AIML-dict-ja は、オープンソースの人工知能・機械学習分野の英語→日本語用語辞典です。[クリエイティブ・コモンズ表示 - 継承 3.0 非移植 (CC BY-SA 3.0) ライセンス](https://creativecommons.org/licenses/by-sa/3.0/deed.ja) の下で利用できます。

メインの辞書ファイルは [aiml-dict-ja.yml](aiml-dict-ja.yml) です。YAML 形式で書かれています。

[validate.py](validate.py) は、辞書ファイル `aiml-dict-ja.yml` が、決められた構造に従っているかどうか検査するスクリプトです。実行するには `PyYAML` パッケージが必要です。構造に問題がなければ、 `Validation: PASSED` を出力します。
