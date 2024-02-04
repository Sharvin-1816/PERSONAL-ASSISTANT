from textblob import TextBlob
import re
import webbrowser
from spellchecker import SpellChecker 
from nltk.corpus import wordnet

# spacy.cli.download("en_core_web_sm")
# nltk.download('brown')
# nltk.download('averaged_perceptron_tagger')
# nlp = spacy.load("en_core_web_sm")

# https://www.guru99.com/pos-tagging-chunking-nltk.html   REFER THIS WEBSITE FOR POS TAGS

def extract_nouns_textblob(sentence):
    blob = TextBlob(sentence)
    nouns = [word for (word, pos) in blob.tags if pos.startswith('NN')]
    return nouns

command = input("COMMAND: ")
useless_text = ["a","an","the","is","on","in","for"]
main_command = re.findall(r'\w+', command)   #SEPERATING ALL THE WORDS
corrected_command = [SpellChecker().correction(x) for x in main_command]   #CORRECTING MISPELLED WORDS
# print(corrected_command)
main_command_lower = [x.lower() for x in corrected_command if x.lower() not in useless_text]  #REMOVING USELESS WORDS AND CONVERTING THEM TO LOWER TEXT
# print(main_command_lower)
specific_keywords = ["search","open","read","article"]      #PRIMARY KEYWORDS WHICH SHOWS THAT I WANT TO READ AN ARTICLE
synonyms = []
def get_synonyms(word,synonyms):
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append((lemma.name()).lower())
    return synonyms

synonyms_specific_keywords = []   # ALL OTHER SYNONYMS OF PRIMARY KEYWORDS WHICH SHOW I WANT TO READ ARTICLE

for x in specific_keywords:
    get_synonyms(x,synonyms)
    synonyms_specific_keywords.extend(set(synonyms))

if "search" or "open" or "read" or "show" in main_command_lower:   
    if "article" or "articles" in main_command_lower:    # CHECKING IF I WANT TO READ AN ARTICLE
        if "medium" in main_command_lower:   # CHECKING IF I WANT TO READ ARTICLE FROM MEDIUM
            if " \" " not in main_command_lower:         # FOR SPECIFIC TOPICS
                main_command_lower.remove("medium")
                command_sentence = []
                for x in main_command_lower:
                    if x not in specific_keywords:
                        command_sentence.append(x)    # FOR EXTRACTING TOPIC WORDS
                # print(command_sentence)
                wiki = TextBlob(" ".join(command_sentence))
                tag = wiki.tags
                print(tag)
                nouns = []
                for x in tag:
                    if x[1]=='NN'  or x[1]=='NNP' or x[1]=='NNPS' or x[1]=='JJ' or x[1]=='JJS':
                        nouns.append(x[0])     #EXTRACTING NOUNS
                # print(nouns)
                if len(nouns) >=2 :
                    name = "+".join(nouns)
                    url = f'https://medium.com/search?q={name}'
                    webbrowser.open(url)
                elif len(nouns) ==1 :
                    url = f'https://medium.com/search?q={nouns[0]}'
                    webbrowser.open(url)
        output = True   # CONSIDER THE OUTPUT WE GOT IS CORRECT
        output_check = print("Got the required output?\n")   #CHECKING IF THE OUTPUT GOT IS CORRECT OR INCORRECT
        output_check_response = input("COMMAND: ")
        if output_check_response.lower() == "no":     # IF OUTPUT IS INCORRECT WE WILL RELP ON OUR PREVIOUS METHOD WHICH IS SURELY GET US THE DESIRED OUTPUT
            retry_topic_name = print("\nPlease type the topic you want the article on. Sorry for the previous response.\n")
            topic_name = input("COMMAND: ")
            medium_topic = [x.lower() for x in re.findall(r'\w+', topic_name)]
            if len(medium_topic)>=2:
                name = "+".join(medium_topic)
                url = f'https://medium.com/search?q={name}'
                webbrowser.open(url)
            else:
                url = f'https://medium.com/search?q={medium_topic[0]}'
                webbrowser.open(url)
        else:
            print("\nThank You")
            output = False

    # elif "user" in main_command_lower:
        

# nltk.download('averaged_perceptron_tagger')
# Example usage:
# sentence = "'open article medium quantum mechanics'"
# nouns = extract_nouns_textblob(sentence)
# print("Nouns:", nouns)
    

# YET TO IMPLEMENT THE SYNONYMS CHECK IN IF IF CONDITIONS