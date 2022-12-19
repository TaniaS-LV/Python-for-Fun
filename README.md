# Automated Flashcard Deck Preparation
As an avid language learner, I am a big fan of flashcards. I do see a number of drawbacks in most existing flashcard solutions which I will hopefully try to gradually overcome with my other projects built on Python, but at this moment, I am using AnkiApp as my main flashcard tool (not to be confused with AnkiDroid). 

Over the years, I have created my own list of words and phrases I wanted to learn with flashcards (the ones I use most frequently in my daily life and which don’t necessarily coincide with word frequency lists found on the Internet (for example, in my list I have a lot words related to my career, my hobbies, my country etc., which may not be relevant to other people), besides I tried to create phrases for each of the words so that I can memorize them in context.).  

Here is how Python helped me create my flashcard decks in seconds: 
* **translate all the words and phrases into my target language**. To achieve that, I used Deepl.com API which is by far the best translating solution on the market. The best part – it is free! 
* **get the voice recording to train pronunciation**. To achieve that, I used an API based on Microsoft Speech Service (hosted on RapidAPI.com). On a side note – I was really surprised by the quality of the voice recordings, which is nothing like the robotic pronunciation used a couple of years ago by most online text-to-speech services. 
* **format all the data according to the AnkiApp requirements into a CSV file**. To achieve that, I used pandas library.

Some screenshots: 

* Input file example: 

![image](https://user-images.githubusercontent.com/91870217/208480958-10e79e2a-77e8-4aa7-9cdf-121ceea2df91.png)

* Output file example:

![image](https://user-images.githubusercontent.com/91870217/208481223-cdbf7a97-1f93-4faf-b35b-bea7691b9227.png)

* CSV file uploaded into AnkiAPP:

![image](https://user-images.githubusercontent.com/91870217/208481424-04983d71-dc54-43da-8b73-a78dd05e9e25.png)





