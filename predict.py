# -*- coding: utf-8 -*-
'''
Created on Jun 14, 2014

@author: Gedas
'''
import Image
import random
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import io
import scipy.ndimage as ndimage
import scipy.io
import numpy.matlib
from scipy.sparse import csr_matrix
from scipy.sparse import dia_matrix

import sys
import cv2

caffe_root='/path/to/caffe/'

sys.path.insert(0, caffe_root + 'python')
import caffe


caffe.set_mode_gpu()
caffe.set_device(0)

# Spatial pathway
model_file='/path/to/model/spatial_pathway.caffemodel'
deploy_file='spatial_pathway.prototxt'
output_dir='spatial_pathway_results/'

## Visual pathway
#model_file='/path/to/model/visual_pathway.caffemodel'
#deploy_file='visual_pathway.prototxt'
#output_dir='visual_pathway_results/'




## input/output files
img_dir='RGB_images/'

if not os.path.exists(output_dir):
   os.mkdir(output_dir)


## Loading the model
if os.path.exists(model_file):
       print 'Loading network...'
       net = caffe.Classifier(deploy_file, model_file)
else:
       print 'Network file doesnt exist!'
       print model_file
       sys.exit(1)
       

files=os.listdir(img_dir)

for ff in files:
   if '.jpg' in ff:

      ## Reading image file
      cur_img_file=img_dir+ff
      cur_im = Image.open(cur_img_file)
      cur_im = np.array(cur_im, dtype=np.float32)
                 
      
      ## RGB to BGR + mean subtraction
      cur_im = cur_im[:,:,::-1]
      cur_im -= np.array((103.939, 116.779, 123.68))
           
      
      num_rows=cur_im.shape[0]
      num_cols=cur_im.shape[1]
             
      print 'Predicting...'
      
      ## Setting RGB data
      in_ = cur_im
      in_ = in_.transpose((2,0,1))
     
      net.blobs['data'].reshape(1, *in_.shape)
      net.blobs['data'].data[...] = in_
    
      ## Setting XY data
      mean_x=num_cols/2.0
      mean_y=num_rows/2.0
  
      XY=np.mgrid[0:num_rows,0:num_cols]
      X=(XY[1,:,:]-mean_x)
      Y=(XY[0,:,:]-mean_y)

     
      xy_in_=np.zeros((num_rows,num_cols,2))
      xy_in_[:,:,0]=X
      xy_in_[:,:,1]=Y

      xy_in_ = xy_in_.transpose((2,0,1))

      net.blobs['xy_data'].reshape(1, *xy_in_.shape)
      net.blobs['xy_data'].data[...] = xy_in_
    
      ## Forward Pass
      net.forward()
      
      print 'Done predicting!'
                      
      ## Outputting the data
      layer_key='fc8_sigm'
      fc8 = net.blobs[layer_key].data[0][:,:,:]
      fc8=np.transpose(fc8, (1, 2, 0))
      
      print 'Outputting...'
      output_path=output_dir+ff
      #scipy.io.savemat(output_path, mdict={'data': fc10})
      cv2.imwrite(output_path, fc8*255)

