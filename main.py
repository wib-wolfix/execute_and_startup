import os
appdata=os.getenv("appdata")
autostart=appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
c0d3="""

# CODE HERE

"""
open(autostart+"\\NAME_OF_AUTO_STARTTUP_FILE.pyw","w").write(c0d3)
exec(c0d3)
