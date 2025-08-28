from rich.progress import Progress
import time

with Progress() as p:
    t = p.add_task("Download...", total=500)
    while not p.finished:
        p.update(t, advance=1)
        time.sleep(0.05)


with Progress() as p:
    t = p.add_task("Installing...", total=500)
    while not p.finished:
        p.update(t, advance=1)
        time.sleep(1.100)