import os
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank

import pickle

song = './data/test.wav'
y, sr = librosa.load(song, sr=16000)

def extract_features(y, sr=16000, nfilt=10, winsteps=0.02):
    try:
        feat = mfcc(y, sr, nfilt=nfilt, winstep=winsteps)
        return feat
    except:
        raise Exception("Extraction feature error")

def crop_feature(feat, i = 0, nb_step=10, maxlen=100):
    crop_feat = np.array(feat[i : i + nb_step]).flatten()
    print(crop_feat.shape)
    crop_feat = np.pad(crop_feat, (0, maxlen - len(crop_feat)), mode='constant')
    return crop_feat

y, sr = librosa.load('./test.wav', sr=16000)
feat = extract_features(y, winsteps=50)
print(crop_feature(feat).shape)

songs = []
features = []


for song in tqdm(os.listdir('./data')):
    song = os.path.join('./data', song)
    y, sr = librosa.load(song, sr=16000)
    feat = extract_features(y)

    for i in range(0, feat.shape[0] - 10, 5):
        features.append(crop_feature(feat, i, nb_step=10))
        songs.append(song)

pickle.dump(features, open('features.pk', 'wb'))
 
pickle.dump(songs, open('songs.pk', 'wb'))