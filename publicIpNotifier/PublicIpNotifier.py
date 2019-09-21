# -*- coding: utf-8 -*-

from environs import Env

import logging
import requests
import os
import smtplib

# --------------------------
# Constants
# --------------------------
env = Env()
env.read_env('../.env')

TO = env('TO')
FROM = env('FROM')
PASSWD = env('PASSWD')

NOIP_USER = env('NOIP_USER')
NOIP_PASSWD = env('NOIP_PASSWD')
NOIP_HOSTNAME = env('NOIP_HOSTNAME')

def _sendMail(newIp, oldIp):
    """ Send email notifying that IP has changed
        
        Args:
            newIp: your old ip
            oldIp: new ip provided
        
        Returns:
            None
    """
    try:
        # Config SMTP server
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(FROM, PASSWD)

        # Writes message
        subject = 'RPI BLACKWOODPInes - IP changed notify'
        body = 'You public has been changed:\n old ip ~> ' + oldIp + '\n new ip ~> ' + newIp
        message = 'Subject: {}\n\n{}'.format(subject, body)

        # Sends it
        server_ssl.sendmail(FROM, TO, message)
        server_ssl.close()

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.error(message)

if __name__ == '__main__':
    
    # Logging
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    
    # Sources
    IP_FILE = '~/.config/ip.info'
    CURRENT_IP = requests.get('http://ip.42.pl/raw').text
    
    # Retrieve saved IP
    if os.path.exists(IP_FILE):
        with open(IP_FILE, "r") as f:
            saved_ip = f.read()
    else:
        saved_ip = None
    
    # IP comparison
    if CURRENT_IP != saved_ip:
        
        # Changed file
        with open(IP_FILE, "w") as f:
            f.seek(0)
            f.write(CURRENT_IP)
            f.truncate()
            f.close()
        
        # Send email
        _sendMail(CURRENT_IP, saved_ip)
        
        # Connect with NO-IP rest API
        url = "http://" + NOIP_USER + ":" + NOIP_PASSWD + "@dynupdate.no-ip.com/nic/update?hostname=" + NOIP_HOSTNAME + "&myip=" + CURRENT_IP
        r = requests.get(url)
        logging.info(r.text)
