# coding=utf-8
from __future__ import absolute_import
import os
import time
import octoprint.plugin

class USBPowerControlPlugin(octoprint.plugin.SettingsPlugin, octoprint.plugin.EventHandlerPlugin, octoprint.plugin.StartupPlugin):
  def __init__(self):
    self.on_command = "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind"
    self.off_command = "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind"

  def get_settings_defaults(self):
    return dict(
      enable_usb_on_connect=True,
      enable_usb_on_startup=True,
      delay_after_usb_enable=2.0
    )

  def on_startup(self, *_):
    self._usb_delay = self._settings.get_float(["delay_after_usb_enable"])
    if self._settings.get_boolean(["enable_usb_on_startup"]):
      self._logger.info("Enabling raspberry pi USB power...")
      os.system(self.on_command)

    if self._settings.get_boolean(["enable_usb_on_startup"]):
      self._logger.info("Patching connect function to enable USB power on connection")
      original_connect=self._printer.connect
      
      def wrapped_connect(*args, **kwargs):
        self._logger.info(
            "Enabling USB power via shell command and sleeping %f seconds." % self._usb_delay)
        os.system(self.on_command)
        time.sleep(self._usb_delay)
        original_connect(*args, **kwargs)
      
      self._printer.connect = wrapped_connect
      return

  def on_event(self, event, payload):
    if event == "Disconnected":
      self._logger.info("Printer disconnected, turning off USB power")
      os.system(self.off_command)
      return

__plugin_implementation__ = USBPowerControlPlugin()
