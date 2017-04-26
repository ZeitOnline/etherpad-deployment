from batou.component import Component
from batou.lib.archive import Extract
from batou.lib.download import Download
from batou.lib.file import File
from batou.lib.supervisor import Program
from batou.utils import Address


class Etherpad(Component):

    port = 9001

    def configure(self):
        self += Download(
            'https://github.com/ether/etherpad-lite/archive/1.6.1.tar.gz',
            checksum='md5:2de5cf27933cf687dcca9ea2350e38d4')
        self += Extract(self._.target, strip=1, target='.')
        self += InstallDependencies()

        self.address = Address(self.host.fqdn, self.port)
        self.provide('etherpad:http', self.address)

        self += File('settings.json')

        self += Program(
            'etherpad',
            options={'startsecs': 20},
            command='/usr/bin/node',
            args='%s --settings %s' % (
                self.map('node_modules/ep_etherpad-lite/node/server.js'),
                self.map('settings.json'))
        )


class InstallDependencies(Component):

    def configure(self):
        self.success_marker = self.map('node_modules/.batou.npm.success')

    def verify(self):
        self.assert_file_is_current(
            self.success_marker, [self.map('src/package.json')])

    def update(self):
        self.cmd(self.map('bin/installDeps.sh'))
        self.touch(self.success_marker)
