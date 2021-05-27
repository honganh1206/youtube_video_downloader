
from pytube import YouTube
import sys
import time
from class_disk import Disk

def save_path():

    # user chooses where to save file
    # I was considering about making available disks as a list, but later realized that different computers
    # have different names for disks (probably)
    print("")
    print("Which disk would you like to save the video in?: (1) C. (2) D. (3) E. (4) F. ")
    save = int(input("Please enter a number here:  "))
    if save == 1:

        # using OOP here seems superfluous, but I'm trying to apply the knowledge gained after watching video

        save_path = Disk("C:/")
        return save_path.hard_disk
    if save == 2:
        save_path = Disk("D:/")
        return save_path.hard_disk
    if save == 3:
        save_path = Disk("E:/")
        return save_path.hard_disk
    if save == 4:
        save_path = Disk("F:/")
        return save_path.hard_disk


def get_user_url(choice):

    # if download 1 video only

    if choice == 1:
        print("")
        single_url = str(input("Enter the URL of the video you want to download: "))
        return single_url

    # if download more than 1 video

    if choice == 2:
        list_url = []
        num_url = 0
        while 1:
            num_url += 1
            print("")
            print("Enter the URLs of the videos you want to download, enter NO when there is no URL to download")
            url = input("Video Number # %d: " % num_url)
            if url == "NO":
                break
            list_url.append(url)
        return list_url


def save_video(video, path):

    # print the title
    print("")
    print("The title of the video is: ", video.title, 'by', video.author, ', published on', video.publish_date)
    print("")
    # choose the resolution

    reso_choice = int(input("Press 1 for 360p video with audio / 2 for 1080p video with separated audio: "))
    if reso_choice == 1:
        # video.streams.filter(progressive=True)

        # so far the 360p is the ONLY resolution that includes audio!

        down_video = video.streams.get_highest_resolution()

        print("The video is being downloaded... ")
        try:
            print("")
            print("The downloading bar (Below if any) is just for fun :) "
                  "Wait time depends on the file's size\nSo please be patient.")
            print("")
            animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%",
                         "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
                         "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]

            # the real download is here :)

            down_video.download(path)

            for i in range(len(animation)): # for the animation
                # after each 0.5 sec, the bar will increase by 10%
                time.sleep(0.5)
                # display the download bar
                sys.stdout.write("\r Preparing..." + animation[i % len(animation)])
                sys.stdout.flush()
        except:
            print("Some errors, please try again!")
        print("")
        print("Video with audio downloaded!")
        print("")

    if reso_choice == 2:
        #video.streams.filter(adaptive=True)

        # download the video in 1080p without audio

        down_video = video.streams.get_by_itag(137)
        print("Please be patient, the video is being downloaded... ")
        try:
            print("")
            print("The downloading bar (Below if any) is just for fun :) "
                  "Wait time depends on the file's size\nSo please be patient.")
            print("")
            animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%",
                         "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
                         "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]

            down_video.download(path)

            for i in range(len(animation)): # for the animation
                time.sleep(0.5)
                sys.stdout.write("\rPreparing..." + animation[i % len(animation)])
                sys.stdout.flush()

        except:
            print("Some errors, please try again!")
        print("")
        print("Video without audio downloaded!")
        print("")


def download_vid(choice, url, path):

    # if download 1 video only

    if choice == 1:
        # download the video
        try:
            video = YouTube(url)
            save_video(video, path)
        except:
            print("Connection Error, please try again!")

    # if download more than 1 video

    if choice == 2:
        # download the video
        for i in url:
            try:
                video = YouTube(i)
                save_video(video, path)
            except:
                print("Connection Error, please try again!")


def save_audio(audio, path):

    # download audio separately in 128kbps only

    print("The audio is being downloaded...")

    # To view codecs of the audio, add the print() statement

    # print(audio.streams.filter(only_audio=True)) to see codecs of the streams

    # downloading the video
    down_audio = audio.streams.get_audio_only('webm')
    try:
        print("")
        print("The downloading bar (Below if any) is just for fun :) "
              "Wait time depends on the file's size\nSo please be patient.")
        print("")
        animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%",
                     "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
                     "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]

        down_audio.download(path)

        for i in range(len(animation)):  # for the animation
            time.sleep(0.5)
            sys.stdout.write("\rPreparing..." + animation[i % len(animation)])
            sys.stdout.flush()
    except:
        print("Some error, please try again!")
    print("")
    print("Audio downloaded!")
    print("")
    print("All done!")


def download_audio(choice, url, path):
    # if download 1 audio only

    if choice == 1:
        # download the video
        try:
            audio = YouTube(url)
            save_audio(audio, path)
        except:
            print("Connection Error, please try again!")

    # if download more than 1 video

    if choice == 2:
        # download the video
        for i in url:
            try:
                audio = YouTube(i)
                save_audio(audio, path)
            except:
                print("Connection Error, please try again!")


def main():
    print("")
    print(" --- Welcome to a YouTube videos downloader ---")
    print("")
    while True:

        # Ask the user to restart after the program finishes
        print("")
        print("Would you like to download one video or multiple videos? ")
        vid_choice = int(input("Press 1 for a single video and 2 for multiple videos: "))
        if vid_choice == 1:
            # get the url
            url = get_user_url(vid_choice)
            path = save_path()
            # download video from url
            download_vid(vid_choice, url, path)

            # download audio if needed

            audio_choice = int(input("Press 1 to download the audio separately / 2 if you don't need the audio: "))
            if audio_choice == 1:
                download_audio(vid_choice, url, path)
            if audio_choice == 2:
                print("")
                print("All done!")
        if vid_choice == 2:

            url = get_user_url(vid_choice)
            path = save_path()
            download_vid(vid_choice, url, path)

            # download audio(s) if needed

            audio_choice = int(input("Press 1 to download the audio separately / 2 if you don't need the audio: "))
            if audio_choice == 1:
                download_audio(vid_choice, url, path)
            if audio_choice == 2:
                print("")
                print("All done!")

            # Restarting the program

        while True:
            print("")
            answer = str(input("Would you like to run the program again? (Y/N)\nPlease type in upper case: "))
            if answer in ('Y', 'N'):
                break
            print("Invalid input. Please try again.")
        if answer == 'Y':
            continue
        else:
            print("")
            print("Thank you for using this program :) Goodbye and stay safe!")
            break


if __name__ == '__main__':
    main()
