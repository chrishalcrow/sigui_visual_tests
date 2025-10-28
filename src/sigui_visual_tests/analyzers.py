from pathlib import Path

import probeinterface as pi
import spikeinterface.full as si

def make_tetrode_analyzer():

    tetrode = pi.generate_tetrode()
    tetrode.device_channel_indices = [0,1,2,3]

    rec, sort = si.generate_ground_truth_recording(
        probe = tetrode,
        num_units=5,
        durations=[600],
    )

    tetrode_analyzer = si.create_sorting_analyzer(sort, rec)

    return tetrode_analyzer

def make_nn64_analyzer():
    
    probe = pi.read_probeinterface(Path(__file__).absolute().parent / Path('resources/nn64.json')).probes[0]
    rec, sort = si.generate_ground_truth_recording(
        probe = probe,
        num_units=50,
        durations=[600],
    )

    nn_analyzer = si.create_sorting_analyzer(sort, rec)
    return  nn_analyzer

def make_NP1_analyzer():

    rec, _, sort = si.generate_drifting_recording()
    NP1_analyzer = si.create_sorting_analyzer(sort, rec)
    return NP1_analyzer


def make_analyzers():

    analyzers = {}

    cached_analyzers_folder = Path(__file__).absolute().parent / Path('../../cached_analyzers')
    cached_analyzers_folder.mkdir(exist_ok=True)

    compute_analyzer_dict = {
        'tetrode': make_tetrode_analyzer,
        'NP1': make_NP1_analyzer,
        'nn64': make_nn64_analyzer,
    }

    for analyzer_name, make_function in compute_analyzer_dict.items():

        tetrode_folder = cached_analyzers_folder / analyzer_name
        if tetrode_folder.is_dir():
            analyzers[analyzer_name] = si.load_sorting_analyzer(tetrode_folder)
        else:
            analyzers[analyzer_name] = make_function()

        if not (cached_analyzers_folder / analyzer_name).is_dir():
            analyzers[analyzer_name].compute([
                'random_spikes',
                'unit_locations',
                'noise_levels',
                'templates',
            ])
            analyzers[analyzer_name].save_as(format='binary_folder', folder = cached_analyzers_folder / analyzer_name)

    return analyzers



