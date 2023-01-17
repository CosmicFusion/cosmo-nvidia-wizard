#! /bin/bash

	zenity --question \
       --title="Reboot Required." \
       --width=600 \
       --text="`printf "The system requires a reboot before newly done actions can take effect. Would you like to reboot now?\n\n"`"
