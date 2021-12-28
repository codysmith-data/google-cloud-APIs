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

Once in your VM:

I used Python 3.6.9 for this project. This should already be a part of the Linux Ubuntu 18.04 OS.

Although, you will need pip3 for installing the Google Cloud packages. Do the dollowing commands:

        sudo apt update
        sudo apt install python3-pip
        
Once you have pip3, get Google Cloud Vision (the first API we will use).

        pip3 install --upgrade google-cloud-vision
        
------------------------
***CODE***
