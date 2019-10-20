# myscripts
Useful scripts written in bash and python

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
