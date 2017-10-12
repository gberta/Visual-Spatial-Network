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


## Usage

Change the path to your caffe directory in the "predict.py" file. Then, change the paths to the locations where the caffe models are placed. Select which pathway you want to use (Visual or Spatial). Finally, run "predict.py"

## Pretrained Models

Please download the pretrained models from the following link: https://drive.google.com/drive/folders/0B5ev-b4SAFZVQjVxdU1jZjZKV2s?usp=sharing. We provide models for the 1) visual and 2) spatial pathways, which are described in the paper.