import json
import random
import math


def load_email_data(spam_path, ham_path):
    with open(spam_path, encoding="utf-8") as f1, open(ham_path, encoding="utf-8") as f2:
        spam_data = json.load(f1)
        ham_data = json.load(f2)
    return spam_data + ham_data



def train_test_split(data, test_ratio=0.2):

    random.shuffle(data)
    cut = int(len(data) * (1 - test_ratio))
    return data[:cut], data[cut:]






def preprocess(text):
    return text.lower().replace("-", " ").replace("–", " ").replace("—", " ").replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").split()







def train_naive_bayes(train_data, alpha=1.0):

    class_counts = {}
    word_counts = {}
    total_words = {}
 
    for rec in train_data:
        label = rec["label"]
        class_counts[label] = class_counts.get(label, 0) + 1
        word_counts.setdefault(label, {})
        total_words.setdefault(label, 0)
 
        words = preprocess(rec["text"])
        for word in words:
            word_counts[label][word] = word_counts[label].get(word, 0) + 1
            total_words[label] += 1
 
    vocab = set()
    for wc in word_counts.values():
        vocab.update(wc.keys())
 
    return {
        "class_counts": class_counts,
        "word_counts": word_counts,
        "total_words": total_words,
        "vocab": vocab,
        "alpha": alpha,
        "total_docs": len(train_data)
    }






def log_prob(model, words, class_name):
    logp = math.log(model["class_counts"][class_name] / model["total_docs"])
    V = len(model["vocab"])
    a = model["alpha"]
    for word in words:
        wc = model["word_counts"][class_name].get(word, 0)
        logp += math.log((wc + a) / (model["total_words"][class_name] + a * V))
    return logp



def predict(model, text):
    words = preprocess(text)
    best_class, best_log = None, -float("inf")

    for c in model["class_counts"]:
        lp = log_prob(model, words,  c)
        if lp > best_log:
            best_class, best_log = c, lp
    return best_class

    
        




def evaluate_model(model, test_data):
    correct = 0
    for rec in test_data:
        pred = predict(model, rec["text"])
        if pred == rec["label"]:
            correct += 1
    accuracy = correct / len(test_data)
    print(f"Skutecznosc na zbiorach testowych: {accuracy * 100:.2f}%")
    
    return accuracy






from pprint import pprint


def main():
    data = load_email_data("spam.json", "ham.json")
    train, test = train_test_split(data)
    model = train_naive_bayes(train)


    evaluate_model(model, test)

    while True:
        user_input = input("Enter a message to clasyfication or exit: \n")
        if user_input.lower() == "exit":
            print("Goodbey")
            break
        prediction = predict(model, user_input)
        print(f"Clasyfication {prediction}")



    


    #pprint(model)




if __name__ == "__main__":
    main()