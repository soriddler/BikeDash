import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)

class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            logging.error("Stopping the Watcher...")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            logging.debug (f"Received created event - {event.src_path}")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            logging.info (f"Received modified event - {event.src_path}")

        elif event.event_type == 'moved':
            # Taken any action here when a file is modified.
            logging.info (f"Received moved event - {event.src_path} to {event.dest_path}")


if __name__ == '__main__':
    w = Watcher()
    w.DIRECTORY_TO_WATCH = "."
    w.run()