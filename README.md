# myscripts
Useful scripts written in bash and python

## FromChromeToMP3
Script which downloads the youtube songs saved in certain bookmark

#### env variables
* **DOWNLOAD_FOLDER**: folder where song will be save
* **SOURCE_FILE**: where is the bookmark file (Linux ~> $HOME/.config/google-chrome/Default/Bookmarks; Windowns ~> AppData\Local\Google\Chrome\User Data\Default)
* **BOOKMARK_ROOT_FOLDER_NAME**: bookmark name where are the urls

#### How to run it:

```sh
python toMp3FromChrome.py 
```

## FindWordAndPageInPDF
Script which find and report where some word appears in a PDF file

#### script variables
* **WORD_TO_SEARCH**: the word that you want to find
* **SOURCE_FILE**: path to pdf file where script is going to look up

#### How to run it:

```sh
python findWordAndPageInPDF.py foo /home/luis/Documents/test.pdf
```

## PublicIpNotifier
Script which detect and notify the public ip changes. Also, it replaces the public ip in noip domain

#### env variables
* **TO**: who receives the notification
* **FROM**: who sends the notification mail
* **PASSWD**: From account's password
* **NOIP_USER**: NO-IP account
* **NOIP_PASSWD**: N: NO-IP password
* **NOIP_HOSTNAME**: NO-IP domain

#### How to run it:

```sh
CRON_LINE="*/15 * * * * python $HOME/workspace/myscripts/publicIpNotifier/publicIpNotifier.py > /var/log/publicIpNotifier.out 2>&1"
(crontab -u $USER -l; echo "$CRON_LINE" ) | crontab -u $USER -
```

## (Incremental) Backup System
Script which backup your important files/folders (such as: /opt, /home, etc) against NFS.

#### script variables
There is no script variables, because there is a lot of casuistry, so my recommendations are:

* line 6: set yours backup ids
* line 11: mount remote/NFS folder
* line 16: remote folder where backups will be safe
* line 26: stablish what folders/files in your home are in the home_backup
* line 56: stablish what folders in your root (/) are in the system_backup

#### How to run it:

```sh
CRON_LINE="59 23 * * FRI bash $HOME/workspace/myscripts/backup_system/incremental_backup.sh > /var/log/backup_system.out 2>&1"
(crontab -u $USER -l; echo "$CRON_LINE" ) | crontab -u $USER -
```