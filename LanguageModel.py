import string
import numpy as np
from pickle import dump
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Embedding
from random import randint
from pickle import load
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import math

def ReLU(value):
    if value < 0:
        return 0
    return value

def softmax(layer):
    out = np.exp(layer) / sum(np.exp(layer))
    return out

def separate():
    f2 = open("republic_clean.txt", "r")
    intro = f2.read()
    f2.close()

    intro.replace("-", " ")
    tokens = intro.split()
    # replaces x with y, z is deleted from the string all together. The deletion occurs before other
    # things are added, meaning that it only deletes from the original string
    table = str.maketrans("", "", string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    for w in tokens:
        w.translate(table)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [w.lower() for w in tokens]
    print(tokens[0])
    return tokens

def clean_text(tokens):
    print("Token Length: %d" % len(tokens))
    print('Unique Tokens: %d' % len(set(tokens)))

    length = 51
    groups = list()
    for i in range(length, len(tokens)):
        words = tokens[i-length : i]
        line = ""
        for w in words:
            line += w + " "
        groups.append(line)

    print(len(groups))
    return groups

def save_to_doc(groups):
    f = open("save.txt", "w")
    f.truncate()
    for data in groups:
        f.writelines("% s\n" % data)
    f.close()

def assign_values(tokens):
    index = list()
    index.append(0)
    for w in tokens:
        if not w in index:
            index.append(w)
    print(index[1])
    return index

def encode(sequences, values):
    f = open("input.txt", "w")
    sequence_nums = list()
    for line in sequences:
        nums = ""
        words = line.split()
        for w in words:
            nums += str(values.index(w)) + ","
        sequence_nums.append(nums)
        f.writelines(nums + "\n")
    f.close()
    return sequence_nums


tokens = separate()
groups = clean_text(tokens)
save_to_doc(groups)

doc = read_text('save.txt')
sequences = doc.readlines()
lines = doc.split('\n')


assigned_values = assign_values(tokens)
#encoded_sequences = encode(sequences, assigned_values)
vocab_size = len(assigned_values)


tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
unique_words = len(tokenizer.word_index) + 1

def read_text(file_name):
    f = open(file_name, "r")
    text = f.read()
    f.close()
    return text

doc = read_text('save.txt')
lines = doc.split('\n')

length = len(lines[0]) - 1

model = load_model('model.h5')
tokenizer = load(open('tokenizer.pkl', 'rb'))

seed_text = lines[randint(0, len(lines))]
print(seed_text + '\n')


def generate_sequence(seed_text, sequence_length, tokenizer, model, wordNum):
    result = list()
    in_text = seed_text

    encoded = tokenizer.texts_to_sequences(seed_text)[0]
    for i in range(0,wordNum):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=sequence_length, truncating='pre')
        yhat = model.predict_classes(encoded, verbose=0)
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break

    in_text += ' ' + out_word
    result.append(out_word)
    return ' '.join(result)

generate = generate_sequence(seed_text, length, tokenizer, model, 50)
print(generate + str(len(generate)))

#add encode function (encodes each line in save.txt, does oneHot to find the output word)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
