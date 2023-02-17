#A SIMPLE TRANSLATER

def translator(phrase):
   translate=""
   #this translate variable is the one that gonna store our translated sentense with the "t"'s in it
   for letter in phrase:
      if letter.lower() in 'aeiou':
         if letter.isupper():
            translate=translate+"T"
         else:
            translate=translate+"t"
      else:
         translate=translate+letter
   return translate
   #here with this "return", we return the final result after the translation and then it is ready to be printed  
print(translator(input("enter your phrase here: ")))

#this is a translator which translates every vowel of the given phrase into a specific letter which can be a convention for a specific language...

#HERE WE USED THE FOR LOOP WITH THE IF STATEMENT with others IF STATEMENTS NESTED IN them 😊!!







#👇👇👇👇👇👇👇👇👇👇 is the same code but it is a trial to do after learned to make sure that i understod the concept 












def translators(phrases):
   translated=""
   for letters in phrases:
      if letters.lower() in "aeiou":
         if letters.isupper():
            translated=translated+"T"
         else:
            translated=translated+"t"
      else:
         translated=translated+letters
   return translated
print(translators(input("translate here: ")))
            