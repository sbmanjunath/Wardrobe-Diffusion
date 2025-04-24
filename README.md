# Wardrobe Diffusion

Wardrobe Diffusion is a Python Server that accepts the image of a person and an image of a clothing article. It utilizes IDM-VTON, a diffusion-based image generation model, to generate an image of the person wearing the clothing article.

# Requirements

In order to run Wardrobe Diffusion, the minimum system requirements are:

1. Python 3.10 or later
2. At least 17 GB of CPU RAM
3. An NVIDIA GPU with at least 19 GB of RAM (CUDA 12.2 or higher)
4. 62 GB of disk space
5. You must have docker installed on your system

# Instructions

1. Build the docker image using 
     > docker build -t wardrobe_diffusion .
2. Run the docker container with the command
     > docker run -d --name wd_container --gpus all -p 80:80 wardrobe_diffusion
3. Veryify the container is running and test the api by going to localhost/docs.
    
    *Note: replace local hoset with hosting url if running on webserver*

# Reference

This project depends on [PyVirtry](https://github.com/powerjsv/VirtualTryOn-python-package) for the model implementation.