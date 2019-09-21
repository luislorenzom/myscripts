#!/bin/bash

# -----------------------------------------
# Variables
# -----------------------------------------
BACKUP_ID=$(date +"%s")

# -----------------------------------------
# Mount NFS backup folder
# -----------------------------------------
sudo mount 192.168.1.77:/media/pi/Kangaroo/nfs /nfs/

# -----------------------------------------
# Create incremental backup of home
# -----------------------------------------
LAST_BACKUP=$(ls -r /nfs/backups/backup.home.*.file | head -1)

if [ -f "$LAST_BACKUP" ]
then
    cp $LAST_BACKUP $(LAST_BACKUP)_copy
    BACKUP_FILE=$LAST_BACKUP
else
    BACKUP_FILE=backup.home.${BACKUP_ID}.file
fi

tar --listed-incremental=backup.home.${BACKUP_ID}.file -cvzf backup.home.${BACKUP_ID}.tar.gz \
${HOME}/.ssh/ \
${HOME}/.bashrc \
${HOME}/workspace/ \
${HOME}/Imágenes/ \
${HOME}/Documentos/ \
${HOME}/Música/ \
${HOME}/Descargas/ \
${HOME}/Vídeos/ \

if [ -z "$LAST_BACKUP" ]
then
    mv BACKUP_NAME backup.home.${BACKUP_ID}.file
    mv $(LAST_BACKUP)_copy $(LAST_BACKUP)
fi


# -----------------------------------------
# Create incremental backup of system
# -----------------------------------------
LAST_BACKUP=$(ls -r /nfs/backups/backup.system.*.file | head -1)

if [ -f "$LAST_BACKUP" ]
then
    cp $LAST_BACKUP $(LAST_BACKUP)_copy
    BACKUP_FILE=$LAST_BACKUP
else
    BACKUP_FILE=backup.system.${BACKUP_ID}.file
fi

tar --listed-incremental=backup.system.${BACKUP_ID}.file -cvzf backup.system.${BACKUP_ID}.tar.gz \
/etc/ \
/usr/ \
/opt/ \
/boot/ \
/sys/

if [ -z "$LAST_BACKUP" ]
then
    mv BACKUP_NAME backup.system.${BACKUP_ID}.file
    mv $(LAST_BACKUP)_copy $(LAST_BACKUP)
fi

# -----------------------------------------
# Umount NFS backup folder
# -----------------------------------------
sudo umount -l /nfs

