'''
Created on 30 avr. 2015

@author: Bertrand Verdu
'''
import uuid
import socket
from upnpy_spyne.devices import Device
from upnpy_spyne.services.switchpower import SwitchPower


class MainDevice(Device):
    '''
    classdocs
    '''

    def __init__(self, path, player, datadir):
        super(MainDevice, self).__init__(path)
        self._description = None
        self.datadir = datadir
        self.player = player
        self.type = 'UpnP'
        self.deviceType = 'urn:schemas-upnp-org:device:BinaryLight:1'
        self.manufacturer = "upnpy"
        self.manufacturerURL = "http://github.com/bverdu/upnpy"
        self.manufacturerInfo = "coucou, c'est nous"
        self.modelDescription =\
            "onDemand Light switch"
        self.modelName = "Snap_Light (OpenHome)"
        self.version = (1, 0,)
        self.uuid = str(
            uuid.uuid5(uuid.NAMESPACE_DNS, socket.gethostname() + path))
        self.switch = SwitchPower(
            datadir + 'xml/switchpower.xml', self.player, name=self.name)
        self.switch.parent = self
        self.services = [self.switch]
