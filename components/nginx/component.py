from batou.component import Component, platform
from batou.lib.file import File


class Nginx(Component):

    port = 80

    def configure(self):
        self.appserver = self.require_one('etherpad:http')
        self += File('etherpad.conf')


@platform('debian', Nginx)
class ReloadNginx(Component):

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd('sudo /etc/init.d/nginx reload')
