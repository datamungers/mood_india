##<p style='text-align: center;'>Indian Mood Throughout the Day Inferred from Twitter</p>
--------

<p style='text-align: center;'>Anmol Gulati<sup>[1]</sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pawan Goyal<sup>[1]</sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Buddha Prakash<sup>[1]</sup></p>

<p style='text-align : center;'><sup>[1]</sup>Indian Institute of Technology Kharagpur, Kharagpur, India-721302</p>
##Abstract
---------

We aim to develop a robust system for analysing Tweets for emotion. And further apply the system to identify and analyse the national psyche as expressed on Twitter. We present a lexicon-based apprach to extracting sentiment from text. We apply a state of the art approach to perform the normalization of tweets. We then compare and contrast various lexicon sources based on their performance in the polarity classification task. We consider three methods, namely Bing Liu's opinion lexicon, AFINN sentiment lexicon and sentiwordnet and find out that sentiwordnet generally performs better. We then study and analyze the temporal and geographical variations of sentiments of the whole country by considering all the geocoded tweets, tweeted from the country.

##Introduction
----------------


In the past decade, new forms of communication, such as microblogging and text messaging have emerged and become ubiquitous. 
While there is no limit to the range of information conveyed by tweets and texts, often these short messages are used to share opinions and sentiments that people have about what is going on in the world around them.Over the past few years, Twitter has become very popular and has also been described as "The SMS of the Internet" .According to the latest Twitter entry on Wikipedia, the number of Twitter users has climbed to 500 million and the number of tweets published on Twitter every day is over 340 million<sup>[1]</sup>


##Data Description
-------------------
Tweets are short messages restricted to 140 characters in length.Due to the nature of this Microblogging Service(quick and short messages) people often use acronyms,make spelling mistakes,use emoticons and other characters that express special meanings.<br><br>
__Emoticons__ : These are facial expressions signifying the user's mood,pictorially represented using punctuation and letters.<br>
__Target__    : Twitter users often use __'@'__ to refer to other users on the microblog.<br>
__Hastags__   : Hashtags are words prefixed with __'#'__ and are used to mark topics.Users often use hashtags primarily  to increase visibility of their tweets.

##Twitter API
--------------
Twitter exposes its data via an Application Programming Interface, (API). Twitter itself offers the functionality where researchers can search for tweets pertaining to a query. Twitter Search provides a __GET Search API__ so that we can search for tweets in an automated fashion.GET allows to stream tweets on specific queries based on many characteristics as language,country,location,particular user and many more.<br>
In our work, we wrote a code for the GET Search API which to stream tweets specifically from India.

##PreProcessing
-----------------------------------

In our approach,data pre-processing is necessary in order to perform any data mining functionality. It becomes even more essential to our method because we use a lexicon-based approach for sentimental polarity classification.<br><br>
<p>
1. __Removing URL's, Image links and Retweets __<br>
    In general, URLs,Image links and Retweets do not contribute to analyze the sentiment in the informal text.<br>For example consider the sentence "@JohnDoe I lost all my bets at www.win.com :(".<br> Actually the above tweet is negative but because of the presence of the word "win" it might get considered as a Positive Tweet. In order to avoid this sort of failures, we must employ a technique to remove URL's,Image Links and Retweets.<br><br>
2. __Removing Special Characters__<br>
    Special Characters like "!@#%^&*" etc. don't convey <a href=""></a>ny particular emotion or sentiment so they must also be filtered from the tweets.<br>For example, "Go SF Giants! Such an amaazzzzzing feelin’!!!! \m/ :D".<br> Here, if the special characters are not removed, they might concatenate with the other words and would make those words unavailable in the lexicon.<br><br>
3. __Tokenization and Conversion to Lower Case__<br>
    Tokenization of the tweets is then done to break the stream of text into tokens.These tokens are then also converted to lower case to maintain uniformity.<br><br>
4. __Removing Reduntant Characters__<br>
    Lengthening by character repitition is widely done by twitter users to indicate heightened emotion but in English, sequences of continous three or more identical letters are basically unattested in the standard lexicon. So it becomes, very essential to remove the reduntant characters in a word to later be able to map them onto the words in the lexicon.<br>For example, "Go SF Giants! Such an amaazzzzzing feelin’!!!! \m/ :D".<br>Here "amaazzzing" gets converted to "amaazzing" and this becomes essential in the later stage of our pre-processing methodology.<br><br>
5. __Spell Correction__<br>
    We perform spelling correction in order to map the mispelled words to their nearest correct word form. We use the a really powerful spell correction algorithm developed by Peter Norvig<sup>[2]</sup><br><br>
6. __Removing Stop Words__<br>
    Some extremely common words which would be of little value for sentiment polarity classification are excluded from the vocabulary entirely.We use the stop words list available in NLTK Library which is widely used for this purpose.<br><br>
7. __Stemming__<br>
    In most tweets, morphological variants of words have similar semantic interpretations but in our task. For this reason we use a stemming algorithm to reduce the words of the tweets to their root form. We use the Lancaster stemmer for our stemming task as we found it generally performs well in such tasks.<br>For example,['go','sf','giants','such','an','feeling'].<br> In the example above 'giants' is reduced to its root form 'giant' and 'feeling' gets reduced to 'feel'.

</p>
##Methodology
----
Simple sentiment analysis looks at individual words and surely does not necessarily capture the ‘true’ expressed emotion ignoring, say, context, negation and sarcasm. Nevertheless, many studies now show that this simple word-based approach can to some degree determine the sentiment of a text. With access to a annotated data set, machine learning can be used to boost the performance even further. Currently we study the performance of various lexicon based approaches and compare their accuracy. For testing the performance of the different methods we calculated their accuracy on about 10,000 annotated tweets which is made available by SemEval-2013<sup>[3]</sup> . We are currently working on developing a supervised learning algorithm to improve the accuracy of the classifier.

###Bing Liu's Opinion Lexicon

Bing Liu maintains and freely distributes a sentiment lexicon consisting of lists of strings.This list consists of positive and negative opinion words or sentiment words for English(around 6800 words). The list performs well as it also includes mis-spellings, morphological variants, slang, and social-media mark-up besides english words.
We use this list to compute the score of each tweet depending on whether the tokens of tweet is positive or negative words in the lexicon.

###AFINN Lexicon

AFINN is a list of English words rated for valence with an integer between minus five (negative) and plus five (positive).The words have been manually labeled by Finn Årup Nielsen in 2009-2011. We use the newest lexicon which contains 2477 words<sup>[4]</sup>
We compute the sentiment score of a tweet by summing up the individual valence scores of each word in the AFINN list.

###SentiWordNet

SentiWordNet<sup>[5]</sup> is a lexicon resource which comprises of synsets of WordNet which are assigned three sentiment scores: positivity, negativity and objectivity. The above approaches use a small set of  collected affective words. And thus these lexicons are limited to their domain and do not take into account the relation between words. SentiWordNet provides an extension for WordNet, and thus allows for assigning scores to different words based on the context in which they are used.

The part-of-speech tagging is first performed on the tokens of the tweet. The name and the pos tag of each token is then used to find all the synsets having the same context as the tokens. Then the word is considered to be positive if it has more synsets where the positive score is greater than negative score, negative if it has more entries where the negative scoreis greater than the positive score and neutral when there is no variation in the number of entries between positive and negative. The score of the whole tweet is then computed as the number of positive tokens minus the number of negative tokens in the tweet.


##Evaluation
-----

We use the Sem-Eval-2013 annotated twitter dataset for comparing the performance of the above approaches.
Based on our experiments we got the following accuracies of the above methods:<br>
###Accuracy
| Approach                     | Accuracy (%)            | 
|:-----------------------------|-------------------------:|
| Bing Liu's Opinion Lexicon   |        42.31              |
| AFINN Lexicon                |      39.78             |
| SentiWordNet                 |        67.34              |

<div style="page-break-after: always;"></div>
##References
[1] : [Twitter](http://en.wikipedia.org/wiki/Twitter "Twitter")
    
[2] : [Peter Norvig's Spell Coorrect](http://norvig.com/spell-correct.html, "Spell Correct")
    
[3] : [SemEval'2013: SemEval-2013 Task 2: Sentiment Analysis in Twitter.
      Preslav Nakov, Sara Rosenthal, Zornitsa Kozareva,Veselin Stoyanov, Alan Ritter, Theresa Wilson
      ](http://www.aclweb.org/anthology/S/S13/S13-2052.pdf, "Paper")
      
[4] : Lars Kai Hansen, Adam Arvidsson, Finn Årup Nielsen, Elanor Colleoni, Michael Etter, 
      "Good Friends, Bad News - Affect and Virality in Twitter", SocialComNet 2011.

[5] : [SentiWordNet](http://sentiwordnet.isti.cnr.it, "SentiWordNet")








