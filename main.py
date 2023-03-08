# Copyright (c) 2020 brainlife.io
#
# This file is the main script for applying baseline correction to MEG/EEG Epochs files.
#
# Author: Kamilya Salibayeva
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


fname = config['epochs']
tmin = config['tmin']
tmax = config['tmax']

epochs = mne.io.read_epochs(fname)
epochs.apply_baseline((tmin,tmax))

# save mne/epochs: blc stands for baseline corrected
epochs.save(os.path.join('out_dir','blc-epo.fif'))

