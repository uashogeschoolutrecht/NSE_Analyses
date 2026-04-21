# Title:             NSE data cleaning
# Project start:     2026-04-21
# Last edited:       2026-04-21
# Author:            Anne Leemans in collaboration with claude-sonnet-4-5

import os
import numpy as np
import pandas as pd


path = r'C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\DM NSE'
main_file = 'NSEsignificantietabel.csv'
file_2026 = 'NSEsignificantietabel2026.csv'
file_2026_T1 = 'NSEsignificantietabel2026_T1.csv'
NSEsignificantietabel = pd.read_csv(os.path.join(path, main_file) , sep=";", decimal=",")
NSEsignificantietabel_2026 = pd.read_csv(os.path.join(path, file_2026) , sep=";", decimal=",")
NSEsignificantietabel_2026_T1 = pd.read_csv(os.path.join(path, file_2026_T1) , sep=";", decimal=",")

NSEsignificantietabel_new = pd.concat([NSEsignificantietabel, NSEsignificantietabel_2026, NSEsignificantietabel_2026_T1], ignore_index=True)

NSEsignificantietabel_new.to_csv(os.path.join(path, 'NSEsignificantietabel_new.csv'), sep=";", decimal=",", index=False)

