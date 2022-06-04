# ForestScope

| Training data                  | Testing/Validation Data   | Prediction data |
| -----------                    | ----------- | ----------- |
| isolated segments high quality | arbitrary length/quality? segmented/unsegmented?  | Deliberately mixed faint sources, noise, foresets sounds poor quality |
| can be safely automated? | need data cuts to be verified by experts?  | need results to be verified by experts? |
| N>=(500, inf) | N can be ?  | N can be ? |
| Must contain a labelled target | May not contain any target species  | May not contain any target species  |

* Plan pre-process forest animal sounds with [CARFACAGC](https://github.com/vschaik/CARFAC/blob/master/CARFACAGC.ipynb), before applying machine learning classifier.
