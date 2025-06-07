# pose_estimation_video.py
# --------------------------------------------------
# このスクリプトは、入力された動画に対して以下を実行します：
# 1. 棒人間（Pose landmarks）を重ねて描画した動画を出力 (--output_with_pose)
# 2. 背景を除去し、棒人間だけの動画を出力 (--output_pose_only)
#
# 使い方：
# python pose_estimation_video.py --input input.mp4 --output_with_pose output_with_pose.mp4 --output_pose_only pose_only.mp4
#
# 必要ライブラリ：
# pip install mediapipe opencv-python
# --------------------------------------------------

import cv2
import mediapipe as mp
import argparse
import os
import csv
import numpy as np

# 引数の設定
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='入力動画ファイルパス')
parser.add_argument('--output_with_pose', default=None, help='棒人間を重ねた動画の出力先')
parser.add_argument('--output_pose_only', default=None, help='背景なし棒人間動画の出力先')
args = parser.parse_args()

# 入力ファイル名（拡張子除く）を取得
basename = os.path.splitext(os.path.basename(args.input))[0]

# デフォルト値の補完
if args.output_with_pose is None:
    args.output_with_pose = f'{basename}_with_pose.mp4'

if args.csv_output is None:
    args.csv_output = f'{basename}_right_wrist_3d.csv'

# MediaPipe pose の初期化
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 入力動画読み込み
cap = cv2.VideoCapture(args.input)
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 出力動画の設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_with_pose = cv2.VideoWriter(args.output_with_pose, fourcc, fps, (width, height))
out_pose_only = cv2.VideoWriter(args.output_pose_only, fourcc, fps, (width, height))

# 棒人間の検出と描画処理
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # MediaPipe 用に RGB 変換
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        # 元フレームに棒人間を重ねる
        overlay = frame.copy()
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                overlay, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 棒人間のみ（背景黒）
        pose_only_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pose_only_frame = cv2.cvtColor(pose_only_frame, cv2.COLOR_GRAY2BGR)
        pose_only_frame[:] = (0, 0, 0)  # 背景を黒く
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                pose_only_frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 書き出し
        out_with_pose.write(overlay)
        out_pose_only.write(pose_only_frame)

# リソース解放
cap.release()
out_with_pose.release()
out_pose_only.release()

print("✅ 出力が完了しました")
