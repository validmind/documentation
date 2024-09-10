# StopWords

Evaluates and visualizes the frequency of English stop words in a text dataset against a defined threshold.

### Purpose

The StopWords threshold test is a tool designed for assessing the quality of text data in an ML model. It focuses
on the identification and analysis of "stop words" in a given dataset. Stop words are frequent, common, yet
semantically insignificant words (for example: "the", "and", "is") in a language. This test evaluates the
proportion of stop words to the total word count in the dataset, in essence, scrutinizing the frequency of stop
word usage. The core objective is to highlight the prevalent stop words based on their usage frequency, which can
be instrumental in cleaning the data from noise and improving ML model performance.

### Test Mechanism

The StopWords test initiates on receiving an input of a 'VMDataset' object. Absence of such an object will trigger
an error. The methodology involves inspection of the text column of the VMDataset to create a 'corpus' (a
collection of written texts). Leveraging the Natural Language Toolkit's (NLTK) stop word repository, the test
screens the corpus for any stop words and documents their frequency. It further calculates the percentage usage of
each stop word compared to the total word count in the corpus. This percentage is evaluated against a predefined
min_percent_threshold'. If this threshold is breached, the test returns a failed output. Top prevailing stop words
along with their usage percentages are returned, facilitated by a bar chart visualization of these stop words and
their frequency.

### Signs of High Risk

- A percentage of any stop words exceeding the predefined 'min_percent_threshold'.
- High frequency of stop words in the dataset which may adversely affect the application's analytical performance
due to noise creation.

### Strengths

- The ability to scrutinize and quantify the usage of stop words.
- Provides insights into potential noise in the text data due to stop words.
- Directly aids in enhancing model training efficiency.
- Includes a bar chart visualization feature to easily interpret and action upon the stop words frequency
information.

### Limitations

- The test only supports English stop words, making it less effective with datasets of other languages.
- The 'min_percent_threshold' parameter may require fine-tuning for different datasets, impacting the overall
effectiveness of the test.
- Contextual use of the stop words within the dataset is not considered, potentially overlooking their significance
in certain contexts.
- The test focuses specifically on the frequency of stop words, not providing direct measures of model performance
or predictive accuracy.