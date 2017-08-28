
import os
import cv2


class Dataset:

    
    def __init__(self):
        
        self.authorized_list = []
        self.unauthorized_list = []
        self.resize_height = 80
        self.resize_width = 80
      
    # traverse folder
    def traverse_image_dir(self, image_path):
        for file_or_dir in os.listdir(image_path):
            abs_path = os.path.abspath(os.path.join(image_path, file_or_dir))
            if os.path.isdir(abs_path):
                self.traverse_image_dir(abs_path)
            else:
                # read jpg file and filter size equals zero file
                if file_or_dir.lower().endswith('.jpg') and os.stat(abs_path)[6] > 0:
                    image = self.read_resize_image(abs_path)
                                        
                    if abs_path.find('unauthorized') > 0:
                        self.unauthorized_list.append(image)
                    else:
                        self.authorized_list.append(image)
                            
        return self.authorized_list, self.unauthorized_list

    # read and resize
    def read_resize_image(self, full_name):
        image = cv2.imread(full_name)
        #image = cv2.resize(image,(self.resize_height,self.resize_width),interpolation = cv2.INTER_LINEAR) ##not clear
        image = cv2.resize(image,(self.resize_height,self.resize_width),interpolation = cv2.INTER_AREA)
        return image

