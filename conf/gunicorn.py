command = "__INSTALL_DIR__/venv/bin/gunicorn"
pythonpath = "__INSTALL_DIR__"
workers = 4
user = "__APP__"
bind = ['127.0.0.1:__PORT__']
pid = "/run/gunicorn/__APP__-pid"
errorlog = "/var/log/__APP__/error.log"
accesslog = "/var/log/__APP__/access.log"
access_log_format = '%({X-Real-IP}i)s %({X-Forwarded-For}i)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
loglevel = "warning"
capture_output = True
