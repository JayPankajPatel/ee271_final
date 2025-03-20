# EE-271 Project
This was created as the final project for SJSU's EE271 class 

## Premise
This project aims to execute a simple Convolution Neural Network (CNN) on an FPGA. The MNIST handwritten dataset will be used to train a CNN model, then the pretrained weights and biases will be deployed on the FPGA for inferencing. 
## Goals
The goal of the project is to implement and accelerate inferencing on hardware. Focusing on making full use of the FPGA's unique parallel architecuture to obtain a faster and higher throughput than conventional software techniques.
## Model 
The software model of our end goal exists under `./py/cnn.py`
### Using the model
The model uses `pyenv` and `pyenv-virtualenv`to manage python versions and packages.
#### Installation
Clone this repository in your desired location, change directories into `py` and run the setup script
Note, before running make sure you have the prerequisites for `python` 
```
git clone https://github.com/JayPankajPatel/ee271_final.git
cd ./ee271_final/py
source ./setup.sh
```
#### Run
Make sure you are in the `py` directory before running.
```
source ./run_py_model.sh
```
## Documentation
All documentation can be found under `./Docs/`. 
Currently, a design document explaining the basics of CNNs and the architecture being used is mentioned. 
