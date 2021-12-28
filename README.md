# google-cloud-APIs

@author: Cody Smith | codysmith.contact@gmail.com

https://github.com/codysmith-tech

https://www.linkedin.com/in/codysmithprofile/

------------------------
***OVERVIEW***

This is a walkthrough of how to access some of the APIs through Google Cloud and how to use them with Python.

_Disclaimer: this is mainly an example of how to use the APIs via the Google Cloud platform. The Python code in this project is simple, and just meant to show basics within the GCP._

------------------------
***SETUP***

To replicate my setup for interacting with the Google APIs, you will need to access the Google cloud platform and create an Virtual Machine instance with the following settings:

    US-East server

    e2-micro (No GPU)

    Linux environment - Ubuntu 18.04 (15 Gb)

You will need to create an SSH key and add it to the VM instance as well. I used PuTTy for this. Download here:

    https://www.putty.org/
  
You will also need to make an Owner level Service Account and add it. There is Google documentation on how to do this.

    https://cloud.google.com/vision/docs/before-you-begin

Once in your VM:

I used Python 3.6.9 for this project. This should already be a part of the Linux Ubuntu 18.04 OS.

Although, you will need pip3 for installing the Google Cloud packages. Do the dollowing commands:

    sudo apt update
    sudo apt install python3-pip
        
Once you have pip3, get Google Cloud Vision (the first API we will use).

    pip3 install --upgrade google-cloud-vision
        
------------------------
***VISION API***

Now, create a working directory for the project:

    cd ~

    mkdir gcloudpractice

    cd gcloudpractice

    mkdir visionexample

    cd visionexample
        
Now, get an image to do the Vision analysis on. I used Guido van Rossum's Wiki picture. Use this command to add this to your directory:

    wget https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Guido-portrait-2014-drc.jpg/220px-Guido-portrait-2014-drc.jpg
        
Now create your Python script:

    nano visionexample.py

Now paste this code into your Python file:

    import io
    from google.cloud import vision

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = '220px-Guido-portrait-2014-drc.jpg'

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection and scoring  on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        print(label.description, label.score)

