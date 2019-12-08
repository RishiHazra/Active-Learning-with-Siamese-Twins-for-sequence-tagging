#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from statistics import mean
# t = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# random  = [58.55,65.00,70.16,75.45,78.50,78.77,79.35,80.00,82.50,82.35,82.25,82.30,82.23,82.42,82.66,83.00,84.64,84.15,84.19,84.25,84.75,84.50,84.89,85.05]
# base = [90]*len(t)
#==============================================================================
'''
NER CoNLL BALD
'''
# siamese = [58.55,79.32,83.24,84.77,85.69,85.75,86.39,86.88,87.05,87.50,87.85,87.70,87.75,88.10,88.30,88.35,88.50,88.65,89.20,89.09,89.22,89.38,89.78,89.79]
# cosine  = [58.55,78.00,82.35,84.00,84.12,85.40,85.12,84.74,85.84,86.26,86.85,86.86,87.30,87.80,88.10,88.15,88.50,88.70,88.78,88.80,89.05,89.12,89.30,89.50]
# ST      = [58.55,78.20,82.38,83.70,85.00,85.20,86.20,85.75,87.10,85.75,87.25,87.35,87.30,87.78,87.45,87.75,88.10,88.20,88.00,88.11,88.30,88.50,88.70,89.35]
# none    = [58.55,67.00,71.45,79.95,81.86,82.50,84.23,84.50,85.37,86.21,86.54,87.30,86.44,87.50,87.80,87.90,88.10,88.05,88.30,88.58,88.78,88.89,89.01,89.20]
# iso     = [58.55,78.10,82.66,82.90,84.65,85.30,86.20,85.90,86.65,86.80,87.55,87.70,88.10,87.30,88.23,88.20,88.50,88.55,88.70,88.58,88.85,89.10,89.00,89.25]
#==============================================================================
'''
NER CoNLL Entropy
'''
# siamese = [58.55,73.70,81.70,82.71,82.88,83.63,84.88,85.26,85.09,85.50,86.00,85.85,86.15,86.45,85.25,86.05,86.73,86.54,86.72,87.05,87.20,87.99,88.10,88.20]
# cosine  = [58.55,73.20,78.15,79.70,82.31,82.11,83.55,84.59,83.50,84.26,84.38,85.68,84.78,85.02,84.90,85.12,85.30,85.21,85.60,85.70,85.75,86.05,86.35,86.45]
# ST      = [58.55,72.80,79.20,80.50,82.80,83.45,83.60,84.00,84.35,84.50,85.45,85.50,85.46,86.20,85.45,85.30,85.70,85.90,86.20,85.95,86.25,86.70,86.85,86.92]
# none    = [58.55,68.10,74.10,78.00,80.97,78.58,81.00,82.40,82.86,83.52,84.26,84.69,82.91,83.71,84.74,84.92,85.14,85.09,85.31,85.20,85.75,85.85,85.90,86.12]
# iso     = [58.55,73.35,78.32,79.20,82.10,82.70,83.35,84.00,84.80,84.60,84.79,85.50,85.10,85.50,85.65,85.54,86.20,85.24,85.40,85.67,85.45,86.10,86.05,86.19]
# #==============================================================================
'''
NER CoNLL Margin
'''
# siamese = [58.55,73.78,79.00,82.20,83.20,84.00,84.81,85.56,86.05,86.00,86.75,86.86,86.55,87.30,88.00,87.50,88.25,88.10,88.50,88.70,88.45,88.69,88.95,89.20]
# cosine  = [58.55,73.50,77.20,79.31,81.76,82.90,83.26,83.37,84.00,83.50,83.89,84.24,84.84,85.00,85.57,85.50,85.65,85.86,86.02,85.95,86.30,86.35,85.95,86.30]
# ST      = [58.55,73.30,78.50,80.00,82.00,83.05,83.40,83.65,84.35,84.05,84.80,85.00,85.21,85.83,85.20,85.00,85.60,86.05,86.15,86.25,86.60,86.89,86.70,87.05]
# none    = [58.55,68.00,72.95,77.40,80.85,81.00,81.10,81.31,81.43,81.83,82.10,82.92,84.16,84.20,83.80,84.45,84.56,84.21,84.57,84.87,84.70,85.01,85.10,85.05]
# iso     = [58.55,73.25,77.00,78.05,81.80,82.80,83.15,83.50,84.20,84.06,84.38,84.40,84.50,84.80,85.00,85.68,85.34,85.45,85.50,85.19,85.55,85.70,86.45,86.34]

#===============================================================================
#===============================================================================
#===============================================================================

# t = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# random  = [75.06,80.55,83.14,84.00,85.12,85.85,86.50,87.20,87.45,87.85,88.59,88.50,88.60,88.68,88.54,88.85,88.95,88.90,88.82,89.01,89.15,89.25,89.30,89.35]
# base = [91.80]*len(t)
'''
POS CoNLL BALD
'''
# siamese = [75.06,84.50,86.56,87.21,87.72,88.77,89.20,89.86,89.90,90.05,90.15,90.13,90.30,90.25,90.45,90.57,90.75,90.55,90.78,90.88,90.95,90.80,91.01,91.10]
# cosine  = [75.06,84.52,86.40,87.00,87.59,88.50,88.83,89.50,88.90,89.95,89.05,89.69,90.05,90.22,90.12,90.35,90.45,90.39,90.43,90.50,90.65,90.26,90.59,90.79]
# ST      = [75.06,85.00,86.50,87.55,88.00,88.60,88.80,89.10,89.30,89.50,89.70,89.85,90.00,90.15,90.65,90.10,90.20,89.85,90.22,90.30,90.50,90.55,90.85,90.60]
# none    = [75.06,83.85,85.48,87.35,87.30,87.75,88.32,88.32,88.72,89.20,89.30,89.52,89.45,89.65,89.75,89.90,90.01,89.86,89.80,89.90,90.05,90.12,90.15,90.10]
# iso     = [75.06,84.00,86.00,87.22,88.10,88.45,89.20,89.05,89.39,90.00,90.22,89.80,89.90,90.05,90.30,90.20,90.26,90.45,90.00,90.40,90.45,90.57,90.70,90.65]
#===============================================================================
'''
POS CoNLL Entropy 
'''
# siamese = [75.06,83.25,84.00,84.30,86.19,85.78,87.02,87.20,87.38,87.77,87.90,88.05,88.35,88.53,88.85,88.70,88.90,89.05,88.98,89.07,89.25,89.30,89.45,89.91]
# cosine  = [75.06,83.21,84.12,84.08,85.00,85.96,86.15,87.05,87.50,87.92,87.97,88.00,88.97,88.12,88.53,88.64,88.59,89.21,89.60,89.69,89.79,89.15,89.24,89.55]
# ST      = [75.06,83.80,84.70,85.30,86.00,86.80,87.05,87.10,87.81,87.50,87.79,87.80,88.10,88.05,88.15,88.26,88.35,88.40,88.89,88.45,88.50,88.92,88.75,89.16]
# none    = [75.06,83.08,83.88,84.25,85.26,86.00,85.29,86.00,87.25,87.53,87.65,87.50,87.89,88.00,88.10,88.32,88.54,89.05,89.10,89.30,89.50,89.09,89.21,89.63]
# iso     = [75.06,83.15,84.80,85.50,86.00,86.72,86.50,86.80,87.50,87.50,87.70,87.80,88.00,88.89,88.25,88.40,88.65,88.55,88.63,88.60,88.70,89.29,89.10,89.35]
#===============================================================================
'''
POS CoNLL Margin
'''
# siamese = [75.06,81.20,84.25,85.84,86.16,86.86,87.10,87.59,88.24,88.79,89.02,88.75,88.90,88.78,89.01,89.15,89.55,89.87,89.78,89.75,89.91,89.97,89.85,89.99]
# cosine  = [75.06,81.15,83.87,86.55,86.92,86.50,87.69,87.23,87.83,88.23,88.83,89.10,89.34,88.45,89.00,89.05,89.25,89.70,89.50,89.70,89.80,89.76,89.80,89.75]
# ST      = [75.06,81.25,84.50,86.20,86.20,86.95,87.35,87.75,88.30,88.15,88.45,88.80,88.75,89.20,88.85,89.10,89.50,89.45,89.29,89.35,89.28,89.58,89.65,89.48]
# none    = [75.06,81.00,83.45,84.25,84.85,85.96,86.89,85.50,87.21,87.53,87.73,87.32,87.99,88.21,88.52,88.70,88.64,88.90,89.05,89.25,89.12,89.22,89.50,89.58]
# iso     = [75.06,81.50,85.00,85.40,85.80,86.62,86.70,87.55,88.20,88.05,88.32,88.50,88.40,89.10,88.70,88.85,88.90,89.15,89.09,89.40,89.24,89.75,89.60,89.70]

#===============================================================================
#===============================================================================
#===============================================================================

# t = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# random  = [57.00,57.71,58.18,60.10,61.00,61.45,62.40,62.70,62.80,63.30,64.00,64.45,64.60,65.00,65.15,65.45,65.50,65.55,66.10,66.00,66.05,65.79,66.10,66.78,66.44,66.40,66.66,67.00,67.44]
# base = [70.50]*len(t)
'''
MIT Movie BALD
'''
# siamese = [57.00,58.00,61.77,62.33,63.50,64.50,64.86,65.32,65.80,66.30,66.70,67.09,67.50,68.27,68.00,68.29,68.49,68.57,68.75,68.32,68.40,68.65,69.56,69.54,68.83,68.63,69.35,69.91,70.00]
# cosine  = [57.00,58.05,60.00,62.00,62.55,63.40,64.95,65.30,65.40,66.10,66.50,67.20,66.41,68.30,67.00,67.55,67.54,67.85,68.30,68.40,68.50,68.09,68.30,68.63,69.23,68.75,69.00,69.30,68.73]
# ST      = [57.00,58.00,59.60,61.31,62.75,63.10,64.50,64.35,65.00,65.79,66.00,66.85,66.20,67.00,67.10,66.50,67.00,67.95,68.50,67.80,68.20,68.71,68.40,68.83,68.58,68.60,68.75,68.90,69.05]
# none    = [57.00,57.80,58.50,60.20,62.00,62.80,63.40,63.50,63.80,63.75,64.70,65.45,65.00,66.01,66.50,66.00,65.85,66.20,66.50,67.05,67.15,67.90,67.75,68.20,68.50,68.60,67.95,68.35,68.52]
# iso     = [57.00,58.05,60.50,61.85,63.20,63.00,64.40,65.00,65.15,65.55,66.20,67.00,67.02,67.31,66.25,67.01,67.38,67.80,68.43,67.55,67.73,68.00,68.50,68.40,68.15,68.25,68.00,67.50,67.76]
#================================================================================
'''
MIT Movie Entropy 
'''
# siamese = [57.00,58.00,58.99,61.00,61.95,63.00,64.00,64.20,65.05,65.25,66.05,66.00,65.15,66.35,66.20,66.50,67.15,67.00,67.20,67.70,67.00,67.30,67.25,67.29,67.40,67.57,67.80,68.00,68.55]
# cosine  = [57.00,57.50,59.19,60.00,61.20,62.50,63.47,63.51,64.00,64.05,65.25,64.52,65.00,65.50,65.00,65.50,65.80,66.03,66.44,66.90,66.58,66.75,67.20,67.40,67.05,67.75,67.15,67.00,67.80]
# ST      = [57.00,57.40,58.20,60.00,61.30,61.52,62.50,63.06,64.25,64.02,64.75,64.95,65.30,66.45,65.05,65.70,65.35,65.81,66.75,67.35,66.25,67.00,66.50,67.25,66.35,67.00,66.85,67.40,67.59]
# none    = [57.00,57.35,58.15,59.85,61.05,61.50,62.35,63.00,63.70,64.02,64.50,64.40,64.70,65.20,65.15,65.30,65.80,65.70,65.85,65.90,66.10,66.30,66.80,66.30,66.40,66.80,67.00,67.20,67.50]
# iso     = [57.00,57.45,58.70,60.50,62.20,63.20,63.95,63.66,64.40,65.00,65.34,65.05,65.25,65.45,65.65,66.00,66.20,66.05,65.80,67.00,66.70,67.05,67.80,67.45,66.85,67.60,67.21,67.61,66.80]
# #===============================================================================
# '''
# MIT Movie Margin
# '''
# siamese = [57.00,58.00,60.00,60.50,62.60,63.00,64.10,64.30,65.45,65.80,66.75,65.75,66.70,66.20,66.80,67.50,68.20,68.15,68.30,68.10,67.75,68.50,67.50,68.35,68.20,68.60,68.12,68.85,69.15]
# cosine  = [57.00,57.80,58.80,60.30,61.50,63.30,64.20,64.10,65.25,65.55,66.50,65.85,66.50,66.10,66.70,66.85,67.20,67.35,67.30,68.05,66.50,67.55,67.15,68.00,67.80,68.45,68.05,68.55,67.81]
# ST      = [57.00,58.00,60.25,60.50,62.00,62.50,63.45,64.50,65.20,65.45,66.15,65.10,66.05,65.35,66.10,66.43,66.70,67.20,67.05,67.65,66.40,67.30,66.50,67.05,67.05,67.50,67.80,68.50,68.10]
# none    = [57.00,57.50,58.50,60.05,61.09,61.50,62.75,62.85,63.25,63.75,64.10,64.60,65.50,65.35,65.45,65.55,65.70,65.90,66.40,66.65,66.25,66.35,66.20,66.30,66.42,66.72,67.05,67.20,67.45]
# iso     = [57.00,58.00,59.86,60.00,61.26,63.00,63.80,64.45,65.60,66.20,66.75,66.00,66.44,66.01,66.70,67.55,67.05,67.20,67.19,67.25,67.50,68.35,68.03,68.15,68.10,68.00,68.20,67.74,67.80]

#===============================================================================
#===============================================================================
#===============================================================================

t = [2,4,6,8,10,12,14,16,18,20,22,24,26]
random  = [58.50,62.70,65.05,66.72,67.57,67.80,68.70,68.28,69.50,70.60,70.93,70.60,70.99]
base = [72.36]*len(t)
#===============================================================================
'''
GENIA BALD
'''
# outlier = [58.55,66.80,68.50,70.15,71.10,71.50,71.80,72.75,73.05,73.10,73.05,73.15,73.10]
# siamese = [58.55,66.63,69.17,70.07,71.00,71.35,71.96,72.56,72.82,73.15,72.74,72.86,73.15]
# iso     = [58.55,66.05,68.80,69.50,71.05,70.65,71.30,72.50,71.70,72.23,72.55,72.74,72.87]
# cosine  = [58.55,65.84,69.76,69.58,71.50,71.19,71.87,72.06,73.15,72.53,72.20,72.79,72.94]
# ST      = [58.55,65.12,68.52,70.20,70.53,70.50,71.65,72.00,72.47,71.58,72.95,72.76,73.11]
# none    = [58.55,63.81,66.19,68.15,68.78,69.50,71.15,70.75,70.25,71.56,70.78,71.55,72.71]
#===============================================================================
'''
GENIA Entropy
'''
# outlier = [58.55,65.15,68.00,70.10,70.20,70.50,71.10,71.66,72.05,72.10,72.15,72.28,72.35]
# siamese = [58.55,64.81,67.57,70.05,70.42,69.77,71.15,71.51,71.75,72.10,71.69,71.15,72.50]
# iso     = [58.55,64.32,68.00,69.00,69.50,69.57,70.80,70.50,69.90,70.90,70.84,71.35,71.80]
# cosine  = [58.55,65.15,68.00,70.00,69.78,70.14,70.20,71.25,70.50,71.70,71.30,71.10,72.00]
# ST      = [58.55,63.88,67.56,69.69,69.10,68.75,69.90,71.10,71.14,71.15,71.11,70.44,71.68]
# none    = [58.55,62.81,64.23,66.90,67.82,68.30,69.15,68.50,69.86,70.23,70.48,70.98,71.60]
#===============================================================================
'''
GENIA Margin
'''
# outlier = [58.55,64.80,68.10,69.19,69.32,69.99,70.10,70.74,71.15,71.65,71.57,71.50,71.55]
# siamese = [58.55,64.77,67.10,68.34,69.20,70.10,69.73,70.63,70.74,71.50,71.25,70.77,71.37]
# iso     = [58.55,64.15,67.00,67.75,68.00,69.50,68.80,69.90,70.05,70.87,70.58,70.63,71.34]
# cosine  = [58.55,63.23,66.77,68.30,69.22,69.74,69.32,70.54,69.80,70.59,70.90,71.05,71.23]
# ST      = [58.55,64.13,68.10,69.19,68.05,69.99,69.75,70.00,71.05,71.00,70.80,70.50,71.31]
# none    = [58.55,62.80,64.87,67.14,67.76,68.15,68.63,69.51,69.75,69.90,70.55,70.75,70.95]

###################################################################################################
'''
BILSTM BILSTM CRF
'''
###################################################################################################
############################################  BILSTM BILSTM CRF #############################################
# t = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
# random  = [48.47,56.00,57.50,62.00,63.10,62.75,63.67,64.50,65.30,66.00,66.15,66.48,66.80,67.00,67.80]
# base = [71.33]*len(t)
#===============================================================================
'''
MIT Movie BALD
'''
# siamese = [48.47,58.35,62.50,64.50,65.25,66.30,67.53,66.73,67.54,68.31,68.80,69.25,69.80,69.55,70.00]
# iso     = [48.47,58.20,61.18,63.90,64.50,65.56,67.13,67.50,68.31,67.10,67.43,67.79,67.90,69.10,69.02]
# cosine  = [48.57,58.00,60.00,62.99,64.83,65.50,67.14,67.04,67.66,68.20,68.50,68.00,67.91,69.00,68.92]
# ST      = [48.57,58.10,61.09,63.25,64.60,64.61,66.77,67.10,67.61,67.17,67.70,68.30,68.44,68.80,69.15]
# none    = [48.57,56.50,59.80,63.15,62.82,63.91,64.80,65.50,66.62,65.70,66.80,66.59,66.84,67.75,68.15]
#===============================================================================
'''
MIT Movie Entropy
'''
# siamese = [48.47,58.20,59.95,61.80,63.93,65.60,66.30,66.61,67.23,66.98,67.25,67.80,68.00,68.69,69.30]
# iso     = [48.47,57.50,59.80,61.50,62.51,64.50,65.17,66.00,67.20,66.73,67.00,66.10,66.95,66.80,67.46]
# cosine  = [48.47,58.30,60.43,63.00,64.12,63.80,64.56,66.34,67.09,67.50,66.80,66.63,67.27,68.00,68.70]
# ST      = [48.47,58.00,60.54,62.50,63.57,64.63,66.00,65.50,66.97,67.21,67.71,67.80,67.65,67.22,67.99]
# none    = [48.47,56.74,59.22,61.57,62.73,64.23,64.10,64.90,65.00,66.30,66.00,66.26,66.25,67.12,68.05]
#===============================================================================
'''
MIT Movie Margin
'''
# siamese = [48.47,59.20,63.67,62.82,65.06,64.13,66.34,66.50,67.54,68.01,67.80,67.58,68.20,68.51,69.03]
# iso     = [48.47,58.50,60.19,63.00,64.22,64.00,64.90,65.80,67.37,67.55,68.13,67.50,68.32,67.51,68.52]
# cosine  = [48.47,58.00,59.74,62.51,64.00,64.40,66.01,65.56,67.27,67.47,68.10,67.16,67.77,67.75,68.29]
# ST      = [48.47,59.00,61.85,62.00,63.32,64.20,66.37,65.83,67.56,67.16,67.69,67.30,67.77,67.80,68.65]
# none    = [48.47,55.80,59.25,62.70,63.33,62.90,64.20,64.85,65.85,65.88,66.45,66.65,66.30,67.16,67.71]

#===============================================================================
#===============================================================================
#===============================================================================

t = [4,6,8,10,12,14,16,18,20,22,24,26]
random  = [53.52,67.80,73.66,79.15,79.72,79.44,79.16,80.57,82.57,81.15,81.57,82.98]
base = [88.50]*len(t)
#===============================================================================
'''
CoNLL 2003 (NER) BALD BiLSTM
'''
siamese = [69.10,77.54,82.20,84.02,85.68,86.56,85.83,86.90,87.25,87.74,87.15,87.90]
iso     = [68.50,77.10,82.00,83.53,85.30,85.90,86.30,86.78,87.10,86.65,87.05,87.08]
cosine  = [67.08,77.38,80.84,83.72,84.70,86.00,86.19,87.01,86.33,86.77,86.68,87.00]
ST      = [66.80,76.80,81.00,82.90,83.56,85.20,86.20,85.95,86.10,86.25,86.80,86.90]
none    = [65.80,74.50,79.70,80.15,82.50,84.76,85.28,85.64,86.00,86.16,86.39,86.79]
#===============================================================================
'''
CoNLL 2003 (NER) Entropy BiLSTM
'''
# siamese = [68.75,77.41,80.85,82.50,83.51,83.81,84.60,84.75,85.05,85.28,85.51,85.84]
# iso     = [68.90,77.81,81.11,82.12,83.14,83.82,84.61,84.23,84.58,84.70,84.95,85.20]
# cosine  = [69.00,78.71,80.25,82.25,82.70,84.00,84.75,83.89,84.45,84.80,85.02,85.30]
# ST      = [70.00,80.00,81.63,82.26,83.03,83.74,83.93,84.20,84.80,84.32,84.89,85.12]
# none    = [68.00,73.92,77.56,81.77,82.31,83.51,83.82,83.65,84.45,84.12,84.67,85.05]
#===============================================================================
'''
CoNLL 2003 (NER) Margin BiLSTM
'''
# siamese = [69.35,74.58,80.05,82.65,83.85,83.67,84.45,85.20,85.08,86.15,85.60,86.08]
# iso     = [68.50,75.10,78.90,82.50,82.80,83.11,83.33,84.47,84.71,84.95,84.69,85.18]
# cosine  = [69.50,74.50,79.80,82.27,82.82,83.80,84.00,84.80,84.54,84.33,84.91,85.23]
# ST      = [66.80,75.00,77.95,81.53,83.80,83.34,84.54,84.94,85.00,84.73,85.20,85.15]
# none    = [66.50,71.18,74.80,77.87,80.36,80.53,81.73,82.55,83.41,84.00,84.43,85.00]

#===============================================================================
#===============================================================================
#===============================================================================

# t = [2,5,10,15,20,25,30,35,40,45,50]
# random  = [81.33,81.89,86.79,87.51,88.50,89.00,89.19,89.46,89.42,89.75,90.14]
# base = [90.87]*len(t)
#===============================================================================
'''
POS CoNLL BALD BiLSTM
'''
# siamese = [81.33,87.84,89.13,89.50,90.10,90.34,90.76,90.79,90.80,90.90,90.88]
# iso     = [81.39,86.87,88.58,89.00,89.14,89.74,90.18,90.20,90.22,90.50,90.48]
# cosine  = [81.46,86.70,88.34,88.86,89.74,89.90,90.23,90.17,90.25,90.50,90.63]
# ST      = [80.89,87.00,88.15,89.00,89.95,90.05,90.12,90.35,90.37,90.60,90.54]
# none    = [81.44,85.32,88.58,88.50,89.23,89.51,90.00,90.05,90.12,90.40,90.44]
#===============================================================================
'''
POS CoNLL Entropy BiLSTM
'''
# siamese = [81.33,86.30,87.40,87.74,88.90,89.50,90.00,90.10,90.25,90.27,90.35]
# iso     = [81.39,85.29,87.12,87.65,88.61,89.06,89.23,89.80,90.05,90.15,90.20]
# cosine  = [81.46,85.72,87.30,88.27,88.59,89.23,89.53,89.70,90.10,89.98,90.25]
# ST      = [80.89,86.06,86.83,88.76,88.50,89.11,89.25,89.70,89.85,90.15,90.17]
# none    = [81.44,85.85,87.29,87.57,88.56,89.07,89.27,89.57,89.87,90.00,90.10]
#===============================================================================
'''
POS CoNLL Margin BiLSTM
'''
# siamese = [81.33,85.58,87.59,87.72,88.83,89.45,89.50,90.44,90.42,90.55,90.58]
# iso     = [81.39,84.80,86.33,88.04,88.85,88.96,89.30,89.70,90.12,90.30,90.25]
# cosine  = [81.46,85.60,87.63,87.90,89.10,89.25,90.08,89.88,90.18,90.15,90.27]
# ST      = [80.89,85.71,87.10,88.00,88.31,89.40,89.34,89.90,89.80,90.10,90.15]
# none    = [81.44,84.00,86.60,88.00,88.50,89.38,89.31,89.25,89.87,89.99,90.10]


#===============================================================================
#===============================================================================
#===============================================================================

t = [2,4,6,8,10,12,14,16,18,20,22,24,26]
random  = [55.50,62.70,65.05,66.72,67.57,67.80,68.70,68.28,69.50,70.00,70.03,70.16,70.29]
base = [71.80]*len(t)
#===============================================================================
'''
GENIA BALD BiLSTM
'''
# siamese = [55.55,64.63,68.17,69.07,70.05,70.42,70.77,71.15,71.51,71.75,72.10,71.79,72.45]
# iso     = [55.55,63.05,67.80,69.10,69.65,70.65,70.30,71.10,71.30,71.23,71.55,71.34,71.97]
# cosine  = [55.55,64.84,68.00,68.58,69.50,70.19,70.70,71.06,71.15,71.53,71.65,71.29,72.14]
# ST      = [55.55,64.12,67.52,68.29,69.83,70.20,70.65,71.00,72.07,71.38,71.80,71.36,72.11]
# none    = [55.55,62.81,66.19,67.15,68.78,69.20,69.15,70.75,70.25,70.46,70.38,70.55,70.71]
#===============================================================================
'''
GENIA Entropy BiLSTM
'''
# siamese = [55.55,64.77,67.50,68.34,69.20,70.10,69.73,70.63,70.74,71.50,71.25,70.97,71.37]
# iso     = [55.55,64.32,68.00,69.00,68.50,69.57,69.50,70.15,69.90,70.60,70.84,70.80,70.80]
# cosine  = [55.55,65.15,67.30,68.00,68.78,69.14,69.20,70.25,70.30,70.70,71.03,71.10,70.50]
# ST      = [55.55,63.88,67.36,67.69,68.10,69.75,69.30,70.10,70.14,70.55,70.71,70.64,70.68]
# none    = [55.55,62.80,64.87,67.14,67.76,68.15,68.63,69.51,69.75,69.90,70.55,70.75,70.95]
#===============================================================================
'''
GENIA Margin BiLSTM
'''
siamese = [55.55,64.17,67.10,68.34,69.20,70.10,69.73,70.63,70.74,71.50,71.25,71.37,71.37]
iso     = [55.55,64.15,67.00,67.75,68.00,69.50,68.80,69.90,70.05,70.87,70.68,70.83,71.10]
cosine  = [55.55,63.23,66.77,68.30,69.22,69.74,69.32,70.54,69.80,70.59,70.90,71.05,71.03]
ST      = [55.55,63.13,67.10,68.19,68.05,68.99,69.55,70.00,70.55,71.00,70.80,70.90,70.95]
none    = [55.55,62.81,65.23,66.90,67.82,68.30,68.95,69.20,69.66,70.23,70.28,70.48,70.50
           
#===============================================================================
#===============================================================================
#===============================================================================
#
t = [2,6,9,12,15,18,21,24,27,30,33,36,39,42]
random  = [50.00,54.60,62.00,66.00,69.00,68.23,67.11,68.59,69.25,70.21,70.50,71.15,71.63,71.93]
base = [75.83]*len(t)
#===============================================================================
'''
semtr BALD BiLSTM
'''
# siamese = [50.00,67.40,69.00,70.65,72.50,73.38,74.25,74.05,74.18,74.81,75.15,75.50,75.65]
# iso     = [50.05,66.45,70.42,70.30,70.85,72.15,73.10,73.97,74.46,74.25,74.63,74.81,75.00]
# cosine  = [50.10,68.00,68.80,69.43,71.22,72.42,73.62,73.26,73.44,74.19,74.50,74.49,74.60]
# ST      = [50.07,66.20,69.80,70.64,71.50,71.25,73.00,74.10,74.17,74.20,74.37,74.61,74.20]
# none    = [50.00,62.50,66.10,67.20,69.27,70.64,72.20,72.56,72.70,73.15,72.90,73.55,74.00]
#===============================================================================
'''
semtr Entropy BiLSTM
'''
# siamese = [50.10,66.54,68.40,69.20,70.10,71.11,72.00,72.20,72.80,72.70,73.20,73.30,73.40,73.90,74.50]
# iso     = [50.00,64.88,67.21,68.70,69.57,70.00,71.50,71.31,72.50,72.90,73.05,73.04,73.10,73.45,74.00]
# cosine  = [50.05,65.00,67.11,67.20,70.50,70.23,71.25,70.96,70.55,71.54,71.91,72.00,72.05,72.15,72.71]
# ST      = [50.15,66.00,68.00,69.78,70.15,70.07,70.37,71.68,72.54,72.40,72.77,72.83,72.39,72.55,72.98]
# none    = [50.05,62.50,66.10,66.20,67.27,68.64,69.20,69.56,70.70,70.15,70.90,71.55,71.60,71.55,71.87]
#===============================================================================
'''
semtr Margin BiLSTM
'''
siamese = [50.10,65.00,67.81,68.40,70.06,70.25,72.04,72.18,72.45,72.90,73.76,73.55,73.94,74.04]
iso     = [50.07,65.65,68.50,69.27,69.80,70.50,71.80,72.30,72.70,72.55,73.18,73.34,73.55,73.67]
cosine  = [50.05,65.00,67.50,68.30,69.70,71.27,71.23,71.55,72.00,72.45,72.00,72.90,73.06,73.40]
ST      = [50.15,65.13,67.70,68.32,69.90,70.00,70.50,72.18,72.80,73.00,72.30,72.20,72.55,73.15]
none    = [50.05,63.50,65.10,66.20,67.27,69.64,69.20,69.56,71.10,71.15,71.20,71.55,71.60,71.55]

#===============================================================================
#===============================================================================
#===============================================================================
#
t = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34]
random  = [77.30,84.10,86.10,87.15,88.89,89.40,89.60,90.10,90.25,90.55,90.46,90.80,90.55,91.20,91.46,91.85,92.18]
base = [93.36]*len(t)
#===============================================================================
'''
chunking BALD BiLSTM
'''
# siamese = [77.50,84.00,87.50,90.00,90.80,91.40,91.85,92.10,92.25,92.24,92.88,93.00]
# iso     = [77.45,84.00,87.30,89.20,90.00,91.24,91.63,91.80,92.00,92.12,92.44,92.56]
# cosine  = [77.40,83.80,87.75,89.80,90.40,91.00,91.20,91.70,92.06,92.14,92.48,92.60]
# ST      = [77.55,83.90,87.53,89.50,90.31,90.80,91.34,91.64,92.14,92.10,92.30,92.22]
# none    = [77.43,83.38,86.80,88.30,89.04,89.74,90.34,90.80,91.22,91.30,91.70,92.00]
#===============================================================================
'''
chunking Entropy BiLSTM
'''
# siamese = [77.40,84.25,89.35,88.50,90.00,90.10,90.80,91.00,91.50,91.60,91.83,91.95,92.10,92.50,92.86]
# iso     = [77.45,84.00,87.02,87.75,89.63,90.00,90.90,90.90,91.30,91.28,91.65,91.95,91.85,91.90,92.00]
# cosine  = [77.42,84.15,86.90,88.10,89.88,89.80,90.50,91.00,91.11,91.48,91.35,91.94,92.09,92.18,92.30]
# ST      = [77.50,84.00,87.15,88.20,89.35,89.85,90.35,90.70,90.80,91.10,91.71,91.50,91.75,92.08,92.15]
# none    = [77.51,84.25,86.30,87.20,88.75,89.50,89.75,90.20,90.45,90.70,90.94,91.30,91.50,91.70,91.83]
#===============================================================================
'''
chunking Margin BiLSTM
'''
siamese = [77.50,84.50,86.39,88.20,89.57,90.00,90.66,90.52,90.80,91.50,91.40,91.54,91.75,91.87,92.00,92.20,92.50]
iso     = [77.30,84.35,86.28,88.05,89.05,89.05,89.91,90.00,90.50,91.00,91.00,91.30,91.56,91.60,91.85,92.08,91.70]
cosine  = [77.40,84.40,87.00,88.00,88.75,89.50,90.30,90.20,90.40,90.80,91.10,91.40,91.54,91.72,91.55,91.80,91.73]
ST      = [77.44,84.45,87.10,88.05,89.39,89.50,90.48,90.80,91.28,91.35,91.51,91.20,91.55,91.70,92.00,92.06,92.35]
none    = [77.35,84.35,86.65,88.00,88.75,89.30,89.71,90.35,90.52,91.05,91.10,91.20,91.48,91.70,92.00,92.20,92.25]


plt.rcParams['font.size'] = 25
plt.figure(figsize=(10,10))
#plt.plot(t, p, 'r--', t, r, 'b--', t, f1, 'g--', marker='o',linewidth=2, markersize=12)

import math
xint = range(min(t), math.ceil(max(t))+1,2)
plt.xticks(xint)
#yint = range(55, 92, 2)
#yint = range(55, 72, 2)
#yint = range(56, 74, 2)
#yint = range(48, 72, 2)
yint = range(52, 89, 2)
plt.yticks(yint)

#plt.ylim(58,91)

import matplotlib.patches as mpatches


# construct some data like what you have:
# Visualize the result
plt.plot(t,base,'g--',linewidth=3.0,label='100 % data')

plt.plot(t, siamese, 'sk-',linewidth=2.0, label='MA Siamese')
plt.plot(t, iso, '+c-.', label='Iso Siamese')
#plt.plot(t, cosine, 'ob')
plt.plot(t, cosine, 'xm--',label='Cosine')
plt.plot(t, ST, '*b-.',label='InferSent')

plt.plot(t, none,'.r:',label='None')
plt.plot(t, random, ',y-.', label='Random')

##plt.fill_between(t, f1_min, f1_max,color='darkslategrey', alpha=0.2)
#================================= outlier ========================================#
# plt.plot(t,base,'g--',linewidth=3.0,label='100 % data')
# plt.plot(t, outlier, 'or-.',linewidth=2.0, label='MA Siamese (with outlier filtering)')
# plt.plot(t, siamese, 'sk-',label='MA Siamese (without outlier filtering)')
#==================================================================================#

#green_patch = mpatches.Patch(color='g', label='100 % data')
#red_patch = mpatches.Patch(color='r', label='Siamese')
#black_patch = mpatches.Patch(color='k', label='Cosine')
#blue_patch = mpatches.Patch(color='b', label='SkipThoughts')
#magenta_patch = mpatches.Patch(color='m', label='None')

plt.legend()
#plt.legend(handles=[green_patch, red_patch,blue_patch,black_patch,magenta_patch])
plt.title('Dataset: CoNLL 2003 (NER), Model: BiLSTM_BiLSTM_CRF, ALS: BALD', fontsize=25)
plt.xlabel('Percentage of data')
plt.ylabel('F-score')
plt.savefig('Dataset: CoNLL 2003 (NER), Model: BiLSTM_BiLSTM_CRF, ALS: BALD.png')
#GENIA Corpus
#CoNLL 2003 (NER)
#MIT Movie
