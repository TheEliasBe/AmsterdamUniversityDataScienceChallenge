import xml.etree.ElementTree as ET # for parsing the xml file
import re # use regex to clean the document
import inflection # library to convert
import matplotlib.pyplot as plt # for create the histogram

class Assignment:

    def part1(self, filename):

        # read xml file
        with open(filename, "r") as file:
            xml_data = file.read()

        xml_data = xml_data.replace("<p>","") # p tags are not required
        xml_data = xml_data.replace("</p>","")
        xml_data = re.sub("\\.|,|-|\"|\(|\)|:|\'|\?|!", "", xml_data) # punctuation not required
        xml_data = xml_data.replace("\n", " ") # replace linebreaks with spaces
        xml_data = re.sub(" +", " ", xml_data) # remove any unnecessary whitespaces
        xml_data = xml_data.lower() # make everything lower case

        # parse the resulting xml string
        parsed_xml = ET.fromstring(xml_data)

        # extract text from xml tree
        articles = []
        for article in parsed_xml:
            text = article.find('text').text.split(" ") # split on blank spaces
            text = list(map(lambda x : inflection.singularize(x), text)) # singularize words
            articles.append(text)

        # create a hash set containng all unique words
        all_words = set(articles[0])
        all_words.update(articles[1])
        all_words.update(articles[2])


        # now create a dictionary (it's hashed) with word -> [(document_index, term frequency), ...]
        hashmap = {}
        for word in all_words:
            frequencies = []
            index = 0
            for article in articles:
                frequencies.append((index, article.count(word)))
                index += 1
            hashmap[word] = frequencies

        return hashmap


    def __init__(self):
        hm = self.part1("txt-for-assignment-data-science.xml")

        print("the", hm["the"], sep=" -> ")
        print("author", hm["author"], sep=" -> ")

Assignment()