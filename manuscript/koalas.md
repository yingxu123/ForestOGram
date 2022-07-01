-----
title: 'a Data Analysis of Koala Bellows and Vocalisations'
tags:
  - Ecologicolal Monitoring
  - Data Standardisation
  - Neuromorphic Engineering
  - Machine Learning Data Set
  - Reproducible Data Engineering Workflow

authors:

  - name: Ying Xu
    affiliation: International Center for Neuromorphic Systems, MARCs, Western Sydney University

  - name: Saeed
    affiliation: International Center for Neuromorphic Systems, MARCs, Western Sydney University

  - name: Russell Jarvis
    affiliation: International Center for Neuromorphic Systems, MARCs, Western Sydney University

date: June  2022

Bibliography: paper.bib

### Summary

We enhanced an audio koala monitoring approach, using a spiking cochlea model so that it to perform koala count estimation, by classifying recordings as either containing koalas or not, counting koala occurences ultimately count information could be used to assign the presence of koalas to a geographic spaces, giving rise to density information.

## Methods

A bio-inspired spiking cochlea model is efficient at noise suppression, and signal detection. We used an existing Python tool PyAudioAnalysis to perform silence removal and koala recording signal segmentation. We then used the cochlea model to pre-process the mp3 files. Cochlea model pre-processing facilitated correct koala classification because it was able to re-represent koala bellows as a more sparse set of spectral features.

PyAudioAnalysis also contained a two spectral based feature extraction algorithms that where used to inform a machine learning classifier.


### Statement of Need

The success of data driven temporal-spatial models in ecology may depend on the quality observations recorded from the field. Low powered embedded real time sound source identifiers are an expected advance in the field of ecological surveying, but the realization of this technology has been hampered by difficulties in machine learning (solving the cocktail party effect), and the prohibitive requirement that expensive expert ecologists edit verify and manually intervene at the data engineering level. Generally expert ecologists are in demmand and they are too not available to data-engineer training and verification datasets.


#### Data Descriptors

Data consists of male koalas from coastal eucalytpus forests

### Results

Plot of cochleagram versus MEL spectrogram showing greater spectral feature sparsity of Cochleagram over spectrogram.
