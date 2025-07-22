import os
import subprocess
import time
from watchdog.observers import Observer  # type: ignore
from watchdog.events import FileSystemEventHandler  # type: ignore
import shlex
from dotenv import load_dotenv

load_dotenv()

CUSTOM_ADDONS_PATH = os.path.abspath("./addons/custom")  # sesuaikan jika berbeda
DB_NAME = "odoo18-BroilerX"
DOCKER_SERVICE = "odoo"

def get_all_module_names(path):
    return ' '.join([
        name for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name)) and not name.startswith('.')
    ])

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.module_names = get_all_module_names(CUSTOM_ADDONS_PATH)

    def on_modified(self, event):
        if event.src_path.endswith(('.py', '.xml', '.js')):
            print(f"[Watcher] Change detected: {event.src_path}")

            restart_cmd = f"docker compose restart {DOCKER_SERVICE}"
            print(f"[Watcher] Restarting Odoo: {restart_cmd}")
            subprocess.run(restart_cmd, shell=True)

            time.sleep(2)  # Wait for Odoo to restart 2 seconds


            cmd = f'docker compose exec {DOCKER_SERVICE} odoo --dev=all -u "{self.module_names}" -d {DB_NAME}'

            print("[DEBUG] Final CMD String:", cmd)
            print("[DEBUG] Parsed Args:", shlex.split(cmd))
            subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, CUSTOM_ADDONS_PATH, recursive=True)
    observer.start()
    print(f"[Watcher] Watching all modules in: {CUSTOM_ADDONS_PATH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
