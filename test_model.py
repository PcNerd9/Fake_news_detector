import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


tfidf, clf = joblib.load("created_dataset/fake_news_detector_without_stopwords.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    stop_words = set(stopwords.words('english'))
    word_tokens = text.split()
    text = " ".join([word for word in word_tokens if word not in stop_words])
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def predict_fake_news(claim):
    x_new = tfidf.transform([claim])

    prediction = clf.predict(x_new)[0]
    probabilities = clf.predict_proba(x_new)[0][1]

    print(f"Prediction: {'Fake' if prediction == 0 else 'Real'}")
    print(f"Confidence: {max(probabilities):.2%}")

examples = [
    "Buhari is the current president of Nigeria.",
    "A Twitter user claims that Nigeria's produces the purest petrol in the world.",
    "A facebook user claims that Nigeria has the best educational system in Africa",
    "Bola Tinubu is the current president of Nigerial.",
    "President Bola Tinubu said Nigeria currency is the highest in Africa. A twitter user claims",
    "flouride is a cause of cancer",
    "VeryDarkMan on X shared an image of a lifeless farmer, claiming that the farmer was attacked and killed by Fulani herdsmen in the South."
    "An Instagram user claimed that a boiled mixture of pineapple peels, cinnamon, cloves, ginger, black pepper, and lemon juice could flatten one’s stomach.",
    "A Facebook user claims via video that Israel’s Prime Minister Benjamin Netanyahu has promised to liberate Africa.",
    "Liberia’s former vice president, Madam Jewel Howard Taylor, advocates for a female candidate in the Nimba by-election, claiming only three or four counties have elected female senators, and the others have never elected a female senator.",
    "A Facebook user claimed that Ukraine had attempted to assassinate Russian President Vladimir Putin in Moscow. ", #T
    "A Facebook user shared a post alleging that PDP’s Acting National Chairperson, Umar Damagum, has resigned, attributing the report to Arise News.",
    "Popular blog Instablog9ja reposted a video on X, claiming it shows youth in Edo protesting against bad governance.",
    'Some Facebook users claimed the “NEC did not stamp the candidate nomination printout of Samuel Kogar.', #T
    " An X user claimed that over 70 per cent of Nigeria’s population is illiterate.",

]

if __name__ == "__main__":
    for claim in examples:
        cleaned_claim = clean_text(claim)
        print(f"Cleaned Claim: {cleaned_claim}")
        predict_fake_news(cleaned_claim)
        print()