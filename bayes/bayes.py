import xmltodict
import nltk
from nltk.corpus import stopwords
from random import choice,shuffle
from collections import defaultdict
import string
import math

#english stopwords to remove all common words
stopwords = stopwords.words('english')


def indicate_word(message):
        """Create a dictionary of entries{word: True} for every unique word in each message.
        """
        features = defaultdict(list)
        for k in message:
                features[k] = True
        return features

# make (feature, label) lists
def label_features(summary, label):
        """ Make (features, label) list, features are the dictionaries { word: True} of each
        message, label is 'spam' or 'ham'. Thus all the features are listed of each message'
        """
        features_labels = []
        for word in summary:
        	tokens = []
        	if word not in string.punctuation: 
			tokens.append(word)
        	features = indicate_word(tokens)
		features_labels.append((features, label))
        return features_labels

def evaluate_classifier(train_set, test_ignore, test_check):
        """ Using NaiveBayesClassifier.train() method from NLTK to train the train_set (spam + ham),
        then classifier is used to evaluate the accuracy of test Spam, Ham. Finally, the most informative
        features are showed.
        """
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        print('Test Ignore accuracy: {0:.2f} %'.format(100 * nltk.classify.accuracy(classifier, test_ignore)))
        print('Test Check accuracy: {0:.2f} %'.format(100 * nltk.classify.accuracy(classifier, test_check)))
        print classifier.show_most_informative_features(20)



#TODO
# prepare a set with CVEs that affect us and sets "not for us" (with apple and cisco information)

# feature to extract: summary
#remove header
def get_novell_summaries():
	return get_summary('novell')

def get_apple_summaries():
	return get_summary('apple')

def get_cisco_summaries():
	return get_summary('cisco')

def get_summary(vendor):
	content = open(vendor+'.tsv').readlines()[1:] 
  	# list with tab separated entries where just the last arg is relevant
	tokenized_words = nltk.word_tokenize(' '.join([ entry.split('\t')[-1].strip() for entry in content ]))
	return [ word.lower() for word in tokenized_words if word.lower() not in stopwords and len(word) > 1 ]


""" Get a random summary available on a specific dataset
    return the summary as a dictionary (the format expected by NayeBayesClassifier.classify
"""
def get_description(vendor):
	content = open(vendor+'.tsv').readlines()[1:] 
	rand_summary = choice(content).split('\t')[-1].strip()
	return {'summary':rand_summary}


novell_set = get_novell_summaries()
apple_set  = get_apple_summaries()
cisco_set  = get_cisco_summaries()



s1 = label_features(novell_set, 'check')
s2 = label_features(apple_set,  'ignore')
s2 += label_features(cisco_set,  'ignore')

sample1_size = int(math.ceil(len(s1) / 2))
sample2_size = int(math.ceil(len(s2) / 2))


train_set = s1[sample1_size:] + s2[sample2_size:]
test_check = s1[:sample1_size]
test_ignore = s2[:sample2_size]

evaluate_classifier(train_set, test_ignore, test_check)
