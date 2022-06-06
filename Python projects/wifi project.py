import subprocess
import re
cmd_output = subprocess.run(['netsh','wlan','show','profiles'],capture_output=True).stdout.decode()
profile_names != 0:
    for name in profile_names:
        wifi_profile={}
        profile_info = subprocess.run(['netsh','wlan','show','profiles',name],capture_output=True).stdout.decode()
        if re.search("security key      :Absent",profile_info):
            continue
        else:
            wifi_profile['ssid'] = name
            profile__info_password = subprocess.run(['netsh','wlan','show','profiles',name,'key=clear'],capture_output=True).stdout.decode()
            password = re.search("key content                     :(.*)\r",profile_info_password)
            if password == None:
                wifi_profil["password"] = None
            else:
                wifi_profile["password"] = password[1]
        wifi_list.append(wifi_profile)
for i in range(len(wifi_list)):
    print(wifi_list[i])