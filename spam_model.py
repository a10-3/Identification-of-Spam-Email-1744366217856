import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Dummy dataset for demonstration
data = {
    'text': [
        'Congratulations! You have won a lottery. Click here to claim your prize.',
        'Dear friend, I hope you are doing well. Let’s catch up soon.',
        'Get paid to work from home! Limited time offer.',
        'Hi, just checking in to see how you are doing.',
        'You have a new message from your bank. Please verify your account.',
        'This is a reminder for your appointment tomorrow.',
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Train the model
def train_model():
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(df['text'], df['label'])
    joblib.dump(model, 'spam_model.pkl')

# Load the model
def load_model():
    return joblib.load('spam_model.pkl')

# Predict function
def predict_email(email_text):
    model = load_model()
    if not email_text:
        raise ValueError("Email text cannot be empty.")
    prediction = model.predict([email_text])
    return prediction[0]

# Train the model on startup
train_model()
