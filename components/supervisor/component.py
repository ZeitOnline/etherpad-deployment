from batou.lib.debian import Logrotate
from batou.lib.cron import CronTab
import batou.lib.debian


class Supervisor(batou.lib.debian.Supervisor):

    logrotate = True
