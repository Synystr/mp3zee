#********** LIBRARY IMPORTS **********
#os for system calls, time for delays so user can read output

import os, time

#********** FUNCTION DEFS ************

def mp3():
	os.system("clear")
	urls = []
	currenturl = "1"
	while currenturl != "":
    		currenturl = raw_input('Enter URL (leave blank to proceed): ')
    		if currenturl == "":
        		break
    		urls.append(currenturl)
    		os.system("clear")

	print ("Downloading videos:")
	time.sleep(3)

	count = 1
	for i in urls:
    		if count <= 9:
    			os.system("~/youtube-dl -f best -o 'Track_0" + str(count) + "_-_%(title)s.%(ext)s' --restrict-filenames --prefer-ffmpeg --write-description --write-info-json --write-annotations --write-thumbnail --extract-audio --audio-format mp3 " + i)
    		else:
    			os.system("~/youtube-dl -f best -o 'Track_" + str(count) + "_-_%(title)s.%(ext)s' --restrict-filenames --prefer-ffmpeg --write-description --write-info-json --write-annotations --write-thumbnail --extract-audio --audio-format mp3 " + i)
    		count = count + 1
    		os.system("clear")
	print ("Finished downloading queue.")
	
	name = raw_input("Give a name to the compilation you've made:")
	name = name.replace(" ", "_")
	os.system("mkdir " + name)
	os.system("mv *.mp3 " + name)
	print("Moved MP3 into a folder called " + name + ".")
	os.system("mkdir " + name + "/description")
	os.system("mv *.description " + name + "/description")
	print ("Saved description to file.")
	os.system("mkdir " + name + "/meta")
	os.system("mv *.info.json " + name + "/meta")
	print ("Saved metadata to file.")
	os.system("mkdir " + name + "/annotations")
	os.system("mv *.annotations.xml " + name + "/annotations")
	print ("Saved annotations to file.")
	os.system("mkdir " + name + "/thumb")
	os.system("mv *.jpg " + name + "/thumb")
	print ("Saved thumbnails to file.")
	os.system("mv " + name + " storage/downloads")
	print ("All finished. Moved folder to Download folder on internal storage. Hit Enter to return to main menu.")
	raw_input("")
	os.system("clear")
	
def mp4():
	os.system("clear")
	urls = []
	currenturl = "1"
	while currenturl != "":
    		currenturl = raw_input('Enter URL (leave blank to proceed): ')
    		if currenturl == "":
        		break
    		urls.append(currenturl)
    		os.system("clear")

	print ("Downloading videos:")
	time.sleep(3)

	for i in urls:
    		os.system("~/youtube-dl -f best -o '%(title)s.%(ext)s' --restrict-filenames --prefer-ffmpeg " + i)
    		os.system("clear")
	
	name = raw_input("Give a name to the compilation you've made:")
	name = name.replace(" ", "_")
	os.system("mkdir " + name)
	os.system("mv *.mp4 " + name)
	print("Moved videos into a folder called " + name + ".")
	os.system("mv " + name + " storage/downloads")
	print ("All finished. Moved to Download folder on internal storage. Hit Enter to return to main menu.")
	raw_input("")
	os.system("clear")

def update():

	os.system("clear")
	os.system("apt update && apt upgrade -y")
	print("Checking for youtube-dl and FFMpeg...")
	time.sleep(3)

	os.system("apt-get install -y wget")

	time.sleep(3)
	
	os.system("wget https://yt-dl.org/downloads/latest/youtube-dl -O ~/youtube-dl && chmod a+rx ~/youtube-dl")
	os.system("termux-fix-shebang ~/youtube-dl")

	time.sleep(3)

	print("Now updating youtube-dl...")
	os.system("~/youtube-dl -U")

	print("Installing/Updating lame codec through apt-get...")
	time.sleep(2)
	os.system("apt-get install -y lame")
	print("Installing/Updating python-dev through apt-get...")
	time.sleep(2)
	os.system("apt-get install -y python-dev")
		
	time.sleep(5)
	os.system("clear")
	menu()

def menu():


	os.system("clear")
	while 1==1:
		print("********************************")
		print("*       Leecher v. 0.3         *")
		print("*       by Misanthr0pe         *")
		print("********************************")
		print("")
		print("")
		print("Select an option:")
		print("")
		print("1. Download MP3 from Youtube, Soundcloud, Bandcamp, etc.")
		print("2. Download Video to MP4")
		print("3. Quit Program")
		print("")
		print("")
		print("More options coming soon...")
		choice = input("Option: ")
		if choice == 1:
			mp3()
		if choice == 2:
			mp4()	
		if choice == 3:
			break

os.system("clear")
choice = raw_input("Would you like to check for updates/verify files? y for yes, anything else for no: ")
if choice == "y":
	update()
else:
	menu()

