## This program takes a dataset and calculates the fft of the contour
# vector of each image and saves all those features on a file to later
# processing
## USAGE
# python generate_descriptors.py --dataset database --output_file file

# import the necessary pre-installed packages
from imutils import paths
import argparse
import json
import os

# import self-made library
import contour_fft

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-f", "--output_file", required=True,
	help="path to save output file")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the raw pixel intensities matrix, the features matrix,
# and labels list
features = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
	# update every 10 images processed
    if (i+1)%10 == 0:
        print("[INFO] describing image: ", i+1)
    # load the image and extract the class label (assuming that our
    # path as the format: /path/to/dataset/{class}.{image_num}.jpg
    label = imagePath.split(os.path.sep)[-1].split(".")[0]

    # extract contour fft
    contour = contour_fft.get_contour_fft(imagePath)

    # update the features, and labels matricies, respectively
    features.append(contour)
    labels.append(label)

# Convert from numpy array to python standard list to be able to save it
features = [list(i) for i in features]

# Save descriptors to file for later processing using different algorithms
print("[INFO] saving descriptors...")
with open(args["output_file"], 'w') as f:
    f.write(json.dumps([list(features), list(labels)]))
