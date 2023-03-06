1. Put all the resources in templates folder.
2. For deployment: you need two files: requirements.txt, app.yaml
3. To generate requirements.txt: pip3 freeze > requirements.txt
4. Go to gcloud and create a new project
5. Click on open console
6. git clone your repo
7. gcloud app deploy

Note: name of the pyhton file should be main.py

If any file is placed that is unable to be read. It is becuase of permissions issue. So, place it at /tmp folder. So, if you want to use example.db. Use /tmp/example.db location.
