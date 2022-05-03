# # -*- coding: utf-8 -*-


# timeout = 600
# bind = '0.0.0.0:8001'
# accesslog = '-'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" in %(D)sµs'



from os import environ
# -- coding: utf-8 --

from config.settings import SERVER_PORT, SERVER_HOST

# bind = f"0.0.0.0:{environ.get('SERVER_PORT')}"
# bind = f"0.0.0.0:{SERVER_PORT}"
bind = f"{SERVER_HOST}:{SERVER_PORT}"
accesslog = "-"
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" in %(D)sµs'
)
