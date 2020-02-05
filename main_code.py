from moviepy.editor import VideoFileClip, concatenate_videoclips
import soundfile as sf
import pyloudnorm as pyln
import pandas as pd
import os


def task_input_video():
    """
    This function takes input video file from user.
    """
    while True:
        try:
            video_file = input("Enter your video file path: ")
            if not(os.path.exists(video_file)):
                raise FileNotFoundError
        except (FileNotFoundError, OSError, IOError):
            print("You have entered wrong file path,please enter proper file path")
        else:
            return video_file


def task_input_data():
    """
    This function takes input service time excel file from user.

    Returns:
    df_one:pandas dataframe

    """
    while True:
        try:
            file_pointer = pd.ExcelFile(input("Enter your data file path: "))
            df_one = file_pointer.parse("Sheet1")
        except (FileNotFoundError, OSError):
            print("You have entered wrong file path,please enter proper file path")
        else:
            return df_one


def task_no_highlights():
    """
    This function takes number of highlights user want to watch.

    Returns:
    highlights:int

    """
    while True:
        try:
            highlights = int(
                input("Please enter number of highlights you want to watch: "))
            if highlights <= 5 or highlights >= 90:
                print("Number of highlights should be greater than 5 and less than 90")
                continue
        except (ValueError, TypeError):
            print("Please enter valid input")
        else:
            return highlights


def task_break(video_file, data_file):
    """
    This function breaks video file into subclips and generated each subclip's .wav file.

    Parameters:
    video_file:mp4 file
    data_file:pandas dataframe

    Returns:
    loudness_dict:dictionary(key:.wav file name,value:loudness of .wav file)
    wav_video_dict:dictionary(key:.wav file name,value:corresponding .mp4 file name)

    """
    count = 0
    video_clip_list = []
    video_clip_list_wav = []
    wav_video_dict = {}
    loudness_dict = {}
    # iterate this loop till the last row in data frame
    for number in data_file.index:
        with VideoFileClip(video_file) as clips:
            # start and end time is provided from data file dynamically
            clip = clips.subclip(
                data_file["start_time"][number], data_file["end_time"][number])
            count += 1  # keep count of number of files
            clip.write_videofile("output_%s.mp4" % str(count).zfill(3))
            # appends the video file in video_clip_list
            video_clip_list.append("output_%s.mp4" % str(count).zfill(3))
            # creates .wav file of subclips
            clip.audio.write_audiofile("output_%s.wav" % str(count).zfill(3))
            # appends the .wav file of video in list
            video_clip_list_wav.append("output_%s.wav" % str(count).zfill(3))
            # created dictionary to keep track of .wav and its corresponding .mp4 file
            wav_video_dict["output_%s.wav" % str(count).zfill(3)] = str(
                "output_%s.mp4" % str(count).zfill(3))
        for my_file in video_clip_list_wav:
            # load audio (with shape (samples, channels))
            data, rate = sf.read(my_file)
            # create BS.1770 meter
            meter = pyln.Meter(rate)
            # measure loudness
            loudness = meter.integrated_loudness(data)
            # key is wav file name and its loudeness is value
            loudness_dict[my_file] = loudness
    return loudness_dict, wav_video_dict


def task_merge(loudness_dict, wav_video_dict, highlights):
    """
    This function merges the video files which are with high loudeness, according to time.

    Parameters:
    loudness_dict:dictionary(key:.wav file name,value:loudness of .wav file)
    wav_video_dict:dictionary(key:.wav file name,value:corresponding .mp4 file name)
    highlights:int

    Returns:
    final_clip:clip of concatenated video files

    """
    new_wav_list = []
    # sorts the dictionary according to its values.
    # returns list of tuples
    sorted_wav_list = sorted(loudness_dict.items(),
                             key=lambda kv: (kv[1], kv[0]))
    # taking key name as it is .wav file name
    # created new list which contains loud files
    # in ascending order
    for loud_file in sorted_wav_list:
        new_wav_list.append(loud_file[0])
    # took the number of highlights user wants
    modified_list = new_wav_list[-highlights:]
    # sorted according to time
    modified_list_one = sorted(modified_list)
    new_video_list = []
    # takes corresponding .mp4 file to .wav file
    # and appends in new_video_list
    for new_key in modified_list_one:
        new_video_list.append(VideoFileClip(wav_video_dict[new_key]))
    # conctatenates all the highlights we took
    final_clip = concatenate_videoclips(new_video_list)
    return final_clip


def task_output(final_clip):
    """
    This function gives final highlights video path.

    Parameters:
    final_clip:clip of concatenated video files

    """
    # creates final highlights video
    final_clip.write_videofile("final_highlights.mp4")
    # get path of video file
    final_clip_path = os.path.abspath("final_highlights.mp4")
    # checking is directory valid or not
    clip_dir_path = os.path.dirname(final_clip_path)
    # write on console directory name and final video clip name
    # if directory is valid
    if os.path.isdir(clip_dir_path):
        print("Your highlights video is located in {0} with name {1} ".format(
            clip_dir_path, os.path.basename(final_clip_path)))


def task_cleanup():
    """
    This function removes the generated output.mp4 and output.wav files from our directory.
    """
    dir_path = os.getcwd()
    dir_files = os.listdir(dir_path)
    for dir_file in dir_files:
        # reomves the files which are created for project
        # those starts with output, will get removed
        if dir_file.startswith("output"):
            os.remove(os.path.join(dir_path, dir_file))
    print("*Thanks For Using Our Application*")
    return


# driver code
if __name__ == "__main__":
    # runs function to take video file path from user
    video_file = task_input_video()
    # runs function to take excel file path from user
    data_file = task_input_data()
    # runs to take number of highlights from user
    highlights = task_no_highlights()
    # runs to break video into subclips for further processing
    loudness_dict, wav_video_dict = task_break(video_file, data_file)
    # runs to merge our selected clips to get final output
    final_clip = task_merge(loudness_dict, wav_video_dict, highlights)
    # runs to show output to user
    task_output(final_clip)
    # runs to clean our directory
    task_cleanup()
