#!/bin/bash

# Remove annoying spaces in file names.
for f in *\ *; do mv "$f" "${f// /_}"; done

##
# convert mp3 files to wave
##

for file in *.mp3; do
   ffmpeg -i "$file" -acodec pcm_s16le -ac 1 -ar 44100 "${file%.mp3}".wav
done
##
# move the mp3 files into an mp3 directory
##
mkdir wav
mkdir mp3
for f in *.mp3; do mv "$f" "mp3/${f}"; done
for f in *.wav; do mv "$f" "wav/${f}"; done
