import sublime
import sublime_plugin


class ToggleReadonlyModeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if self.view.is_read_only():
      self.view.set_read_only(False)
      self.view.erase_status('read_only_mode')
    else:
      self.view.set_read_only(True)
      self.view.set_status('read_only_mode', 'ReadOnly')

  def is_checked(self):
    return self.view.is_read_only()

class ToggleReadonlyListener(sublime_plugin.EventListener):
  def on_load_async(self, view):
    if view.is_read_only():
      view.set_status('read_only_mode', 'ReadOnly')
    elif view.settings().get('read_only_mode'):
       view.set_read_only(True)
       view.set_status('read_only_mode', 'ReadOnly')
