import os
import time
import stat
from http.server import ThreadingHTTPServer
from http.server import BaseHTTPRequestHandler


HEALTH_DAEMON_PORT = int(os.environ.get('HEALTH_DAEMON_PORT') or '8081')
HEALTH_DAEMON_MAX_HOURS_SINCE_LAST_BACKUP = int(os.environ.get('HEALTH_DAEMON_MAX_HOURS_SINCE_LAST_BACKUP') or '72')
PG_BACKUP_FILENAME = os.environ.get('PG_BACKUP_FILENAME')


def get_hours_since_last_backup():
    seconds = time.time() - os.stat(PG_BACKUP_FILENAME)[stat.ST_MTIME]
    return seconds / 60 / 60


class HealthDaemonHTTPRequestHandler(BaseHTTPRequestHandler):

    def _send_ok(self, msg='OK'):
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(msg.encode())

    def _send_error(self, error='Server Error', status_code=500):
        self.send_response(status_code)
        self.end_headers()
        self.wfile.write(error.encode())

    def do_GET(self):
        hours_since_last_backup = get_hours_since_last_backup()
        msg = '{} hours since last backup'.format(hours_since_last_backup)
        if hours_since_last_backup > HEALTH_DAEMON_MAX_HOURS_SINCE_LAST_BACKUP:
            self._send_error(error='ERROR: ' + msg)
        else:
            self._send_ok(msg='OK: ' + msg)


class HealthDaemonHTTPServer(ThreadingHTTPServer):

    def __init__(self):
        print("Starting health daemon on port {}".format(HEALTH_DAEMON_PORT))
        super(HealthDaemonHTTPServer, self).__init__(('0.0.0.0', HEALTH_DAEMON_PORT), HealthDaemonHTTPRequestHandler)


def start():
    HealthDaemonHTTPServer().serve_forever()


if __name__ == '__main__':
    start()
