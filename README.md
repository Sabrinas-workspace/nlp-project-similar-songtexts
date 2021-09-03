# nlp-project-similar-songtexts

About the project

The goal of my project is to find similar songs to a song with different NLP
methods. For this I only consider the songtext of the songs.
I am working alone on this project and it is my project work for my university class
"Advanced Natural Language Processing with Python": https://esther.seyffarth.one/classes/2021-advanced-nlp/.

The data

For my project I created a corpus of songtexts which I cannot include do to copyright 
reasons. However, now will follow instructions on how you can create a corpus for
this project yourself.
I created my corpus in XML and used https://genius.com/ as source for the songtext.
This is how my corpus is structured:
<data>
    <song name="This is a song">
        <artist name= "This is an artist">
        </artist>
        <songtext>
            This is a songtext
        </songtext>
    </song>
    <song name="This is another song">
        <artist name= "This is another artist">
        </artist>
        <songtext>
           This is another songtext
        </songtext>
    </song>
</data>

Because I wanted to work with XML, it was the easiest for me to just copy and paste
the songtext and delete "Chorus", "Verse", "Bridge" etc., so that it is just one connected
text. I thought about using a web scrapper but since I wanted that exact structure above,
it would have been more time_consuming.

How you can try out the code yourself

You can find all the packages I used for this project in the requirements.txt file.
There is also the linter that I used included, in case you want change and add to the code
but keep the code style. I decided to follow Google's style and therefore used pylint.


