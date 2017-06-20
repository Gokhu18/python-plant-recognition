# USAGE
# python sgd_classifier.py --dataset database

# import the necessary packages
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import argparse
import json

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--descriptors", required=True,
	help="path to descriptors file")
ap.add_argument("-k", "--neighbors", type=int, default=1,
	help="# of nearest neighbors for classification")
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

# load descriptors
with open(args["descriptors"], 'r') as f:
	features,labels = json.load(f)

features = np.array(features)
labels = np.array(labels)

# partition the data into training and testing splits, using 85%
# of the data for training and the remaining 15% for testing
(trainFeat, testFeat, trainLabels, testLabels) = train_test_split(
	features, labels, test_size=0.15, random_state=42)

print("[INFO] features matrix: {:.2f}MB".format(
	features.nbytes / (1024 * 1000.0)))

# train and evaluate a Logistic Regression classifer on the contour ffts
print("[INFO] evaluating GaussianProcessClassifier accuracy...")
gpc = GaussianProcessClassifier()

gpc.fit(trainFeat, trainLabels)
acc = gpc.score(testFeat, testLabels)
print("[INFO] GaussianProcessClassifier accuracy: {:.2f}%".format(acc * 100))
