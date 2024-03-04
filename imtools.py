import os
def get_imlist(path):
# Returns a list of filenames forall jpg images in a directory. """
    return [os.path.join(path,f) 
            for f in os.listdir(path) 
            if f.endswith('.jpg')]