# Sirens: A Data Sonification of the COVID-19 Pandemic

[Final Render - click here](https://drive.google.com/file/d/1mHj1pfbGgbz1pp7jB2feuoc3_iqL6Qsq/view?usp=sharing)

This project is my first work in Data Sonification, which I completed during my 4th semester at Brown University. I am concentrating in both Applied Math - Computer Science and Music; through this project, I have found a way to tie together these two interests.
I was inspired to begin this project by a round table discussion I had with data journalist Mona Chalabi, sponsored by Brown's Data Science Initiative. We were discussing creative ways of displaying data through non-visual mediums, for example depicting rising and falling data using sound waves. My mind immediately jumped to the COVID-19 Pandemic, and how I could recreate rising and falling case counts via sound, perhaps on a global scale.

## Part 1: starterFiles

First, I needed to understand how to create sound from code. I used the Python libraries Numpy for mathematical tools and SciPy for I/O to .wav files, to explore musical concepts like pitch, volume, timbre, and harmony.

## Part 2: sirens

Once I understood the basics of coding sound, I returned to my original goal: sonifying the COVID-19 Pandemic. I downloaded a CSV file from the World Health Organization, and wrote a script that runs a terminal interface. The user inputs a region, a minimum frequency, and a maximum frequency. The code creates a Numpy array of that region's daily COVID data, smoothed via 2-week averages, and generates sound using the techniques I learned in Part 1. In the "waves" folder are some waves that I generated using this script.

## Part 3: compositions

Finally, I took these generated waves and combined them with other sounds to create music.


In "Sirens - generated waves," I combined the generated audio files, and panned them roughly to their geographic location on a Western-standard map (i.e. Americas panned left, Western Pacific panned right, etc.). Immediately some patterns became evident: the slow gradual rise at the start of the pandemic, a wave in winter 2021, and an even worse wave in winter 2022. I also learned some unexpected information; WPRO's most prominent wave happened in winter 2023, during a sudden series of outbreaks in China.


With these contours in mind, I wrote accompaniment parts for piano and percussion, to create some musical structure to the waves, which I dubbed "sirens" at this point for their eerie atonal quality. I had the pleasure of presenting this arrangement live to my fellow students at a college composition showcase, with the piano and snare drum on stage and the Python-generated waves coming from speakers encircling the auditorium seating. The file "Sirens - rough cut with MuseScore instruments" is an approximation of this, using the auto-generated instrumental performances of my composition software.


My next arrangement of this was a final project for MUSC 1200, "Recording and Sound Design." I added many more sound effects, most notably a collage of news soundbites, mostly lined up to the timeline of the waves. Except for the intro and outro, each clock tick marks 1 day, each heartbeat marks 1 month, and each chime marks 1 year. The link at the top of this document links to an mp3 of this arrangement.


## Future 

I have plans to create a visualization to accompany this music; whether this takes the form of a YouTube video, a physical exhibit, or something else, is to be determined.

I also plan on creating more Data Sonifications like these, with the eventual goal of releasing an entire album. I believe in the emotional power that music can have on people, and how good data storytelling can lead audiences to resonate with numerical data (pardon the pun), by taking advantage of the unique medium of sound.