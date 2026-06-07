import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from agent import process_task

class NewTaskHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_processed_time = 0

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.md'):
            current_time = time.time()
            if current_time - self.last_processed_time > 10:
                if os.path.getsize(event.src_path) > 10:
                    print(f"📂 Content detected! Processing in 3 seconds...")
                    time.sleep(3) # Wait for you to finish typing the sentence
                    self.last_processed_time = current_time
                    process_task(event.src_path)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    watch_path = os.path.join(base_dir, 'vault', 'Inbox')
    event_handler = NewTaskHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=False)
    print(f"🤖 AI Employee active! Wait 10s between requests.")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()