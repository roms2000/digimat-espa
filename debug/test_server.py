import time
from digimat.espa import LinkSerial, Server, MultiChannelServer


class MyMultiChannelServer(MultiChannelServer):
    def onNotification(self, notification):
        print notification
        if notification.isName('calltopager'):
            print "[%s]->paging(%s) with message <%s>..." % (notification.source,
                 notification.callAddress,
                 notification.message)


servers=MyMultiChannelServer()

link=LinkSerial('ts940', 'COM5', 9600, 'N', 8, 1)
servers.add(Server(link))

link=LinkSerial('espa2', 'COM6', 9600, 'N', 8, 1)
servers.add(Server(link))

servers.run()
