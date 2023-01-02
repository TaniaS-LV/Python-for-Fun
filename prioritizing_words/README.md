# Prioritizing new words 

*Technologies used: OOP, web scraping via selenium, API calls via requests, difflib* 

If you have ever tried learning a foreign language, you have probably realized, just like me, that some of the words are more important than the others. For example, it's very likely we will use the word "phone" or "city" much more frequently than "summer solstice" or "procedure" in any language we learn (unless these less frequent words are not specific to our life in some way).

Hence, for me it makes sense to prioritize all the words I encounter, before I decide how to deal with them: I only try to remember the most important words first, especially while I am new to my target language. Once I know the basics (the 1st priority words), I can move on to the less frequent words, and there will always be some that I will only want to learn passively, i.e., just be able to recognize them if I ever hear them, but not necessarily produce them myself.
That's how I optimize my learning process to learn languages faster!

## Program 
To help myself with this process, I wrote a Python program (using OOP, which was an interesting challenge for me) doing the following. 

### Defining word frequency 
With the help of **web scraping of Collins dictionary** I find out the frequency of any word (that's a truly amazing resource, I wish they develop it for more languages in the future). 
They rate frequency of any given word from 1 to 5, where 5 means the word is extremely common, i.e., one of the 1000 most frequent words, and 1 is extremely rare. My sweet spot at the beginner's level is 5, then 4, and then 3 for Upper Intermediate and Advanced levels. 
I almost never bother learning words with frequency of 1 or 2, unless it is a word I may use in a professional context. 

![image](https://user-images.githubusercontent.com/91870217/210251534-8229d7a3-7eda-4797-a1b2-b87b7e50f093.png)

### Sample sentences 
I also pull sample sentences from Linguee dictionary via API  - if I decide to put an effort into learning a word, I'll always try to memorize it in a phrase or a sentence. When I become more confident in a language, I try to create my own sentences, but at the beginning I rely on the great Linguee database to look for gramatically correct sentences.
I can then select the one that somehow feels closer to my real life and then I can save it into my flashcard deck. 

### Checking existing word lists
Also, for some languages I have a separate list of core words right from the start that I'm learning with flashcards (see my other project for doing this) - so, I also check any new word against the records in my existing flashcard list.
In some languages grammar may tweak the word a little, so I also look for similarities using Python package *difflib*. 

## Here is a screenshot: 

![image](https://user-images.githubusercontent.com/91870217/210252580-fb6efccd-7a60-426e-9778-bd826f41a360.png)

### And, if I already have the word in my existing list: 

![image](https://user-images.githubusercontent.com/91870217/210252661-bf23b778-4017-4959-94a4-3982aff307e2.png)

