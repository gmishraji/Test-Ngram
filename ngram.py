from builtins import range
import six
import random
from string import punctuation
import sys
import logging

logging.basicConfig(level=logging.INFO)


def _tuplifyString(inputString):
    '''
        Method to return a tuple against a splace separated input string
    '''

    return tuple(inputString.split(' '))


def getCleanText(textFile):
    ''' 
        Method to take an input file and remove any punctuations( special characters )
        through the text to make it clean.

        Example Text in the input File:
            I wish./ I may-,. I wish!<> I might.??

        Outout Text:
            I wish I may I wish I might
    '''

    removedPunctuation = set(punctuation)
    with open(textFile, 'r') as f:
        result = f.read()
        result = ''.join(punc for punc in result if punc not in removedPunctuation)
        logging.info(' Removing all special characters from the given text ')
        return result


def generateNgram(inputFile, chars=2):
    '''
        Generate a Ngram based on a provided input file text.
        Ngram means a structure defined as below based on the input provided
        for chars, defaulted to 2, which makes it a Bigram.

        Exp Bigram:

            Text:
                I wish I may I wish I might

            Generated Ngram ( Bigram in this case ):
                {('I','may'): ['I'],
                 ('I','wish'): ['I','I'],
                 ('may','I'): ['wish'],
                 ('wish','I'): ['may','might']
                }
    '''

    cleanText = getCleanText(inputFile).split(' ')
    ngram = {}
    if len(cleanText) > 0:
        for i in range(len(cleanText) - chars):
            seq = tuple(cleanText[i:i + chars])
            if seq not in list(six.iterkeys(ngram)):
                ngram[seq] = []
            ngram[seq].append(cleanText[i + chars])
    logging.info(' Generated a ngam against the given text and chars description ')
    return ngram


def generateNewText(ngram, chars=2):
    '''
        Generate a new Text based on the Ngram input

        Input Ngram( a dictionary ) may look like:
            {('I','may'): ['I'],
             ('I','wish'): ['I','I'],
             ('may','I'): ['wish'],
             ('wish','I'): ['may','might']
            }

        Output Text ( Random ):
            'may I wish I may I wish I may I wish I might'
    '''

    try:
        start = ' '.join(random.choice(list(six.iterkeys(ngram))))
        logging.info(' Picking a random pair from the Ngram Keys \'%s\' ', start)
        output = start
    except:
        raise KeyError(' No Ngram key-value pairs found to be traversed ')

    while _tuplifyString(start) in list(six.iterkeys(ngram)):
        plausibles = ngram[_tuplifyString(start)]
        logging.info(' The possible next words against the picked pair \'%s\' could be %s ', start, plausibles)
        nextWord = plausibles[random.randrange(len(plausibles))]
        output = output + ' ' + nextWord
        output = output.split(' ')
        start = ' '.join(output[len(output) - chars:len(output)])
        output = ' '.join(output)
        logging.info(' The next text : %s ', output)
    return output


if __name__ == '__main__':
    inputFile, chars = sys.argv[1], int(sys.argv[2])
    ngram = generateNgram(inputFile, chars)
    generateNewText(ngram, chars)
