from ffprobe import FFProbe as ffprobe
import ffmpeg
import subprocess as sp

def exec(cmd):
    return sp.Popen(cmd, stdout = sp.PIPE, stderr = sp.PIPE).communicate()

def combiner(videos, output = "video.mp4"):
    maxRes = (0, 0)
    maxFPS = 0
    filteredVids = []
    for vid in videos:
        r = ffprobe(vid)
        if r.video:
            newVid = (vid, vm := r.video[0], bool(r.audio))
            maxRes = (max(int(vm.width), maxRes[0]), max(int(vm.height), maxRes[1]))
            maxFPS = max(vm.framerate, maxFPS)
            filteredVids.append(newVid)
        else:
            print(f"""File {vid} does not contain any video streams, skipping.""")
    assert len(filteredVids) > 0, "Error: Found no suitable videos."
    
    for filename, properties, hasAudio in filteredVids:
        print(filename)
        # if properties.framerate != maxFPS:
            #
    
    print(filteredVids)
    print(maxRes, maxFPS)

if __name__ == "__main__":
    from sys import argv
    #do args stuff
    
    videos = [
        r"C:\Users\Administrator\Documents\Projects\Video_Combiner\bruh\1631887446622.webm",
        r"C:\Users\Administrator\Documents\Projects\Video_Combiner\bruh\fasdf.mp4"
    ]
    output = r"C:\Users\Administrator\Documents\Projects\Video_Combiner"
    combiner(videos, output)