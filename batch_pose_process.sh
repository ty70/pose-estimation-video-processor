#!/bin/bash

INPUT_DIR="input"
OUTPUT_DIR="output"
SCRIPT="scripts/pose_estimation_video.py"

mkdir -p "$OUTPUT_DIR"

for input_file in "$INPUT_DIR"/*.mp4; do
    filename=$(basename -- "$input_file")
    name="${filename%.*}"

    output_with_pose="${OUTPUT_DIR}/${name}_with_pose.mp4"
    output_pose_only="${OUTPUT_DIR}/${name}_pose_only.mp4"

    echo "🎬 Processing $filename..."
    python "$SCRIPT" --input "$input_file" --output_with_pose "$output_with_pose" --output_pose_only "$output_pose_only"
done

echo "✅ All videos processed and saved to $OUTPUT_DIR"
