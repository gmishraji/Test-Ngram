# Test-Ngram
An implementation against http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

# Implementation Logic:

  The implementation takes 2 input parameters:
    1) The Input Text file
    2) The no defining what Ngram should be generated.
    
  Based on the provided input the a data cleansing method cleans the data and feeds that further as a
  plain text with all special characters removed.
  
  Further the logic generates a Ngram, where N 
  defining the key length.
  N = 2 => Bigram
  N = 3 => Trigram
  
  Based on the generated Ngram, it further generates a new text by randomly picking a key from the
  Ngram dictionary. It runs a loop for randomly picking the keys from Ngram dictionary and appends the
  text with the corresponding value. The loop breaks when the key combination couldn't be found in the Ngram
  dictionary.
  
 # Run Method:
 Open cmd/terminal:
    * python3 ngram.py <<'inputfile name'>> <<'ngram key length'>>
      Exp: python3 ngram.py test_file.txt 2
  
 The code should show some meaningfull log to understand what random key has been picked and how it has
  identified the further text.
  
  
