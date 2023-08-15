The Sight Reading Generator uses machine learning methods, specifically neural network-based sequence prediction, to analyze the probability distribution of notes used in masterpieces from over a dozen famous composers and automatically construct sheet music based upon this analysis and given parameters selected by the user, therefore creating a progression of notes that sound more musically advanced than what would normally be sampled randomly. 

The website will soon be open to the public. For now, the Sight Reading Generator can be run locally on Mac, Python 3.7
1. Download the repository.
2. Download Musescore (version 2 or higher). 
3. Pip Install Flask, numpy, music21, scikit-learn, and pandas. 
4. Open Terminal
5. cd Desktop/sight_reading_generator
6. export FLASK_APP=flaskr
7. export FLASK_ENV=development
8. python3 -m flask run

Have fun!

