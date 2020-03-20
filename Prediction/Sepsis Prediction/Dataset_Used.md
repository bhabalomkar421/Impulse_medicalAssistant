# DATASET USED:
Dataset link: https://physionet.org/content/challenge-2019/1.0.0/
It consists of two folders, Training A and Training B of 20,336 and 20,000 files respectively. Also, Training A consists of 7,90,215 entries of patient data with 41 parameters. Since this is a real-world dataset there was no test dataset given. Each of the files in these given folders, there were hundreds of data of pipe separated file. The training to our model was given in two ways to give the best accuracy and less error. It was of two types:
1. Using Training A as training dataset and Training B as test dataset.
2. Combining these two folders and splitting this dataset into train and test datasets.
Both these methods can be used to train the model yet one that gives the best accuracy and less false positives and true negatives will be chosen. A Model that gives the best accuracy, specificity, and sensitivity will be chosen for deployment.
