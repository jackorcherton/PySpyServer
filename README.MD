File Server
--------------
This is the file/web server used to store & fetch the database. A demo server can be viewed at https://error404coventry.hopto.org. This server is also used
as a reverse ssh server.
This program will run on Linux.

Setup
--------------
Copy these files into the root directory (or other place), apart from the fileServer.py (otherwise anyone can inspect code - place in root directory (/)) - NB: it is possible to access any files/sub-folders within the folder from which you run the script!!!
Type the following, 'sudo crontab -e', then the following: '@reboot python3 /fileServer.py' - or change the path to where you placed the folder

Website
--------------
Currently, our website just redirects you to the projects main website - https://pyspy.jordanclark.uk. However, you are able to change this - just go to the index.html file,remove line 3 and write your own content.

Robots.txt
--------------
As I do not wish for the site to be searched (and for database to be found) - I have added a robots.txt files.

Security
--------------
To prevent anyone from uploading the file, the server will only accept post requests with files that are named 'info.sqlite3' - we recommend that you change
this file name, otherwise anyone who uses this software could potenially overload the server/fill it up with usless files.

Dependancies
-------------------------
Python 3.8+ (should work with any interpreter in the 3.x branch)
Server/Static IP for the Web Server
Let's Encrypt Free SSL Certificate (allows for HTTPS encrypted data transfer)

Legal
-------------------------
PLEASE NOTE - this code is only for educational purposes - and does work on a network. Due to what these tools do, please do not run them on any network that you do not have permision too - we accept no liability.