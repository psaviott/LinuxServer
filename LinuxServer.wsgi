activate_this = '/var/www/LinuxServer/LinuxServer/venv3/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/LinuxServer/LinuxServer")
sys.path.insert(1, "/var/www/LinuxServer")

from __init__ import app as application
application.secret_key = 'super_secret_key'
