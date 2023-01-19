#! /usr/bin/bash
echo "EGGY REPLACE THIS ECHO WITH NV GPU INSTALLATION"
if zenity --question
then
	echo "EGGY REPLACE THIS ECHO WITH NV GPU POST INSTALLATION, Reboot i assume"
	/etc/nobara/scripts/cosmo-nvidia-wizard/end.sh
else
	/etc/nobara/scripts/cosmo-nvidia-wizard/end.sh
fi
