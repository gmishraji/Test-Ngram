# Test-Ngram
An implementation against http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

# Implementation Logic:

  Against an input text file and defining limit for key length, the logic generates a Ngram, where N 
  defining the key length.
  N = 2 => Bigram
  N = 3 => Trigram
  
  It further processes the generated Ngram to prepare a next Text by randomly picking a key from the
  Ngram dictionary.
  
 # Run Method:
 Open cmd/terminal:
    * python3 ngram.py <<'inputfile name'>> <<'ngram key length'>>
  
 The code should show some meaningfull log to understand what random key has been picked and how it has
  identified the further text.
  
  
