# myscripts
Useful scripts written in bash and python

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
