

# Import libraries
import nltk
import spacy

# Download required NLTK data
nltk.download('punkt')

# Load a short paragraph
text = """
Friends are the pillars of our happiness and support in life. They share our laughter, wipe away our tears, and stand by us through every challenge. A true friend understands us without judgment and accepts us as we are. They celebrate our victories with genuine joy and encourage us when we feel low. Friendship is built on trust, respect, and countless shared memories. Small acts of kindness make the bond stronger each day. Friends turn ordinary moments into unforgettable experiences. They inspire us to grow and become better versions of ourselves. With friends, even the toughest journeys feel lighter. Life becomes more meaningful and beautiful when we have good friends around.
"""

# Count number of words
words = text.split()
word_count = len(words)

# Convert text to lowercase
lower_text = text.lower()

# Display results
print("Original Text:\n", text)
print("\nLowercase Text:\n", lower_text)
print("\nNumber of Words:", word_count)
