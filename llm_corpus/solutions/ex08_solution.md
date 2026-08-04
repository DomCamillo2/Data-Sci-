---
id: "ex08-solution"
title: "Assignment 8 Solution"
kind: "solution"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "assignment_08/datsci-ex08-solution.pdf"
pages: 102
---

# Assignment 8 Solution

> Extracted from `datsci-ex08-solution.pdf` for LLM use. All pages included.

<!-- page:1 source:datsci-ex08-solution.pdf -->

datsci-ex08-solution
July 9, 2026
1 Data Science for Linguists Summer 2026: Assignment 8
[1]: import re
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize'] = (18, 10)
/home/jdellert/.local/lib/python3.8/site-
packages/pandas/core/computation/expressions.py:20: UserWarning: Pandas requires
version '2.7.3' or newer of 'numexpr' (version '2.7.1' currently installed).
from pandas.core.computation.check import NUMEXPR_INSTALLED
1.1 Task 1: Loading and Exploring the Data
a) Unzip and load the corpus, performing the usual steps for tokenisation: process each line (=
paragraph), split it into sentences by the three sentence-final marks (!?.), then split each
sentence into tokens based on spaces, remove potential trailing punctuation (,.:) from each
token, and convert it into lowercase. Make sure to avoid (or delete) empty tokens. You should
end up with a list of about 5.9 million tokens.
[2]: tokens = list()
with open("cym-os-corpus.txt", "r", encoding="utf-8") as corpus_file:
for line in corpus_file:
sentences = re.split("[.!?] ", line.strip() + " ")
for sentence in sentences:
for token in re.split(" ", sentence):
token = token.replace(".","").replace(",","").replace(":","")
if token == None or token == "": continue
tokens.append(token.lower())
[3]: len(tokens)
[3]: 5923536
1

---

<!-- page:2 source:datsci-ex08-solution.pdf -->

b) Use a counter to perform a tally of all characters occurring in the text, and sort the charac-
ters by frequency (hint: the most frequent character is d, it should occur about 2.5 million
times). Compute the logarithms of character probabilities, and store them in a dictionary
log_char_prob.
[4]: from collections import Counter
char_counter = Counter()
for token in tokens:
char_counter.update(token)
[5]: char_counter.most_common()
[5]: [('d', 2527859),
('n', 2290728),
('y', 2145236),
('a', 2098655),
('i', 1962627),
('e', 1923056),
('r', 1474202),
('o', 1342576),
('h', 1335231),
('w', 1289612),
('l', 1135734),
('c', 892387),
('f', 742800),
('g', 729388),
('m', 728368),
('t', 632750),
('s', 590261),
('u', 536520),
('b', 463657),
("'", 425309),
('p', 212728),
('â', 42964),
('k', 36190),
('ô', 22893),
('-', 15674),
('v', 14760),
('j', 14397),
('ŵ', 9830),
('x', 5685),
('z', 5358),
('ê', 3197),
('á', 2729),
('q', 2618),
('ŷ', 1558),
('ï', 1556),
2

---

<!-- page:3 source:datsci-ex08-solution.pdf -->

('î', 1395),
('é', 675),
('û', 184),
('à', 144),
('ë', 121),
('ö', 69),
('í', 42),
('ü', 40),
('ñ', 16),
('æ', 12),
('ä', 8),
('ú', 7),
('ó', 6),
('è', 4),
('ÿ', 4),
('å', 4),
('ð', 3),
('ã', 2),
('ç', 2),
('ò', 1),
('ß', 1),
('ū', 1),
('ė', 1)]
[6]: num_chars = sum(char_counter.values())
num_chars
[6]: 25661835
[7]: log_char_prob = {char: np.log(count/num_chars) for char, count in char_counter.
,→items()}
[8]: log_char_prob
[8]: {'c': -3.3588602527000884,
'e': -2.5910892813642072,
'r': -2.856888042271529,
'd': -2.3176321692990287,
'o': -2.9504147121123867,
'i': -2.5707209867552807,
'a': -2.503708205365276,
't': -3.702684748268587,
'h': -2.9559005581202107,
'g': -3.5605543213328303,
'n': -2.4161351977361516,
'k': -6.56397731011817,
's': -3.7721953357307356,
3

---

<!-- page:4 source:datsci-ex08-solution.pdf -->

'v': -7.4608393285214945,
'y': -2.4817552990738,
'l': -3.117725730760847,
'p': -4.792745793342869,
'u': -3.867656307659931,
'f': -3.54233331821527,
'w': -2.9906634707738315,
'm': -3.5619537327109483,
"'": -4.099944184125099,
'b': -4.0136150929663845,
'â': -6.39239759195802,
'-': -7.400756859063148,
'ô': -7.021928960718214,
'j': -7.4857402961496025,
'ï': -9.71064172193762,
'ê': -8.990547277616116,
'ŵ': -7.867321213534745,
'z': -8.474169376571403,
'á': -9.148824905967619,
'x': -8.414929020491321,
'û': -11.845579669066971,
'î': -9.819865732420492,
'ŷ': -9.709357200245265,
'q': -9.190349480206113,
'é': -10.545802735803427,
'à': -12.090702127099958,
'ë': -12.264724881079216,
'ö': -12.826408922078699,
'í': -13.32284580839259,
'ü': -13.371635972562022,
'è': -15.674221065556067,
'æ': -14.575608776887957,
'ÿ': -15.674221065556067,
'ð': -15.961903138007848,
'å': -15.674221065556067,
'ó': -15.268755957447903,
'ò': -17.06051542667596,
'ñ': -14.287926704436176,
'ã': -16.367368246116012,
'ß': -17.06051542667596,
'ç': -16.367368246116012,
'ä': -14.981073884996121,
'ū': -17.06051542667596,
'ė': -17.06051542667596,
'ú': -15.114605277620644}
c) Create a token counter, and extract the 20 most common tokens with their counts. (Hint:
4

---

<!-- page:5 source:datsci-ex08-solution.pdf -->

the most common token is yn, it occurs around 283000 times)
[9]: token_counter = Counter()
for token in tokens:
token_counter.update((token,))
[10]: token_counter.most_common(20)
[10]: [('yn', 283201),
('i', 199050),
('y', 154599),
('chi', 94304),
('o', 81807),
('ei', 78366),
('mae', 74220),
('ni', 65825),
('ar', 60664),
('wedi', 59915),
('a', 59090),
("chi'n", 54718),
('beth', 53328),
('eich', 50240),
('fy', 47604),
('nid', 47570),
("mae'n", 45905),
('bod', 43126),
('ond', 39837),
('yr', 38487)]
1.2 Task 2: Identifying Vowels and Consonants
When taking a first look at the data, you might have wondered how words which apparently consist
only of consonant characters (such as yw, ydyw, fyddwn, cychwyn, synnwyr) can be articulated. We
quickly arrive at the suspicion that some symbols that represent consonants in English actually
serve as vowels in Welsh orthography. Clustering symbols by the environments in which they occur
can provide us with hints.
a) We build a dictionary in which we store for every character the environments in which it is
attested. Environments are of shape A_B where A and B are the preceding and following
character. In order to represent positions at the start and end of words, we pad each token
by the sentinel symbol # on both sides. For instance, the token ydyw contains attestations
of the environments "#_d" and "d_w" for "y", "y_y" for "d", and "y_#"" for "w".
[11]: envs_per_char = dict()
for char in char_counter.keys():
envs_per_char[char] = set()
5

---

<!-- page:6 source:datsci-ex08-solution.pdf -->

[12]: for token in tokens:
padded_token = "#" + token + "#"
for i in range(1, len(padded_token) - 1):
envs_per_char[padded_token[i]].add(padded_token[i-1] + "_" +␣
,→padded_token[i+1])
[13]: envs_per_char["w"]
[13]: {'#_#',
"#_'",
'#_-',
'#_a',
'#_c',
'#_d',
'#_e',
'#_f',
'#_g',
'#_h',
'#_i',
'#_l',
'#_n',
'#_o',
'#_p',
'#_r',
'#_s',
'#_t',
'#_u',
'#_v',
'#_y',
'#_â',
'#_ê',
'#_î',
'#_ŷ',
"'_#",
"'_-",
"'_e",
"'_h",
"'_n",
"'_o",
"'_r",
"'_y",
'-_a',
'-_e',
'-_h',
'-_i',
'-_l',
'-_n',
6

---

<!-- page:7 source:datsci-ex08-solution.pdf -->

'-_o',
'-_r',
'-_u',
'-_y',
'a_#',
"a_'",
'a_-',
'a_a',
'a_b',
'a_c',
'a_d',
'a_e',
'a_f',
'a_g',
'a_h',
'a_i',
'a_k',
'a_l',
'a_m',
'a_n',
'a_o',
'a_p',
'a_r',
'a_s',
'a_t',
'a_u',
'a_w',
'a_y',
'a_ê',
'b_a',
'b_c',
'b_d',
'b_e',
'b_f',
'b_g',
'b_i',
'b_l',
'b_m',
'b_n',
'b_o',
'b_r',
'b_s',
'b_t',
'b_y',
'b_â',
'c_#',
'c_a',
7

---

<!-- page:8 source:datsci-ex08-solution.pdf -->

'c_b',
'c_c',
'c_d',
'c_e',
'c_f',
'c_i',
'c_l',
'c_m',
'c_n',
'c_o',
'c_p',
'c_r',
'c_s',
'c_t',
'c_y',
'd_#',
"d_'",
'd_a',
'd_b',
'd_c',
'd_d',
'd_e',
'd_f',
'd_i',
'd_l',
'd_m',
'd_n',
'd_o',
'd_p',
'd_r',
'd_s',
'd_t',
'd_y',
'e_#',
"e_'",
'e_-',
'e_a',
'e_b',
'e_c',
'e_d',
'e_e',
'e_f',
'e_g',
'e_h',
'e_i',
'e_l',
'e_m',
8

---

<!-- page:9 source:datsci-ex08-solution.pdf -->

'e_n',
'e_o',
'e_p',
'e_r',
'e_s',
'e_t',
'e_w',
'e_y',
'f_a',
'f_c',
'f_d',
'f_e',
'f_f',
'f_g',
'f_i',
'f_l',
'f_m',
'f_n',
'f_r',
'f_s',
'f_t',
'f_y',
'f_â',
'g_#',
'g_a',
'g_b',
'g_c',
'g_d',
'g_e',
'g_f',
'g_g',
'g_h',
'g_i',
'g_l',
'g_m',
'g_n',
'g_o',
'g_p',
'g_r',
'g_s',
'g_t',
'g_y',
'g_â',
'g_ê',
'g_ŷ',
'h_#',
"h_'",
9

---

<!-- page:10 source:datsci-ex08-solution.pdf -->

'h_-',
'h_a',
'h_b',
'h_c',
'h_d',
'h_e',
'h_f',
'h_h',
'h_i',
'h_l',
'h_m',
'h_n',
'h_o',
'h_p',
'h_r',
'h_s',
'h_t',
'h_y',
'i_#',
"i_'",
'i_a',
'i_b',
'i_c',
'i_d',
'i_e',
'i_g',
'i_i',
'i_l',
'i_m',
'i_n',
'i_o',
'i_r',
'i_s',
'i_t',
'i_u',
'i_w',
'i_y',
'i_î',
'j_d',
'j_g',
'j_r',
'k_a',
'k_e',
'k_i',
'k_o',
'l_#',
"l_'",
10

---

<!-- page:11 source:datsci-ex08-solution.pdf -->

'l_a',
'l_b',
'l_c',
'l_e',
'l_f',
'l_g',
'l_h',
'l_i',
'l_l',
'l_m',
'l_n',
'l_o',
'l_r',
'l_s',
'l_t',
'l_w',
'l_y',
'l_é',
'm_a',
'm_c',
'm_d',
'm_e',
'm_f',
'm_g',
'm_i',
'm_l',
'm_m',
'm_n',
'm_o',
'm_r',
'm_s',
'm_t',
'm_y',
'n_#',
"n_'",
'n_a',
'n_c',
'n_d',
'n_e',
'n_i',
'n_l',
'n_m',
'n_n',
'n_o',
'n_r',
'n_s',
'n_w',
11

---

<!-- page:12 source:datsci-ex08-solution.pdf -->

'n_y',
'o_#',
"o_'",
'o_-',
'o_a',
'o_b',
'o_c',
'o_d',
'o_e',
'o_f',
'o_g',
'o_i',
'o_j',
'o_k',
'o_l',
'o_m',
'o_n',
'o_o',
'o_r',
'o_s',
'o_t',
'o_u',
'o_w',
'o_y',
'o_z',
'p_a',
'p_c',
'p_d',
'p_e',
'p_f',
'p_i',
'p_l',
'p_m',
'p_n',
'p_o',
'p_r',
'p_s',
'p_t',
'p_y',
'r_#',
"r_'",
'r_-',
'r_a',
'r_b',
'r_c',
'r_d',
'r_e',
12

---

<!-- page:13 source:datsci-ex08-solution.pdf -->

'r_f',
'r_g',
'r_i',
'r_m',
'r_n',
'r_o',
'r_p',
'r_r',
'r_s',
'r_t',
'r_y',
's_#',
's_a',
's_c',
's_e',
's_i',
's_l',
's_m',
's_n',
's_o',
's_p',
's_r',
's_s',
's_y',
's_â',
's_ê',
's_î',
't_#',
't_a',
't_b',
't_c',
't_e',
't_f',
't_h',
't_i',
't_l',
't_m',
't_n',
't_o',
't_p',
't_r',
't_s',
't_t',
't_y',
'u_#',
"u_'",
'u_-',
13

---

<!-- page:14 source:datsci-ex08-solution.pdf -->

'u_a',
'u_c',
'u_d',
'u_i',
'u_n',
'u_o',
'u_r',
'u_y',
'w_#',
'w_c',
'w_e',
'w_m',
'w_n',
'w_o',
'w_r',
'w_y',
'x_e',
'x_s',
'y_#',
"y_'",
'y_-',
'y_a',
'y_b',
'y_c',
'y_d',
'y_e',
'y_f',
'y_g',
'y_h',
'y_i',
'y_j',
'y_l',
'y_n',
'y_o',
'y_r',
'y_s',
'y_u',
'y_w',
'y_y',
'z_e',
'z_i',
'ä_r',
'ë_c',
'ë_r',
'ë_y',
'í_t',
'ï_c',
14

---

<!-- page:15 source:datsci-ex08-solution.pdf -->

'ï_n',
'ï_r',
'ï_y',
'ö_r'}
b) Convert the stored attestations into a Pandas dataframe with characters in the rows and en-
vironments as columns, where each environment attested for the respective character receives
the value 1, and all other environments the value 0. (Hint: reshape the dictionary so that it
can be imported via pd.DataFrame.from_dict, set all missing entries to 0 after the import).
Reduce the dataframe to only those characters which are attested in at least 200 different
environments. (Hint: In my solution, the resulting dataframe has 23 rows and 1130 columns
of binary values).
[84]: env_attestations = {char: {env: 1 for env in envs_per_char[char]} for char in␣
,→envs_per_char}
env_attestations["w"]
[84]: {'h_m': 1,
'c_o': 1,
'o_d': 1,
'd_f': 1,
'r_-': 1,
'd_m': 1,
'r_g': 1,
'n_r': 1,
'#_g': 1,
"u_'": 1,
'e_a': 1,
'n_#': 1,
'i_n': 1,
'm_a': 1,
's_c': 1,
't_#': 1,
'p_i': 1,
's_s': 1,
'b_o': 1,
"'_r": 1,
'b_t': 1,
'a_b': 1,
'g_y': 1,
'i_b': 1,
'o_b': 1,
't_i': 1,
'e_p': 1,
's_ê': 1,
'c_a': 1,
'o_-': 1,
15

---

<!-- page:16 source:datsci-ex08-solution.pdf -->

'f_s': 1,
'u_y': 1,
't_y': 1,
'a_d': 1,
'p_n': 1,
'u_n': 1,
'o_l': 1,
'r_p': 1,
'g_â': 1,
'c_e': 1,
'h_-': 1,
'a_m': 1,
's_r': 1,
'a_f': 1,
'a_r': 1,
'#_s': 1,
'o_u': 1,
'j_r': 1,
'g_s': 1,
'#_#': 1,
'n_s': 1,
'e_b': 1,
'ï_c': 1,
't_r': 1,
'#_d': 1,
'i_e': 1,
's_o': 1,
'l_c': 1,
'g_e': 1,
'c_b': 1,
'h_i': 1,
's_y': 1,
'b_c': 1,
'm_d': 1,
'h_a': 1,
'c_f': 1,
'o_w': 1,
'y_e': 1,
'y_o': 1,
'o_s': 1,
'y_d': 1,
's_p': 1,
'r_s': 1,
'a_s': 1,
'a_y': 1,
'p_m': 1,
'f_r': 1,
16

---

<!-- page:17 source:datsci-ex08-solution.pdf -->

'b_g': 1,
'l_b': 1,
'm_c': 1,
'e_n': 1,
'y_a': 1,
'l_e': 1,
'g_g': 1,
'g_c': 1,
'm_s': 1,
'e_#': 1,
's_a': 1,
'p_y': 1,
'm_y': 1,
'l_w': 1,
'b_s': 1,
'y_i': 1,
"i_'": 1,
"e_'": 1,
'a_i': 1,
't_l': 1,
'm_l': 1,
'e_w': 1,
'f_c': 1,
'z_e': 1,
'-_e': 1,
'c_d': 1,
'o_f': 1,
't_b': 1,
'#_a': 1,
'l_o': 1,
'-_r': 1,
'e_y': 1,
'l_s': 1,
"y_'": 1,
't_p': 1,
'-_i': 1,
'p_f': 1,
'-_l': 1,
'a_a': 1,
"l_'": 1,
'u_r': 1,
"'_y": 1,
'd_c': 1,
'm_e': 1,
'k_i': 1,
'g_b': 1,
'n_m': 1,
17

---

<!-- page:18 source:datsci-ex08-solution.pdf -->

'g_o': 1,
'd_l': 1,
'#_l': 1,
'-_o': 1,
'#_y': 1,
'r_#': 1,
'f_g': 1,
'f_d': 1,
'k_e': 1,
'f_f': 1,
'b_a': 1,
'p_r': 1,
'#_r': 1,
"'_h": 1,
'x_s': 1,
'o_i': 1,
'f_i': 1,
'#_ê': 1,
'h_f': 1,
'y_c': 1,
'h_e': 1,
'b_â': 1,
'o_g': 1,
'l_m': 1,
'l_r': 1,
'c_l': 1,
'b_l': 1,
'e_f': 1,
'd_s': 1,
'h_d': 1,
'w_#': 1,
'm_f': 1,
'y_u': 1,
'd_y': 1,
'e_h': 1,
"#_'": 1,
'd_p': 1,
'a_l': 1,
'i_î': 1,
'k_o': 1,
'l_i': 1,
'f_y': 1,
'n_i': 1,
'ä_r': 1,
't_e': 1,
'g_ê': 1,
'o_z': 1,
18

---

<!-- page:19 source:datsci-ex08-solution.pdf -->

'l_l': 1,
'd_t': 1,
'í_t': 1,
'i_r': 1,
'ï_y': 1,
'a_t': 1,
't_c': 1,
'b_r': 1,
'n_a': 1,
'r_y': 1,
'l_a': 1,
'#_u': 1,
'g_i': 1,
'f_t': 1,
's_#': 1,
'f_â': 1,
'b_y': 1,
'i_m': 1,
'a_u': 1,
'a_o': 1,
'u_o': 1,
'#_e': 1,
'y_g': 1,
'r_m': 1,
'g_p': 1,
'a_ê': 1,
'h_b': 1,
'-_u': 1,
't_a': 1,
'i_#': 1,
'i_w': 1,
'm_g': 1,
'n_w': 1,
'i_i': 1,
'g_r': 1,
'#_c': 1,
'a_w': 1,
'i_g': 1,
'#_î': 1,
'h_c': 1,
'ë_y': 1,
'o_#': 1,
'u_d': 1,
'o_c': 1,
'i_l': 1,
'a_c': 1,
'i_a': 1,
19

---

<!-- page:20 source:datsci-ex08-solution.pdf -->

'ï_r': 1,
'm_t': 1,
'#_p': 1,
'g_a': 1,
'e_l': 1,
'ï_n': 1,
'n_e': 1,
'e_o': 1,
'r_i': 1,
'o_a': 1,
'n_d': 1,
'c_m': 1,
'h_n': 1,
"h_'": 1,
'w_o': 1,
'y_h': 1,
'#_i': 1,
'l_h': 1,
'g_#': 1,
'd_b': 1,
'r_t': 1,
'g_d': 1,
'h_l': 1,
'-_y': 1,
'p_o': 1,
'y_y': 1,
'w_n': 1,
'w_e': 1,
'#_n': 1,
'y_#': 1,
"'_#": 1,
'r_c': 1,
'r_r': 1,
'i_c': 1,
's_i': 1,
'r_e': 1,
'r_a': 1,
'w_r': 1,
'i_d': 1,
'a_e': 1,
'a_k': 1,
'e_r': 1,
"'_n": 1,
'n_l': 1,
'd_o': 1,
'-_a': 1,
'u_#': 1,
20

---

<!-- page:21 source:datsci-ex08-solution.pdf -->

'y_r': 1,
'p_d': 1,
'd_r': 1,
'g_m': 1,
'p_l': 1,
'd_d': 1,
'g_l': 1,
'f_n': 1,
'-_n': 1,
'n_y': 1,
'o_r': 1,
'r_f': 1,
't_m': 1,
'h_s': 1,
'd_n': 1,
"'_-": 1,
'g_n': 1,
'b_n': 1,
'r_d': 1,
'r_b': 1,
'j_g': 1,
'o_k': 1,
'j_d': 1,
'a_n': 1,
'c_t': 1,
'a_-': 1,
'm_i': 1,
"d_'": 1,
'y_j': 1,
'i_u': 1,
's_î': 1,
'ö_r': 1,
'o_n': 1,
'e_m': 1,
'n_c': 1,
'#_h': 1,
'i_o': 1,
'p_e': 1,
'a_g': 1,
"'_o": 1,
'#_f': 1,
'o_y': 1,
'y_b': 1,
'f_l': 1,
'u_-': 1,
'g_f': 1,
'o_e': 1,
21

---

<!-- page:22 source:datsci-ex08-solution.pdf -->

'h_t': 1,
'g_t': 1,
'l_g': 1,
'u_i': 1,
'm_r': 1,
"r_'": 1,
'l_n': 1,
'b_m': 1,
't_s': 1,
'a_p': 1,
'g_ŷ': 1,
's_â': 1,
'h_r': 1,
'n_o': 1,
'h_#': 1,
'c_#': 1,
's_m': 1,
'y_l': 1,
'l_f': 1,
'ë_r': 1,
't_f': 1,
'b_f': 1,
'p_a': 1,
'o_m': 1,
'p_t': 1,
'r_n': 1,
'p_c': 1,
'c_c': 1,
'x_e': 1,
'#_v': 1,
'w_c': 1,
'b_e': 1,
's_n': 1,
'#_t': 1,
'l_é': 1,
'm_m': 1,
'o_j': 1,
'g_h': 1,
'd_a': 1,
'u_a': 1,
'f_e': 1,
'y_n': 1,
'i_t': 1,
'c_r': 1,
'o_t': 1,
't_n': 1,
'c_y': 1,
22

---

<!-- page:23 source:datsci-ex08-solution.pdf -->

'w_m': 1,
'e_t': 1,
'h_o': 1,
'w_y': 1,
'-_h': 1,
'#_o': 1,
'#_â': 1,
"n_'": 1,
'p_s': 1,
'e_d': 1,
't_o': 1,
'c_p': 1,
'y_w': 1,
'y_s': 1,
'e_c': 1,
'e_e': 1,
'm_o': 1,
'c_n': 1,
'#_-': 1,
's_e': 1,
'd_i': 1,
'h_p': 1,
't_t': 1,
'y_-': 1,
'a_#': 1,
'k_a': 1,
'r_o': 1,
'ë_c': 1,
'h_h': 1,
'e_i': 1,
"a_'": 1,
'y_f': 1,
'#_ŷ': 1,
'e_-': 1,
'u_c': 1,
'e_g': 1,
'm_n': 1,
'a_h': 1,
'l_t': 1,
'c_i': 1,
'i_y': 1,
'h_y': 1,
'd_e': 1,
'b_d': 1,
'c_s': 1,
"o_'": 1,
'b_i': 1,
23

---

<!-- page:24 source:datsci-ex08-solution.pdf -->

'f_a': 1,
'e_s': 1,
'i_s': 1,
'z_i': 1,
's_l': 1,
't_h': 1,
'l_#': 1,
'o_o': 1,
'n_n': 1,
'f_m': 1,
"'_e": 1,
'd_#': 1,
'l_y': 1}
[15]: env_attested = pd.DataFrame.from_dict(env_attestations, orient="index")
env_attested[env_attested.isna()] = 0
env_attested = env_attested[env_attested.sum(axis=1) > 200]
[16]: env_attested
[16]: c_o o_d r_- n_r w_b e_a n_# i_n m_a s_c … #_ñ ï_ï í_ñ ç_á \
c 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
e 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
r 1.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
d 1.0 1.0 0.0 1.0 0.0 1.0 1.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
o 1.0 1.0 1.0 1.0 1.0 0.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
i 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
a 1.0 1.0 1.0 1.0 1.0 0.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
t 1.0 0.0 1.0 1.0 0.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
h 1.0 1.0 0.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 … 0.0 0.0 0.0 0.0
n 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
k 1.0 0.0 1.0 0.0 0.0 1.0 1.0 1.0 0.0 0.0 … 0.0 0.0 0.0 0.0
s 1.0 0.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
l 1.0 1.0 0.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
p 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 … 0.0 0.0 0.0 0.0
u 1.0 1.0 1.0 1.0 0.0 1.0 1.0 1.0 0.0 1.0 … 0.0 0.0 0.0 0.0
w 1.0 1.0 1.0 1.0 0.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
m 1.0 1.0 0.0 0.0 0.0 1.0 0.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
b 1.0 0.0 0.0 1.0 0.0 1.0 0.0 0.0 1.0 0.0 … 0.0 0.0 0.0 0.0
- 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
g 0.0 1.0 1.0 1.0 0.0 1.0 1.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
y 0.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 … 0.0 0.0 0.0 0.0
f 0.0 1.0 1.0 1.0 0.0 1.0 0.0 1.0 1.0 0.0 … 0.0 0.0 0.0 0.0
' 0.0 1.0 0.0 0.0 0.0 1.0 1.0 1.0 0.0 0.0 … 0.0 0.0 0.0 0.0
ð_ü å_ã ñ_ï ï_ç ß_ó u_á
c 0.0 0.0 0.0 0.0 0.0 0.0
24

---

<!-- page:25 source:datsci-ex08-solution.pdf -->

e 0.0 0.0 0.0 0.0 0.0 0.0
r 0.0 0.0 0.0 0.0 0.0 0.0
d 0.0 0.0 0.0 0.0 0.0 0.0
o 0.0 0.0 0.0 0.0 0.0 0.0
i 0.0 0.0 0.0 0.0 0.0 0.0
a 0.0 0.0 0.0 0.0 0.0 0.0
t 0.0 0.0 0.0 0.0 0.0 0.0
h 0.0 0.0 0.0 0.0 0.0 0.0
n 0.0 0.0 0.0 0.0 0.0 0.0
k 0.0 0.0 0.0 0.0 0.0 0.0
s 0.0 0.0 0.0 0.0 0.0 0.0
l 0.0 0.0 0.0 0.0 0.0 0.0
p 0.0 0.0 0.0 0.0 0.0 0.0
u 0.0 0.0 0.0 0.0 0.0 0.0
w 0.0 0.0 0.0 0.0 0.0 0.0
m 0.0 0.0 0.0 0.0 0.0 0.0
b 0.0 0.0 0.0 0.0 0.0 0.0
- 0.0 0.0 0.0 0.0 0.0 0.0
g 0.0 0.0 0.0 0.0 0.0 0.0
y 0.0 0.0 0.0 0.0 0.0 0.0
f 0.0 0.0 0.0 0.0 0.0 0.0
' 0.0 0.0 0.0 0.0 0.0 0.0
[23 rows x 1130 columns]
c) Use agglomerative clustering with the default parameters in order to infer a clustering of the
sounds based on the similarity of environments in which they occur. Use the code provided at
https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html
to create a dendogram in order to visualise the clustering. Do the symbols cluster differently
from what we would expect in English, and does it seem sensible to reclassify some symbols
as vowels?
[17]: from sklearn.cluster import AgglomerativeClustering
[18]: X = env_attested.to_numpy()
clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
clustering_result = clustering.fit(X)
[19]: from scipy.cluster.hierarchy import dendrogram
[20]: def plot_dendrogram(model, **kwargs):
# Create linkage matrix and then plot the dendrogram
# create the counts of samples under each node
counts = np.zeros(model.children_.shape[0])
n_samples = len(model.labels_)
for i, merge in enumerate(model.children_):
25

---

<!-- page:26 source:datsci-ex08-solution.pdf -->

current_count = 0
for child_idx in merge:
if child_idx < n_samples:
current_count += 1 # leaf node
else:
current_count += counts[child_idx - n_samples]
counts[i] = current_count
linkage_matrix = np.column_stack(
[model.children_, model.distances_, counts]
).astype(float)
# Plot the corresponding dendrogram
dendrogram(linkage_matrix, **kwargs)
[21]: plt.title("Hierarchical Clustering Dendrogram")
# plot the top three levels of the dendrogram
plot_dendrogram(clustering_result, labels=env_attested.index, leaf_font_size=12)
#plt.rcParams["figure.figsize"] = (15,5)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
It is quite obvious that we have managed to separate the consonants and vowels here, and that the
symbols w and y pattern like vowels, giving us a much clearer perspective on the pronunciation, as
many of the apparent consonant clusters are in reality just quite ordinary CVC syllables.
26

---

<!-- page:27 source:datsci-ex08-solution.pdf -->

1.3 Task 3: Search for Potential Digraphs
After having established the vowel inventory, we take a closer look at the orthography and get
the impression that, some sequences of consonants might serve as digraphs (sequences of two or-
thographic symbols which together represent a single sound), as in English ( sh, th, wh etc.). In
particular, we suspect that combinations of consonant symbols with h and geminates such as ll
might serve as digraphs. Again, we will try to use clustering in order to see whether the digraphs
might fall out as a natural category from their distribution.
[22]: digraphs = []
a) We start with some intuitions about what might characterise digraphs and distinguish them
from consonant clusters. Two ideas seem especially promising and easy to implement: they
should be among the most frequent consonant bigrams, and they should not only appear
word-internally, but also at the start or end of words. In order to measure these two prop-
erties, create counters cons_bigram_counter and internal_bigram_counter to count the
occurrences of bigrams of the relevant shapes (two identical consonants or a consonant fol-
lowed by h) as well as the word-internal occurrences. For both counts, the bigrams in each
every attested word form are counted only once.
[23]: vowels = ["a", "e", "i", "o", "u", "w", "y", "-"]
[24]: cons_bigram_counter = Counter()
internal_bigram_counter = Counter()
for token in token_counter.keys():
for i in range(0, len(token) - 1):
bigram = token[i:i+2]
if bigram[0] in vowels or bigram[1] in vowels: continue
if bigram[0] == bigram[1] or bigram[1] == "h":
if i > 0 and i < len(token) - 2:
internal_bigram_counter.update((bigram,))
cons_bigram_counter.update((bigram,))
[25]: cons_bigram_count_sum = sum(cons_bigram_counter.values())
[26]: cons_bigram_prob_dict = dict()
b) Create a dataframe in which for 25 most common candidate digraphs, you store the digraph’s
log probability (suggested column name jointLogProb) and the ratio of occurrences which
were word-internal (suggested name internalRatio). Create a scatter plot in order to un-
derstand the structure of the data (drawing text labels onto the node will help you interpret
the results later). Good digraphs should be high in joint log probability and low in the word-
internal ratio, but without labeled data, we cannot determine directly how these two factors
should be weighted. We will attempt to use clustering in order to leverage the distribution
within this two-dimensional space.
[27]: for bigram, count in cons_bigram_counter.most_common(25):
joint_log_prob = np.log(count/cons_bigram_count_sum)
27

---

<!-- page:28 source:datsci-ex08-solution.pdf -->

internal_ratio = 0
if bigram in internal_bigram_counter:
internal_ratio = internal_bigram_counter[bigram] / count
features = dict()
features["jointLogProb"] = joint_log_prob
features["internalRatio"] = internal_ratio
cons_bigram_prob_dict[bigram] = features
[28]: digraphs = pd.DataFrame.from_dict(cons_bigram_prob_dict, orient="index")
digraphs
[28]: jointLogProb internalRatio
dd -1.338987 0.467167
ch -1.693273 0.340409
th -1.919365 0.621212
ll -2.347223 0.652563
ff -2.721159 0.637072
nn -3.087970 0.975625
gh -3.517791 0.922190
rh -3.632697 0.228448
sh -3.861785 0.399729
ph -3.914648 0.232857
nh -3.927589 0.655572
rr -4.231318 0.941176
ss -4.330164 0.683983
mh -4.420723 0.473934
tt -4.610657 0.830946
mm -5.272772 0.827778
pp -5.488995 0.944828
hh -5.509901 0.626761
gg -5.531255 0.913669
bb -5.553074 0.970588
dh -6.083702 0.975000
cc -6.109020 0.871795
lh -6.306845 0.953125
zz -6.422677 0.842105
kh -6.615581 0.510638
[29]: digraphs.jointLogProb = (digraphs.jointLogProb - np.min(digraphs.jointLogProb))/
,→(np.max(digraphs.jointLogProb) - np.min(digraphs.jointLogProb))
[30]: type(digraphs)
[30]: pandas.core.frame.DataFrame
[31]: sns.set()
28

---

<!-- page:29 source:datsci-ex08-solution.pdf -->

bigram_plot = sns.scatterplot(data=digraphs, x="internalRatio",␣
,→y="jointLogProb")
for line in range(0,digraphs.shape[0]):
bigram_plot.text(digraphs.internalRatio[line]+0.01, digraphs.
,→jointLogProb[line],
digraphs.index[line], horizontalalignment='left',
size='medium', color='black', weight='semibold')
c) Use k-means clustering in order to divide the space of candidate digraphs into clusters. Use
silhouette scores to compare clustering quality for different choices of the number of clusters
k. There is likely not going to be a clearly preferable number, so you should explore the two
best options, and see whether they lead to similar conclusions. Visualise the clustering results
using the hue attribute of Seaborn’s scatter plot function, and use the intuitions to determine
the most plausible cluster(s) based on their cluster means. Extract the digraphs contained
in the best cluster(s), and compare the results between your two choices of k. Compare your
conclusions to a list of Welsh digraphs that you can easily find online.
[32]: digraphs_X = digraphs[["internalRatio", "jointLogProb"]].to_numpy()
[33]: from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
[34]: km2 = KMeans(n_clusters = 2).fit(digraphs_X)
silhouette_score(digraphs_X, km2.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
29

---

<!-- page:30 source:datsci-ex08-solution.pdf -->

`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[34]: 0.46145390638784134
[35]: km3 = KMeans(n_clusters = 3).fit(digraphs_X)
silhouette_score(digraphs_X, km3.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[35]: 0.3862284877458852
[36]: km4 = KMeans(n_clusters = 4).fit(digraphs_X)
silhouette_score(digraphs_X, km4.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[36]: 0.4627009709706268
[37]: km5 = KMeans(n_clusters = 5).fit(digraphs_X)
silhouette_score(digraphs_X, km5.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[37]: 0.4896123667237665
[38]: km6 = KMeans(n_clusters = 6).fit(digraphs_X)
silhouette_score(digraphs_X, km6.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
30

---

<!-- page:31 source:datsci-ex08-solution.pdf -->

[38]: 0.4753440567399837
[39]: km7 = KMeans(n_clusters = 7).fit(digraphs_X)
silhouette_score(digraphs_X, km7.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[39]: 0.5042119817328351
[40]: km8 = KMeans(n_clusters = 8).fit(digraphs_X)
silhouette_score(digraphs_X, km8.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[40]: 0.45084584746643214
[41]: km9 = KMeans(n_clusters = 9).fit(digraphs_X)
silhouette_score(digraphs_X, km9.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[41]: 0.4779239508404169
[42]: km10 = KMeans(n_clusters = 10).fit(digraphs_X)
silhouette_score(digraphs_X, km10.labels_)
/home/jdellert/.local/lib/python3.8/site-
packages/sklearn/cluster/_kmeans.py:1416: FutureWarning: The default value of
`n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init`
explicitly to suppress the warning
super()._check_params_vs_input(X, default_n_init=10)
[42]: 0.4776126140277857
[43]: sns.scatterplot(digraphs, x="internalRatio", y="jointLogProb", hue=km2.
,→predict(digraphs_X))
31

---

<!-- page:32 source:datsci-ex08-solution.pdf -->

[43]: <Axes: xlabel='internalRatio', ylabel='jointLogProb'>
[44]: km2.cluster_centers_
[44]: array([[0.47089625, 0.68942886],
[0.85268044, 0.25978872]])
[45]: digraphs.iloc[km2.predict(digraphs_X) == 1]
[45]: jointLogProb internalRatio
nn 0.668539 0.975625
gh 0.587081 0.922190
rr 0.451856 0.941176
ss 0.433124 0.683983
tt 0.379966 0.830946
mm 0.254484 0.827778
pp 0.213506 0.944828
hh 0.209544 0.626761
gg 0.205497 0.913669
bb 0.201362 0.970588
dh 0.100800 0.975000
cc 0.096002 0.871795
lh 0.058510 0.953125
zz 0.036558 0.842105
kh 0.000000 0.510638
32

---

<!-- page:33 source:datsci-ex08-solution.pdf -->

[46]: sns.scatterplot(digraphs, x="internalRatio", y="jointLogProb", hue=km7.
,→predict(digraphs_X))
[46]: <Axes: xlabel='internalRatio', ylabel='jointLogProb'>
[47]: km7.cluster_centers_
[47]: array([[0.91236097, 0.14584002],
[0.33374202, 0.50375637],
[0.63694901, 0.81232933],
[0.72349996, 0.44083577],
[0.56869943, 0.10477208],
[0.40378791, 0.96642853],
[0.94633056, 0.56915909]])
[48]: digraphs.iloc[km7.predict(digraphs_X) == 2]
[48]: jointLogProb internalRatio
th 0.890009 0.621212
ll 0.808923 0.652563
ff 0.738056 0.637072
[49]: digraphs.iloc[km7.predict(digraphs_X) == 6]
[49]: jointLogProb internalRatio
nn 0.668539 0.975625
gh 0.587081 0.922190
33

---

<!-- page:34 source:datsci-ex08-solution.pdf -->

rr 0.451856 0.941176
The two clusters with the highest average bigram probability contain a total of five digraphs, all
of which are also on the lists of Welsh digraphs that we can find in online resources ( ch, dd, ff, ng,
ll, ph, rh, th). It seems that we have only missed ph, rh, and ng (which we did not consider as an
option).
1.4 Task 4: Open and Closed Word Classes
All languages have several closed word classes (e.g. prepositions and pronouns) and several open
word classes (e.g. nouns and verbs), and we can try to group the words of an unknown language into
similar categories based on the intuition that closed word classes typically contain shorter words of
high frequency, whereas open word classes mostly consist of longer words of lower frequency.
a) Use the data structures from Task 1 in order to fill a Pandas dataframe with the follow-
ing two measures for the 5,000 most frequent tokens: 1) log probability (logarithm of the
product of character probabilities, can be computed by summing over the values stored in
log_char_prob) and 2) log frequency (the logarithm of the count in your token counter).
Normalise both dimensions (substract mean and divide by standard deviation), and visualise
the data as a a scatterplot. Is there any obvious clustering structure?
[50]: token_to_vars = dict()
for token, count in token_counter.most_common(5000):
token_length = 0
for char in token:
#token_length += 1
token_length += log_char_prob[char]
token_to_vars[token] = {"prob": token_length, "logfreq": np.log(count)}
[51]: token_stats = pd.DataFrame.from_dict(token_to_vars, orient="index")
token_stats
[51]: prob logfreq
yn -4.897890 12.553912
i -2.570721 12.201311
y -2.481755 11.948590
chi -8.885482 11.454279
o -2.950415 11.312118
… … …
androvax -31.424255 4.174387
serf -12.762506 4.174387
brofion -21.300522 4.158883
ddianaf -18.171870 4.158883
barth -16.032797 4.158883
[5000 rows x 2 columns]
34

---

<!-- page:35 source:datsci-ex08-solution.pdf -->

[52]: token_stats_normalised = (token_stats - token_stats.mean()) / token_stats.std()
token_stats_normalised
[52]: prob logfreq
yn 2.098421 5.641043
i 2.434413 5.358104
y 2.447258 5.155311
chi 1.522700 4.758659
o 2.379594 4.644584
… … …
androvax -1.731406 -1.082983
serf 0.962942 -1.082983
brofion -0.269761 -1.095424
ddianaf 0.181948 -1.095424
barth 0.490784 -1.095424
[5000 rows x 2 columns]
[53]: sns.scatterplot(token_stats_normalised, x="prob", y="logfreq")
[53]: <Axes: xlabel='prob', ylabel='logfreq'>
b) Cluster the data using Gaussian mixture models. Again, work with the default settings
of all parameters, but vary the number of components between 1 and 10. Use the Akaike
Information Criterion in order to decide on a good number of clusters, and visualise the results
using hues in a repetition of the scatter plot.
35

---

<!-- page:36 source:datsci-ex08-solution.pdf -->

[54]: token_stats_X = token_stats_normalised.to_numpy()
[55]: from sklearn.mixture import GaussianMixture
[56]: gm1 = GaussianMixture(n_components=1, random_state=0).fit(token_stats_X)
gm1.aic(token_stats_X)
[56]: 27791.050314533582
[57]: gm2 = GaussianMixture(n_components=2, random_state=0).fit(token_stats_X)
gm2.aic(token_stats_X)
[57]: 25717.237893746216
[58]: gm3 = GaussianMixture(n_components=3, random_state=0).fit(token_stats_X)
gm3.aic(token_stats_X)
[58]: 25633.09153561036
[59]: gm4 = GaussianMixture(n_components=4, random_state=0).fit(token_stats_X)
gm4.aic(token_stats_X)
[59]: 24969.38457773316
[60]: gm5 = GaussianMixture(n_components=5, random_state=0).fit(token_stats_X)
gm5.aic(token_stats_X)
[60]: 24698.494316954166
[61]: gm6 = GaussianMixture(n_components=6, random_state=0).fit(token_stats_X)
gm6.aic(token_stats_X)
[61]: 24625.608789648853
[62]: gm7 = GaussianMixture(n_components=7, random_state=0).fit(token_stats_X)
gm7.aic(token_stats_X)
[62]: 24564.073014094287
[63]: gm8 = GaussianMixture(n_components=8, random_state=0).fit(token_stats_X)
gm8.aic(token_stats_X)
[63]: 24612.025851923776
[64]: gm9 = GaussianMixture(n_components=9, random_state=0).fit(token_stats_X)
gm9.aic(token_stats_X)
36

---

<!-- page:37 source:datsci-ex08-solution.pdf -->

[64]: 24580.918083711476
[65]: sns.scatterplot(token_stats_normalised, x="prob", y="logfreq", hue=gm8.
,→predict(token_stats_X))
[65]: <Axes: xlabel='prob', ylabel='logfreq'>
[66]: gm8.means_
[66]: array([[ 0.72837167, -0.42305171],
[-0.98428555, 0.21839824],
[ 0.67510899, 0.94008323],
[-0.50536061, -0.54098014],
[-1.87771614, -0.67752832],
[ 0.02265569, -0.92003005],
[ 0.13124724, 0.10260562],
[ 1.06181541, 2.29098695]])
c) How large are the different clusters? Extract a sample of 20 tokens from each cluster, format
them as one token per line, and feed them through Google translate (or similar) to get a
rough impression of what kinds of things the tokens from the different clusters mean. Pick
the cluster(s) with the highest density of closed word classes among the translations, and look
back at your scatter plot to see whether the cluster(s) sit(s) cover the region of space you
would have expected.
[67]: pd.Series(gm8.predict(token_stats_X)).value_counts()
37

---

<!-- page:38 source:datsci-ex08-solution.pdf -->

[67]: 5 1148
6 834
2 695
3 675
0 652
1 461
7 301
4 234
Name: count, dtype: int64
[68]: token_stats_normalised["cluster"] = gm8.predict(token_stats_X)
token_stats_normalised
[68]: prob logfreq cluster
yn 2.098421 5.641043 7
i 2.434413 5.358104 7
y 2.447258 5.155311 7
chi 1.522700 4.758659 7
o 2.379594 4.644584 7
… … … …
androvax -1.731406 -1.082983 5
serf 0.962942 -1.082983 5
brofion -0.269761 -1.095424 5
ddianaf 0.181948 -1.095424 5
barth 0.490784 -1.095424 5
[5000 rows x 3 columns]
[69]: for i in range(0,8):
print("Sample from class " + str(i) + ":")
for token in token_stats_normalised[token_stats_normalised.cluster == i].
,→sample(20).index:
print(token)
print()
Sample from class 0:
sioe
fydden
gynnes
fodoli
diffyg
glaw
nod
dref
sam
cell
drefn
38

---

<!-- page:39 source:datsci-ex08-solution.pdf -->

milwr
cyd
defnydd
swynol
raddfa
helm
plith
heh
mân
Sample from class 1:
torpidos
ymarferol
gofynnwch
dechreuwch
ddifrifol
dynoliaeth
gwreiddiol
dilyniant
seiliedig
gwyliwch
darlleniadau
swyddogaeth
systemau
bajorans
gwastraffu
problemau
amddiffyniad
gyffredin
amherthnasol
meddygol
Sample from class 2:
llawn
stopio
cloi
wn
eiliad
fam
ystod
borg
cyfrif
gwrdd
af
llongau
ymladd
chael
niwed
39

---

<!-- page:40 source:datsci-ex08-solution.pdf -->

ateb
mrs
clo
tynnu
ynte
Sample from class 3:
difetha
warchod
planhigion
chwiliwch
adwaith
delweddau
ddiflannu
cadarnhau
ganrifoedd
gyfarfod
allyrrydd
ffactor
tueddu
trwsio
goleuni
phosibl
ysbïwr
diffoddwch
ceisiodd
trwyddo
Sample from class 4:
argyhoeddedig
afresymegol
dinistrio'ch
nghyfrifoldeb
nodweddiadol
trefedigaeth
soffistigedig
llongyfarchiadau
ufuddhewch
gynorthwyydd
actifadu'r
rhywogaethau
absenoldeb
bwystfilod
gweithrediad
milltiroedd
strwythurol
amddiffynfeydd
cyfathrebwr
40

---

<!-- page:41 source:datsci-ex08-solution.pdf -->

amddiffynnol
Sample from class 5:
gyllell
methodd
gwendid
buan
dechnegol
gywilydd
theta
mordor
gludwr
wyliadwrus
gwas
diangen
tarddiad
chawsom
niwrnod
byrdwn
meddygaeth
cogydd
anfodlon
amod
Sample from class 6:
arnynt
datrys
gyda'ch
gwerthu
wirio
ymlacio
alpha
bennaf
cylched
rheoli'r
ynddynt
arogli
raglaw
ffyrdd
cwympo
ffôn
cymerodd
nadolig
drosto
wylio
Sample from class 7:
inni
41

---

<!-- page:42 source:datsci-ex08-solution.pdf -->

ydych
pam
iddo
digwydd
mam
roi
barod
yno
ai
dyma
a
le
ewch
hi'n
dyn
gallai
meddwl
bod
dwi'n
Translations and UPOS tags provided by Gemini, with number of words from closed word classes:
Sample from class 0: (3 from closed classes)
show NOUN
would be AUX
warm ADJ
exist VERB
lack NOUN
rain NOUN
goal NOUN
town NOUN
sam PROPN
cell NOUN
order NOUN
soldier NOUN
joint ADJ
use NOUN
charming ADJ
scale NOUN
helmet NOUN
among ADP
heh INTJ
fine ADJ
Sample from class 1: (0 from closed classes)
torpedoes NOUN
practical ADJ
ask VERB
42

---

<!-- page:43 source:datsci-ex08-solution.pdf -->

start VERB
serious ADJ
humanity NOUN
original ADJ
sequence NOUN
based VERB
watch VERB
readings NOUN
function NOUN
systems NOUN
bajorans PROPN
waste VERB
problems NOUN
protection NOUN
common ADJ
irrelevant ADJ
medical ADJ
Sample from class 2: (1 from closed classes)
full ADJ
stop VERB
lock VERB
i know VERB
second NOUN
mother NOUN
range NOUN
borg PROPN
count VERB
meet VERB
i will go VERB
ships NOUN
fight VERB
get VERB
harm NOUN
answer NOUN
mrs NOUN
lock VERB
pull VERB
right INTJ
Sample from class 3: (1 from closed classes)
destroy VERB
protect VERB
plants NOUN
search VERB
reaction NOUN
images NOUN
disappear VERB
confirm VERB
43

---

<!-- page:44 source:datsci-ex08-solution.pdf -->

centuries NOUN
meet VERB
emitter NOUN
factor NOUN
tend VERB
fix VERB
light NOUN
possible ADJ
spy NOUN
turn off VERB
tried VERB
through it ADP
Sample from class 4: (0 from closed classes)
convinced ADJ
irrational ADJ
destroy your VERB
my responsibility NOUN
typical ADJ
colony NOUN
sophisticated ADJ
congratulations NOUN
obey VERB
assistant NOUN
activate the VERB
species NOUN
absence NOUN
beasts NOUN
operation NOUN
miles NOUN
structural ADJ
defenses NOUN
communicator NOUN
defensive ADJ
Sample from class 5: (0 from closed classes)
knife NOUN
failed VERB
weakness NOUN
quick ADJ
technical ADJ
shame NOUN
theta PROPN
mordor PROPN
transporter NOUN
watchful ADJ
servant NOUN
unnecessary ADJ
origin NOUN
44

---

<!-- page:45 source:datsci-ex08-solution.pdf -->

we had VERB
day NOUN
thrust NOUN
medicine NOUN
chef NOUN
reluctant ADJ
condition NOUN
Sample from class 6: (0 from closed classes)
on them ADP
solve VERB
with your ADP
sell VERB
check VERB
relax VERB
alpha PROPN
mainly ADV
circuit NOUN
control the VERB
in them ADP
smell VERB
lieutenant NOUN
ways NOUN
fall VERB
phone NOUN
took VERB
christmas PROPN
for him ADP
watch VERB
Sample from class 7: (6 from closed classes)
to us ADP
you are VERB
why ADV
to him ADP
happen VERB
mother NOUN
give VERB
ready ADJ
there ADV
or CCONJ
here is ADV
and CCONJ
place NOUN
go VERB
it is VERB
man NOUN
could AUX
think VERB
45

---

<!-- page:46 source:datsci-ex08-solution.pdf -->

be VERB
i am VERB
Class 7 has the highest density of words from closed classes by a wide margin (arguably, it could
have been higher if we treat the copula as a separate category, but this is what we get for not doing
the tagging manually). As could have been expected, this Class 7 sits in the upper-right corner of
the distribution, i.e. short tokens (high probability) with high frequency.
1.5 Task 5: Detecting Paradigmatic Sets of Markers
As a final step for illustrating the various tasks which can be approached through clustering, we
will attempt to determine sets of co-occurring suﬀixes which might provide some information about
inflectional paradigms in a purely data-driven fashion.
a) Word forms that are in a paradigmatic relationship to each other can be expected to share a
longer chunk of symbols which we can tentatively treat as their common stem. We start by
indexing our most frequently occurring 5000 forms by their potential stems. Treat any prefix
that has at least length 4 as a stem candidate, and use a dictionary to store for each stem can-
didate the forms which could potentially feature that stem. For instance, my implementation
has the set {'meddyg', 'meddygol', 'meddygon', 'meddyliau', 'meddyliol'} stored
under 'meddy'.
[70]: candidate_stems_to_forms = dict()
for token, count in token_counter.most_common(5000):
for i in range(max(4,len(token)-4),len(token)):
candidate_stem = token[0:i]
if candidate_stem not in candidate_stems_to_forms:
candidate_stems_to_forms[candidate_stem] = set()
candidate_stems_to_forms[candidate_stem].add(token)
[71]: candidate_stems_to_forms
[71]: {"chi'": {"chi'ch", "chi'n", "chi'r"},
"mae'": {"mae'ch", "mae'n", "mae'r"},
"rwy'": {"rwy'n"},
'rydy': {'rydych', 'rydym', 'rydyn'},
'rydyc': {'rydych'},
'ydyc': {'ydych'},
'hynn': {'hynny', "hynny'n"},
'rhai': {'rhaid', 'rhain'},
'unrh': {'unrhyw'},
'unrhy': {'unrhyw'},
'wneu': {'wneud'},
'gwyb': {'gwybod'},
'gwybo': {'gwybod'},
'alla': {'allaf',
'allai',
"allai'r",
'allan',
46

---

<!-- page:47 source:datsci-ex08-solution.pdf -->

'allanfa',
'allanol',
'allant'},
'amse': {'amser', 'amserlen', 'amserol'},
'gwne': {'gwnes', 'gwneud', 'gwnewch'},
'gwneu': {'gwneud'},
'capt': {'capten'},
'capte': {'capten'},
'ymla': {'ymlacio', 'ymladd', 'ymladdwr', 'ymlaen'},
'ymlae': {'ymlaen'},
'medd': {'meddai', 'meddwl', 'meddyg', 'meddygol', 'meddygon'},
'meddw': {'meddwl'},
'efal': {'efallai'},
'efall': {'efallai'},
'efalla': {'efallai'},
'roed': {'roedd', 'roeddech', 'roeddem', 'roedden', 'roeddent', 'roeddwn'},
'fell': {'felly'},
'hynny': {"hynny'n"},
"hynny'": {"hynny'n"},
"nhw'": {"nhw'n", "nhw'r"},
'dewc': {'dewch'},
'meddy': {'meddyg', 'meddygol', 'meddygon', 'meddyliau', 'meddyliol'},
'ange': {'angel', 'angen'},
'llon': {'llong', 'llongau', 'llonydd'},
'wedi': {"wedi'ch", "wedi'i", "wedi'r", "wedi'u"},
"wedi'": {"wedi'ch", "wedi'i", "wedi'r", "wedi'u"},
'gwel': {'gwelaf',
'gwelais',
'gweld',
'gweledol',
'gwell',
'gwella',
"gwella'n",
'gwelodd',
'gwelsom',
'gwelwch',
'gwely'},
'cred': {'credaf', 'credu', "credu'r", 'credwch', 'credwn'},
'aral': {'arall'},
'ffor': {'ffordd', 'fforddio', 'ffortiwn'},
'fford': {'ffordd', 'fforddio'},
'bydd': {'bydda',
'byddaf',
'byddai',
"byddai'n",
"byddai'r",
'byddan',
47

---

<!-- page:48 source:datsci-ex08-solution.pdf -->

'byddant',
'byddech',
'byddem',
'bydden',
'byddent',
'byddin',
'byddwch',
'byddwn'},
'byddw': {'byddwch', 'byddwn'},
'peid': {'peidio', 'peidiwch', 'peidiwn'},
'peidi': {'peidio', 'peidiwch', 'peidiwn'},
'peidiw': {'peidiwch', 'peidiwn'},
'peidiwc': {'peidiwch'},
'dweu': {'dweud'},
'ychy': {'ychydig'},
'ychyd': {'ychydig'},
'ychydi': {'ychydig'},
'eisi': {'eisiau', "eisiau'r"},
'eisia': {'eisiau', "eisiau'r"},
'roedd': {'roeddech', 'roeddem', 'roedden', 'roeddent', 'roeddwn'},
'roeddw': {'roeddwn'},
'bydda': {'byddaf', 'byddai', "byddai'n", "byddai'r", 'byddan', 'byddant'},
'edry': {'edrych', 'edrychaf'},
'edryc': {'edrych', 'edrychaf', 'edrychwch'},
'hwnn': {'hwnna', 'hwnnw', "hwnnw'n"},
'genn': {'gennych', 'gennyf', 'gennym'},
'genny': {'gennych', 'gennyf', 'gennym'},
'gennyc': {'gennych'},
'byddwc': {'byddwch'},
'ddwe': {'ddweud'},
'ddweu': {'ddweud'},
'gade': {'gadewais', 'gadewch'},
'gadew': {'gadewais', 'gadewch'},
'gadewc': {'gadewch'},
'siar': {'siarad'},
'siara': {'siarad', 'siaradais', 'siaradodd', 'siaradwch'},
'rhyw': {'rhywbeth', 'rhywle', 'rhywsut', 'rhywun'},
'rhywb': {'rhywbeth'},
'rhywbe': {'rhywbeth'},
'rhywbet': {'rhywbeth'},
'diol': {'diolch'},
'diolc': {'diolch'},
'erio': {'erioed'},
'erioe': {'erioed'},
'wnaet': {'wnaeth', 'wnaethant', 'wnaethoch', 'wnaethom', 'wnaethon'},
'wnaeth': {'wnaethant', 'wnaethoch', 'wnaethom', 'wnaethon'},
'wnaetho': {'wnaethoch', 'wnaethom', 'wnaethon'},
48

---

<!-- page:49 source:datsci-ex08-solution.pdf -->

'wnaethoc': {'wnaethoch'},
'allw': {'allwch', 'allwedd', 'allweddi', 'allwn'},
'allwc': {'allwch'},
'doct': {'doctor'},
'docto': {'doctor'},
"dwi'": {"dwi'n"},
'gyfe': {'gyfer'},
'newy': {'newydd', 'newyn'},
'newyd': {'newydd', 'newyddion'},
'digw': {'digwydd'},
'digwy': {'digwydd'},
'digwyd': {'digwydd', 'digwyddiad', 'digwyddodd'},
'ffwr': {'ffwrdd'},
'ffwrd': {'ffwrdd'},
'gall': {'gallaf',
'gallai',
"gallai'r",
'gallant',
'gallech',
'gallem',
'gallen',
'gallent',
'gallu',
'galluog',
'gallwch',
'gallwn'},
'gallw': {'gallwch', 'gallwn'},
'hefy': {'hefyd'},
'cyfa': {'cyfaddef',
'cyfamser',
'cyfan',
'cyfarch',
'cyfarfod',
'cyfarfûm',
'cyfateb'},
'ddrw': {'ddrwg', 'ddrws'},
'gada': {'gadael', 'gadair', 'gadarn', 'gadawaf', 'gadawodd'},
'gadae': {'gadael'},
'galla': {'gallaf', 'gallai', "gallai'r", 'gallant'},
'help': {'helpa', 'helpodd', 'helpu', "helpu'r", 'helpwch'},
'ymdda': {'ymddangos'},
'ymddan': {'ymddangos'},
'ymddang': {'ymddangos'},
'ymddango': {'ymddangos', 'ymddangosiad', 'ymddangosodd'},
'gwelw': {'gwelwch'},
'gwelwc': {'gwelwch'},
'unio': {'union', 'uniondeb'},
49

---

<!-- page:50 source:datsci-ex08-solution.pdf -->

'llaw': {'llawen', 'llawer', 'llawlyfr', 'llawn', 'llawr'},
'llawe': {'llawen', 'llawenydd', 'llawer'},
'baro': {'barod'},
'edrych': {'edrychaf', 'edrychwch'},
'edrychw': {'edrychwch'},
'edrychwc': {'edrychwch'},
'ceis': {'ceisiais', 'ceisio', "ceisio'i", 'ceisiodd', 'ceisiwch'},
'ceisi': {'ceisiais',
'ceisio',
"ceisio'ch",
"ceisio'i",
'ceisiodd',
'ceisiwch'},
'bynn': {'bynnag'},
'bynna': {'bynnag'},
'symu': {'symud', 'symudiad', 'symudodd', 'symudol', 'symudwch'},
'honn': {'honni', 'honno', "honno'n"},
'wrth': {'wrtha',
'wrthdaro',
'wrthi',
'wrtho',
'wrthod',
'wrthych',
'wrthyf',
'wrthym',
'wrthyn',
'wrthynt'},
'wrthy': {'wrthych', 'wrthyf', 'wrthym', 'wrthyn', 'wrthynt'},
'gallwc': {'gallwch'},
'cymr': {'cymrawd', 'cymryd'},
'cymry': {'cymryd'},
'oher': {'oherwydd'},
'oherw': {'oherwydd'},
'oherwy': {'oherwydd'},
'oherwyd': {'oherwydd'},
'unwa': {'unwaith'},
'unwai': {'unwaith'},
'unwait': {'unwaith'},
'pope': {'popeth'},
'popet': {'popeth'},
'amda': {'amdanaf',
'amdani',
'amdano',
'amdanoch',
'amdanom',
'amdanon',
'amdanyn',
50

---

<!-- page:51 source:datsci-ex08-solution.pdf -->

'amdanynt'},
'amdan': {'amdanaf',
'amdani',
'amdano',
'amdanoch',
'amdanom',
'amdanon',
'amdanyn',
'amdanynt'},
'byddai': {"byddai'n", "byddai'r"},
"byddai'": {"byddai'n", "byddai'r"},
'llad': {'lladd', 'lladdodd', 'lladdwyd', 'lladron'},
'bywy': {'bywyd', 'bywydau'},
'deby': {'debycach', 'debyg', 'debygol'},
'gyda': {"gyda'ch", "gyda'i", "gyda'n", "gyda'r", "gyda'u", 'gydag'},
"gyda'": {"gyda'ch", "gyda'i", "gyda'n", "gyda'r", "gyda'u"},
'wrthyc': {'wrthych'},
'blan': {'blaned', 'blanedau', 'blant'},
'blane': {'blaned', 'blanedau'},
'wybo': {'wybod'},
'deal': {'deall', 'deallus'},
'gwei': {'gweiddi', 'gweill', 'gweision', 'gweithio'},
'gweit': {'gweithio', 'gweithred', 'gweithwyr'},
'gweith': {'gweithio',
"gweithio'n",
'gweithiodd',
'gweithred',
'gweithredu',
'gweithwyr'},
'gweithi': {'gweithio', "gweithio'n", 'gweithiodd'},
'rhow': {'rhowch'},
'rhowc': {'rhowch'},
'ddae': {'ddaear', 'ddaeth', 'ddaethom', 'ddaethon'},
'ddaea': {'ddaear'},
'goly': {'golygfa', 'golygu', "golygu'r"},
'golyg': {'golygfa', 'golygu', "golygu'r"},
'dywe': {'dywed',
'dywedaf',
'dywedais',
'dywedir',
'dywedodd',
'dywedon',
'dywedwch',
'dywedwyd'},
'dywed': {'dywedaf',
'dywedais',
'dywedir',
51

---

<!-- page:52 source:datsci-ex08-solution.pdf -->

'dywedodd',
'dywedon',
'dywedwch',
'dywedwyd'},
'dywedw': {'dywedwch', 'dywedwyd'},
'dywedwc': {'dywedwch'},
'newi': {'newid', 'newis'},
'rhywu': {'rhywun'},
'adae': {'adael'},
'gwirio': {"gwirio'r", 'gwirion', 'gwirionedd'},
'gwirion': {'gwirionedd'},
'gwirione': {'gwirionedd', 'gwirioneddol'},
'gwirioned': {'gwirionedd', 'gwirioneddol'},
'arho': {'arholiad', 'arholwr', 'arhosaf', 'arhosodd', 'arhoswch', 'arhoswn'},
'arhos': {'arhosaf', 'arhosodd', 'arhoswch', 'arhoswn'},
'arhosw': {'arhoswch', 'arhoswn'},
'arhoswc': {'arhoswch'},
'arna': {'arnaf'},
'dyma': {"dyma'ch", "dyma'r"},
"dyma'": {"dyma'ch", "dyma'r"},
'eith': {'eithaf', 'eithafol', 'eithrio'},
'eitha': {'eithaf', 'eithafol'},
'fydd': {'fydda',
'fyddaf',
'fyddai',
"fyddai'n",
"fyddai'r",
'fyddan',
'fyddant',
'fyddech',
'fyddem',
'fydden',
'fyddent',
'fyddin',
'fyddwch',
'fyddwn'},
'fydda': {'fyddaf', 'fyddai', "fyddai'n", "fyddai'r", 'fyddan', 'fyddant'},
'arno': {'arnoch', 'arnofio', 'arnom', 'arnon'},
'arnoc': {'arnoch'},
'cynt': {'cyntaf', 'cyntefig'},
'cynta': {'cyntaf'},
'dyna': {"dyna'ch", "dyna'n", "dyna'r"},
"dyna'": {"dyna'ch", "dyna'n", "dyna'r"},
'erby': {'erbyn'},
'gily': {'gilydd'},
'gilyd': {'gilydd'},
'gora': {'gorau'},
52

---

<!-- page:53 source:datsci-ex08-solution.pdf -->

'fedd': {'feddwl', 'feddyg', 'feddygol'},
'feddw': {'feddwl'},
'ddig': {'ddigon', 'ddigonol', 'ddigwydd'},
'ddigo': {'ddigon', 'ddigonol'},
'oedd': {'oeddech', 'oeddem', 'oedden', 'oeddent', 'oeddwn'},
'oedde': {'oeddech', 'oeddem', 'oedden', 'oeddent'},
'oeddec': {'oeddech'},
'wnae': {'wnaeth', 'wnaethom', 'wnaethon'},
'iddy': {'iddyn', 'iddynt'},
'dyno': {'dynodi', 'dynol'},
'gymr': {'gymrawd', 'gymryd'},
'gymry': {'gymryd'},
'spoc': {'spock'},
'gobei': {'gobeithio'},
'gobeit': {'gobeithio'},
'gobeith': {'gobeithio'},
'gobeithi': {'gobeithio'},
'syst': {'system', 'systemau'},
'syste': {'system', 'systemau'},
'ohon': {'ohoni',
'ohono',
'ohonoch',
'ohonof',
'ohonom',
'ohonyn',
'ohonynt'},
'ohono': {'ohonoch', 'ohonof', 'ohonom'},
'ohonoc': {'ohonoch'},
'rhed': {'rhedais', 'rhedeg', 'rhedfa', 'rhediad'},
'rhede': {'rhedeg'},
'ffri': {'ffrind', 'ffrio'},
'ffrin': {'ffrind', 'ffrindiau'},
'blae': {'blaen', 'blaenau'},
'peth': {'pethau', "pethau'n"},
'petha': {'pethau', "pethau'n"},
'bydde': {'byddech', 'byddem', 'bydden', 'byddent'},
'byddec': {'byddech'},
'ddigwyd': {'ddigwydd', 'ddigwyddiad', 'ddigwyddodd'},
'ddigwydd': {'ddigwyddiad', 'ddigwyddodd'},
'ddigwyddo': {'ddigwyddodd'},
'ddigwyddod': {'ddigwyddodd'},
'starf': {'starfleet'},
'starfl': {'starfleet'},
'starfle': {'starfleet'},
'starflee': {'starfleet'},
'fyddw': {'fyddwch', 'fyddwn'},
'rywb': {'rywbeth', 'rywbryd'},
53

---

<!-- page:54 source:datsci-ex08-solution.pdf -->

'rywbe': {'rywbeth'},
'rywbet': {'rywbeth'},
'fwrd': {'fwrdd'},
'dech': {'dechrau'},
'dechr': {'dechrau', "dechrau'r"},
'dechra': {'dechrau', "dechrau'r"},
'sefy': {'sefydlog', 'sefydlu', 'sefyll', 'sefyllfa'},
'sefyl': {'sefyll', 'sefyllfa'},
'syni': {'syniad', 'syniadau'},
'synia': {'syniad', 'syniadau'},
'erai': {'eraill'},
'erail': {'eraill'},
'gyfl': {'gyflawn', 'gyflawni', 'gyfle', 'gyflwr', 'gyflwyno', 'gyflym'},
'gyfly': {'gyflym', 'gyflymach', 'gyflymder'},
'gynt': {'gyntaf', 'gynted', 'gyntefig'},
'gynta': {'gyntaf'},
'huna': {'hunain', 'hunan'},
'hunai': {'hunain'},
'trwy': {"trwy'r", 'trwyddo', 'trwyn'},
"trwy'": {"trwy'r"},
'gyrr': {'gyrraedd', 'gyrru', 'gyrrwch', 'gyrrwr'},
'gyrra': {'gyrraedd'},
'gyrrae': {'gyrraedd'},
'gyrraed': {'gyrraedd'},
'roedde': {'roeddech', 'roeddem', 'roedden', 'roeddent'},
'roeddec': {'roeddech'},
'ymlad': {'ymladd', 'ymladdwr'},
'tard': {'tarddiad', 'tardis'},
'tardi': {'tardis'},
'dros': {'drosedd', 'drosoch', 'drosodd', 'drosof', 'drosto'},
'droso': {'drosoch', 'drosodd', 'drosof'},
'drosod': {'drosodd'},
'ysta': {'ystafell'},
'ystaf': {'ystafell'},
'ystafe': {'ystafell'},
'ystafel': {'ystafell'},
'olyg': {'olygfa', 'olygu'},
'gofo': {'gofod', 'gofodol'},
'hoff': {'hoffai', 'hoffech', 'hoffem', 'hoffi', "hoffi'r", 'hoffwn'},
'fydde': {'fyddech', 'fyddem', 'fydden', 'fyddent'},
'fyddec': {'fyddech'},
'cyfrifi': {'cyfrifiadur'},
'cyfrifia': {'cyfrifiadur'},
'cyfrifiad': {'cyfrifiadur', 'cyfrifiadurol', 'cyfrifiaduron'},
'cyfrifiadu': {'cyfrifiadur', 'cyfrifiadurol', 'cyfrifiaduron'},
'gwmp': {'gwmpas'},
'gwmpa': {'gwmpas'},
54

---

<!-- page:55 source:datsci-ex08-solution.pdf -->

'fyddwc': {'fyddwch'},
'hoffw': {'hoffwn'},
'is-ga': {'is-gapten'},
'is-gap': {'is-gapten'},
'is-gapt': {'is-gapten'},
'is-gapte': {'is-gapten'},
'coma': {'comander'},
'coman': {'comander'},
'comand': {'comander'},
'comande': {'comander'},
'gwai': {'gwaith'},
'gwait': {'gwaith'},
'adna': {'adnabod'},
'adnab': {'adnabod'},
'adnabo': {'adnabod'},
'cyrr': {'cyrraedd'},
'cyrra': {'cyrraedd'},
'cyrrae': {'cyrraedd'},
'cyrraed': {'cyrraedd'},
'lawe': {'lawer'},
'teim': {'teimlad', 'teimlo', "teimlo'n", "teimlo'r"},
'teiml': {'teimlad', 'teimladau', 'teimlo', "teimlo'n", "teimlo'r"},
'wnew': {'wnewch'},
'wnewc': {'wnewch'},
'gand': {'gandalf', 'ganddi', 'ganddo', "ganddo'r", 'ganddyn', 'ganddynt'},
'gandd': {'ganddi', 'ganddo', "ganddo'r", 'ganddyn', 'ganddynt'},
'oeddw': {'oeddwn'},
'eili': {'eiliad', 'eiliadau'},
'eilia': {'eiliad', 'eiliadau'},
'ysto': {'ystod', 'ystof'},
'gofy': {'gofyn', 'gofynion', 'gofynnaf'},
'diwr': {'diwrnod'},
'diwrn': {'diwrnod'},
'diwrno': {'diwrnod'},
'anfo': {'anfodlon',
'anfon',
'anfonaf',
'anfonais',
'anfonodd',
'anfonwch',
'anfonwyd'},
'clyw': {'clywais', 'clywch', 'clywed'},
'clywe': {'clywed'},
'wyne': {'wyneb', 'wynebau', 'wynebu', "wynebu'r"},
'achu': {'achub'},
'fent': {'fenter', 'fenthyg', 'fentro'},
'fente': {'fenter'},
55

---

<!-- page:56 source:datsci-ex08-solution.pdf -->

'cadly': {'cadlywydd'},
'cadlyw': {'cadlywydd'},
'cadlywy': {'cadlywydd'},
'cadlywyd': {'cadlywydd'},
'dioge': {'diogel', 'diogelwch'},
'diogel': {'diogelwch'},
'diogelw': {'diogelwch'},
'diogelwc': {'diogelwch'},
'ffedera': {'ffederasiwn'},
'ffederas': {'ffederasiwn'},
'ffederasi': {'ffederasiwn'},
'ffederasiw': {'ffederasiwn'},
'cynn': {'cynnal',
'cynnar',
'cynnes',
'cynnig',
'cynnwys',
'cynnydd',
'cynnyrch'},
'cynni': {'cynnig'},
'rhywf': {'rhywfaint'},
'rhywfa': {'rhywfaint'},
'rhywfai': {'rhywfaint'},
'rhywfain': {'rhywfaint'},
'coll': {'collais', 'colled', 'colli', "colli'ch", "colli'r", 'collodd'},
'nesa': {'nesaf'},
'ddio': {'ddiod', 'ddioddef', 'ddiogel', 'ddiolch'},
'ddiog': {'ddiogel'},
'ddioge': {'ddiogel', 'ddiogelwch'},
'ffrind': {'ffrindiau'},
'ffrindi': {'ffrindiau', "ffrindiau'n"},
'ffrindia': {'ffrindiau', "ffrindiau'n"},
'dali': {'daliodd', 'daliwch'},
'daliw': {'daliwch'},
'daliwc': {'daliwch'},
'anod': {'anodd', 'anoddach'},
'holl': {'holliday', 'hollol'},
'hollo': {'hollol'},
'mwya': {'mwyach', 'mwyaf', 'mwyafrif'},
'chwi': {'chwiliad', 'chwilio', 'chwith'},
'chwil': {'chwiliad', 'chwilio', "chwilio'r", 'chwiliwch'},
'chwili': {'chwiliad', 'chwilio', "chwilio'r", 'chwiliwch'},
'eiso': {'eisoes'},
'eisoe': {'eisoes'},
'gwnew': {'gwnewch'},
'gwnewc': {'gwnewch'},
'falc': {'falch'},
56

---

<!-- page:57 source:datsci-ex08-solution.pdf -->

'dyla': {'dylai', "dylai'r", 'dylanwad'},
'stop': {'stopio', 'stopiodd', 'stopiwch'},
'stopi': {'stopio', 'stopiodd', 'stopiwch'},
'stopiw': {'stopiwch'},
'stopiwc': {'stopiwch'},
'rhyf': {'rhyfedd', 'rhyfel', 'rhyfela', 'rhyfelwr'},
'rhyfe': {'rhyfedd',
'rhyfeddol',
'rhyfel',
'rhyfela',
'rhyfelwr',
'rhyfelwyr'},
'torr': {'torres', 'torri', "torri'r", 'torrodd', 'torrwch'},
'angh': {'angheuol', 'anghofio', 'anghyson', 'anghywir'},
'anghy': {'anghyson', 'anghytuno', 'anghywir'},
'anghyw': {'anghywir'},
'anghywi': {'anghywir'},
'digo': {'digon', 'digonol'},
'adre': {'adref'},
'dyweda': {'dywedaf', 'dywedais', 'dywedasoch'},
'dywedai': {'dywedais'},
'dinis': {'dinistr', 'dinistrio'},
'dinist': {'dinistr', 'dinistrio'},
'dinistr': {'dinistrio', "dinistrio'r", 'dinistriodd', 'dinistriwyd'},
'dinistri': {'dinistrio',
"dinistrio'ch",
"dinistrio'r",
'dinistriodd',
'dinistriwyd'},
'iddyn': {'iddynt'},
'annw': {'annwyl'},
'annwy': {'annwyl'},
'gwrand': {'gwrandewch', 'gwrando'},
'gwrande': {'gwrandewch'},
'gwrandew': {'gwrandewch'},
'gwrandewc': {'gwrandewch'},
'poen': {'poeni'},
'arfa': {'arfau'},
'gapt': {'gapten'},
'gapte': {'gapten'},
'fain': {'faint'},
'dywedo': {'dywedodd', 'dywedon'},
'dywedod': {'dywedodd'},
'sait': {'saith'},
'amdano': {'amdanoch', 'amdanom', 'amdanon'},
'amdanoc': {'amdanoch'},
'galle': {'gallech', 'gallem', 'gallen', 'gallent'},
57

---

<!-- page:58 source:datsci-ex08-solution.pdf -->

'ohony': {'ohonyn', 'ohonynt'},
'geis': {'geisiaf', 'geisio'},
'geisi': {'geisiaf', 'geisio'},
'swyd': {'swydd', 'swyddfa', 'swyddi', 'swyddog'},
'swydd': {'swyddfa', 'swyddi', 'swyddog', 'swyddogol'},
'swyddo': {'swyddog', 'swyddogion', 'swyddogol'},
'gwnaet': {'gwnaeth', 'gwnaethant', 'gwnaethoch', 'gwnaethom', 'gwnaethon'},
'gwnaeth': {'gwnaethant', 'gwnaethoch', 'gwnaethom', 'gwnaethon'},
'gwnaetho': {'gwnaethoch', 'gwnaethom', 'gwnaethon'},
'gwnaethoc': {'gwnaethoch'},
'amlw': {'amlwg'},
'munu': {'munud'},
'gorch': {'gorchudd', 'gorchymyn'},
'gorchy': {'gorchymyn'},
'gorchym': {'gorchymyn'},
'gorchymy': {'gorchymyn'},
'maen': {'maent'},
'rhyfed': {'rhyfedd', 'rhyfeddol'},
'alle': {'allech', 'allem', 'allen', 'allent'},
'allec': {'allech'},
'ddefny': {'ddefnydd', 'ddefnyddio', 'ddefnyddir'},
'ddefnyd': {'ddefnydd', 'ddefnyddio', 'ddefnyddiol', 'ddefnyddir'},
'ddefnydd': {'ddefnyddio', "ddefnyddio'r", 'ddefnyddiol', 'ddefnyddir'},
'ddefnyddi': {'ddefnyddio',
"ddefnyddio'ch",
"ddefnyddio'r",
'ddefnyddiol',
'ddefnyddir'},
'diwe': {'diwedd', 'diweddar', 'diwethaf'},
'diwed': {'diwedd', 'diweddar'},
'bosi': {'bosib', 'bosibl'},
'bosib': {'bosibl'},
'hawd': {'hawdd'},
'wydd': {'wyddoch', 'wyddonol'},
'wyddo': {'wyddoch', 'wyddonol', 'wyddonydd'},
'wyddoc': {'wyddoch'},
'arfe': {'arfer', 'arferai', 'arferiad', 'arferion', 'arferol'},
'estr': {'estron'},
'estro': {'estron'},
'gyfa': {'gyfaddef', 'gyfan', 'gyfarfod'},
'hann': {'hanner'},
'hanne': {'hanner'},
'leia': {'leiaf'},
'ddec': {'ddechrau'},
'ddech': {'ddechrau'},
'ddechr': {'ddechrau', "ddechrau'r"},
'ddechra': {'ddechrau', "ddechrau'r"},
58

---

<!-- page:59 source:datsci-ex08-solution.pdf -->

'cyma': {'cymaint', 'cymar'},
'cymai': {'cymaint'},
'cymain': {'cymaint'},
'klin': {'klingon', 'klingons'},
'kling': {'klingon', 'klingons'},
'klingo': {'klingon', 'klingons'},
'ymddi': {'ymddiried'},
'ymddir': {'ymddiried'},
'ymddiri': {'ymddiried'},
'ymddirie': {'ymddiried'},
'dang': {'dangos'},
'dango': {'dangos', 'dangoswch'},
'cofi': {'cofio', "cofio'r", 'cofiwch'},
'ymat': {'ymateb'},
'ymate': {'ymateb', 'ymatebwch'},
'ddarga': {'ddarganfod'},
'ddargan': {'ddarganfod'},
'ddarganf': {'ddarganfod'},
'ddarganfo': {'ddarganfod'},
'dale': {'dalek', 'daleks'},
'dalek': {'daleks'},
'defny': {'defnydd', 'defnyddio'},
'defnyd': {'defnydd', 'defnyddio', 'defnyddiol'},
'defnydd': {'defnyddio',
"defnyddio'r",
'defnyddiodd',
'defnyddiol',
'defnyddiwch'},
'defnyddi': {'defnyddio',
"defnyddio'ch",
"defnyddio'r",
'defnyddiodd',
'defnyddiol',
'defnyddiwch'},
'siaw': {'siawns'},
'siawn': {'siawns'},
'meth': {'methiant', 'methodd', 'methu'},
'dewi': {'dewis', 'dewisodd', 'dewiswch'},
'argl': {'arglwydd'},
'arglw': {'arglwydd', 'arglwyddi'},
'arglwy': {'arglwydd', 'arglwyddes', 'arglwyddi'},
'arglwyd': {'arglwydd', 'arglwyddes', 'arglwyddi'},
'chwa': {'chwaer', 'chwaith', 'chwalu', 'chwarae', 'chwarter'},
'chwar': {'chwarae',
"chwarae'n",
"chwarae'r",
'chwaraeon',
59

---

<!-- page:60 source:datsci-ex08-solution.pdf -->

'chwarter',
'chwarteri'},
'chwara': {'chwarae', "chwarae'n", "chwarae'r", 'chwaraeon'},
'beid': {'beidio'},
'beidi': {'beidio'},
'orsa': {'orsaf'},
'dychw': {'dychwelaf', 'dychwelyd'},
'dychwe': {'dychwelaf', 'dychwelwch', 'dychwelyd'},
'dychwel': {'dychwelaf', 'dychwelwch', 'dychwelyd'},
'dychwely': {'dychwelyd'},
'amddi': {'amddiffyn'},
'amddif': {'amddiffyn'},
'amddiff': {'amddiffyn'},
'amddiffy': {'amddiffyn', 'amddiffyniad', 'amddiffynnol'},
'ddea': {'ddeall', 'ddeallus'},
'ddeal': {'ddeall', 'ddeallus'},
'wnaetha': {'wnaethant'},
'wnaethan': {'wnaethant'},
'ganddy': {'ganddyn', 'ganddynt'},
'athr': {'athro'},
'uche': {'uchel', 'uchelder'},
'gwyc': {'gwych'},
'voya': {'voyager'},
'voyag': {'voyager'},
'voyage': {'voyager'},
'cyme': {'cymeraf',
'cymerais',
'cymeriad',
'cymerodd',
'cymerwch',
'cymerwyd'},
'cymer': {'cymeraf',
'cymerais',
'cymeriad',
'cymerodd',
'cymerwch',
'cymerwyd'},
'cymerw': {'cymerwch', 'cymerwyd'},
'cymerwc': {'cymerwch'},
'dyni': {'dynion'},
'dynio': {'dynion'},
'synwyryd': {'synwyryddion'},
'synwyrydd': {'synwyryddion'},
'synwyryddi': {'synwyryddion'},
'synwyryddio': {'synwyryddion'},
'marwol': {'marwolaeth'},
'marwola': {'marwolaeth'},
60

---

<!-- page:61 source:datsci-ex08-solution.pdf -->

'marwolae': {'marwolaeth', 'marwolaethau'},
'marwolaet': {'marwolaeth', 'marwolaethau'},
'ifan': {'ifanc'},
'fwya': {'fwyaf'},
'dydy': {'dydych', 'dydyn'},
'dydyc': {'dydych'},
'uffe': {'uffern'},
'uffer': {'uffern'},
'disg': {'disglair', 'disgwyl', 'disgyn'},
'disgw': {'disgwyl'},
'disgwy': {'disgwyl'},
'ymos': {'ymosod', 'ymosodol'},
'ymoso': {'ymosod', 'ymosodiad', 'ymosododd', 'ymosodol', 'ymosodwyd'},
'adrod': {'adrodd', 'adroddiad'},
'adrodd': {'adroddiad'},
'adroddi': {'adroddiad', 'adroddiadau'},
'adroddia': {'adroddiad', 'adroddiadau'},
'daet': {'daeth', 'daethant', 'daethoch', 'daethom', 'daethon'},
'sign': {'signal', 'signalau'},
'signa': {'signal', 'signalau'},
'bell': {'bellach', 'belled', 'bellter'},
'bella': {'bellach'},
'bellac': {'bellach'},
'bydy': {'bydysawd'},
'bydys': {'bydysawd'},
'bydysa': {'bydysawd'},
'bydysaw': {'bydysawd'},
'acho': {'achos', 'achosi', "achosi'r", 'achosion', 'achosodd'},
'rheo': {'rheol', 'rheolau', 'rheoli', "rheoli'r", 'rheolwr'},
'rheol': {'rheolaeth',
'rheolaidd',
'rheolau',
'rheoli',
"rheoli'r",
'rheolwr'},
'meis': {'meistr', 'meistres', 'meistri'},
'meist': {'meistr', 'meistres', 'meistri'},
'dylw': {'dylwn'},
'phoe': {'phoeni'},
'phoen': {'phoeni'},
'wybod': {'wybodaeth'},
'wyboda': {'wybodaeth'},
'wybodae': {'wybodaeth'},
'wybodaet': {'wybodaeth'},
'ysty': {'ystyfnig', 'ystyr', 'ystyried'},
'ystyr': {'ystyried', 'ystyriwch'},
'ystyri': {'ystyried', 'ystyriwch'},
61

---

<!-- page:62 source:datsci-ex08-solution.pdf -->

'ystyrie': {'ystyried'},
'system': {'systemau'},
'systema': {'systemau'},
'weit': {'weithiau', 'weithio', 'weithred'},
'weith': {'weithiau', 'weithio', 'weithiodd', 'weithred', 'weithredu'},
'weithi': {'weithiau', 'weithio', 'weithiodd'},
'waha': {'wahanol', 'wahardd'},
'wahan': {'wahanol'},
'wahano': {'wahanol'},
'taria': {'tarian', 'tariannau'},
'tarian': {'tariannau'},
'tariann': {'tariannau'},
'tarianna': {'tariannau'},
'pwyn': {'pwynt', 'pwyntio'},
'funu': {'funud', 'funudau'},
'ferc': {'ferch', 'ferched'},
'cadw': {"cadw'ch", "cadw'n", "cadw'r", 'cadwch'},
'cadwc': {'cadwch'},
'enni': {'ennill'},
'ennil': {'ennill'},
'cwrd': {'cwrdd'},
'cefa': {'cefais'},
'cefai': {'cefais'},
'feny': {'fenyw'},
'beth': {'bethau'},
'betha': {'bethau'},
'dian': {'dianc', 'diangen'},
'glyw': {'glywais', 'glywed', 'glywsoch'},
'glywe': {'glywed'},
'dyle': {'dylech', 'dyledus', 'dylem', 'dylen', 'dylent'},
'angho': {'anghofio'},
'anghof': {'anghofiais', 'anghofio', "anghofio'r", 'anghofiwch'},
'anghofi': {'anghofiais', 'anghofio', "anghofio'r", 'anghofiwch'},
'llwy': {'llwybr',
'llwybrau',
'llwyd',
'llwyddo',
'llwyr',
'llwyth',
'llwytho'},
'nege': {'neges'},
'vulc': {'vulcan', 'vulcans'},
'vulca': {'vulcan', 'vulcans'},
'rhyb': {'rhybudd'},
'rhybu': {'rhybudd', 'rhybuddio'},
'rhybud': {'rhybudd', 'rhybuddio'},
'doed': {'doedd', 'doedden', 'doeddwn'},
62

---

<!-- page:63 source:datsci-ex08-solution.pdf -->

'doedd': {'doedden', 'doeddwn'},
'doeddw': {'doeddwn'},
'cyfl': {'cyflawn',
'cyflawni',
'cyfle',
'cyflenwi',
'cyflogi',
'cyflwr',
'cyflwyno',
'cyflym',
'cyflymu'},
"chi'c": {"chi'ch"},
'mate': {'mater', 'materion'},
'ofal': {'ofalu', 'ofalus'},
'ofalu': {'ofalus'},
'croe': {'croen', 'croesawu', 'croesi', "croesi'r", 'croeso'},
'croes': {'croesawu', 'croesi', "croesi'r", 'croeso'},
'eist': {'eistedd'},
'eiste': {'eistedd'},
'eisted': {'eistedd', 'eisteddwch'},
'brob': {'broblem'},
'brobl': {'broblem', 'broblemau'},
'broble': {'broblem', 'broblemau'},
'rhag': {'rhaglen', 'rhagofal', 'rhagori', 'rhagorol', 'rhagweld'},
'rhagl': {'rhaglen', 'rhaglenni', 'rhaglennu'},
'rhagle': {'rhaglen', 'rhaglenni', 'rhaglennu'},
'hedd': {'heddiw', 'heddlu', 'heddwch'},
'heddi': {'heddiw'},
"fe'c": {"fe'ch"},
'brif': {'brifo'},
'tynn': {'tynnu', "tynnu'n", "tynnu'r", 'tynnwch'},
'sara': {'sarah'},
'heib': {'heibio', "heibio'r"},
'heibi': {'heibio', "heibio'r"},
'ddyl': {'ddylai',
'ddylech',
'ddyled',
'ddyledus',
'ddylem',
'ddylen',
'ddylid',
'ddylwn'},
'ddyle': {'ddylech', 'ddyled', 'ddyledus', 'ddylem', 'ddylen'},
'ddylec': {'ddylech'},
'chae': {'chael'},
'ymun': {'ymuno', 'ymunwch'},
'ddyn': {'ddynes', 'ddynion', 'ddynol'},
63

---

<!-- page:64 source:datsci-ex08-solution.pdf -->

'ddyno': {'ddynol'},
'bwys': {'bwysau', 'bwysig', 'bwystfil'},
'bwysi': {'bwysicach', 'bwysig'},
'sefyll': {'sefyllfa'},
'sefyllf': {'sefyllfa'},
'darl': {'darling', 'darllen'},
'darll': {'darllen'},
'darlle': {'darllen', 'darllenais', 'darlleniad', 'darllenwch'},
'ddew': {'ddewch', 'ddewis', 'ddewr', 'ddewrder'},
'ddewi': {'ddewis'},
'flynydd': {'flynyddoedd'},
'flynyddo': {'flynyddoedd'},
'flynyddoe': {'flynyddoedd'},
'flynyddoed': {'flynyddoedd'},
'dyfo': {'dyfodol'},
'dyfod': {'dyfodol'},
'dyfodo': {'dyfodol'},
'pica': {'picard'},
'picar': {'picard'},
'yndd': {'ynddo', 'ynddynt'},
'hapu': {'hapus', 'hapusach'},
'sere': {'seremoni', 'seren'},
'gweithr': {'gweithred', 'gweithredol', 'gweithredu'},
'gweithre': {'gweithred',
'gweithrediad',
'gweithredol',
'gweithredu',
"gweithredu'n"},
'gweithred': {'gweithrediad',
'gweithredoedd',
'gweithredol',
'gweithredu',
"gweithredu'n"},
'ment': {'menter', 'mentro'},
'mente': {'menter'},
'bwri': {'bwriad', 'bwriadu'},
'bwria': {'bwriad', 'bwriadu'},
'bwriad': {'bwriadu'},
'llong': {'llongau'},
'llonga': {'llongau'},
'wait': {'waith'},
'esguso': {'esgusodi', 'esgusodion', 'esgusodwch'},
'esgusod': {'esgusodi', 'esgusodion', 'esgusodwch'},
'esgusodw': {'esgusodwch'},
'esgusodwc': {'esgusodwch'},
'tuvo': {'tuvok'},
'fywy': {'fywyd', 'fywydau'},
64

---

<!-- page:65 source:datsci-ex08-solution.pdf -->

'peir': {'peiriant'},
'peiri': {'peiriant'},
'peiria': {'peiriannau', 'peirianneg', 'peiriant'},
'peirian': {'peiriannau', 'peirianneg', 'peiriannydd', 'peiriant'},
'gallec': {'gallech'},
'cafo': {'cafodd'},
'cafod': {'cafodd'},
'cych': {'cychod', 'cychwyn'},
'cychw': {'cychwyn'},
'cychwy': {'cychwyn', 'cychwynnol'},
'gynn': {'gynnal',
'gynnar',
'gynnau',
'gynnes',
'gynnig',
'gynnwys',
'gynnydd'},
'gynni': {'gynnig'},
'meddyg': {'meddygaeth', 'meddygol', 'meddygon'},
'meddygo': {'meddygol', 'meddygon'},
'hane': {'hanes'},
'goso': {'gosod', 'gosodwch'},
'dily': {'dilyn', 'dilynwch'},
'sylwed': {'sylwedd', 'sylweddol', 'sylweddoli'},
'sylwedd': {'sylweddol', 'sylweddoli'},
'sylweddo': {'sylweddol', 'sylweddolais', 'sylweddoli'},
'sylweddol': {'sylweddolais', 'sylweddoli'},
'rhoi': {"rhoi'r"},
"rhoi'": {"rhoi'r"},
'draw': {'draws', 'drawst', 'drawstio'},
'ensi': {'ensign'},
'ensig': {'ensign'},
'dysg': {'dysgais', 'dysgodd', 'dysgu'},
'ddinis': {'ddinistrio'},
'ddinist': {'ddinistrio'},
'ddinistr': {'ddinistrio', "ddinistrio'r"},
'ddinistri': {'ddinistrio', "ddinistrio'r"},
'boda': {'bodau'},
'cynna': {'cynnal', 'cynnar'},
'arwy': {'arwydd', 'arwyddo'},
'arwyd': {'arwydd', 'arwyddion', 'arwyddo'},
'fyddai': {"fyddai'n", "fyddai'r"},
"fyddai'": {"fyddai'n", "fyddai'r"},
'awgr': {'awgrym', 'awgrymaf', 'awgrymu'},
'awgry': {'awgrym', 'awgrymaf', 'awgrymu'},
'awgrym': {'awgrymaf', 'awgrymu'},
'cwes': {'cwestiwn'},
65

---

<!-- page:66 source:datsci-ex08-solution.pdf -->

'cwest': {'cwestiwn', 'cwestiynu'},
'cwesti': {'cwestiwn', 'cwestiynau', 'cwestiynu'},
'cwestiw': {'cwestiwn'},
'gwra': {'gwraig', 'gwrando'},
'gwran': {'gwrando'},
'ymosod': {'ymosodiad', 'ymosododd', 'ymosodol', 'ymosodwyd'},
'ymosodi': {'ymosodiad', 'ymosodiadau'},
'ymosodia': {'ymosodiad', 'ymosodiadau'},
'plan': {'planed', 'planedau', 'planedol', 'planet', 'plant'},
'stor': {'storfa', 'stori', 'storio', 'storm', 'stormydd'},
'gred': {'greddf', 'gredu'},
'hedf': {'hedfan'},
'hedfa': {'hedfan'},
'darga': {'darganfod'},
'dargan': {'darganfod'},
'darganf': {'darganfod'},
'darganfo': {'darganfod'},
'jami': {'jamie', 'jamio'},
'dylec': {'dylech'},
'gorf': {'gorff', 'gorffen', 'gorffwys', 'gorfod', 'gorfodi'},
'gorff': {'gorffen', 'gorfforol', 'gorffwys'},
'gorffe': {'gorffen', 'gorffennol'},
'arwa': {'arwain'},
'arwai': {'arwain'},
'cart': {'cartref'},
'cartr': {'cartref'},
'cartre': {'cartref'},
'cofiw': {'cofiwch'},
'cofiwc': {'cofiwch'},
'diwet': {'diwethaf'},
'diweth': {'diwethaf'},
'diwetha': {'diwethaf'},
'derb': {'derbyn'},
'derby': {'derbyn', 'derbyniad'},
'rheola': {'rheolaeth', 'rheolaidd', 'rheolau'},
'rheolae': {'rheolaeth', 'rheolaethau'},
'rheolaet': {'rheolaeth', 'rheolaethau'},
'ar-l': {'ar-lein'},
'ar-le': {'ar-lein'},
'ar-lei': {'ar-lein'},
'ydoe': {'ydoedd'},
'ydoed': {'ydoedd'},
'teimlo': {"teimlo'n", "teimlo'r"},
"teimlo'": {"teimlo'n", "teimlo'r"},
'ymen': {'ymennydd'},
'ymenn': {'ymennydd'},
'ymenny': {'ymennydd'},
66

---

<!-- page:67 source:datsci-ex08-solution.pdf -->

'ymennyd': {'ymennydd'},
'byddan': {'byddant'},
"roi'": {"roi'r"},
'chwart': {'chwarter', 'chwarteri'},
'chwarte': {'chwarter', 'chwarteri'},
'chwarter': {'chwarteri'},
'llei': {'lleiaf', 'lleidr', 'lleied', 'lleihau', 'lleill', 'lleisiau'},
'lleil': {'lleill'},
'gwae': {'gwaed',
'gwaedlyd',
'gwaedu',
'gwael',
'gwaelod',
'gwaeth',
'gwaethaf'},
'merc': {'merch', 'merched'},
'rhywl': {'rhywle'},
'gwrd': {'gwrdd'},
'clud': {'cludiant', 'cludo', 'cludwr', 'cludwyr'},
'sefw': {'sefwch'},
'sefwc': {'sefwch'},
'llyg': {'llygad', 'llygaid', 'llygod', 'llygoden'},
'llyga': {'llygad', 'llygaid'},
'llygai': {'llygaid'},
'ddidd': {'ddiddorol'},
'ddiddo': {'ddiddordeb', 'ddiddorol'},
'ddiddor': {'ddiddordeb', 'ddiddorol'},
'ddiddoro': {'ddiddorol'},
'harr': {'harris', 'harry'},
'adro': {'adrodd'},
'cytu': {'cytundeb', 'cytuno', 'cytunwyd'},
'cytun': {'cytundeb', 'cytuno', 'cytunwyd'},
'arda': {'ardal'},
'mwyac': {'mwyach'},
'gynte': {'gynted', 'gyntefig'},
'orbi': {'orbit'},
'rike': {'riker'},
'corf': {'corff'},
'ddywe': {'ddywedaf', 'ddywedais', 'ddywedoch', 'ddywedodd', 'ddywedwch'},
'ddywed': {'ddywedaf', 'ddywedais', 'ddywedoch', 'ddywedodd', 'ddywedwch'},
'ddywedo': {'ddywedoch', 'ddywedodd'},
'ddywedod': {'ddywedodd'},
'ddychw': {'ddychwelyd'},
'ddychwe': {'ddychwelyd'},
'ddychwel': {'ddychwelyd'},
'ddychwely': {'ddychwelyd'},
'bery': {'berygl', 'beryglus'},
67

---

<!-- page:68 source:datsci-ex08-solution.pdf -->

'beryg': {'berygl', 'beryglus'},
'berygl': {'beryglus'},
'beryglu': {'beryglus'},
'tybe': {'tybed'},
'gywi': {'gywilydd', 'gywir', 'gywiro'},
'teby': {'tebyg', 'tebygol'},
'reol': {'reolaeth', 'reolau', 'reoli', "reoli'r"},
'ofna': {'ofnadwy'},
'ofnad': {'ofnadwy'},
'ofnadw': {'ofnadwy'},
'swni': {'swnio', "swnio'n"},
'dywedas': {'dywedasoch'},
'dywedaso': {'dywedasoch'},
'dywedasoc': {'dywedasoch'},
'minn': {'minnau', "minnau'n"},
'minna': {'minnau', "minnau'n"},
'parh': {'parhaol', 'parhau', 'parhaus', 'parhewch'},
'parha': {'parhaol', 'parhau', 'parhaus'},
'rede': {'redeg'},
'hyno': {'hynod'},
'weithia': {'weithiau'},
'gwna': {'gwnaed', 'gwnaeth', 'gwnaf', 'gwnawn'},
'gwnae': {'gwnaed', 'gwnaeth', 'gwnaethom', 'gwnaethon'},
'uniongyr': {'uniongyrchol'},
'uniongyrc': {'uniongyrchol'},
'uniongyrch': {'uniongyrchol'},
'uniongyrcho': {'uniongyrchol'},
'hoffe': {'hoffech', 'hoffem'},
'hoffec': {'hoffech'},
'yfor': {'yfory'},
'ceisiw': {'ceisiwch'},
'ceisiwc': {'ceisiwch'},
'cynl': {'cynllun', 'cynllwyn'},
'cynll': {'cynllun', 'cynllunio', 'cynllwyn'},
'cynllu': {'cynllun', 'cynlluniau', 'cynllunio'},
'eglu': {'egluro'},
'eglur': {'egluro'},
'adei': {'adeilad', 'adeiladu'},
'adeil': {'adeilad', 'adeiladu'},
'adeila': {'adeilad', 'adeiladodd', 'adeiladu', "adeiladu'r"},
'adeilad': {'adeiladodd', 'adeiladu', "adeiladu'r"},
'pedw': {'pedwar'},
'pedwa': {'pedwar'},
'dymu': {'dymuniad', 'dymuno', 'dymunol', 'dymunwch'},
'dymun': {'dymuniad', 'dymuno', 'dymunol', 'dymunwch'},
'heddl': {'heddlu'},
'draff': {'drafferth'},
68

---

<!-- page:69 source:datsci-ex08-solution.pdf -->

'draffe': {'drafferth', 'drafferthu'},
'draffer': {'drafferth', 'drafferthu'},
'draffert': {'drafferth', 'drafferthu'},
'ddys': {'ddysgu'},
'ddysg': {'ddysgu'},
'aria': {'arian'},
'arbe': {'arbed', 'arbedwch', 'arbennig'},
'arben': {'arbenigwr', 'arbennig'},
'arbenn': {'arbennig'},
'arbenni': {'arbennig'},
'sicr': {'sicrhaf', 'sicrhau', 'sicrwydd'},
'sicrh': {'sicrhaf', 'sicrhau', 'sicrhewch'},
'sicrha': {'sicrhaf', 'sicrhau'},
'golw': {'golwg'},
'gwen': {'gwendid', 'gwennol', 'gwenu', 'gwenwyn', 'gwenyn'},
'gwenn': {'gwennol'},
'gwenno': {'gwennol'},
'ddia': {'ddial', 'ddianaf', 'ddianc', 'ddiangen'},
'ddian': {'ddianaf', 'ddianc', 'ddiangen'},
'helpw': {'helpwch'},
'helpwc': {'helpwch'},
'ddigw': {'ddigwydd'},
'ddigwy': {'ddigwydd'},
'ymbelyd': {'ymbelydredd'},
'ymbelydr': {'ymbelydredd'},
'ymbelydre': {'ymbelydredd'},
'ymbelydred': {'ymbelydredd'},
'traw': {'traws', 'trawst', 'trawstio'},
'traws': {'trawst', 'trawstiau', 'trawstio'},
'plane': {'planed', 'planedau', 'planedol', 'planet'},
'mywy': {'mywyd'},
'wall': {'wallgof'},
'wallg': {'wallgof'},
'wallgo': {'wallgof'},
'cyfr': {'cyfradd', 'cyfraith', 'cyfredol', 'cyfres', 'cyfrif', 'cyfrifo'},
'cyfri': {'cyfrif', 'cyfrifo', 'cyfrinach'},
'agor': {'agored', 'agoriad', 'agorwch'},
'agore': {'agored'},
'chwai': {'chwaith'},
'chwait': {'chwaith'},
'rhwn': {'rhwng'},
'cani': {'caniatáu', 'caniatâd'},
'cania': {'caniatáu', 'caniatâd'},
'caniat': {'caniatáu', 'caniatâd'},
'caniatá': {'caniatáu'},
'saet': {'saethu', 'saethwr'},
'saeth': {'saethu', 'saethwr'},
69

---

<!-- page:70 source:datsci-ex08-solution.pdf -->

'dorr': {'dorri', "dorri'r"},
'rywu': {'rywun'},
'bope': {'bopeth'},
'bopet': {'bopeth'},
'ffur': {'ffurf', 'ffurfiau', 'ffurfio', 'ffurfiol'},
'teit': {'teithio', 'teithiwr', 'teithwyr'},
'teith': {'teithio', 'teithiwr', 'teithwyr'},
'teithi': {'teithio', 'teithiwr'},
'goll': {'golled', 'golli', "golli'r", 'gollon', 'gollwng'},
'bach': {'bachgen'},
'bachg': {'bachgen'},
'bachge': {'bachgen'},
'tani': {'tanio'},
'celw': {'celwydd'},
'celwy': {'celwydd', 'celwyddau'},
'celwyd': {'celwydd', 'celwyddau'},
'gorm': {'gormod'},
'gormo': {'gormod'},
'olrh': {'olrhain'},
'olrha': {'olrhain'},
'olrhai': {'olrhain'},
'rhyfedd': {'rhyfeddol'},
'rhyfeddo': {'rhyfeddol'},
'dyfa': {'dyfais', 'dyfalu', 'dyfalwch'},
'dyfal': {'dyfalu', 'dyfalwch'},
'smit': {'smith'},
'difl': {'diflannu', 'diflas', 'diflasu'},
'difla': {'diflannu', 'diflas', 'diflasu'},
'diflan': {'diflannodd', 'diflannu'},
'diflann': {'diflannodd', 'diflannu'},
'gwed': {'gweddill'},
'gwedd': {'gweddill'},
'gweddi': {'gweddill'},
'gweddil': {'gweddill', 'gweddilliol', 'gweddillion'},
'heddw': {'heddwch'},
'heddwc': {'heddwch'},
'arny': {'arnyn', 'arnynt'},
'pery': {'perygl', 'peryglu', 'peryglus'},
'peryg': {'perygl', 'peryglu', 'peryglus'},
'wyth': {'wythnos'},
'wythn': {'wythnos', 'wythnosau'},
'wythno': {'wythnos', 'wythnosau'},
'cardas': {'cardassia', 'cardassian'},
'cardass': {'cardassia', 'cardassiaid', 'cardassian'},
'cardassi': {'cardassia', 'cardassiaid', 'cardassian'},
'cardassia': {'cardassiaid', 'cardassian'},
'lefe': {'lefel', 'lefelau'},
70

---

<!-- page:71 source:datsci-ex08-solution.pdf -->

'parat': {'paratoi', 'paratowch'},
'parato': {'paratoi', 'paratowch'},
'paratow': {'paratowch'},
'paratowc': {'paratowch'},
'ymyr': {'ymyrryd'},
'ymyrr': {'ymyrraeth', 'ymyrryd'},
'ymyrry': {'ymyrryd'},
'dynn': {'dynnu', "dynnu'n", "dynnu'r"},
'peiriann': {'peiriannau', 'peirianneg', 'peiriannydd'},
'peirianna': {'peiriannau'},
'synn': {'synnu', 'synnwyr'},
'synnw': {'synnwyr'},
'synnwy': {'synnwyr'},
'jane': {'janeway'},
'janew': {'janeway'},
'janewa': {'janeway'},
'neel': {'neelix'},
'neeli': {'neelix'},
'plen': {'plentyn'},
'plent': {'plentyn'},
'plenty': {'plentyn'},
'wert': {'werth', 'werthu'},
'genhad': {'genhadaeth'},
'genhada': {'genhadaeth'},
'genhadae': {'genhadaeth'},
'genhadaet': {'genhadaeth'},
'amdana': {'amdanaf'},
'bodo': {'bodoli'},
'bodol': {'bodolaeth', 'bodoli'},
'crea': {'creadur'},
'cread': {'creadur'},
'creadu': {'creadur'},
'resw': {'reswm'},
'hwnnw': {"hwnnw'n"},
"hwnnw'": {"hwnnw'n"},
'chak': {'chakotay'},
'chako': {'chakotay'},
'chakot': {'chakotay'},
'chakota': {'chakotay'},
'ddiddord': {'ddiddordeb'},
'ddiddorde': {'ddiddordeb'},
'bydden': {'byddent'},
'ymwyb': {'ymwybodol'},
'ymwybo': {'ymwybodol'},
'ymwybod': {'ymwybodol'},
'ymwybodo': {'ymwybodol'},
'rhyd': {'rhydd', 'rhyddhad', 'rhyddhau', 'rhyddid'},
71

---

<!-- page:72 source:datsci-ex08-solution.pdf -->

'synhwy': {'synhwyro', 'synhwyrol', 'synhwyrydd'},
'synhwyr': {'synhwyro', 'synhwyrol', 'synhwyrydd'},
'synhwyry': {'synhwyrydd'},
'synhwyryd': {'synhwyrydd'},
'sgri': {'sgrin'},
'orch': {'orchymyn'},
'orchy': {'orchymyn'},
'orchym': {'orchymyn'},
'orchymy': {'orchymyn'},
'amgy': {'amgylch'},
'amgyl': {'amgylch'},
'amgylc': {'amgylch', 'amgylchedd', 'amgylchynu'},
'gofa': {'gofal', 'gofalu', 'gofalus', 'gofalwr'},
'gofal': {'gofalu', 'gofalus', 'gofalwr'},
…}
b) In the next step, we extract a list of sets of co-occuring suﬀixes which result from removing
the stem from each list. For instance, the example from the previous step would yield the set
{'g', 'gol', 'gon', 'liau', 'liol'} as one of the items on our list.
[72]: overlapping_tokens = list()
for stem, forms in candidate_stems_to_forms.items():
#print("token: " + token1)
tokens = set()
for form in forms:
tokens.add(form[len(stem):])
if len(tokens) > 1:
overlapping_tokens.append(tokens)
[73]: overlapping_tokens
[73]: [{'ch', 'n', 'r'},
{'ch', 'n', 'r'},
{'ch', 'm', 'n'},
{'y', "y'n"},
{'d', 'n'},
{'f', 'i', "i'r", 'n', 'nfa', 'nol', 'nt'},
{'r', 'rlen', 'rol'},
{'s', 'ud', 'wch'},
{'cio', 'dd', 'ddwr', 'en'},
{'ai', 'wl', 'yg', 'ygol', 'ygon'},
{'d', 'dech', 'dem', 'den', 'dent', 'dwn'},
{'n', 'r'},
{'g', 'gol', 'gon', 'liau', 'liol'},
{'l', 'n'},
{'g', 'gau', 'ydd'},
{"'ch", "'i", "'r", "'u"},
72

---

<!-- page:73 source:datsci-ex08-solution.pdf -->

{'ch', 'i', 'r', 'u'},
{'af', 'ais', 'd', 'edol', 'l', 'la', "la'n", 'odd', 'som', 'wch', 'y'},
{'af', 'u', "u'r", 'wch', 'wn'},
{'dd', 'ddio', 'tiwn'},
{'d', 'dio'},
{'a',
'af',
'ai',
"ai'n",
"ai'r",
'an',
'ant',
'ech',
'em',
'en',
'ent',
'in',
'wch',
'wn'},
{'ch', 'n'},
{'io', 'iwch', 'iwn'},
{'o', 'wch', 'wn'},
{'ch', 'n'},
{'au', "au'r"},
{'u', "u'r"},
{'ech', 'em', 'en', 'ent', 'wn'},
{'f', 'i', "i'n", "i'r", 'n', 'nt'},
{'ch', 'chaf'},
{'h', 'haf', 'hwch'},
{'a', 'w', "w'n"},
{'ych', 'yf', 'ym'},
{'ch', 'f', 'm'},
{'wais', 'wch'},
{'ais', 'ch'},
{'d', 'dais', 'dodd', 'dwch'},
{'beth', 'le', 'sut', 'un'},
{'h', 'hant', 'hoch', 'hom', 'hon'},
{'ant', 'och', 'om', 'on'},
{'ch', 'm', 'n'},
{'ch', 'edd', 'eddi', 'n'},
{'dd', 'n'},
{'d', 'dion'},
{'d', 'diad', 'dodd'},
{'af',
'ai',
"ai'r",
'ant',
73

---

<!-- page:74 source:datsci-ex08-solution.pdf -->

'ech',
'em',
'en',
'ent',
'u',
'uog',
'wch',
'wn'},
{'ch', 'n'},
{'ddef', 'mser', 'n', 'rch', 'rfod', 'rfûm', 'teb'},
{'g', 's'},
{'el', 'ir', 'rn', 'waf', 'wodd'},
{'f', 'i', "i'r", 'nt'},
{'a', 'odd', 'u', "u'r", 'wch'},
{'s', 'siad', 'sodd'},
{'n', 'ndeb'},
{'en', 'er', 'lyfr', 'n', 'r'},
{'n', 'nydd', 'r'},
{'af', 'wch'},
{'iais', 'io', "io'i", 'iodd', 'iwch'},
{'ais', 'o', "o'ch", "o'i", 'odd', 'wch'},
{'d', 'diad', 'dodd', 'dol', 'dwch'},
{'i', 'o', "o'n"},
{'a', 'daro', 'i', 'o', 'od', 'ych', 'yf', 'ym', 'yn', 'ynt'},
{'ch', 'f', 'm', 'n', 'nt'},
{'awd', 'yd'},
{'naf', 'ni', 'no', 'noch', 'nom', 'non', 'nyn', 'nynt'},
{'af', 'i', 'o', 'och', 'om', 'on', 'yn', 'ynt'},
{"'n", "'r"},
{'n', 'r'},
{'d', 'dodd', 'dwyd', 'ron'},
{'d', 'dau'},
{'cach', 'g', 'gol'},
{"'ch", "'i", "'n", "'r", "'u", 'g'},
{'ch', 'i', 'n', 'r', 'u'},
{'ed', 'edau', 't'},
{'d', 'dau'},
{'l', 'lus'},
{'ddi', 'll', 'sion', 'thio'},
{'hio', 'hred', 'hwyr'},
{'io', "io'n", 'iodd', 'red', 'redu', 'wyr'},
{'o', "o'n", 'odd'},
{'ar', 'th', 'thom', 'thon'},
{'gfa', 'gu', "gu'r"},
{'fa', 'u', "u'r"},
{'d', 'daf', 'dais', 'dir', 'dodd', 'don', 'dwch', 'dwyd'},
{'af', 'ais', 'ir', 'odd', 'on', 'wch', 'wyd'},
74

---

<!-- page:75 source:datsci-ex08-solution.pdf -->

{'ch', 'yd'},
{'d', 's'},
{"'r", 'n', 'nedd'},
{'dd', 'ddol'},
{'d', 'dol'},
{'liad', 'lwr', 'saf', 'sodd', 'swch', 'swn'},
{'af', 'odd', 'wch', 'wn'},
{'ch', 'n'},
{"'ch", "'r"},
{'ch', 'r'},
{'af', 'afol', 'rio'},
{'f', 'fol'},
{'a',
'af',
'ai',
"ai'n",
"ai'r",
'an',
'ant',
'ech',
'em',
'en',
'ent',
'in',
'wch',
'wn'},
{'f', 'i', "i'n", "i'r", 'n', 'nt'},
{'ch', 'fio', 'm', 'n'},
{'af', 'efig'},
{"'ch", "'n", "'r"},
{'ch', 'n', 'r'},
{'wl', 'yg', 'ygol'},
{'on', 'onol', 'wydd'},
{'n', 'nol'},
{'ech', 'em', 'en', 'ent', 'wn'},
{'ch', 'm', 'n', 'nt'},
{'th', 'thom', 'thon'},
{'n', 'nt'},
{'di', 'l'},
{'awd', 'yd'},
{'em', 'emau'},
{'m', 'mau'},
{'i', 'o', 'och', 'of', 'om', 'yn', 'ynt'},
{'ch', 'f', 'm'},
{'ais', 'eg', 'fa', 'iad'},
{'nd', 'o'},
{'d', 'diau'},
75

---

<!-- page:76 source:datsci-ex08-solution.pdf -->

{'n', 'nau'},
{'au', "au'n"},
{'u', "u'n"},
{'ch', 'm', 'n', 'nt'},
{'d', 'diad', 'dodd'},
{'iad', 'odd'},
{'ch', 'n'},
{'eth', 'ryd'},
{'au', "au'r"},
{'u', "u'r"},
{'dlog', 'dlu', 'll', 'llfa'},
{'l', 'lfa'},
{'ad', 'adau'},
{'d', 'dau'},
{'awn', 'awni', 'e', 'wr', 'wyno', 'ym'},
{'m', 'mach', 'mder'},
{'af', 'ed', 'efig'},
{'in', 'n'},
{"'r", 'ddo', 'n'},
{'aedd', 'u', 'wch', 'wr'},
{'ch', 'm', 'n', 'nt'},
{'d', 'dwr'},
{'diad', 'is'},
{'edd', 'och', 'odd', 'of', 'to'},
{'ch', 'dd', 'f'},
{'fa', 'u'},
{'d', 'dol'},
{'ai', 'ech', 'em', 'i', "i'r", 'wn'},
{'ch', 'm', 'n', 'nt'},
{'ur', 'urol', 'uron'},
{'r', 'rol', 'ron'},
{'lad', 'lo', "lo'n", "lo'r"},
{'ad', 'adau', 'o', "o'n", "o'r"},
{'alf', 'di', 'do', "do'r", 'dyn', 'dynt'},
{'i', 'o', "o'r", 'yn', 'ynt'},
{'ad', 'adau'},
{'d', 'dau'},
{'d', 'f'},
{'n', 'nion', 'nnaf'},
{'dlon', 'n', 'naf', 'nais', 'nodd', 'nwch', 'nwyd'},
{'ais', 'ch', 'ed'},
{'b', 'bau', 'bu', "bu'r"},
{'er', 'hyg', 'ro'},
{'l', 'lwch'},
{'al', 'ar', 'es', 'ig', 'wys', 'ydd', 'yrch'},
{'ais', 'ed', 'i', "i'ch", "i'r", 'odd'},
{'d', 'ddef', 'gel', 'lch'},
76

---

<!-- page:77 source:datsci-ex08-solution.pdf -->

{'l', 'lwch'},
{'au', "au'n"},
{'u', "u'n"},
{'odd', 'wch'},
{'d', 'dach'},
{'iday', 'ol'},
{'ch', 'f', 'frif'},
{'liad', 'lio', 'th'},
{'iad', 'io', "io'r", 'iwch'},
{'ad', 'o', "o'r", 'wch'},
{'i', "i'r", 'nwad'},
{'io', 'iodd', 'iwch'},
{'o', 'odd', 'wch'},
{'edd', 'el', 'ela', 'elwr'},
{'dd', 'ddol', 'l', 'la', 'lwr', 'lwyr'},
{'es', 'i', "i'r", 'odd', 'wch'},
{'euol', 'ofio', 'yson', 'ywir'},
{'son', 'tuno', 'wir'},
{'n', 'nol'},
{'f', 'is', 'soch'},
{'tr', 'trio'},
{'r', 'rio'},
{'io', "io'r", 'iodd', 'iwyd'},
{'o', "o'ch", "o'r", 'odd', 'wyd'},
{'ewch', 'o'},
{'dd', 'n'},
{'ch', 'm', 'n'},
{'ch', 'm', 'n', 'nt'},
{'n', 'nt'},
{'iaf', 'io'},
{'af', 'o'},
{'d', 'dfa', 'di', 'dog'},
{'fa', 'i', 'og', 'ogol'},
{'g', 'gion', 'gol'},
{'h', 'hant', 'hoch', 'hom', 'hon'},
{'ant', 'och', 'om', 'on'},
{'ch', 'm', 'n'},
{'udd', 'ymyn'},
{'d', 'dol'},
{'ch', 'm', 'n', 'nt'},
{'dd', 'ddio', 'ddir'},
{'d', 'dio', 'diol', 'dir'},
{'io', "io'r", 'iol', 'ir'},
{'o', "o'ch", "o'r", 'ol', 'r'},
{'dd', 'ddar', 'thaf'},
{'d', 'dar'},
{'b', 'bl'},
77

---

<!-- page:78 source:datsci-ex08-solution.pdf -->

{'och', 'onol'},
{'ch', 'nol', 'nydd'},
{'r', 'rai', 'riad', 'rion', 'rol'},
{'ddef', 'n', 'rfod'},
{'au', "au'r"},
{'u', "u'r"},
{'int', 'r'},
{'gon', 'gons'},
{'on', 'ons'},
{'n', 'ns'},
{'s', 'swch'},
{'o', "o'r", 'wch'},
{'b', 'bwch'},
{'k', 'ks'},
{'dd', 'ddio'},
{'d', 'dio', 'diol'},
{'io', "io'r", 'iodd', 'iol', 'iwch'},
{'o', "o'ch", "o'r", 'odd', 'ol', 'wch'},
{'iant', 'odd', 'u'},
{'s', 'sodd', 'swch'},
{'ydd', 'yddi'},
{'dd', 'ddes', 'ddi'},
{'d', 'des', 'di'},
{'er', 'ith', 'lu', 'rae', 'rter'},
{'ae', "ae'n", "ae'r", 'aeon', 'ter', 'teri'},
{'e', "e'n", "e'r", 'eon'},
{'elaf', 'elyd'},
{'laf', 'lwch', 'lyd'},
{'af', 'wch', 'yd'},
{'n', 'niad', 'nnol'},
{'ll', 'llus'},
{'l', 'lus'},
{'n', 'nt'},
{'l', 'lder'},
{'raf', 'rais', 'riad', 'rodd', 'rwch', 'rwyd'},
{'af', 'ais', 'iad', 'odd', 'wch', 'wyd'},
{'ch', 'yd'},
{'th', 'thau'},
{'h', 'hau'},
{'ch', 'n'},
{'lair', 'wyl', 'yn'},
{'od', 'odol'},
{'d', 'diad', 'dodd', 'dol', 'dwyd'},
{'d', 'diad'},
{'ad', 'adau'},
{'d', 'dau'},
{'h', 'hant', 'hoch', 'hom', 'hon'},
78

---

<!-- page:79 source:datsci-ex08-solution.pdf -->

{'al', 'alau'},
{'l', 'lau'},
{'ach', 'ed', 'ter'},
{'s', 'si', "si'r", 'sion', 'sodd'},
{'l', 'lau', 'li', "li'r", 'lwr'},
{'aeth', 'aidd', 'au', 'i', "i'r", 'wr'},
{'tr', 'tres', 'tri'},
{'r', 'res', 'ri'},
{'fnig', 'r', 'ried'},
{'ied', 'iwch'},
{'ed', 'wch'},
{'hiau', 'hio', 'hred'},
{'iau', 'io', 'iodd', 'red', 'redu'},
{'au', 'o', 'odd'},
{'nol', 'rdd'},
{'n', 'nnau'},
{'t', 'tio'},
{'d', 'dau'},
{'h', 'hed'},
{"'ch", "'n", "'r", 'ch'},
{'c', 'gen'},
{'ais', 'ed', 'soch'},
{'ch', 'dus', 'm', 'n', 'nt'},
{'iais', 'io', "io'r", 'iwch'},
{'ais', 'o', "o'r", 'wch'},
{'br', 'brau', 'd', 'ddo', 'r', 'th', 'tho'},
{'an', 'ans'},
{'n', 'ns'},
{'dd', 'ddio'},
{'d', 'dio'},
{'d', 'den', 'dwn'},
{'en', 'wn'},
{'awn', 'awni', 'e', 'enwi', 'ogi', 'wr', 'wyno', 'ym', 'ymu'},
{'r', 'rion'},
{'u', 'us'},
{'n', 'sawu', 'si', "si'r", 'so'},
{'awu', 'i', "i'r", 'o'},
{'d', 'dwch'},
{'em', 'emau'},
{'m', 'mau'},
{'len', 'ofal', 'ori', 'orol', 'weld'},
{'en', 'enni', 'ennu'},
{'n', 'nni', 'nnu'},
{'iw', 'lu', 'wch'},
{'u', "u'n", "u'r", 'wch'},
{'io', "io'r"},
{'o', "o'r"},
79

---

<!-- page:80 source:datsci-ex08-solution.pdf -->

{'ai', 'ech', 'ed', 'edus', 'em', 'en', 'id', 'wn'},
{'ch', 'd', 'dus', 'm', 'n'},
{'o', 'wch'},
{'es', 'ion', 'ol'},
{'au', 'ig', 'tfil'},
{'cach', 'g'},
{'ing', 'len'},
{'n', 'nais', 'niad', 'nwch'},
{'ch', 'is', 'r', 'rder'},
{'o', 'ynt'},
{'s', 'sach'},
{'moni', 'n'},
{'ed', 'edol', 'edu'},
{'d', 'diad', 'dol', 'du', "du'n"},
{'iad', 'oedd', 'ol', 'u', "u'n"},
{'er', 'ro'},
{'ad', 'adu'},
{'d', 'du'},
{'di', 'dion', 'dwch'},
{'i', 'ion', 'wch'},
{'d', 'dau'},
{'nnau', 'nneg', 'nt'},
{'nau', 'neg', 'nydd', 't'},
{'od', 'wyn'},
{'n', 'nnol'},
{'al', 'ar', 'au', 'es', 'ig', 'wys', 'ydd'},
{'aeth', 'ol', 'on'},
{'l', 'n'},
{'d', 'dwch'},
{'n', 'nwch'},
{'d', 'dol', 'doli'},
{'ol', 'oli'},
{'l', 'lais', 'li'},
{'ais', 'i'},
{'s', 'st', 'stio'},
{'ais', 'odd', 'u'},
{'io', "io'r"},
{'o', "o'r"},
{'l', 'r'},
{'dd', 'ddo'},
{'d', 'dion', 'do'},
{"'n", "'r"},
{'n', 'r'},
{'ym', 'ymaf', 'ymu'},
{'m', 'maf', 'mu'},
{'af', 'u'},
{'iwn', 'iynu'},
80

---

<!-- page:81 source:datsci-ex08-solution.pdf -->

{'wn', 'ynau', 'ynu'},
{'ig', 'ndo'},
{'iad', 'odd', 'ol', 'wyd'},
{'ad', 'adau'},
{'d', 'dau'},
{'ed', 'edau', 'edol', 'et', 't'},
{'fa', 'i', 'io', 'm', 'mydd'},
{'df', 'u'},
{'e', 'o'},
{'f', 'fen', 'fwys', 'od', 'odi'},
{'en', 'orol', 'wys'},
{'n', 'nnol'},
{'n', 'niad'},
{'eth', 'idd', 'u'},
{'th', 'thau'},
{'h', 'hau'},
{"'n", "'r"},
{'n', 'r'},
{'er', 'eri'},
{'r', 'ri'},
{'af', 'dr', 'ed', 'hau', 'll', 'siau'},
{'d', 'dlyd', 'du', 'l', 'lod', 'th', 'thaf'},
{'h', 'hed'},
{'iant', 'o', 'wr', 'wyr'},
{'ad', 'aid', 'od', 'oden'},
{'d', 'id'},
{'rdeb', 'rol'},
{'deb', 'ol'},
{'is', 'y'},
{'ndeb', 'no', 'nwyd'},
{'deb', 'o', 'wyd'},
{'d', 'fig'},
{'daf', 'dais', 'doch', 'dodd', 'dwch'},
{'af', 'ais', 'och', 'odd', 'wch'},
{'ch', 'dd'},
{'gl', 'glus'},
{'l', 'lus'},
{'lydd', 'r', 'ro'},
{'g', 'gol'},
{'aeth', 'au', 'i', "i'r"},
{'o', "o'n"},
{'au', "au'n"},
{'u', "u'n"},
{'aol', 'au', 'aus', 'ewch'},
{'ol', 'u', 'us'},
{'ed', 'eth', 'f', 'wn'},
{'d', 'th', 'thom', 'thon'},
81

---

<!-- page:82 source:datsci-ex08-solution.pdf -->

{'ch', 'm'},
{'lun', 'lwyn'},
{'un', 'unio', 'wyn'},
{'n', 'niau', 'nio'},
{'lad', 'ladu'},
{'ad', 'adu'},
{'d', 'dodd', 'du', "du'r"},
{'odd', 'u', "u'r"},
{'niad', 'no', 'nol', 'nwch'},
{'iad', 'o', 'ol', 'wch'},
{'rth', 'rthu'},
{'th', 'thu'},
{'h', 'hu'},
{'d', 'dwch', 'nnig'},
{'igwr', 'nig'},
{'haf', 'hau', 'wydd'},
{'af', 'au', 'ewch'},
{'f', 'u'},
{'did', 'nol', 'u', 'wyn', 'yn'},
{'l', 'naf', 'nc', 'ngen'},
{'af', 'c', 'gen'},
{'s', 'st', 'stio'},
{'t', 'tiau', 'tio'},
{'d', 'dau', 'dol', 't'},
{'add', 'aith', 'edol', 'es', 'if', 'ifo'},
{'f', 'fo', 'nach'},
{'ed', 'iad', 'wch'},
{'atáu', 'atâd'},
{'táu', 'tâd'},
{'áu', 'âd'},
{'hu', 'hwr'},
{'u', 'wr'},
{'i', "i'r"},
{'f', 'fiau', 'fio', 'fiol'},
{'hio', 'hiwr', 'hwyr'},
{'io', 'iwr', 'wyr'},
{'o', 'wr'},
{'ed', 'i', "i'r", 'on', 'wng'},
{'dd', 'ddau'},
{'d', 'dau'},
{'is', 'lu', 'lwch'},
{'u', 'wch'},
{'annu', 'as', 'asu'},
{'nnu', 's', 'su'},
{'nodd', 'nu'},
{'odd', 'u'},
{'l', 'liol', 'lion'},
82

---

<!-- page:83 source:datsci-ex08-solution.pdf -->

{'n', 'nt'},
{'gl', 'glu', 'glus'},
{'l', 'lu', 'lus'},
{'os', 'osau'},
{'s', 'sau'},
{'sia', 'sian'},
{'ia', 'iaid', 'ian'},
{'a', 'aid', 'an'},
{'id', 'n'},
{'l', 'lau'},
{'oi', 'owch'},
{'i', 'wch'},
{'aeth', 'yd'},
{'u', "u'n", "u'r"},
{'au', 'eg', 'ydd'},
{'u', 'wyr'},
{'h', 'hu'},
{'aeth', 'i'},
{'d', 'dhad', 'dhau', 'did'},
{'ro', 'rol', 'rydd'},
{'o', 'ol', 'ydd'},
{'h', 'hedd', 'hynu'},
{'l', 'lu', 'lus', 'lwr'},
{'u', 'us', 'wr'},
{'as', 'iwed'},
{'edd', 'eddu'},
{'dd', 'ddu', 'ddus'},
{'d', 'du', 'dus'},
{'l', 'lo', 'o'},
{'k', "k's"},
{'f', 'is'},
{'p', 'po'},
{'diad', 'do', "do'r", 'dwch', 'dydd'},
{'iad', 'o', "o'r", 'wch', 'ydd'},
{'rth', 'rthu'},
{'th', 'thu'},
{'h', 'hu'},
{'i', 'nwad'},
{'i', "i'r", 'ion', 'odd'},
{'eth', 'u'},
{'l', 'lu'},
{'edd', 'erth', 'rnod'},
{'s', 'sodd'},
{'m', 'mder', 'mu'},
{'dd', 'g'},
{'iti', 'ly'},
{'goel', 'sbys'},
83

---

<!-- page:84 source:datsci-ex08-solution.pdf -->

{'b', 'bion', 'bu', 'r'},
{'ion', 'u'},
{'ad', 'o'},
{'r', 'ryn'},
{'liad', 'log', 'logi', 'lu', "lu'r", 'lwyr'},
{'iad', 'og', 'ogi', 'u', "u'r", 'wyr'},
{'iais', 'iau', 'iol', 'iwch'},
{'ais', 'au', 'ol', 'wch'},
{'is', 'u'},
{'u', 'wr'},
{'id', 'ir', 'oedd'},
{'d', 'r'},
{'h', 'hoch', 'hom', 'hon'},
{'i', "i'r"},
{'niad', 'niol', 'nwyr', 'nydd'},
{'iad', 'iodd', 'iol', 'wyr', 'ydd'},
{'n', 'nion'},
{'hau', 'io'},
{'a', 'gelu', 'hlu', 'rys'},
{'ach', 'af', 'áu'},
{'r', 'rau'},
{'ch', 'n'},
{'i', 'iad', 'ion'},
{'gi', "gi'r", 'giad', 'l'},
{'ef', 'efol'},
{'f', 'fol'},
{'r', 'riad'},
{'och', 'om'},
{'ch', 'm'},
{'lydd', 'r'},
{'iwch', 'ur'},
{'ai', 'iad', 'ion', 'ol'},
{'had', 'hau', 'id'},
{'ad', 'au', "au'r", 'ewch'},
{'d', 'u', "u'r"},
{'add', 'aith', 'if', 'ifo', 'ifol'},
{'f', 'fo', 'fol', 'nach'},
{'o', 'ol'},
{'l', 'ldeb'},
{'ais', 'alu', 'nach', 'odol'},
{'is', 'lu'},
{'hori', 'or'},
{'rdeb', 'rol'},
{'deb', 'ol'},
{'ad', 'adau'},
{'d', 'dau'},
{'tr', 'wm', 'ymau', 'ymeg', 'ymol'},
84

---

<!-- page:85 source:datsci-ex08-solution.pdf -->

{'ifol', 'od', 'odi'},
{'d', 'di'},
{'si', 'swyr'},
{'i', 'wyr'},
{'dd', 'ddi', 'ddol'},
{'d', 'di', 'dol'},
{'ion', 'naf', 'nais', 'nodd', 'nwch'},
{'af', 'ais', 'odd', 'wch'},
{'t', 'ty'},
{'lan', 'lans', 'lus'},
{'an', 'ans', 'us'},
{'n', 'ns'},
{'em', 'emau'},
{'m', 'mau'},
{'nais', 'niad', 'nu'},
{'ais', 'iad', 'u'},
{'n', 'niol'},
{'ant', 'och', 'om'},
{'ch', 'm'},
{'lo', 'n'},
{'n', 'nnau'},
{'fwng', 'mell'},
{'yn', 'ynas'},
{'n', 'nas'},
{'od', 'odi', 'odol', 'u', "u'n"},
{'er', 'ers'},
{'r', 'rs'},
{'antu', 'chod', 'ed'},
{'iau', 'io', "io'r", 'iwch', 'iwr', 'lt'},
{'au', 'o', "o'r", 'wch', 'wr'},
{'dr', 'dro'},
{'r', 'ro'},
{'ell', 'yn'},
{'ll', 'llau'},
{'l', 'lau'},
{'g', 'go', "go'r"},
{'o', "o'r", 'oedd'},
{'ion', 'o'},
{'i', 'iad', 'ion'},
{'ddo', 'ldro', 'n', 'th', 'thu'},
{'h', 'hodd', 'hu', "hu'r"},
{'odd', 'u', "u'r"},
{'iais', 'io', 'iwch'},
{'ais', 'o', 'wch'},
{'sib', 'sibl'},
{'ib', 'ibl'},
{'b', 'bl'},
85

---

<!-- page:86 source:datsci-ex08-solution.pdf -->

{'ch', 'f'},
{'tiad', 'tu', 'twch'},
{'iad', 'u', 'wch'},
{'th', 'thau'},
{'h', 'hau'},
{'g', 'gol', 'liau'},
{'l', 'man'},
{'uais', 'uodd', 'uwch'},
{'ais', 'odd', 'wch'},
{'d', 'dwch'},
{'r', 'riol'},
{'anol', 'anu', 'ardd', 'odd'},
{'nol', 'nu', 'rdd'},
{'ol', 'u'},
{'liad', 'lio'},
{'iad', 'io', "io'r"},
{'ad', 'o', "o'r"},
{'ad', 'adau'},
{'d', 'dau'},
{'mygu', 'ryn', 'ymyg'},
{'au', 'ewch'},
{'r', 'ran', 'rans'},
{'an', 'ans'},
{'n', 'ns'},
{'u', "u'r"},
{'ded', 'yn'},
{'d', 'dau'},
{'ais', 'ch', 'edd', 'i'},
{'ch', 'r'},
{'lad', 'lo', "lo'n"},
{'ad', 'adau', 'o', "o'n"},
{'di', 'ge'},
{'on', 'onol', 'onél'},
{'n', 'nol', 'nél'},
{'ig', 'ws'},
{'l', 'lo'},
{'od', 'odol', 'on'},
{'d', 'dol', 'n'},
{'ch', 'fod', 'fûm', 'wydd'},
{'od', 'ûm'},
{'dd', 'ddau'},
{'d', 'dau'},
{'h', 'i', 'ïon'},
{'en', 'enol'},
{'n', 'nol', 'nydd'},
{'n', 'r'},
{'der', 'u'},
86

---

<!-- page:87 source:datsci-ex08-solution.pdf -->

{'r', 'yr'},
{'in', 'inol'},
{'n', 'nol'},
{'d', 'idio'},
{'u', 'wch'},
{'iau', 'io', "io'r", 'iwch', 'iwr', 'wyr'},
{'au', 'o', "o'r", 'wch', 'wr'},
{'ol', 'él'},
{'r', 'yno'},
{'dr', 'dro'},
{'r', 'ro'},
{'s', 'siad', 'su', "su'r"},
{'iad', 'u', "u'r"},
{'ebu', 'ebwr'},
{'bu', 'bwr'},
{'u', 'wr'},
{'iad', 'io'},
{'ad', 'o'},
{'och', 'om', 'on'},
{'ch', 'm', 'n'},
{'tiad', 'tu'},
{'iad', 'u'},
{'hiau', 'hio', 'hiol', 'hlon'},
{'iau', 'io', 'iol', 'lon'},
{'au', 'o', 'ol'},
{'iad', 'iau'},
{'ad', 'au'},
{'d', 'u'},
{'aeth', 'au', 'awd'},
{'eth', 'u', 'wd'},
{'l', 'r', 'u'},
{'ef', 'efwr'},
{'f', 'fwr', 'fwyr'},
{'ad', 'adau'},
{'d', 'dau'},
{'wil', 'wydd'},
{'il', 'ilio', 'ydd'},
{'l', 'liad', 'lio', 'lydd'},
{'iwr', 'l', 'wyr'},
{'llen', 'n', 'nau', 'paru'},
{"'ch", "'r", 'dd'},
{'ch', 'r'},
{'ol', 'wm', 'ymau', 'ôl'},
{'fa', 'ol', 't'},
{'deck', 'gram'},
{'d', 'diad', 'diau'},
{'iad', 'iau'},
87

---

<!-- page:88 source:datsci-ex08-solution.pdf -->

{'ad', 'au'},
{'d', 'u'},
{'aeth', 'ion', 'ol'},
{"'ch", "'r", 'dd', 'l'},
{'ch', 'r'},
{'dais', 'do', 'dodd'},
{'ais', 'iant', 'o', 'odd'},
{'iad', 'io', 'ydd'},
{'ad', 'o'},
{'si', 'swyr'},
{'i', 'wyr'},
{'iad', 'io', "io'r", 'ion', 'iwch'},
{'ad', 'o', "o'r", 'on', 'wch'},
{'egol', 'oleg'},
{'th', 'thwr'},
{'h', 'hwr'},
{'drad', 'dro', 'drol', 'dron', 'thau'},
{'rad', 'ro', 'rol', 'ron'},
{'ad', 'o', 'ol', 'on'},
{'io', "io'r"},
{'o', "o'r"},
{'aw', 'en', 'ennu'},
{'f', 'is'},
{'f', 'is', 'soch'},
{'h', 'hed'},
{'du', "du'r"},
{'u', "u'r"},
{'egol', 'oleg'},
{'dd', 'l'},
{'r', 'rol', 'yr'},
{'ed', 'edol', 'edu'},
{'d', 'dol', 'du'},
{'ol', 'u'},
{'dd', 'ddar', 'rth', 'thaf'},
{'d', 'dar'},
{'ad', 'adau'},
{'d', 'dau'},
{'ach', 'ter'},
{'a', "a'n"},
{'wn', 'wni'},
{'n', 'ni', "ni'r"},
{'i', "i'r"},
{'l', 'lu'},
{'i', 'us'},
{'au', 'u', "u'r"},
{'di', 'diad'},
{'i', 'iad'},
88

---

<!-- page:89 source:datsci-ex08-solution.pdf -->

{'io', "io'r"},
{'adau', 'o', "o'r"},
{'dd', 'ddol'},
{'d', 'dol'},
{'f', 'fol'},
{'iaid', 'ol'},
{'daro', 'droi', 'iant', 'od', 'rych'},
{'n', 'ns'},
{'ad', 'adau'},
{'d', 'dau'},
{'s', 'sio'},
{'ngys', 'ol'},
{'ar', 'aror'},
{'r', 'ror'},
{'dod', 'dodi'},
{'od', 'odau', 'odi'},
{'d', 'dau', 'di', 'diad'},
{'dd', 'ddau'},
{'d', 'dau'},
{'t', 'tio'},
{'wn', 'wni'},
{'n', 'ni', "ni'r"},
{'i', "i'r"},
{'ad', 'on'},
{'ll', 'n'},
{'l', 'lach'},
{'ri', 'rydd'},
{'i', 'ydd'},
{'yd', 'ydol'},
{'d', 'dion', 'dol'},
{'ynol', 'ynu'},
{'niad', 'nol', 'nu'},
{'iad', 'ol', 'u'},
{'ewid', 'od'},
{'d', 'r'},
{'fawr', 'u'},
{'r', 'rogi'},
{'gwyl', 'gyn'},
{'lair', 'wyl', 'yn'},
{'eb', 'ebu', 'er', 'if'},
{'on', 'onol', 'onél'},
{'n', 'nol', 'nél'},
{'ol', 'él'},
{'etha', 'fodd', 'fyg', 'las', 'rif', 'rod', 'rodi'},
{'if', 'ifol', 'od', 'odi'},
{'f', 'fol'},
{'wn', 'ynau'},
89

---

<!-- page:90 source:datsci-ex08-solution.pdf -->

{"'ch", "'r", 'l'},
{'ch', 'r'},
{'ffa', 'fion'},
{'fa', 'ion'},
{'gi', "gi'r"},
{'i', "i'r"},
{'atáu', 'atâd'},
{'táu', 'tâd'},
{'áu', 'âd'},
{'du', "du'r"},
{'u', "u'r"},
{'fod', 'wydd'},
{'dd', 'ddeb'},
{'d', 'deb'},
{'g', 'go', 'str', 'stro'},
{'tr', 'tro'},
{'r', 'ro'},
{'l', 'lfan', 'log'},
{'fan', 'og'},
{'nau', 'nu'},
{'au', 'u'},
{'od', 'rom'},
{'n', 'nhau'},
{'r', 'rau'},
{'nnau', 'nneg', 'nt'},
{'nau', 'neg', 'nydd', 't'},
{'au', 'eg', 'ydd'},
{'ewid', 'od'},
{'d', 'dwyr'},
{'iant', 'o', 'wr'},
{'aol', 'au', 'aus'},
{'ol', 'u', 'us'},
{'o', 'wch'},
{'nu', 'nydd'},
{'u', 'ydd'},
{'iau', 'io'},
{'au', 'o'},
{'edd', 'l', 'li', 'liad'},
{'i', 'iad'},
{'es', 'esu'},
{'s', 'su'},
{'d', 'dlu', 'dwr', 'dwyr'},
{'lu', 'wr', 'wyr'},
{'r', 'yr'},
{'n', 'nnau'},
{'io', "io'r"},
{'o', "o'r"},
90

---

<!-- page:91 source:datsci-ex08-solution.pdf -->

{'fro', 'nydd', 'od'},
{'es', 'i'},
{'d', 'f'},
{'al', 'nod'},
{'eu', "eu'r", 'lad', 'yn'},
{'er', 'erol'},
{'r', 'rol'},
{'g', 'gi'},
{'adau', 'ni'},
{'l', 'lwch'},
{'en', 'wys'},
{'egol', 'egu'},
{'gol', 'gu'},
{'ol', 'u'},
{'ain', 'er', 'eron'},
{'r', 'ron'},
{'s', 'sodi'},
{'edin', 'ous'},
{'diad', 'do'},
{'iad', 'o'},
{'au', 'eg', 'egol', 'ol'},
{'g', 'gol'},
{'ys', 'ysu'},
{'s', 'su', "su'r"},
{'en', 'eon'},
{'n', 'on'},
{'iad', 'odd'},
{'d', 'di'},
{'io', "io'r"},
{'aeth', 'o', "o'r"},
{'ch', 'ched', 'dl', 'dlau', 'il'},
{'h', 'hed'},
{'ld', 'liad', 'lwyr', 'lydd'},
{'d', 'iad', 'wyr', 'ydd'},
{'dain', 'iau', 'io'},
{'niad', 'niaf', 'nio'},
{'iad', 'iaf', 'io', "io'r", 'iwch'},
{'ad', 'af', 'o', "o'r", 'wch'},
{'d', 'f'},
{'r', 'rion'},
{'ur', 'urol'},
{'r', 'rol'},
{'n', 'nt'},
{'aeth', 'on', 's'},
{'ach', 'der'},
{'haol', 'hau'},
{'aol', 'au', 'awyd'},
91

---

<!-- page:92 source:datsci-ex08-solution.pdf -->

{'ol', 'u', 'wyd'},
{'u', 'us'},
{'r', 'rach'},
{'len', 'oedd', 'ol'},
{'edd', 'l'},
{'d', 'di'},
{'irio', 'r'},
{'iant', 'wch'},
{'bwn', 'ol'},
{'au', 'u'},
{'o', "o'r", 'on'},
{'fal', 'ri', 'rol'},
{'i', 'ol'},
{'ol', 'ydd'},
{'dedd', 'dig'},
{'edd', 'ig'},
{'dw', 'el', 'lon', 'nol', 'riad', 'ru'},
{'un', 'unio'},
{'n', 'niau', 'nio'},
{'d', 'dion'},
{'h', 'haf', 'hygu'},
{'af', 'ygu'},
{'iant', 'u'},
{'au', "au'r", 'ewch'},
{'u', "u'r"},
{'od', 'odlu', 'odwr'},
{'d', 'dwch'},
{'io', 'iwch'},
{'o', 'wch'},
{'eth', 'ethu'},
{'th', 'thau', 'thu'},
{'h', 'hau', 'hu'},
{'au', 'u'},
{'rth', 'rthu'},
{'th', 'thu'},
{'h', 'hu'},
{'gu', 'gwch'},
{'u', 'wch'},
{'ais', 'odd', 'wch'},
{'o', "o'n"},
{'g', 'gi'},
{'d', 'di'},
{'w', 'wod'},
{'awf', 'ofi'},
{'au', 'icaf', 'ig', 'o'},
{'caf', 'g'},
{"'n", "'r", 'ad', 'af', 'odd'},
92

---

<!-- page:93 source:datsci-ex08-solution.pdf -->

{'d', 'f'},
{'ion', 'wch'},
{'ni', "ni'n"},
{'i', "i'n"},
{'iau', 'io', 'iol'},
{'au', 'o', 'ol'},
{'u', 'wch'},
{'ed', 'edu'},
{'d', 'du'},
{'aff', 'affu'},
{'ff', 'ffu'},
{'f', 'fu'},
{'u', "u'ch"},
{'io', 'wedd'},
{'aeth', 'o', 'on'},
{'n', 'na'},
{'am', 'amau'},
{'ffig', 'm', 'mau'},
{'ad', 'o'},
{'l', 'lwch'},
{'mygu', 'ryn'},
{'i', "i'r", 'iad'},
{"'r", 'ad', 'adau'},
{'d', 'dau'},
{'d', 'dwch'},
{'a', 'oedd', 'wr', 'wyr'},
{'r', 'yr'},
{'giad', 'gu'},
{'edig', 'iad', 'u'},
{'hio', 'hiwr', 'hwyr'},
{'io', 'iwr', 'wyr'},
{'o', 'wr'},
{'hydi', 'th'},
{"'ch", "'r"},
{'ch', 'r'},
{'af', 'odd', 'wyd'},
{'ni', 'nu'},
{'i', 'u'},
{'d', 'dlon'},
{'nau', 'nol', 'nu', "nu'r"},
{'au', 'ol', 'u', "u'r"},
{'ial', 'iau'},
{'al', 'au'},
{'l', 'u'},
{'ch', 'dd'},
{'yro', 'yrol'},
{'iais', 'io', "io'r"},
93

---

<!-- page:94 source:datsci-ex08-solution.pdf -->

{'ais', 'o', "o'r"},
{'ch', 'r'},
{'au', 'o'},
{'n', 'r'},
{'oedd', 'og', 'wair'},
{'edd', 'g'},
{'ctig', 'eth', 'r'},
{'edo', 'idos'},
{'af', 'ais', 'odd', 'wch', 'wyd'},
{'h', 'hgar'},
{'iau', 'io', 'iwyd'},
{'au', 'o', 'wyd'},
{'ad', 'adau'},
{'d', 'dau'},
{'adur', 'al'},
{'dur', 'l'},
{'ur', 'uron'},
{'r', 'ron'},
{'ad', 'adau'},
{'d', 'dau'},
{'d', 'daf', 'dais', 'dodd', 'dwyd'},
{'af', 'ais', 'odd', 'wyd'},
{'f', 'is'},
{'g', 'odd'},
{"'r", 'n', 'nedd'},
{'wn', 'ynau'},
{'rchu', 'rfu'},
{'chu', 'fu'},
{'d', 'dau'},
{'dd', 'rch'},
{'dd', 'ddau'},
{'d', 'dau'},
{'oid', 'oids', 'ovax'},
{'id', 'ids', 'vax'},
…]
c) Now we derive overlap counts between each pair of suﬀixes. Iterate over the sets of co-
occurring suﬀixes, and when processing such a set, increase the overlap count for each pair
of suﬀixes in the set by one. A sparse matrix representation such as nested dictionaries is
recommended for this step.
[74]: shared_paradigm_counts = dict()
for potential_paradigm in overlapping_tokens:
for element in potential_paradigm:
if element not in shared_paradigm_counts:
shared_paradigm_counts[element] = dict()
for element2 in potential_paradigm:
94

---

<!-- page:95 source:datsci-ex08-solution.pdf -->

if element2 not in shared_paradigm_counts[element]:
shared_paradigm_counts[element][element2] = 0
shared_paradigm_counts[element][element2] += 1
[75]: shared_paradigm_counts.keys()
[75]: dict_keys(['n', 'r', 'ch', 'm', 'y', "y'n", 'd', "i'r", 'nol', 'f', 'nt', 'nfa',
'i', 'rol', 'rlen', 'ud', 'wch', 's', 'dd', 'cio', 'ddwr', 'en', 'ygol', 'ai',
'wl', 'yg', 'ygon', 'dwn', 'dem', 'dech', 'den', 'dent', 'g', 'gon', 'liol',
'liau', 'gol', 'l', 'ydd', 'gau', "'r", "'u", "'ch", "'i", 'u', 'edol', 'odd',
'ais', "la'n", 'af', 'la', 'som', "u'r", 'wn', 'tiwn', 'ddio', 'dio', 'ent',
'em', 'ech', 'an', 'ant', "ai'r", "ai'n", 'a', 'in', 'iwn', 'iwch', 'io', 'o',
'au', "au'r", "i'n", 'chaf', 'haf', 'hwch', 'h', "w'n", 'w', 'ych', 'ym', 'yf',
'wais', 'dais', 'dwch', 'dodd', 'un', 'le', 'beth', 'sut', 'hant', 'hon', 'hom',
'hoch', 'och', 'on', 'om', 'edd', 'eddi', 'dion', 'diad', 'uog', 'mser', 'rfûm',
'rch', 'teb', 'ddef', 'rfod', 'wodd', 'waf', 'el', 'rn', 'ir', 'siad', 'sodd',
'ndeb', 'er', 'lyfr', 'nydd', 'iais', "io'i", 'iodd', "o'ch", "o'i", 'dol',
"o'n", 'daro', 'ynt', 'yn', 'od', 'awd', 'yd', 'noch', 'nynt', 'naf', 'ni',
'nom', 'nyn', 'no', 'non', "'n", 'ron', 'dwyd', 'dau', 'cach', 'edau', 't',
'ed', 'lus', 'ddi', 'll', 'sion', 'thio', 'hwyr', 'hred', 'hio', 'redu', "io'n",
'red', 'wyr', 'ar', 'thon', 'th', 'thom', 'gu', 'gfa', "gu'r", 'fa', 'dir',
'don', 'daf', 'wyd', 'nedd', 'ddol', 'saf', 'swn', 'liad', 'lwr', 'swch',
'afol', 'rio', 'fol', 'fio', 'efig', 'wydd', 'onol', 'di', 'emau', 'mau', 'of',
'eg', 'iad', 'nd', 'diau', 'nau', "au'n", "u'n", 'ryd', 'eth', 'dlog', 'llfa',
'dlu', 'lfa', 'adau', 'ad', 'wr', 'e', 'wyno', 'awn', 'awni', 'mder', 'mach',
'ddo', 'aedd', 'dwr', 'is', 'to', 'ur', 'uron', 'urol', "lo'n", "lo'r", 'lad',
'lo', "o'r", 'dynt', 'dyn', 'do', "do'r", 'alf', 'nnaf', 'nion', 'nais', 'nwch',
'nodd', 'nwyd', 'dlon', 'bau', "bu'r", 'b', 'bu', 'ro', 'hyg', 'lwch', 'es',
'yrch', 'wys', 'ig', 'al', "i'ch", 'lch', 'gel', 'dach', 'ol', 'iday', 'frif',
'lio', "io'r", 'nwad', 'elwr', 'ela', 'lwyr', 'yson', 'ofio', 'euol', 'ywir',
'wir', 'son', 'tuno', 'soch', 'tr', 'trio', 'iwyd', 'ewch', 'iaf', 'dog', 'dfa',
'ogol', 'og', 'gion', 'udd', 'ymyn', 'ddir', 'diol', 'iol', 'ddar', 'thaf',
'dar', 'bl', 'rion', 'riad', 'rai', 'int', 'gons', 'ons', 'ns', 'bwch', 'ks',
'k', 'iant', 'yddi', 'ddes', 'des', 'lu', 'rter', 'rae', 'ith', "ae'n", 'ter',
'ae', 'teri', 'aeon', "ae'r", "e'n", "e'r", 'eon', 'elyd', 'elaf', 'lyd', 'laf',
'nnol', 'niad', 'llus', 'lder', 'rwch', 'rais', 'raf', 'rodd', 'rwyd', 'thau',
'hau', 'lair', 'wyl', 'odol', 'alau', 'lau', 'ach', 'si', "si'r", 'li', "li'r",
'aeth', 'aidd', 'tres', 'tri', 'res', 'ri', 'ried', 'fnig', 'ied', 'hiau',
'iau', 'rdd', 'nnau', 'tio', 'hed', 'gen', 'c', 'dus', 'brau', 'tho', 'br',
'ans', 'ogi', 'enwi', 'ymu', 'us', 'so', 'sawu', 'awu', 'ofal', 'len', 'ori',
'orol', 'weld', 'enni', 'ennu', 'nni', 'nnu', 'iw', 'id', 'edus', 'ion', 'tfil',
'ing', 'rder', 'sach', 'moni', 'edu', 'du', "du'n", 'oedd', 'adu', 'nneg',
'neg', 'wyn', 'doli', 'oli', 'lais', 'st', 'stio', 'ymaf', 'mu', 'maf', 'iynu',
'ynu', 'ynau', 'ndo', 'et', 'mydd', 'df', 'odi', 'fwys', 'fen', 'idd', 'eri',
'dr', 'siau', 'lod', 'dlyd', 'oden', 'aid', 'rdeb', 'deb', 'fig', 'doch', 'gl',
'glus', 'lydd', 'aol', 'aus', 'lwyn', 'lun', 'unio', 'nio', 'niau', 'ladu',
"du'r", 'rth', 'rthu', 'thu', 'hu', 'nnig', 'nig', 'igwr', 'did', 'ngen', 'nc',
95

---

<!-- page:96 source:datsci-ex08-solution.pdf -->

'tiau', 'if', 'add', 'ifo', 'aith', 'fo', 'nach', 'atáu', 'atâd', 'tâd', 'táu',
'áu', 'âd', 'hwr', 'fiol', 'fiau', 'hiwr', 'iwr', 'wng', 'ddau', 'as', 'annu',
'asu', 'su', 'nu', 'lion', 'glu', 'os', 'osau', 'sau', 'sia', 'sian', 'ian',
'ia', 'iaid', 'owch', 'oi', 'dhad', 'dhau', 'rydd', 'hynu', 'hedd', 'iwed',
'eddu', 'ddu', 'ddus', "k's", 'po', 'p', 'dydd', 'rnod', 'erth', 'ly', 'iti',
'sbys', 'goel', 'bion', 'ryn', 'log', 'logi', "lu'r", 'niol', 'nwyr', 'rys',
'hlu', 'gelu', 'rau', "gi'r", 'gi', 'giad', 'efol', 'ef', 'had', 'ifol', 'ldeb',
'alu', 'or', 'hori', 'ymeg', 'ymol', 'ymau', 'wm', 'swyr', 'ty', 'lans', 'lan',
'fwng', 'mell', 'ynas', 'nas', 'ers', 'rs', 'antu', 'chod', 'lt', 'dro', 'ell',
'llau', "go'r", 'go', 'ldro', "hu'r", 'hodd', 'sib', 'sibl', 'ib', 'ibl',
'twch', 'tu', 'tiad', 'man', 'uwch', 'uodd', 'uais', 'riol', 'anol', 'ardd',
'anu', 'ymyg', 'mygu', 'rans', 'ran', 'ded', 'ge', 'onél', 'nél', 'ws', 'fod',
'fûm', 'ûm', 'ïon', 'enol', 'der', 'yr', 'inol', 'idio', 'él', 'yno', "su'r",
'ebwr', 'ebu', 'bwr', 'hlon', 'hiol', 'lon', 'wd', 'efwr', 'fwr', 'fwyr', 'wil',
'ilio', 'il', 'paru', 'llen', 'ôl', 'gram', 'deck', 'oleg', 'egol', 'thwr',
'drad', 'drol', 'dron', 'rad', 'aw', "a'n", 'wni', "ni'r", 'droi', 'rych',
'sio', 'ngys', 'aror', 'ror', 'dod', 'dodi', 'odau', 'lach', 'ydol', 'ynol',
'ewid', 'fawr', 'rogi', 'gyn', 'gwyl', 'eb', 'rodi', 'fyg', 'rod', 'rif', 'las',
'fodd', 'etha', 'fion', 'ffa', 'ddeb', 'stro', 'str', 'tro', 'lfan', 'fan',
'rom', 'nhau', 'dwyr', 'esu', 'fro', 'nod', "eu'r", 'eu', 'erol', 'egu', 'ain',
'eron', 'sodi', 'ous', 'edin', 'ysu', 'ys', 'dlau', 'ched', 'dl', 'ld', 'dain',
'niaf', 'haol', 'awyd', 'rach', 'irio', 'bwn', 'fal', 'dedd', 'dig', 'ru', 'dw',
'hygu', 'ygu', 'odlu', 'odwr', 'ethu', 'gwch', 'wod', 'ofi', 'awf', 'icaf',
'caf', "ni'n", 'aff', 'affu', 'ff', 'ffu', 'fu', "u'ch", 'wedd', 'na', 'am',
'amau', 'ffig', 'edig', 'hydi', "nu'r", 'ial', 'yro', 'yrol', 'wair', 'ctig',
'idos', 'edo', 'hgar', 'adur', 'dur', 'rchu', 'rfu', 'chu', 'oids', 'oid',
'ovax', 'vax', 'ids', 'ds', 'ok', 'ha', 'pwyd', 'ho', 'rudd', 'tai', 'eiwr',
'eion', 'nder', 'meg', 'mol', 'osfa', 'sfa', 'rous', 'wrdd', 'eol', 'sis',
'ral', 'tig', 'gys', 'lgof', 'gof', 'orau', 'sog', 'ydio', 'arol', 'athu',
'leth', 'neb', 'olyn', 'ryw', 'nnus', 'nus', 'rino', 'ino', 'nebu', 'biad',
'chol', 'hol', 'roi', 'aro', 'uon', 'erau', 'nfil', 'uol', 'fil', 'lwm', 'ylch',
'uro', 'uraf', 'hawn', 'negu', 'wed', 'iect', 'dwyo', 'les', 'lie', 'ie',
'adol', 'onig', 'ens', 'ense', 'nse', 'se', 'lay', 'hion', 'syll', 'hedu',
'nwi', 'wi', 'wad', 'gwyr', 'gedd', 'gwr', 'aru', 'erus', 'rus', 'idau', 'anau',
'nill', 'gell', 'ship', 'base', 'yrfu', 'wid', 'wig', 'estr', 'omen', 'stri',
'yfel', 'fel', 'elio', 'port', 'elu', 'rdio', 'rd', 'ddon', 'ddwn', 'tor',
'ynnu', 'ynig', 'olau', 'ychu', 'swr', 'rair', 'hydd', 'hiad', 'ilod', 'yo',
'yydd', 'gom', 'goch', 'das', 'abod', 'aws', 'bod', 'tlon', 'tl', 'ntau', 'tau',
'fi', 'dgar', 'oard', 'ase', 'chau', 'lyn', 'teir', 'eir', 'mm', 'we', 'raff',
'bell', 'ic', 'ddgi', 'dgi', 'for', 'wyo', 'efau', 'fau', 'achu', 'asol', 'sol',
'grau', 'gryn', 'fodi', 'dun', 'duno', 'araf', 'hiwm', 'hium', 'iwm', 'ium',
'um', 'tref', 'ein', 'ocol', 'col', 'sgar', 'gar', 'giol', 'uno', 'esau', 'ren',
'gr', 'fnau', 'fn', 'hfan', 'miad', 'mio', 'riau', 'wiol', 'wiad', 'ost', 'ecs',
'ical', 'tasi', 'lle', 'ines', 'nes', 'unol', 'llan', 'iont', 'urau', 'hal',
'rpas', 'enau', 'ifer', 'rwyr', 'ft', 'ftwr', 'twr', 'ynio'])
d) Convert the overlap counts into a Pandas dataframe, and clean it by replacing all missing
96

---

<!-- page:97 source:datsci-ex08-solution.pdf -->

values by 0. Reduce the matrix on both axes to only those candidate suﬀixes for which 50 or
more overlaps were found, i.e. delete rows or columns which sum up to less than 50.
[76]: morphs = pd.DataFrame.from_dict(shared_paradigm_counts)
[77]: morphs
[77]: n r ch m y y'n d i'r nol f … urau \
n 140.0 20.0 33.0 16.0 NaN NaN 4.0 3.0 10.0 4.0 … NaN
r 20.0 100.0 18.0 NaN NaN NaN 3.0 NaN NaN NaN … NaN
ch 33.0 18.0 78.0 24.0 NaN NaN 1.0 NaN 2.0 7.0 … NaN
m 16.0 NaN 24.0 35.0 NaN NaN 1.0 NaN NaN 3.0 … NaN
d 4.0 3.0 1.0 1.0 1.0 NaN 148.0 NaN NaN 4.0 … NaN
… … … … … … … … … … … … …
wiad NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN … NaN
ecs NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN … NaN
ical NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN … NaN
ft NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN … NaN
ftwr NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN … NaN
hal rpas enau ifer rwyr ft ftwr twr ynio
n NaN NaN NaN NaN NaN NaN NaN NaN NaN
r NaN NaN NaN NaN 1.0 NaN NaN NaN NaN
ch NaN NaN NaN NaN NaN NaN NaN NaN NaN
m NaN NaN NaN NaN NaN NaN NaN NaN NaN
d NaN NaN NaN NaN NaN NaN NaN NaN NaN
… … … … … … … … … …
wiad NaN NaN NaN NaN NaN NaN NaN NaN NaN
ecs NaN NaN NaN NaN NaN NaN NaN NaN NaN
ical NaN NaN NaN NaN NaN NaN NaN NaN NaN
ft NaN NaN NaN NaN NaN 1.0 1.0 NaN NaN
ftwr NaN NaN NaN NaN NaN 1.0 1.0 NaN NaN
[919 rows x 919 columns]
[78]: morphs[morphs.isna()] = 0
to_delete = morphs[morphs.sum(axis=1) < 50].index
morphs = morphs.drop(labels=to_delete).drop(labels=to_delete,axis=1)
morphs
[78]: n r ch m d i'r nol f nt i … \
n 140.0 20.0 33.0 16.0 4.0 3.0 10.0 4.0 16.0 4.0 …
r 20.0 100.0 18.0 0.0 3.0 0.0 0.0 0.0 0.0 2.0 …
ch 33.0 18.0 78.0 24.0 1.0 0.0 2.0 7.0 8.0 4.0 …
m 16.0 0.0 24.0 35.0 1.0 0.0 0.0 3.0 8.0 1.0 …
d 4.0 3.0 1.0 1.0 148.0 0.0 0.0 4.0 0.0 0.0 …
i'r 3.0 0.0 0.0 0.0 0.0 20.0 1.0 4.0 4.0 20.0 …
97

---

<!-- page:98 source:datsci-ex08-solution.pdf -->

nol 10.0 0.0 2.0 0.0 0.0 1.0 25.0 1.0 1.0 1.0 …
f 4.0 0.0 7.0 3.0 4.0 4.0 1.0 38.0 5.0 4.0 …
nt 16.0 0.0 8.0 8.0 0.0 4.0 1.0 5.0 21.0 4.0 …
i 4.0 2.0 4.0 1.0 0.0 20.0 1.0 4.0 4.0 68.0 …
l 5.0 2.0 0.0 0.0 3.0 0.0 0.0 0.0 0.0 0.0 …
dd 3.0 0.0 3.0 0.0 2.0 0.0 0.0 1.0 0.0 0.0 …
en 1.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
u 1.0 3.0 2.0 0.0 4.0 0.0 1.0 1.0 0.0 3.0 …
'r 3.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
th 1.0 1.0 0.0 0.0 4.0 0.0 0.0 0.0 0.0 0.0 …
dol 1.0 0.0 0.0 0.0 18.0 0.0 0.0 0.0 0.0 0.0 …
on 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 2.0 …
s 2.0 1.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 …
ol 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 5.0 …
o'r 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 …
o 0.0 1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 6.0 …
ais 0.0 0.0 3.0 0.0 1.0 1.0 0.0 0.0 0.0 3.0 …
ed 0.0 0.0 1.0 0.0 0.0 2.0 0.0 1.0 0.0 2.0 …
io 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 1.0 …
odd 0.0 0.0 0.0 0.0 1.0 3.0 0.0 0.0 0.0 3.0 …
wch 0.0 0.0 0.0 0.0 1.0 1.0 0.0 0.0 0.0 3.0 …
af 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 …
dwch 0.0 0.0 0.0 0.0 10.0 0.0 0.0 0.0 0.0 0.0 …
dodd 0.0 0.0 0.0 0.0 9.0 0.0 0.0 0.0 0.0 0.0 …
diad 0.0 0.0 0.0 0.0 9.0 0.0 0.0 0.0 0.0 0.0 …
dau 0.0 0.0 0.0 0.0 40.0 0.0 0.0 0.0 0.0 0.0 …
di 0.0 0.0 0.0 0.0 11.0 0.0 0.0 0.0 0.0 0.0 …
u'r 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 …
iad 0.0 0.0 0.0 0.0 1.0 1.0 1.0 0.0 0.0 7.0 …
wyr 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 2.0 …
ydd 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 …
wn 0.0 0.0 0.0 0.0 0.0 1.0 0.0 1.0 0.0 1.0 …
ai 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0 …
em 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0 …
ech 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 2.0 …
wr 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 2.0 …
au 0.0 0.0 0.0 0.0 0.0 2.0 0.0 0.0 0.0 3.0 …
ion 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 6.0 …
yn 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 4.0 …
od 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0 1.0 …
a 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 …
och 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 2.0 …
h 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 2.0 …
adau 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 …
ad 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0 …
ent 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
ant 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
98

---

<!-- page:99 source:datsci-ex08-solution.pdf -->

g 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
iwch 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
io'r 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
iau 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 …
di iad adau ad wr o'r ol io'r iau ion
n 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
r 0.0 0.0 0.0 0.0 0.0 1.0 1.0 0.0 0.0 0.0
ch 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
m 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
d 11.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
i'r 0.0 1.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0
nol 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
f 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
nt 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
i 0.0 7.0 1.0 1.0 2.0 1.0 5.0 0.0 0.0 6.0
l 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
dd 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
en 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
u 0.0 15.0 0.0 0.0 6.0 0.0 11.0 0.0 0.0 1.0
'r 0.0 0.0 3.0 2.0 0.0 0.0 1.0 0.0 0.0 0.0
th 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
dol 4.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
on 0.0 0.0 0.0 5.0 1.0 2.0 4.0 0.0 0.0 0.0
s 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
ol 0.0 6.0 1.0 3.0 0.0 2.0 71.0 0.0 0.0 5.0
o'r 0.0 1.0 2.0 5.0 2.0 25.0 2.0 0.0 0.0 0.0
o 0.0 5.0 4.0 17.0 6.0 25.0 11.0 0.0 1.0 1.0
ais 0.0 4.0 0.0 0.0 0.0 2.0 3.0 0.0 0.0 0.0
ed 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
io 0.0 12.0 0.0 0.0 0.0 0.0 0.0 18.0 12.0 3.0
odd 0.0 6.0 1.0 2.0 0.0 2.0 4.0 0.0 0.0 1.0
wch 0.0 8.0 0.0 3.0 5.0 10.0 4.0 0.0 0.0 2.0
af 0.0 1.0 0.0 2.0 0.0 1.0 0.0 0.0 0.0 0.0
dwch 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
dodd 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
diad 2.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
dau 1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
di 19.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
u'r 0.0 2.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0
iad 0.0 61.0 0.0 0.0 1.0 1.0 6.0 4.0 2.0 4.0
wyr 0.0 4.0 0.0 0.0 9.0 0.0 2.0 1.0 1.0 0.0
ydd 0.0 5.0 0.0 0.0 0.0 1.0 4.0 0.0 0.0 0.0
wn 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
ai 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 1.0
em 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
ech 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
99

---

<!-- page:100 source:datsci-ex08-solution.pdf -->

wr 0.0 1.0 0.0 0.0 27.0 2.0 0.0 0.0 0.0 0.0
au 0.0 1.0 0.0 4.0 3.0 2.0 10.0 0.0 0.0 0.0
ion 0.0 4.0 0.0 0.0 0.0 0.0 5.0 1.0 0.0 23.0
yn 0.0 1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0
od 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0
a 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0
och 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
h 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
adau 0.0 0.0 29.0 24.0 0.0 2.0 1.0 0.0 0.0 0.0
ad 0.0 0.0 24.0 54.0 0.0 5.0 3.0 0.0 0.0 0.0
ent 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
ant 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
g 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
iwch 0.0 3.0 0.0 0.0 0.0 0.0 0.0 7.0 3.0 1.0
io'r 0.0 4.0 0.0 0.0 0.0 0.0 0.0 18.0 2.0 1.0
iau 0.0 2.0 0.0 0.0 0.0 0.0 0.0 2.0 19.0 0.0
[57 rows x 57 columns]
e) Apply agglomerative clustering to the resulting symmetric matrix. Since you likely have
very many candidate morphs (919 in my implementations), we will not infer the tree, but
really only use this as a clustering algorithm which can operate on similarity matrices. Set
the distance threshold to 50, and extract the cluster labels inferred for each morph. Print
the sets of morphs which were inferred to likely appear as part of the same paradigm, and
compare your results to some inflection tables you find online (e.g. here). To what extent
does the procedure appear to have extracted relevant patterns?
[79]: morphs_X = morphs.to_numpy()
morphs_clustering = AgglomerativeClustering(distance_threshold=50,␣
,→n_clusters=None)
morphs_clustering_result = morphs_clustering.fit(morphs_X)
[80]: morphs_clustering_result.labels_
[80]: array([23, 17, 15, 24, 13, 0, 0, 22, 0, 12, 21, 16, 10, 7, 0, 0, 11,
1, 0, 14, 1, 19, 2, 0, 18, 2, 8, 2, 11, 11, 11, 6, 11, 0,
20, 0, 0, 10, 10, 10, 10, 0, 3, 0, 0, 0, 10, 0, 9, 5, 5,
10, 10, 0, 4, 4, 4])
[81]: morph_labels_dict = dict()
for morph, label in zip(morphs.index, morphs_clustering_result.labels_):
morph_labels_dict[morph] = {"label": label}
[82]: morph_labels = pd.DataFrame.from_dict(morph_labels_dict, orient="index")
morph_labels
100

---

<!-- page:101 source:datsci-ex08-solution.pdf -->

[82]: label
'r 0
a 10
ad 5
adau 5
af 2
ai 10
ais 2
ant 10
au 3
ch 15
d 13
dau 6
dd 16
di 11
diad 11
dodd 11
dol 11
dwch 11
ech 10
ed 0
em 10
en 10
ent 10
f 22
g 0
h 9
i 12
i'r 0
iad 20
iau 4
io 18
io'r 4
ion 0
iwch 4
l 21
m 24
n 23
nol 0
nt 0
o 19
o'r 1
och 0
od 0
odd 2
ol 14
on 1
101

---

<!-- page:102 source:datsci-ex08-solution.pdf -->

r 17
s 0
th 0
u 7
u'r 0
wch 8
wn 10
wr 0
wyr 0
ydd 0
yn 0
[83]: for index in morph_labels.groupby("label").groups.values():
if len(index) > 1:
print(list(index.array))
["'r", 'ed', 'g', "i'r", 'ion', 'nol', 'nt', 'och', 'od', 's', 'th', "u'r",
'wr', 'wyr', 'ydd', 'yn']
["o'r", 'on']
['af', 'ais', 'odd']
['iau', "io'r", 'iwch']
['ad', 'adau']
['a', 'ai', 'ant', 'ech', 'em', 'en', 'ent', 'wn']
['di', 'diad', 'dodd', 'dol', 'dwch']
Cluster 1 is a mixed bag of some verb endings ( -nt, -och), noun plurals ( -ion, -on) and derivational
suﬀixes ( -wr, -wyr, -ydd), it does not correspond to a single paradigm in any way.
The two segments in Cluster 2 do not appear together in any paradigm.
Cluster 3 contains part of a paradigm, but it combines a 1st person future tense ending ( -af ) with
two past tense endings (1sg -ais and 3sg -odd).
Cluster 4 combines some forms of -io verbs (-io’r and -iwch) with the unrelated plural ending -iau.
Cluster 5 can be seen as paradigmatic, it combines the action noun ending -ad with its plural -adau.
Cluster 6 represents a nearly complete inflection paradigm for the Welsh conditional and future
tense endings.
Cluster 7 groups together various endings which attach to stems ending with -d (incorrect segmen-
tation).
The results are mixed: some clusters did indeed pick up paradigmatic patterns (especially Cluster
3 and Cluster 6), but there are plenty of random or spurious patterns as well. It seems likely that
this type of preprocessing could speed up the process of making sense of a completely unknown
language, but a lot of linguistic expertise and qualitative work would still be necessary to sift the
true patterns from the spurious.
102

---
