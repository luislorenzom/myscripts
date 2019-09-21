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

## publicIpNotifier
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
CRON_LINE="*/15 * * * * $HOME/workspace/myscripts/publicIpNotifier/publicIpNotifier.py > /var/log/publicIpNotifier.out 2>&1"
(crontab -u $USER -l; echo "$CRON_LINE" ) | crontab -u $USER -
```