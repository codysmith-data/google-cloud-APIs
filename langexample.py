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