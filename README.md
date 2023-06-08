# LM Filters and Textons

This repository contains Python scripts to create a set of Leung-Malik (LM) Filters and compute histograms of textons.

## File Descriptions

- `LMFilters.py`: This script creates a set of Leung-Malik (LM) Filters. The main function, `makeLMfilters`, returns an array of 49x49 LM filters.

- `run_train.py`: This script uses the LM filters to compute histograms of textons for a set of training images, and then saves these histograms (and the textons) for later use.

- `run_test.py`: This script loads the histograms and textons computed by `run_train.py`, and uses them to predict the class of test images.

- `utils.py`: This script contains utility functions that are used by `run_train.py` and `run_test.py`. These functions include `computeHistogram` which computes the histogram of textons for an image and `createTextons` which clusters filter responses to create textons.

## Requirements

The scripts require Python, with dependencies including:

- numpy
- cv2
- matplotlib
- skimage
- scipy
- sklearn

To install these dependencies, use pip:

`pip install numpy opencv-python matplotlib scikit-image scipy scikit-learn`


## Usage

1. First, run `run_train.py` to compute and save the histograms of textons for the training images:

`python run_train.py`


2. Then, run `run_test.py` to load the saved histograms and textons, and predict the class of the test images:

`python run_test.py`


## Dataset

The scripts are designed to work with any dataset of grayscale images. The names of the images should be in the form 'train1.jpg', 'train2.jpg', etc. for training images, and 'test1.jpg', 'test2.jpg', etc. for test images. 

## Contact

For any issues, please contact the repository owner at [anush97](https://github.com/anush97).
