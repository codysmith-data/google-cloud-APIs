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

I used the first few blocks from Google's Wikipedia page as the example text.

Now, save and close out of the file, and run it by using:
   
    python3 langexample.py
    
And you should get the following output or similar:

    0.0 1.0

    Google LLC ORGANIZATION {'mid': '/m/045c7b', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Google'} 0.666184663772583
    services OTHER {} 0.07219050824642181
    advertising technologies OTHER {} 0.0317310094833374
    products CONSUMER_GOOD {} 0.025574326515197754
    search engine CONSUMER_GOOD {} 0.025574326515197754
    American LOCATION {'wikipedia_url': 'https://en.wikipedia.org/wiki/United_States', 'mid': '/m/09c7w0'} 0.02259480208158493
    Larry Page PERSON {'mid': '/m/0gjpq', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Larry_Page'} 0.02208172157406807
    cloud computing OTHER {} 0.013903314247727394
    hardware OTHER {} 0.009819552302360535
    software CONSUMER_GOOD {} 0.009819552302360535
    CEO PERSON {} 0.009275099262595177
    companies ORGANIZATION {} 0.006712904199957848
    company ORGANIZATION {} 0.005592409987002611
    students PERSON {} 0.005502747837454081
    information technology industry OTHER {} 0.004731095861643553
    one PERSON {} 0.004731095861643553
    14% OTHER {} 0.0036498780827969313
    56% OTHER {} 0.0036498780827969313
    stock OTHER {} 0.003349350532516837
    shares OTHER {} 0.0032068095169961452
    stockholder voting power OTHER {} 0.0029426568653434515
    initial public offering EVENT {} 0.0029346030205488205
    IPO EVENT {} 0.0029346030205488205
    Amazon ORGANIZATION {} 0.0028000709135085344
    Big Five ORGANIZATION {} 0.0028000709135085344
    CEO PERSON {} 0.0019189842278137803
    California LOCATION {'mid': '/m/01n7q', 'wikipedia_url': 'https://en.wikipedia.org/wiki/California'} 0.0019034752622246742
    Ph.D. PERSON {'wikipedia_url': 'https://en.wikipedia.org/wiki/Doctor_of_Philosophy', 'mid': '/m/04zx3q1'} 0.0019034752622246742
    Stanford University ORGANIZATION {'wikipedia_url': 'https://en.wikipedia.org/wiki/Stanford_University', 'mid': '/m/06pwq'} 0.0019034752622246742
    Apple ORGANIZATION {'mid': '/m/0k8z', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Apple_Inc.'} 0.0018896120600402355
    Meta ORGANIZATION {'wikipedia_url': 'https://en.wikipedia.org/wiki/Meta_Platforms', 'mid': '/m/0hmyfsv'} 0.0018896120600402355
    Facebook OTHER {'mid': '/m/02y1vz', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Facebook'} 0.0018896120600402355
    Microsoft ORGANIZATION {'mid': '/m/04sv4', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Microsoft'} 0.0018896120600402355
    Sergey Brin PERSON {'mid': '/m/0gjq6', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Sergey_Brin'} 0.0018802153645083308
    holding company ORGANIZATION {} 0.0017562595894560218
    employees PERSON {} 0.0015355442883446813
    Sundar Pichai PERSON {'wikipedia_url': 'https://en.wikipedia.org/wiki/Sundar_Pichai', 'mid': '/m/09gds74'} 0.0013073571026325226
    interests OTHER {} 0.0012062456225976348
    subsidiary ORGANIZATION {} 0.0011022778926417232
    Internet properties OTHER {} 0.0009663362870924175
    Alphabet Workers Union ORGANIZATION {'wikipedia_url': 'https://en.wikipedia.org/wiki/Alphabet_Workers_Union', 'mid': '/g/11llzkc_kl'} 0.0009076223359443247
    Alphabet Inc... ORGANIZATION {'mid': '/g/11bwcf511s', 'wikipedia_url': 'https://en.wikipedia.org/wiki/Alphabet_Inc.'} 0.0005721302004531026
    September 4, 1998 DATE {'day': '4', 'year': '1998', 'month': '9'} 0.0
    2004 DATE {'year': '2004'} 0.0
    2015 DATE {'year': '2015'} 0.0
    October 24, 2015 DATE {'month': '10', 'year': '2015', 'day': '24'} 0.0
    December 3, 2019 DATE {'year': '2019', 'month': '12', 'day': '3'} 0.0
    2021 DATE {'year': '2021'} 0.0
    3 NUMBER {'value': '3'} 0.0
    24 NUMBER {'value': '24'} 0.0
    4 NUMBER {'value': '4'} 0.0
    2004 NUMBER {'value': '2004'} 0.0
    2015 NUMBER {'value': '2015'} 0.0
    2021 NUMBER {'value': '2021'} 0.0
    1998 NUMBER {'value': '1998'} 0.0
    one NUMBER {'value': '1'} 0.0
    2019 NUMBER {'value': '2019'} 0.0
    Five NUMBER {'value': '5'} 0.0
    14 NUMBER {'value': '14'} 0.0
    2015 NUMBER {'value': '2015'} 0.0
    56 NUMBER {'value': '56'} 0.0

The first line has 2 numbers, the first desribes the sentiment (on a scale of -1.0 to 1.0 (neg to pos)).

The second describes the magnitude of the sentiment (0.0 to infinity), which shows the amount of emotional language present in the text.
Since the first number in this 0.0, the overall sentiment of this text is neutral.

And the low magnitude of 1.0 shows that there is little emotional text, which shows that the text is truly neutral (and not mixed negative and positive).
This makes sense as it is a Wikipedia article.

The group of data below the sentiment analysis is the entity analysis.

The first part of the data is the entity that is being described. At the top of the list, it is "Google LLC".

The second part is the entity type. For Google, this is "ORGANIZATION".

The third part (in brackets) is the metadata for the entity. The wiki entry will be included (if available).
In this case, the same wiki entry for Google this text is from was included for Google LLC.

The last part is the entity salience. This describes the importance of its respective entity as compared to all other entities.
In this case, Google LLC has the highest salience. This makes sense as this is the wiki page for Google itself.
