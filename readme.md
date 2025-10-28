A repo to help do visual tests of spikeinterface-gui.

Clone the repo, install your dev version of spikeinterface-gui and run `scripts/make_plots.py`:

``` bash
git clone https://github.com/chrishalcrow/sigui_visual_tests.git
cd sigui_visual_tests
uv add -e path/to/spikeinterface-gui
uv run scripts/make_plots.py
```

Add your own visual tests by defining a new `test_` in `src/sigui_visual_tests/plotting` and your own
analyzers in `src/sigui_visual_test/analyzers.py`.

Will keep an up-to-date of all analyzer/test screenshots in `screenshots`.