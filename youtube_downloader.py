import pytube

#get the url from user
url = input("Enter the URL of the YouTube video: ")

#create a YouTube object
yt = pytube.YouTube(url)

#filter out the videos with the highest resolution in MP4 format
highest_res_videos = yt.streams.filter(file_extension='mp4')

#filter out the streams with None resolution
highest_res_videos = [stream for stream in highest_res_videos if stream.resolution != None]

#convert the list of streams into a set to remove the duplicate items
highest_res_videos = set(highest_res_videos)

#show all the available resolutions
for index, stream in enumerate(highest_res_videos):
    print(f"{index}: {stream.resolution}")

#get the index of the desired resolution from user
desired_res = int(input("Enter the index of the desired resolution: "))

#get the video with the desired resolution
video = list(highest_res_videos)[desired_res]

#download the video
video.download()

print("Video downloaded successfully!")


