from moviepy.editor import VideoFileClip
import os


def convert_mp4_wav(src_file):
    print("filepath is :",src_file)
    src_file = os.path.join(des,src_file)
    video_clip = VideoFileClip(src_file)
    audio_filename = src_file.split('.')[-2] + '.wav'
    video_clip.audio.write_audiofile(audio_filename, fps=16000)  # will save the wave file on the same location
    return audio_filename

if __name__=="__main__":
    des = r"C:\Users\91963\Downloads\YASH SINGH\audio_files_2"
    p4_files = [file for file in os.listdir(des) if file.endswith('.mp4')]
    for file in p4_files:
        print(file)
        convert_mp4_wav(file)