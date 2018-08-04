# mp3zee
A python2 script, designed, tested and optimized for Termux running on Android, utilizing youtube-dl to batch download videos from Youtube and other streaming sites, and automatically convert them to mp3 and package them. The script then moves the folder to the Download folder on your internal storage.

NOTE: This script was written, optimized and applied to a Termux environment running on Android, with Termux storage set up. If you are experiencing errors when the script tries to move your files to accessible internal storage, refer to https://termux.com/storage.html for the fix.

1. git clone https://github.com/Synystr/mp3zee
2. cd mp3zee
3. python2 mp3zee.py

NOTE: The first time you run the script, you will want to run the initial update/install operation. It will not work until you do this. If the script starts throwing errors when trying to download, run the initial update again, as youtube-dl will most likely have an updated version.

A better-streamlined version of this update process is planned for a future version.

CURRENT OPTIONS

1. Download MP3 from Youtube, Soundcloud, Bandcamp, etc. - Allows you to paste in URL's to streaming videos, which the script keeps track of and batch downloads
2. Download Video to MP4 - Same as above, retaining video and skipping the conversion to mp3

More options as the ideas for them come up.
