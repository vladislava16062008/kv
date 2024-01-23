# -*- coding: utf-8 -*-
"""kv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I3Gety2H0z2_3248SEyCZ4LmZSjj8gEX
"""

import pandas as pd
import numpy as np
import scipy
from scipy import signal as sig
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
def chunk(data, need_chanel,count_chanel=6, fs=250, ):   #жоско распределяем по каналам если норм табличка
    sets_new = []
    frames = []
    x = (pd.DataFrame(np.array(data).T[:][0:(fs*count_chanel)]).T)
    for i in range(0,fs*count_chanel,fs):
        sets_new.append(np.array(data.iloc[:, i:i+fs]))
    for j in need_chanel:
      frames.append(pd.DataFrame(sets_new[j].T))
    new_data = pd.concat(frames,ignore_index = True).T
    return new_data

def read(n):     #чтение файлов
    m=[]
    t=[]
    with open (n) as nt:
        for line in nt:
            v=line.strip()
            l,cc,k=v.split(';')
            m.append(cc)
            t.append(k)
    return pd.DataFrame(m),pd.DataFrame(t)

def f_spectrum(data,fre = 250):
  fy=fft(data)  #преобразование фурье
  step = 1.0 / fre
  sz = data.size
  fx = fftfreq( sz, step)[0:sz//2]
  fy_normed = 2.0/sz * np.abs(fy[0:sz//2])
  return fx, fy_normed #частоты, амплитуды

def butter_bandpass(data,lowcut, highcut, fs = 250, order=5):   #фильтр баттерворда
  nyq = 0.5 * fs
  low = lowcut / nyq
  high = highcut / nyq
  b, a = sig.butter(order, [low, high], btype = 'band')
  y = sig.lfilter(b, a, data)
  return y

def average_plt(data,ch = 8,len_ep = 1,fs = 250):  #массив с нужными эпохами
   epo_len =  len_ep*fs
   T = np.zeros((epo_len, ch))
   for t in range(len(data)):
       T += data[t:t+epo_len]

   T = T / len(data)

   handle = plt.plot(T)
   plt.legend(handles=handle, labels=['Cz', 'Pz', 'PO7', 'PO8', 'O1', 'O2'], loc=1)
   plt.ylabel('mV')
   plt.xlabel('ms')
   plt.show()
