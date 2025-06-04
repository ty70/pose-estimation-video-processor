# ポーズ推定ビデオプロセッサー

このPythonスクリプトは、MediaPipeを使って入力されたビデオにポーズランドマーク（棒人間）を重ね合わせ、以下の2種類のビデオを出力します：

* 元のビデオにポーズランドマークを重ねたもの
* 黒背景にポーズランドマークのみを描画したもの

## 📦 必要な環境

* Python 3.6以降
* 必要なライブラリ：

  ```bash
  pip install mediapipe opencv-python
  ```

## 🚀 使用方法

```bash
python pose_estimation_video.py --input input.mp4 --output_with_pose output_with_pose.mp4 --output_pose_only pose_only.mp4
```

### パラメータ

* `--input`：入力ビデオファイルのパス（必須）
* `--output_with_pose`：棒人間を重ねた出力ビデオのパス（デフォルト：`output_with_pose.mp4`）
* `--output_pose_only`：棒人間のみの出力ビデオのパス（デフォルト：`pose_only.mp4`）

## 🖼️ 出力内容

このスクリプトにより、以下の2つのビデオファイルが生成されます：

* `output_with_pose.mp4`：元の映像にポーズランドマーク（骨格）を重ねたビデオ
* `pose_only.mp4`：黒背景にポーズランドマークのみを表示したビデオ

## ⚠️ 注意事項

* 入力ビデオの形式がOpenCVで対応していることを確認してください。
* OpenCVは映像のみを扱うため、出力には音声が含まれません。
* MediaPipeはWebカメラまたはビデオファイルの入力を必要とします。リアルタイムカメラ入力に対応するには追加の修正が必要です。

## 📄 ライセンス

このスクリプトはMITライセンスで提供されます。

## 🙏 クレジット

* Googleによる [MediaPipe](https://github.com/google/mediapipe)
* [OpenCV](https://opencv.org/)
