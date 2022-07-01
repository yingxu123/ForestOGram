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

Data consists of rich and complicated bird and bat vocalisations in a confounding ecological setting.

Main endemics/natives:

1. [Pink Pigeon](https://xeno-canto.org/species/Nesoenas-mayeri) - _Nesoenas mayeri_
2. [Mauritius Bulbul](https://xeno-canto.org/species/Hypsipetes-olivaceus) - _Hypsipetes olivaceus_
3. [Echo Parakeet](https://xeno-canto.org/species/Psittacula-eques) - _Psittacula eques_
4. [Cuckoo Shrike](https://xeno-canto.org/species/Lalage-typica) - _Lalage typica_
5. [Mauritius Kestrel](https://xeno-canto.org/species/Falco-punctatus) - _Falco punctatus_
6.  [Mascarene paradise flycatcher](https://xeno-canto.org/species/Terpsiphone-bourbonnensis) - _Terpsinophone Bourbonensis_
7. [Reunion Grey White-eye](https://xeno-canto.org/species/Zosterops-borbonicus) - _Zosterops borbonicus_

Occasional endemics/natives:

8. [White-tailed Tropicbird](https://xeno-canto.org/species/Phaethon-lepturus) - _Phaeton lepturis_
9. [Mascarene Swiftlet](https://xeno-canto.org/species/Aerodramus-francicus) - _Aerodramus francicus_
10. [White-throated needletail](https://xeno-canto.org/species/Hirundapus-caudacutus) - _Hirundapus caudacutus_

Bats (where to get audio?)

1. [Mauritian flying fox](https://en.wikipedia.org/wiki/Mauritian_flying_fox) - _Pteropus niger_
2. [Mauritian tomb bat](https://en.wikipedia.org/wiki/Mauritian_tomb_bat) -  _Taphozous mauritianus_

Alien:

1. [Red-whiskered bulbul](https://xeno-canto.org/explore?query=Pycnonotus%20jocosus) - Pycnonotus jocosus
2. [Rose-ringed Parakeet](https://xeno-canto.org/species/Psittacula-krameri) - _Psittacula krameri_
3. [Malagasy turtle dove](https://xeno-canto.org/species/Nesoenas-picturatus) - _Nesoenas picturatus_



### Results

**Place holder:** By entering an author’s name into the search box, a system of API calls and web resource requests collects and analyzes text written by that author from the dissemin API. Our tool contrasts the queried authors readability with expected science readability scores because it has pre-processed and quantified the existing corpus of publicly licenced scientific texts contained in ART Corpus (creative commons license), as well as a number of available text repositories and common resources with varying complexity (see Table).

**Place holder:**  After querying an author, the readability of the author's work is evaluated by a variety of pre-established metrics. We used  “text_standard,” a readability consensus score that returns the average estimated school grade level required to understand the text. Results from the dissem query include the number of documents on which the readability score was based. Each mined text is presented to the user in a table with an active link to the source text. This allows the user to verify that the results are correct and also provides individual readability scores for each text source.

### A Conventional Heading
**Place holder:** This work belongs to an emerging scientific discipline that seeks to quantify and understand scientific writing scientifically. Readability metrics have improved in robustness since the publication of the document "the Readability of Science is Declining over Time"[@Plavén-Sigray:2017]. The data set obtained from the Readability of Science is Declininig over Time[@Plavén-Sigray:2017] used a custom implementation of the Flesch reading grade metric, which sometimes yielded negative results, and may have under reported very high readability results. Given the availability of newer more robust readability metrics, it is important to test and calibrate the newer readability metrics against current scientific documents. Text-stats standard obtains a readability metric by averaging over 9 different readability metrics. The presence of frequency word clouds, and large word word-clouds, and hard passages make it possible to sanity check the text-stat metrics as applied to scientific documents. Word clouds act to validate higher readability metrics. Without the word clouds reading grades of >60 might give cause for doubt.

**Place holder:** Generally other science text scraping tools might seek to achieve our results by scraping Google Scholar, an approach which almost usually leads to an un-gratifying experience for the app user, who is forced to solve captchas, in exchange for services. Furthermore, the google scholar robots.txt file, prohibits scraping, and obtaining data from google scholar despite Googles stated non consent does not constitute responsible data stewardship.

**Place holder:**  We present new and reusable methods for mining scientific literature by utilizing many free and newly available APIs dedicated responsible and free dissemination of open access science documents. The tool we described in this document is extensible such that code from various modules could be re-applied to ask more specific questions about readability of science documents.

**Place holder:**  Because a user can download results from the science accessibility app. The tool makes it possible to compare two different scientific authors in the same field, and to compare their readability metrics. A comparison between two or more authors of the same field could be used to clarify if some fields really are generally harder to understand, or are some authors in the same field generally harder to understand.
