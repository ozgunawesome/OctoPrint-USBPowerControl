# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import os

class USBPowerControlPlugin(octoprint.plugin.EventHandlerPlugin):

  def __init__(self):
    self.on_command = "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind; sleep 1"
    self.off_command = "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind"

  def on_after_startup(self):
    self._logger.info("USB Power Control loaded")
    pass

  def on_event(self, event, payload):
    if event == "Disconnected":
      self._logger.info("Printer disconnected, turning off USB power")
      os.system(self.off_command)
      return
    elif event == "Connecting":
      self._logger.info("Printer will connect, turn on USB power")
      os.system(self.on_command)
      return


__plugin_name__ = "USB Power Control"
__plugin_version__ = "0.0.1"
__plugin_description__ = "Cut Raspberry Pi 3B+ USB power on disconnect. Re-enable on connect"
__plugin_implementation__ = USBPowerControlPlugin()
