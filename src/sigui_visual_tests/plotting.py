from spikeinterface_gui import run_mainwindow
import spikeinterface.full as si
import time
from pathlib import Path

si.set_global_job_kwargs(n_jobs=4)

def save_screenshot(win, file_name):
    pixmap = win.grab()
    pixmap.save(str(file_name))

def test_waveformview(analyzer, analyzer_name: str, screenshot_folder: Path):

    screenshot_folder.mkdir(exist_ok=True)

    layout = {'zone1': ['waveform']}
    for a in range(2,9):
        layout[f'zone{a}'] = []
    win = run_mainwindow(analyzer, mode="desktop", start_app=False, curation=True, layout=layout)

    win.views['unitlist']._qt_on_only_next_shortcut()
    win.views['unitlist']._qt_on_only_next_shortcut()
    win.views['unitlist']._qt_on_only_next_shortcut()

    time.sleep(0.1)

    save_screenshot(win, screenshot_folder / f"{analyzer_name}_one_unit.png")


