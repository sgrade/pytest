import subprocess


threshold = 15
partition = "/"

df = subprocess.Popen(["df", "-h"], stdout = subprocess.PIPE)
for line in df.stdout or []:
    #split into space-separated fields
    splitline = line.decode().split()
    # the % full figure is in field 4,
    # the mount point in field 5
    if splitline[5] == partition:
        if int(splitline[4][:-1]) > threshold:
            print("WARNING!")

