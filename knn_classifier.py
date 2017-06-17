# USAGE
# python knn_classifier.py --dataset database

# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
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

# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
(trainFeat, testFeat, trainLabels, testLabels) = train_test_split(
	features, labels, test_size=0.25, random_state=42)

print("[INFO] features matrix: {:.2f}MB".format(
	features.nbytes / (1024 * 1000.0)))

# train and evaluate a k-NN classifer on the contour ffts
print("[INFO] evaluating K-NN accuracy...")
knn = KNeighborsClassifier(n_neighbors=args["neighbors"],
	n_jobs=args["jobs"])
knn.fit(trainFeat, trainLabels)
acc = knn.score(testFeat, testLabels)
print("[INFO] K-NN accuracy: {:.2f}%".format(acc * 100))
