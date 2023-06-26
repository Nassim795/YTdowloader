import pytube

url = input("Enter the URL of the YouTube video: ")

yt = pytube.YouTube(url)

highest_res_videos = yt.streams.filter(file_extension='mp4')

highest_res_videos = [stream for stream in highest_res_videos if stream.resolution != None]

highest_res_videos = set(highest_res_videos)

for index, stream in enumerate(highest_res_videos):
    print(f"{index}: {stream.resolution}")

desired_res = int(input("Enter the index of the desired resolution: "))

video = list(highest_res_videos)[desired_res]

video.download()

print("Video downloaded successfully!")


