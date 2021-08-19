import pyinotify
import os
from worker import add


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print("Got new file: ", event.pathname)
        if not event.dir and event.pathname.endswith('csv'):
            add.delay(event.pathname)


wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CLOSE_WRITE  # watched events
notifier = pyinotify.Notifier(wm, EventHandler())

wdd = wm.add_watch(os.getcwd(), mask, rec=True, auto_add=True)

while True:
    try:
        notifier.process_events()
        if notifier.check_events():
            notifier.read_events()
    except KeyboardInterrupt:
        notifier.stop()
        break
