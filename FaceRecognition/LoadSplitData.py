
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from six.moves import cPickle as pickle



class Process(object):

    
    def __init__(self):
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        self.images_list = []
        self.labels_list = []
        
    # load authorized image data
    def load_image_data(self, data_path):
        
        with open(data_path + '\\authorized_image_data.pickle' , 'rb') as f:
            auth_list = pickle.load(f)
            self.images_list.extend(auth_list)
            self.labels_list.extend([1] * len(auth_list))
            del auth_list
        with open(data_path + '\\unauthorized_image_data.pickle' , 'rb') as f:
            unauth_list = pickle.load(f)
            self.images_list.extend(unauth_list)
            self.labels_list.extend([0] * len(unauth_list))
            del unauth_list
        return self.images_list, self.labels_list
            
    # convert to numpy arrays
    def get_image_array(self, data_path):
        
        images, labels = self.load_image_data(data_path)
        images = np.array(images)
        labels = np.array(labels)

        return images, labels

    def split_data(self, img_rows=80, img_cols=80, img_channels=3, nb_classes=2):

        images, labels = self.get_image_array(r'C:\Users\dbsnail\ImageFolder\data')
        print("Images shape {}, label shape {}, ratio of authorized data {}".format(images.shape, labels.shape, labels.mean()))
    
         # numpy.reshape
        X_train_valid, X_test, y_train_valid, y_test = train_test_split(images, labels, test_size=0.25, random_state=123)
        X_train, X_valid, y_train, y_valid = train_test_split(X_train_valid, y_train_valid, train_size=0.7, random_state=200)
        
        del images
        del labels
        #reshape
        X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 3)
        X_valid = X_valid.reshape(X_valid.shape[0], img_rows, img_cols, 3)
        X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 3)
        input_shape = (img_rows, img_cols, 3)


        # the data, shuffled and split between train and test sets
        print('X_train shape:', X_train.shape)
        print(X_train.shape[0], 'train samples')
        print(X_valid.shape[0], 'valid samples')
        print(X_test.shape[0], 'test samples')

        # convert class vectors to binary class matrices
        Y_train = np_utils.to_categorical(y_train, nb_classes)
        Y_valid = np_utils.to_categorical(y_valid, nb_classes)
        Y_test = np_utils.to_categorical(y_test, nb_classes)
        
        # scale the input data to the range [0,1]
        X_train = X_train.astype('float32')
        X_valid = X_valid.astype('float32')
        X_test = X_test.astype('float32')
        X_train /= 255
        X_valid /= 255
        X_test /= 255

        self.X_train = X_train
        self.X_valid = X_valid
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_valid = Y_valid
        self.Y_test = Y_test