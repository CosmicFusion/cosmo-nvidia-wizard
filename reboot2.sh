#! /bin/bash

	zenity --question \
       --title="Reboot Required." \
       --width=600 \
       --text="`printf "The system requires a reboot before newly installed drivers and firmware can take effect. Would you like to reboot now?\n\n"`"

     if [ $? = 0 ]; then
     	shutdown -r now &>>/tmp/nvcheck.log || {
          		zenity --error --text="Failed to issue reboot:\n\n $(cat /tmp/nvcheck.log)\n\n Please reboot the system manually."
          		exit 1
        }
     else
   	exit 0
     fi
