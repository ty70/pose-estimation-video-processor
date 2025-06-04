# Pose Estimation Video Processor

This Python script processes an input video to overlay pose landmarks (stick figures) using MediaPipe and outputs two videos:

* One with pose landmarks drawn on top of the original video.
* One with only pose landmarks on a black background.

## 📦 Requirements

* Python 3.6 or later
* Libraries:

  ```bash
  pip install mediapipe opencv-python
  ```

## 🚀 Usage

```bash
python scripts/pose_estimation_video.py --input input.mp4 --output_with_pose output_with_pose.mp4 --output_pose_only pose_only.mp4
```

### Parameters

* `--input`: Path to the input video file (required)
* `--output_with_pose`: Output path for the video with stick figures overlaid (default: `output_with_pose.mp4`)
* `--output_pose_only`: Output path for the stick figure-only video (default: `pose_only.mp4`)

## 🖼️ Output

This script will produce two video files:

* `output_with_pose.mp4`: Original video with pose landmarks (skeletons) overlaid.
* `pose_only.mp4`: A black-background video showing only the pose skeletons.

## ⚠️ Notes

* Ensure that your input video format is supported by OpenCV.
* The output may not contain audio, as OpenCV handles only video frames.
* MediaPipe requires a working webcam or video file; real-time camera input can be supported with additional modification.

## 📄 License

This script is provided under the [MIT License](./LICENSE).

## 🙏 Acknowledgments

* [MediaPipe](https://github.com/google/mediapipe) by Google
* [OpenCV](https://opencv.org/)
