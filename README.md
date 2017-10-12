# VSN Model

This is a code repository for the paper "Unsupervised Learning of Important Objects from First-Person Videos". Our method predicts important-objects from first-person images in an unsupervised fashion. This work has been published in the ICCV 2017 Conference.

Citation:  
@InProceedings{gberta_2017_ICCV_vsn,  
author = {Gedas Bertasius and Hyun Soo Park and Stella X. Yu and Jianbo Shi},  
title = {Unsupervised Learning of Important Objects from First-Person Videos},  
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},  
month = {October},  
year = {2017}  
}

## Installation

1. Caffe Deep Learning library and its Python Wrapper (We use DeepLab_v2 version):

	Caffe and its python wrapper need to be compiled as instructed in http://caffe.berkeleyvision.org/installation.html. 


## Running Pretrained Models

Change the path to your caffe directory in the "predict.py" file. Then, change the paths to the locations where the caffe models are placed. Select which pathway you want to use (Visual or Spatial). Finally, run "predict.py"

## Pretrained Models

Please download the pretrained models from the following link: https://drive.google.com/drive/folders/0B5ev-b4SAFZVQjVxdU1jZjZKV2s?usp=sharing. We provide models for the 1) visual and 2) spatial pathways, which are described in the paper.

## Training

To train a new model you will first need to extract Multi-Scale Combinatorial Grouping (MCG) candidates from your training images. The code for the MCG method can be found in https://github.com/jponttuset/mcg. Afterwards, you will need to obtain an approximate supervisory signal in a form of a coarse important object mask. This can be done in a variety of ways: 1) by exploiting some spatial patterns in the data, 2) by using a hand detector, or 3) by using some unsupervised visual saliency method (e.g. GBVS). 

In our work, we exploit spatial consistency in the first-person data, and create a coarse important object mask by putting a Gaussian around a certain location in the image (Please check the paper for more details). After obtaining 1) coarse important object mask, and 2) MCG candidates, you can use the function "mcg_projection.m" to create a sharp segmentation mask that will be used as a supervisory signal. The network can then be trained as is described in our ICCV 2017 paper. Note that the segmentation masks should be continuosly updated as the training progresses (See our paper for more details).
