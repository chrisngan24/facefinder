import cv2

def cell_shade(X):
    X_filt = cv2.pyrMeanShiftFiltering(X, 15, 30)
    X_grey = cv2.cvtColor(X, cv2.COLOR_RGB2BGRA)
    edges = cv2.Canny(X_grey, 100, 200)
    # http://stackoverflow.com/questions/3954484/cartoonizing-real-images
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    shaded = X_filt + 2*edges_rgb
    return shaded 
