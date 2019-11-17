# mh-z19b_text_collector

## 何これ

CO2濃度とか計測できるMH-Z19Bからシリアル経由で値を読み出して、PrometheusのTextfile collector形式でファイルに出力するPythonスクリプトです。

## 使い方

Python 3.7.5上で下記ライブラリを使用して動作します。

- pymh-z19b-serial
- pyserial
- prometheus_client

ライブラリのインストールには`git clone`後にリポジトリ内で下記コマンドを実行します。
```
$ pip3 install -r requirements.txt
```

スクリプト`mh-z19b.py`を動作させるとスクリプト内の定数`EXPORTER_PATH`に定義されているディレクトリ配下に`room_air_condition.prom`という名前で結果を出力します。
出力内容はCO2濃度[ppm]と室温[℃]です。
定期的な動作にはsystemdのtimerとか使えばよいと思います。
