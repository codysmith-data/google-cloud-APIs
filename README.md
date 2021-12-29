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
    
**Before using each API, you will need to activate them within the Google Cloud Platform**

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
        
Now, get an image to do the Vision analysis on. I used Guido van Rossum's Wiki picture.

![image](https://user-images.githubusercontent.com/58944210/147609070-15377240-0693-4bf0-9919-0d638dd1215a.png)


Use this command to add this to your directory:

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
        
Now exit & save this file, and use this command to run it:

    python3 visionexample.py

You should get this output or similar:

    Forehead 0.9846563935279846
    Glasses 0.9836904406547546
    Nose 0.9835830330848694
    Chin 0.9655716419219971
    Hairstyle 0.9509009122848511
    Eyebrow 0.9483392834663391
    Eye 0.935302734375
    Mouth 0.9233428835868835
    Vision care 0.9137829542160034
    Beard 0.897161066532135

We can see that the GCP Vision API was successfully able to label parts of the picture with a high certainty.

------------------------
***LANGUAGE API***

Start again by making the necessary directory:
        
    cd ../

    mkdir langexample
    
    cd langexample
    
Now, pip install the Natural Language API:

    pip3 install --upgrade google-cloud-language
    
Once installation is complete, create the Python file:

    nano langexample.py
    
Now paste this code into your Python file:

    from google.cloud import language_v1

    #Creating function to do sentiment and entity analysis
    def lang_analysis(text):

            #Creating instance of language client
            client = language_v1.LanguageServiceClient()

            #Reading in text
            document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language='en')

            #Performing sentiment analysis
            sentiment = client.analyze_sentiment(request = {"document": document}).document_sentiment

            #Performing entity analysis
            entities = client.analyze_entities(request = {'document': document, 'encoding_type': language_v1.EncodingType.UTF8})

            #Returning sentitment and entity analysis
            return sentiment, entities

    #Creating example text
    example = "Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the Big Five companies in the American information technology industry, along with Amazon, Apple, Meta (Facebook) and Microsoft. Google was founded on September 4, 1998, by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14% of its publicly-listed shares and control 56% of the stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly-owned subsidiary of Alphabet Inc.. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's Internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet. In 2021, the Alphabet Workers Union was founded, mainly composed of Google employees."

    #Using function
    sentiment, entities = lang_analysis(example)

    #Printing sentiment analysis
    print(sentiment.score, sentiment.magnitude)
    print(' ')

    #Printing entity analysis
    for e in entities.entities:
            print(e.name, language_v1.Entity.Type(e.type_).name, e.metadata, e.salience)
