import h5py
import numpy as np

def load_data_from_h5(filename):

    with h5py.File(filename, "r") as hf:

        print("Datasets: ", list(hf.keys()))

        X = hf["X"][:]
        Y = hf["Ytrue"][:]
        Ypred = hf["Ypred"][:]
        redshifts = hf["redshifts"][:]

    return X, Y, Ypred, redshifts

X, Y, Ypred, redshifts = load_data_from_h5("coeval_test_results.h5")


print("X shape: ", X.shape)
