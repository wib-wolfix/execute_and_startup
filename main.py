import os
user=os.getenv("username")
appdata=os.getenv("appdata")
autostart=appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
desk="C:\\users\\"+user+"\\Desktop"
c0d3="""

# CODE HERE

"""
open(autostart+"\\NAME_OF_AUTO_STARTTUP_FILE.pyw","w").write(c0d3)
exec(c0d3)
