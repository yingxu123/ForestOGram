<h1 style="text-align: center;"> 
  ForestOGram aka SonicForest
</h1>


![example workflow](https://github.com/russelljjarvis/ForestOGram/actions/workflows/python-app.yml/badge.svg)


ForestOGram  intends to be code for animal identification and sound source classification in the Mauritius and Réunion forest.

It also intends to supply methods for building an fauna vocalisation data base in the Mauritius and Réunion forest.

![image](https://user-images.githubusercontent.com/7786645/173751900-211a8a66-0d8f-422b-ac66-5a18231ffc7a.png)


# Data Descriptors:

10 native birds, possibly 2 bats. 3 alien birds.
2 bats: a fruit bat and an insect hunting bat.

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


| Training data                  | Testing/Validation Data   | Prediction data |
| -----------                    | ----------- | ----------- |
| isolated segments high quality | arbitrary length/quality? segmented/unsegmented?  | Deliberately mixed faint sources, noise, foresets sounds poor quality |
| can be safely automated? | need data cuts to be verified by experts?  | need results to be verified by experts? |
| N>=(500, inf) | N can be ?  | N can be ? |
| Must contain a labelled target | May not contain any target species  | May not contain any target species  |

