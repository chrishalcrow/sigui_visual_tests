import spikeinterface.full as si
from sigui_visual_tests.analyzers import make_analyzers
from sigui_visual_tests.plotting import test_waveformview
from pathlib import Path

si.set_global_job_kwargs(n_jobs=4)

def main():

    analyzers = make_analyzers()
    screenshots_folder = Path("screenshots")
    screenshots_folder.mkdir(exist_ok=True)

    for analyzer_name, analyzer in analyzers.items():
        
        test_waveformview(analyzer, analyzer_name, Path(screenshots_folder / "waveformview_main"))

if __name__ == '__main__':
    main()