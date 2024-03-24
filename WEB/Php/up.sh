echo "Loged in user: $(whoami)"
echo "Terminal : $TERM"
echo "login time : $(who -b | awk '{print $3, $4}')"
echo -e "\ncurent process : "
ps aux | grep $(whoami)

echo -e "\nDisk Usage for home :"
du -h --max-depth=1 $HOME

echo -e "curent Woking DIR:"
pwd

echo -e "system Uptime : "
uptime

echo -e "\n Number of logged-in users :  who | wc -1 awk '{print $1 }' "
