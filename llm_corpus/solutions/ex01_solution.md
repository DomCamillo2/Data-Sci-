---
id: "ex01-solution"
title: "Assignment 1 Solution"
kind: "solution"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "assignment_01/datsci-ex01-solution.pdf"
pages: 11
---

# Assignment 1 Solution

> Extracted from `datsci-ex01-solution.pdf` for LLM use. All pages included.

<!-- page:1 source:datsci-ex01-solution.pdf -->

datsci-ex01-solution
May 7, 2026
1 Data Science for Linguists Summer 2026, Assignment 1: Solu-
tion
(originally prepared by Dmitry Sukhotin, checked and slightly modified by Johannes Dellert)
1.1 Task 1: Basic Setup and First Steps
Let’s see the full inventory of Unicode characters occurring in the contents of the given file:
[1]: with open('sq-sample.txt', 'r', encoding='utf-8') as file:
text = file.read()
unique_chars = set(text)
print(f"Unique Unicode characters found: {len(unique_chars)}")
print(unique_chars)
Unique Unicode characters found: 842
{'￿', 'ù', 'B', 'ý', '￿', 'ë', '—', '￿', '￿', '￿', '￿', 'N', 'Þ', '￿', 'â', '￿',
'￿', '￿', 'à', 'Đ', 'ż', '￿', 'U', '￿', '￿', '￿', '￿', '￿', 'Z', '￿', '￿', 'C',
'￿', '￿', '￿', '￿', 'L', 'Ú', '￿', 'ę', '￿', '￿', '￿', '￿', '7', '￿', 'č', '￿',
'￿', 'S', '￿', 'ḥ', '￿', '￿', '￿', '￿', '￿', '−', '￿', '￿', 'ñ', 'ò', '￿', 'Ȅ',
'Ș', '￿', '￿', '￿', 'ḏ', 'd', ' ', '´', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '!',
'￿', '￿', '￿', '￿', '￿', '￿', 'Π', '￿', '￿', '￿', '￿', 'Σ', '6', '￿', '￿', '￿',
'￿', 'ö', '£', '￿', '￿', '￿', '￿', 'Y', '￿', '￿', '￿', 'å', 'ʾ', '￿', '￿', '￿',
'￿', 'ņ', '￿', '￿', 'r', '￿', 'Μ', 'Λ', 'ê', '￿', 'I', 'j', '￿', '￿', '￿', '￿',
'￿', '￿', '¼', '￿', 'ň', '￿', 'û', '￿', '￿', 'Œ', '￿', 'Í', '￿', '￿', '￿', 'ǐ',
'￿', '￿', 'Ḥ', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', 'İ', '￿', 'Ē', '￿',
'￿', '￿', 'u', '￿', '￿', '￿', 'º', '￿', 'k', 'Ï', 'È', 'ď', '￿', '￿', '￿', 'Χ',
'￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '\u2009', '￿', '￿', '￿', '￿', '￿', '￿',
'ð', '￿', '￿', '￿', '￿', '￿', 'ṯ', '￿', '￿', '￿', '￿', '￿', '￿', 'ə', '8', 'ś',
'￿', '￿', '￿ ', '￿', '￿', '￿', 't', '‚', 'ā', '￿', '￿', '￿', 'ˇ', '￿ ', '￿', '￿',
'¥', '￿', '￿', 'Ç', 'ä', '￿', '￿', '￿', '→', '-', '￿', '￿', '￿ ', '￿', '￿', '￿',
'￿', '￿', '￿', '￿', 'É', '￿', '￿', '«', '￿', 'ì', '￿', '￿', '￿', 'Δ', '\uf0b0',
'￿', 'Ø', '￿', 'T', '￿', '*', '￿', '￿ ', '￿ ', '￿', '￿', '￿', 'ô', '￿', '￿', 'ț',
'￿', 'ï', '￿', '3', 'Ä', '￿', '￿', '￿ ', '￿', '￿', '²', '￿', '•', '￿ ', '￿', '⁄',
'￿', '￿', 'A', '￿', 'E', '￿', '￿', 'ğ', '￿', 'ĭ', '￿', '￿', '￿', '￿', 'š', '￿',
'￿', '￿', '￿', '￿', '￿', '́', '￿', '˚', '￿', '￿', '￿', '￿', '￿', '￿', 'ġ', '×',
'￿', 'ķ', '￿', '￿ ', 'Æ', '￿', '￿', 'ṣ', '￿', '￿', 'F', 'y', '￿', '￿', '￿', '￿',
1

---

<!-- page:2 source:datsci-ex01-solution.pdf -->

's', '>', '–', '2', '￿', 'Ł', '￿', 'ą', '￿', 'o', '￿', 'Ā', 'œ', '￿', '￿', '￿',
'￿', '￿', 'Q', '·', '~', '￿', '￿', '￿', '￿', '»', '￿', '￿', '￿', '￿', 'R', '￿',
'￿', '￿', '￿', '￿', '￿', '“', 'ÿ', '￿', '￿', '￿', 'æ', '￿', 'Ṣ', '￿', '￿', '\n',
')', '￿', 'ů', 'h', '(', '￿', '4', '￿', '￿', '￿', '￿', '￿', 'w', '+', '￿', '￿',
'¤', '￿', 'ž', '￿ ', 'î', '￿', '￿', '￿', 'g', 'ș', '￿', '￿', "'", '￿', '￿', 'ĝ',
'￿', 'ō', '￿', ':', '￿', '￿', '￿', 'ú', '￿', '￿', '￿', '￿', 'ṇ', '￿', 'm', 'G',
'Ε', '￿', '￿', 'ó', '￿', '￿', '￿', 'ş', '￿', '…', '￿', '￿', '°', '<', '￿', '￿',
'￿', 'v', '￿', 'O', 'ė', '￿', 'p', '￿', '￿', 'ř', '￿', '9', '￿', '￿', 'Φ', '‖',
'a', 'Κ', '￿', '￿', 'ı', '￿', '￿', '￿', 'ć', 'Γ', '￿', '￿', '￿', '￿', '￿', '￿',
'￿', '`', '￿', '￿', '￿', '￿', 'ł', '￿', 'Č', '￿', '±', 'z', '￿', '￿', 'X', '￿',
'￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '†', '￿', '"', 'P', '￿', '￿', '\u200e',
'ī', '￿', '￿', '￿', 'ạ', '￿', '￿', '￿', '￿', '￿', '￿', 'Ş', '‐', '￿', '￿', 'ḫ',
'￿', '№', 'Á', '￿', 'ṅ', '￿', '￿', '￿', '￿', '￿', 'õ', 'á', 'Ö', '￿', '￿', '5',
'￿', 'Ρ', '￿', 'ḱ', '￿', '￿', '￿', '￿', '￿', 'M', '￿', '￿', '½', '0', '￿', '￿',
'Ω', '￿', 'V', 'ź', '￿', '¢', '￿', 'c', '￿', '￿', '￿', '￿', '￿', '￿', 'ü', '￿',
'￿', '￿', '￿', '￿', 'Ħ', '￿', 'K', '&', '￿', '￿', '￿', '\u200b', '￿', '￿', 'þ',
'￿', '￿', '￿', '￿', '￿ ', '￿', '￿', 'Å', 'ű', '￿', '￿', '￿', '￿', '￿', '￿', '￿ ',
'￿', 'Ś', '￿', 'đ', '￿', 'Ü', '￿', '￿', '￿', 'Ż', 'Ć', '￿', '³', 'ø', '￿', '￿',
'￿', '￿', '￿', '￿', '￿', '￿', '￿', 'µ', '￿', 'Š', '„', '￿', '￿', ',', '￿', '￿',
'￿', '$', '￿', '￿', '￿', '￿', 'ţ', '￿', '￿', '￿', '￿', 'Β', 'Ō', ';', '￿', '￿',
'¬', '￿', '.', 'i', '￿', '￿', '￿', 'í', 'Ζ', '￿', '￿', '￿', '￿', '￿', 'n', '￿',
'￿ ', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', 'W',
'ư', 'f', 'Τ', '￿', 'H', 'ƒ', '￿', '￿', '￿', '€', '￿', '￿', '/', '￿', '￿', '￿',
'￿', 'ő', '￿', '￿', 'ợ', 'Α', '￿', '￿', 'ē', '￿', '￿', '￿', '￿', '￿', '￿', 'ȳ',
'￿', '￿', '￿', '￿', '￿', '￿', '￿', 'Ή', 'ʿ', '￿', 'q', '%', '￿', 'è', '￿', '￿',
'￿', '￿', 'Ž', '￿', '￿', 'b', '￿', '￿', 'Θ', 'ấ', '￿', 'Ẓ', 'ṃ', '￿', '￿', '￿',
'￿', '￿', 'ŷ', 'Ë', '￿', '￿', '￿', '￿', 'Ι', '￿', '￿', '’', 'é', '￿', '￿', '￿',
'‰', '￿', 'ß', '￿', 'ç', '1', 'Ν', '?', '￿', '￿', 'ṭ', '¾', '￿', '￿', '￿', 'ū',
'￿', '￿', 'Ḫ', '￿', 'l', 'D', '￿', '￿', '§', '‑', '￿', '￿', 'Ţ', '￿', 'ě', '￿ ',
'ń', '￿', '￿', '￿', '￿', '￿', '‘', 'Ά', 'x', '￿', '￿', '￿', '￿', '￿', '￿', '￿',
'￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', '￿', 'ǔ', 'ċ', 'ã', 'Î', 'ă',
'￿', '￿', 'ḍ', 'e', '￿', '￿', '￿', 'ầ', '”', '￿', '￿', '￿', 'J', '￿'}
There is a surprising variety of scripts represented, which might be unexpected, but is perfectly
normal for a large corpus that was not manually curated.
Now let’s a create a “positive filter” for purely Albanian words with a function is_albanian
[2]: import random
from collections import Counter, defaultdict
[3]: def is_albanian(token):
# For simplicity we'll use the lowercase letters
albanian_chars = set('abcçdefëghijklmnopqrstuvxyz')
# Then we'll have to convert the input token
token_lower = token.lower()
2

---

<!-- page:3 source:datsci-ex01-solution.pdf -->

# Check if all characters in the token are in the Albanian alphabet
for char in token_lower:
if char not in albanian_chars:
return False
return True
test_words = ["mirë", "hello", "çfarë", "albanian123", "shqipëri", "café"]
for word in test_words:
print(f"{word}: {'Albanian' if is_albanian(word) else 'Not Albanian'}")
mirë: Albanian
hello: Albanian
çfarë: Albanian
albanian123: Not Albanian
shqipëri: Albanian
café: Not Albanian
1.2 Task 2: Loading and Preprocessing Corpus Data
[4]: with open('sq-sample.txt', 'r', encoding='utf-8') as file:
content = file.read()
sentences = content.split('\n')
sentences = [s for s in sentences if s.strip()]
Let’s take a look at the first few sentences.
[5]: sentences[:5]
[5]: ['; 01 maj 1999 në Ferizaj).',
'"(16) Ai tha:" Ashtu si ti më la mua për të shkuar në humbje, unë do të rri në
pritë për ta në rrugën tënde të drejtë "(17)" Atëherë unë nga para dhe prapa të
drejtën e saj dhe atë e lanë.',
'«1913 Idriz Seferi u prin edhe një herë kryengritsvë shqiptarë në Grykë të
Kaçanikut kësaj here kundër pushtuesit serb, me kryengritësit në hyrje të
Ferizajit.»',
'``) 1.Fermi u pyet se pse nuk ka prova në formën e hetimeve apo radio valë në
anije,nëse Rruga e Qumështit ka shumë qytetërime të përparuara jashtëtokësore.',
'•2005-Çmimi i parë për pikturë (']
This still seems quite noisy. Let’ continue by removing the punctuation and other symbols we are
not interested in, shuffling the sentences first.
[6]: random.shuffle(sentences)
punctuation_chars = '.,()[]{}:;!?"\'0123456789'
3

---

<!-- page:4 source:datsci-ex01-solution.pdf -->

all_tokens = []
for sentence in sentences:
tokens = sentence.split()
for token in tokens:
token = token.lower()
cleaned_token = ''
for char in token:
if char not in punctuation_chars:
cleaned_token += char
if cleaned_token:
all_tokens.append(cleaned_token)
albanian_tokens = [token for token in all_tokens if is_albanian(token)]
print(f"Total tokens: {len(all_tokens)}")
print(f"Albanian tokens: {len(albanian_tokens)}")
print(f"Sample of first 10 Albanian tokens: {albanian_tokens[:10]}")
Total tokens: 1875029
Albanian tokens: 1837988
Sample of first 10 Albanian tokens: ['bojan', 'vrucina', 'sulmuesi', 'kroat',
'që', 'tani', 'luan', 'për', 'kf', 'shkëndija']
As stated in the assignment, any result between 1.5 million and 2 million Albanian tokens is
acceptable here, results can differ quie a lot depending on how much effort you chose to invest into
the filtering efforts.
1.3 Task 3: Populating Data Structures
1.4 (a) Separating into subcorpora and creating frequency counters
[7]: # We'll split the corpus in exactly equal chunks here, because the sentences ␣
,→are shuffled anyway
midpoint = len(albanian_tokens) // 2
subcorpus1 = albanian_tokens[:midpoint]
subcorpus2 = albanian_tokens[midpoint:]
counter1 = Counter(subcorpus1)
counter2 = Counter(subcorpus2)
print("Top 50 words in subcorpus 1:")
for word, freq in counter1.most_common(50):
print(f"{word}: {freq}")
4

---

<!-- page:5 source:datsci-ex01-solution.pdf -->

print("\nTop 50 words in subcorpus 2:")
for word, freq in counter2.most_common(50):
print(f"{word}: {freq}")
common_words1 = set([word for word, _ in counter1.most_common(50)])
common_words2 = set([word for word, _ in counter2.most_common(50)])
overlap = common_words1.intersection(common_words2)
print(f"\nOverlap between top 50 words in both subcorpora: {len(overlap)}␣
,→words")
print(f"Words in subcorpus 1 but not in subcorpus 2: {common_words1 -␣
,→common_words2}")
print(f"Words in subcorpus 2 but not in subcorpus 1: {common_words2 -␣
,→common_words1}")
Top 50 words in subcorpus 1:
të: 58750
e: 49182
në: 40529
dhe: 26227
i: 22495
një: 16847
me: 15094
për: 12796
nga: 12384
që: 9415
është: 9233
më: 9003
u: 8060
si: 6632
ka: 6130
së: 5493
tij: 4833
se: 4714
ai: 4348
ishte: 3945
te: 3894
edhe: 3823
nuk: 3433
duke: 3361
janë: 3310
shumë: 2919
vitin: 2752
prej: 2578
pas: 2472
por: 2325
ne: 2289
5

---

<!-- page:6 source:datsci-ex01-solution.pdf -->

do: 2164
mund: 2151
saj: 2131
tyre: 2112
ajo: 2045
gjatë: 2032
parë: 1970
këtë: 1778
disa: 1766
dy: 1763
ose: 1760
deri: 1624
ku: 1610
kjo: 1608
kishte: 1550
kur: 1533
kanë: 1464
atë: 1387
gjithashtu: 1319
Top 50 words in subcorpus 2:
të: 58228
e: 49059
në: 40954
dhe: 26222
i: 21902
një: 16949
me: 15099
për: 12915
nga: 12646
që: 9298
është: 9155
më: 8753
u: 8087
si: 6589
ka: 6115
së: 5560
tij: 4814
se: 4742
ai: 4249
ishte: 3867
te: 3787
edhe: 3783
nuk: 3486
duke: 3461
janë: 3306
shumë: 2924
vitin: 2853
6

---

<!-- page:7 source:datsci-ex01-solution.pdf -->

prej: 2598
pas: 2454
do: 2330
por: 2291
ne: 2258
tyre: 2146
mund: 2102
ajo: 2066
saj: 2051
parë: 1937
gjatë: 1861
këtë: 1806
disa: 1781
ose: 1774
dy: 1738
kjo: 1660
deri: 1637
ku: 1587
kishte: 1537
kanë: 1511
kur: 1473
vetëm: 1298
atë: 1285
Overlap between top 50 words in both subcorpora: 49 words
Words in subcorpus 1 but not in subcorpus 2: {'gjithashtu'}
Words in subcorpus 2 but not in subcorpus 1: {'vetëm'}
Is there any difference between subcorpora?
The top-50 lists extracted from the two subcorpora appear to be almost identical, with just one
word difference.
1.5 (b) Creating quantiles based on token frequencies
[8]: list(counter1.values())[:10]
[8]: [1, 1, 11, 13, 9415, 340, 91, 12796, 21, 9]
[9]: list(counter2.values())[:10]
[9]: [322, 9155, 21902, 813, 3783, 15099, 421, 1, 9, 12915]
[10]: def create_frequency_quantiles(token_counter, k=10):
total_tokens = sum(token_counter.values())
quantiles = defaultdict(set)
cumulative_prob = 0
7

---

<!-- page:8 source:datsci-ex01-solution.pdf -->

current_quantile = 1
quantile_threshold = 1 / k
for token, count in token_counter.most_common():
token_prob = count / total_tokens
cumulative_prob += token_prob
quantiles[current_quantile].add(token)
while cumulative_prob > current_quantile * quantile_threshold and␣
,→current_quantile < k:
current_quantile += 1
return quantiles
deciles1 = create_frequency_quantiles(counter1, k=10)
deciles2 = create_frequency_quantiles(counter2, k=10)
print("Number of tokens in each decile for subcorpus 1:")
for decile, tokens in deciles1.items():
print(f"Decile {decile}: {len(tokens)} tokens")
print("\nNumber of tokens in each decile for subcorpus 2:")
for decile, tokens in deciles2.items():
print(f"Decile {decile}: {len(tokens)} tokens")
Number of tokens in each decile for subcorpus 1:
Decile 1: 2 tokens
Decile 2: 3 tokens
Decile 3: 7 tokens
Decile 4: 23 tokens
Decile 5: 116 tokens
Decile 6: 502 tokens
Decile 7: 1518 tokens
Decile 8: 4135 tokens
Decile 9: 13997 tokens
Decile 10: 69044 tokens
Number of tokens in each decile for subcorpus 2:
Decile 1: 2 tokens
Decile 2: 3 tokens
Decile 3: 7 tokens
Decile 4: 24 tokens
Decile 5: 116 tokens
Decile 6: 501 tokens
Decile 7: 1523 tokens
Decile 8: 4102 tokens
8

---

<!-- page:9 source:datsci-ex01-solution.pdf -->

Decile 9: 14122 tokens
Decile 10: 68822 tokens
1.6 Task 4: Answering Questions about the Data
1.7 (a) Analyzing overlap between quantiles
[11]: print("Overlap sizes between deciles of subcorpus 1 and subcorpus 2:")
print("=" * 70)
print(f"{'Decile':^10} | {'Size in S1':^12} | {'Size in S2':^12} | {'Overlap':
,→^12} | {'% Overlap':^12}")
print("-" * 70)
cumulative_s1 = set()
cumulative_s2 = set()
coverage_levels = [0.2, 0.5, 0.7, 0.8, 0.9] # 20%, 50%, 70%, 80%, 90%
sizes_needed = {}
for decile in range(1, 11):
tokens_s1 = deciles1[decile]
tokens_s2 = deciles2[decile]
cumulative_s1.update(tokens_s1)
cumulative_s2.update(tokens_s2)
overlap = tokens_s1.intersection(tokens_s2)
overlap_percent = len(overlap) / max(len(tokens_s1), len(tokens_s2)) * 100␣
,→if max(len(tokens_s1), len(tokens_s2)) > 0 else 0
print(f"{decile:^10} | {len(tokens_s1):^12} | {len(tokens_s2):^12} |␣
,→{len(overlap):^12} | {overlap_percent:.2f}%")
for level in coverage_levels[:]:
if decile / 10 >= level:
unique_forms = cumulative_s1.union(cumulative_s2)
sizes_needed[level] = len(unique_forms)
coverage_levels.remove(level)
print("=" * 70)
print("\nNumber of forms needed for different coverage levels:")
for level, size in sizes_needed.items():
print(f"{level*100:.0f}% c overage: {size} forms")
Overlap sizes between deciles of subcorpus 1 and subcorpus 2:
======================================================================
9

---

<!-- page:10 source:datsci-ex01-solution.pdf -->

Decile | Size in S1 | Size in S2 | Overlap | % Overlap
----------------------------------------------------------------------
1 | 2 | 2 | 2 | 100.00%
2 | 3 | 3 | 3 | 100.00%
3 | 7 | 7 | 7 | 100.00%
4 | 23 | 24 | 23 | 95.83%
5 | 116 | 116 | 111 | 95.69%
6 | 502 | 501 | 458 | 91.24%
7 | 1518 | 1523 | 1240 | 81.42%
8 | 4135 | 4102 | 2981 | 72.09%
9 | 13997 | 14122 | 8375 | 59.30%
10 | 69044 | 68822 | 22073 | 31.97%
======================================================================
Number of forms needed for different coverage levels:
20% coverage: 5 forms
50% coverage: 156 forms
70% coverage: 2415 forms
80% coverage: 7188 forms
90% coverage: 25169 forms
Note the rapidly decreasing overlap at the upper deciles. This shows that the extracting a top-100
or top-500 list can be expected to always yield similar results, but estimating meaningful frequency
differences among less common words is much more diﬀicult (and would likely require a much larger
corpus).
1.8 (b) CEFR Level Analysis
[12]: cefr_levels = {
"A1": 625,
"A2": 1250,
"B1": 2500,
"B2": 5000
}
combined_counter = counter1 + counter2
total_tokens = sum(combined_counter.values())
print("\nCoverage with CEFR vocabulary sizes:")
print("-" * 40)
print(f"{'CEFR Level':^10} | {'Vocab Size':^10} | {'Coverage':^10}")
print("-" * 40)
for level, vocab_size in cefr_levels.items():
top_words = [word for word, _ in combined_counter.most_common(vocab_size)]
covered_tokens = sum(combined_counter[word] for word in top_words)
coverage = covered_tokens / total_tokens * 100
10

---

<!-- page:11 source:datsci-ex01-solution.pdf -->

print(f"{level:^10} | {vocab_size:^10} | {coverage:.2f}%")
print("-" * 40)
Coverage with CEFR vocabulary sizes:
----------------------------------------
CEFR Level | Vocab Size | Coverage
----------------------------------------
A1 | 625 | 59.65%
A2 | 1250 | 65.15%
B1 | 2500 | 71.21%
B2 | 5000 | 77.72%
----------------------------------------
The results look realistic, but is also shows a problem with this simple approach to frequency list.
Since we used word forms instead of lemmas, the coverage looks much lower than would be expected
at the respective CEFR levels. We would have to lemmatise our corpus first in order to get numbers
which better approximate the real situation.
1.9 Task 5: Submission
If you managed to export your solution into a PDF, leaving the outputs available for inspection,
and uploaded your solution as a single PDF as required, that is already suﬀicient to receive the
point for this task.
11

---
