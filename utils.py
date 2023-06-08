from skimage import io
from skimage.util import img_as_float
from skimage.color import rgb2gray
import numpy as np
from scipy.ndimage import correlate
import sklearn.cluster
from scipy.spatial.distance import cdist

def computeHistogram(img_file, F, textons):
    img = img_as_float(rgb2gray(io.imread(img_file)))
    H, W = img.shape
    filter_results = np.zeros((H * W, F.shape[2]))

    for i in range(F.shape[2]):
        filter_response = correlate(img, F[:,:,i])
        filter_results[:, i] = filter_response.flatten()

    D = cdist(filter_results, textons)
    assign = np.argmin(D, axis=1)
    histogram = np.histogram(assign, bins=np.arange(textons.shape[0] + 1))[0]
    histogram = histogram / np.sum(histogram)

    return histogram

def createTextons(F, file_list, K):
    No_of_filters = F.shape[2]
    all_filter_responses = []

    for img in file_list:
        img = img_as_float(rgb2gray(io.imread(img)))
        H, W = img.shape
        filter_responses = np.zeros((H * W, No_of_filters))

        for i in range(No_of_filters):
            filter_response = correlate(img, F[:,:,i])
            filter_responses[:, i] = filter_response.flatten()

        all_filter_responses.append(filter_responses)

    all_filter_responses = np.vstack(all_filter_responses)
    kmeans = sklearn.cluster.KMeans(n_clusters=K, n_init=10, random_state=0).fit(all_filter_responses)
    textons = kmeans.cluster_centers_

    return textons


