import os
import random
import argparse
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

def select_random_video(file_path):
    videos = [f for f in os.listdir(file_path) if f.endswith('.mp4')]
    if not videos:
        raise ValueError(f"No video files found in {file_path}")
    return os.path.join(file_path, random.choice(videos))

def trim_video(video_path, duration=2):
    video = VideoFileClip(video_path)
    return video.subclip(0, duration)

def main():
    parser = argparse.ArgumentParser(description="Process video files and add music")
    parser.add_argument("-f1", "--folder1", required=True, help="Path to folder with video files 1")
    parser.add_argument("-f2", "--folder2", required=True, help="Path to folder with video files 2")
    parser.add_argument("-m", "--music", required=True, help="Path to music file")
    args = parser.parse_args()

    video_path_1 = select_random_video(args.folder1)
    video_path_2 = select_random_video(args.folder2)

    trimmed_video_1 = trim_video(video_path_1)
    trimmed_video_2 = trim_video(video_path_2)

    final_video = concatenate_videoclips([trimmed_video_1, trimmed_video_2], method="compose")
    final_audio = AudioFileClip(args.music)
    final_video = final_video.set_audio(final_audio)

    output_file = "output.mp4"
    final_video.write_videofile(output_file, codec="libx264")

if __name__ == "__main__":
    main()