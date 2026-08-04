---
id: "ex07-solution"
title: "Assignment 7 Solution"
kind: "solution"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "assignment_07/datsci-ex07-solution.pdf"
pages: 12
---

# Assignment 7 Solution

> Extracted from `datsci-ex07-solution.pdf` for LLM use. All pages included.

<!-- page:1 source:datsci-ex07-solution.pdf -->

datsci-ex07-solution
July 9, 2026
1 Data Science for Linguists Summer 2026: Assignment 7
[255]: import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set()
1.1 Task 1: Preparing the Data
[256]: grambank = pd.read_table("grambank.csv", sep =",")
grambank.head()
[256]: Language GB020 GB021 GB022 GB023 GB024 GB025 GB026 \
0 'Are'are present absent absent present Num-N N-Dem absent
1 A'ou present absent present absent Num-N N-Dem absent
2 Abadi NaN NaN NaN NaN N-Num Dem-N absent
3 Abau absent absent absent absent N-Num N-Dem absent
4 Abenlen Ayta absent absent absent absent Num-N Dem-N NaN
GB027 GB028 … GB422 GB430 GB431 GB432 GB433 GB519 \
0 present present … absent absent absent absent present present
1 absent absent … NaN absent absent absent absent present
2 absent present … NaN absent absent absent present NaN
3 present absent … NaN NaN NaN NaN NaN NaN
4 NaN present … NaN NaN NaN NaN NaN present
GB520 GB521 GB522 Macroarea
0 present absent absent Papunesia
1 present absent present Eurasia
2 NaN NaN present Papunesia
3 NaN NaN NaN Papunesia
4 present NaN NaN Papunesia
[5 rows x 197 columns]
1

---

<!-- page:2 source:datsci-ex07-solution.pdf -->

b) Generate a binarised version of the dataset using pandas.get_dummies(). Do not change the
drop_first or dummy_na arguments from their defaults, the intended behavior is that there
are separate columns for the presence and absence of each binary feature, and a missing value
should be indicated by a zero in both columns.
[257]: grambank_binary = pd.get_dummies(grambank, columns =grambank.columns[1:-1])
grambank_binary
[257]: Language Macroarea GB020_absent GB020_present GB021_absent \
0 'Are'are Papunesia 0 1 1
1 A'ou Eurasia 0 1 1
2 Abadi Papunesia 0 0 0
3 Abau Papunesia 1 0 1
4 Abenlen Ayta Papunesia 1 0 1
… … … … … …
2458 Zuni North America 0 1 1
2459 Záparo South America 0 0 0
2460 Äiwoo Papunesia 1 0 1
2461 Ömie Papunesia 0 1 1
2462 Önge Eurasia 0 0 0
GB021_present GB022_absent GB022_present GB023_absent GB023_present \
0 0 1 0 0 1
1 0 0 1 1 0
2 0 0 0 0 0
3 0 1 0 1 0
4 0 1 0 1 0
… … … … … …
2458 0 1 0 1 0
2459 1 0 0 0 0
2460 0 1 0 1 0
2461 0 1 0 0 1
2462 0 1 0 0 0
… GB433_absent GB433_present GB519_absent GB519_present \
0 … 0 1 0 1
1 … 1 0 0 1
2 … 0 1 0 0
3 … 0 0 0 0
4 … 0 0 0 1
… … … … … …
2458 … 1 0 1 0
2459 … 1 0 1 0
2460 … 0 1 1 0
2461 … 1 0 1 0
2462 … 0 0 0 0
2

---

<!-- page:3 source:datsci-ex07-solution.pdf -->

GB520_absent GB520_present GB521_absent GB521_present GB522_absent \
0 0 1 1 0 1
1 0 1 1 0 0
2 0 0 0 0 0
3 0 0 0 0 0
4 0 1 0 0 0
… … … … … …
2458 0 1 1 0 0
2459 1 0 1 0 1
2460 1 0 1 0 0
2461 1 0 1 0 0
2462 0 0 0 0 0
GB522_present
0 0
1 1
2 1
3 0
4 0
… …
2458 0
2459 0
2460 0
2461 1
2462 0
[2463 rows x 400 columns]
c) Prepare the feature matrix X and the label vector y in formats that the Scikit-Learn
classifiers will handle. This involves casting the NumPy array to integers (the de-
fault uint8 will not work!), and converting the labels into an array of strings (not ob-
jects!) which can then be converted to the integer IDs that will be needed (Hint: use
sklearn.preprocessing.LabelEncoder).
[258]: X = grambank_binary[grambank_binary.columns[2:]].to_numpy(dtype=int)
X
[258]: array([[0, 1, 1, …, 0, 1, 0],
[0, 1, 1, …, 0, 0, 1],
[0, 0, 0, …, 0, 0, 1],
…,
[1, 0, 1, …, 0, 0, 0],
[0, 1, 1, …, 0, 0, 1],
[0, 0, 0, …, 0, 0, 0]])
[259]: np.isfinite(X).all()
3

---

<!-- page:4 source:datsci-ex07-solution.pdf -->

[259]: True
[260]: grambank["Macroarea"].isna().any()
[260]: False
[261]: from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = grambank["Macroarea"].to_numpy(dtype="str")
y
[261]: array(['Papunesia', 'Eurasia', 'Papunesia', …, 'Papunesia', 'Papunesia',
'Eurasia'], dtype='<U13')
[262]: y = label_encoder.fit_transform(y)
y
[262]: array([4, 2, 4, …, 4, 4, 2])
d) Prepare train and test splits by randomly selecting 80% of languages as training data and
20% as test data.
[263]: from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2)
1.2 Task 2: Exploring the Data with a Decision Tree
a) Fit a decision tree classifier with the default settings, and use the decision tree that you have
trained in this way in order to predict the labels on the test data.
[264]: from sklearn.tree import DecisionTreeClassifier
decision_tree = DecisionTreeClassifier().fit(X_train, y_train)
[265]: decision_tree_predictions = decision_tree.predict(X_test)
b) Use sklearn.metrics.zero_one_loss in order to compute the accuracy of the predictions
(Hint: make sure you understand the connection of the function to accuracy!). How well does
your single decision tree work? Are you happy with the performance? Can you show what is
going on?
[266]: from sklearn.metrics import zero_one_loss
[267]: decision_tree_accuracy = 1 - zero_one_loss(y_test, decision_tree_predictions)
decision_tree_accuracy
[267]: 0.6328600405679513
4

---

<!-- page:5 source:datsci-ex07-solution.pdf -->

Our suspicion about the cause of the somewhat disappointing accuracy is that we might have run
into the overfitting problem that is so typical of (single) decision trees. Let’s substantiate this by
comparing the performance on the training data:
[268]: 1 - zero_one_loss(y_train, decision_tree.predict(X_train))
[268]: 1.0
Apparently, with the default settings, the tree was flexible enough to perfectly learn the training
data, which is the worst imaginable kind of overfitting.
c) How many nodes does your decision tree have, and what are the three most important features
in the decision tree? Use the Grambank webpage to find out what these three variables are
about.
[269]: decision_tree.get_depth()
[269]: 18
To find the most important features, we retrieve the indices of the features which were placed last
in an ascending sort of the feature importances:
[270]: top_three_indices = np.argsort(decision_tree.feature_importances_)[-3:]
top_three_indices
[270]: array([ 40, 142, 37])
Since the features started in column 3 of our dataframe, we can retrieve the corresponding feature
names from the column index like this:
[271]: grambank_binary.columns[top_three_indices + 2]
[271]: Index(['GB044_absent', 'GB117_present', 'GB042_present'], dtype='object')
According to the Grambank website, * GB042 is about the existence of productive overt morpholog-
ical singular marking on nouns * GB044 is about the existence of productive morphological plural
markers on nouns * GB117 is about the existence of a copula for predicate nominals
As a very preliminary analysis, it seems that number marking on nouns and the copula construction
are key hints in deciding where to place a language (from the training data - as we just found out,
we should not overinterpret this). Obviously, this is where real investigations about the distinctive
grammatical profile of each macroarea would only just start.
1.3 Task 3: A Random Forest Classifier
a) Fit a random forest classifier with 100 estimators to the training data (using the default
settings of all other parameters), and compute the predictions on the test data.
[272]: from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100, random_state =0)
random_forest.fit(X_train,y_train)
5

---

<!-- page:6 source:datsci-ex07-solution.pdf -->

[272]: RandomForestClassifier(random_state=0)
b) Compute the accuracy again, and compare it to the accuracy of the decision tree you inferred
in the previous task. Do you have any idea what might cause the difference you are observing?
[273]: random_forest_predictions = random_forest.predict(X_test)
[274]: random_forest_accuracy = 1 - zero_one_loss(y_test, random_forest_predictions)
random_forest_accuracy
[274]: 0.8356997971602435
This is obviously much better, it seems that rather good performance can be achieved for this
six-way classification problem. It seems that as expected, the problem of overfitting was overcome
by this ensemble method.
d) In order to understand which language areas show grammatical profiles that are too diﬀicult
to differentiate, we can take a look at the confusion matrix. Create and visualise the confusion
matrix based on the code from the slides about the multinomial Naive Bayes example, but
use the normalize argument of the confusion matrix method to normalise the entries with
respect to the true labels. Inspecting the results, which pairs of macroareas appear to be the
hardest to distinguish?
[275]: from sklearn.metrics import confusion_matrix
[276]: random_forest_mat = confusion_matrix(y_test, random_forest_predictions, ␣
,→normalize="true")
sns.heatmap(random_forest_mat.T, square =True, annot =True, cbar =False, \
xticklabels=label_encoder.classes_, yticklabels =label_encoder.
,→classes_, cmap ="Blues")
plt.xlabel('true label ')
plt.ylabel('predicted label ')
[276]: Text(89.18, 0.5, 'predicted label')
6

---

<!-- page:7 source:datsci-ex07-solution.pdf -->

Apparently, Australian and Papunesian languages are the most diﬀicult to reliably distinguish based
on grammatical features, but Papunesia also shows some confusability with North America, and
South America has similarities to both Papunesia and Eurasia.
1.4 Task 4: Support Vector Machine
a) Fit a linear Support Vector Machine to the same dataset, using the recommended seting for
the fudge factor. How does performance compare with the previous two approaches?
[277]: from sklearn.svm import SVC
svc = SVC(kernel='linear', C =1E10)
svc.fit(X_train, y_train)
[277]: SVC(C=10000000000.0, kernel='linear')
[278]: svc_predictions = svc.predict(X_test)
[279]: svc_accuracy = 1 - zero_one_loss(y_test, svc_predictions)
svc_accuracy
7

---

<!-- page:8 source:datsci-ex07-solution.pdf -->

[279]: 0.8600405679513184
This is even a bit better than the random forest model.
b) Try out what happens with the default RBF kernel. Does performance improve any further?
[285]: rbf_svc = SVC(kernel='rbf', C =1E10)
rbf_svc.fit(X_train, y_train)
[285]: SVC(C=10000000000.0)
[286]: rbf_svc_predictions = rbf_svc.predict(X_test)
[288]: rbf_svc_accuracy = 1 - zero_one_loss(y_test, rbf_svc_predictions)
rbf_svc_accuracy
[288]: 0.9107505070993914
The result is an even better model, so introducing some (limited) non-linearity has made it easier
to draw decision boundaries between the macroareas.
c) Create the truth-normalised confusion matrix for the SVC with the RBF kernel. Are the
most confusable pairs of macroareas similar? Do these considerations lead to any idea about
how we could improve performance further?
[290]: rbf_svc_mat = confusion_matrix(y_test, rbf_svc_predictions, normalize ="true")
sns.heatmap(rbf_svc_mat.T, square =True, annot =True, cbar =False, \
xticklabels=label_encoder.classes_, yticklabels =label_encoder.
,→classes_, cmap ="Blues")
plt.xlabel('true label ')
plt.ylabel('predicted label ')
[290]: Text(89.18, 0.5, 'predicted label')
8

---

<!-- page:9 source:datsci-ex07-solution.pdf -->

Yes, provided the overall improved performance, the problematic pairs remain the same.
1.5 Task 5: k-Neighbour Clustering
a) Fit a k-neighbours classifier to the same dataset. Which metric does it use by default, and
how is it different from the Euclidean distance?
[291]: from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier()
neigh.fit(X_train, y_train)
[291]: KNeighborsClassifier()
b) Compute the accuracy in the usual way. How does k-neighbour clustering perform compared
to the previous models?
[292]: neigh_predictions = neigh.predict(X_test)
[293]: neigh_accuracy = 1 - zero_one_loss(y_test, neigh_predictions)
neigh_accuracy
9

---

<!-- page:10 source:datsci-ex07-solution.pdf -->

[293]: 0.8438133874239351
Even a simple k-neighbors classifier appears to perform about as well as the random forest. Since
this is a high-dimensional problem, we would have expected performance to be less convincing, but
this seems to generally be a very good-natured problem.
c) Experiment with different numbers of neighbours to take into account. What do you observe?
What appears to be a good range for this problem?
[294]: for k in range(2,50):
neigh_variant = KNeighborsClassifier(n_neighbors=k)
neigh_variant.fit(X_train, y_train)
neigh_variant_predictions = neigh_variant.predict(X_test)
neigh_variant_accuracy = 1 - zero_one_loss(y_test,␣
,→neigh_variant_predictions)
print(str(k) + "\t" + str(neigh_variant_accuracy))
2 0.8336713995943205
3 0.8316430020283976
4 0.8397565922920892
5 0.8438133874239351
6 0.847870182555781
7 0.8417849898580122
8 0.8316430020283976
9 0.8417849898580122
10 0.8417849898580122
11 0.8356997971602435
12 0.8377281947261663
13 0.8377281947261663
14 0.8296146044624746
15 0.821501014198783
16 0.8235294117647058
17 0.8133874239350912
18 0.8154158215010142
19 0.8133874239350912
20 0.8073022312373225
21 0.8113590263691683
22 0.8093306288032455
23 0.8093306288032455
24 0.8113590263691683
25 0.8052738336713996
26 0.8174442190669371
27 0.8032454361054767
28 0.8113590263691683
29 0.7991886409736308
30 0.8052738336713996
31 0.8032454361054767
32 0.8052738336713996
10

---

<!-- page:11 source:datsci-ex07-solution.pdf -->

33 0.8032454361054767
34 0.8073022312373225
35 0.8093306288032455
36 0.8052738336713996
37 0.795131845841785
38 0.8032454361054767
39 0.795131845841785
40 0.795131845841785
41 0.7971602434077079
42 0.7971602434077079
43 0.7971602434077079
44 0.7931034482758621
45 0.7870182555780934
46 0.7829614604462475
47 0.7768762677484787
48 0.7789046653144016
49 0.7626774847870182
Performance is overall quite robust with respect to different numbers of neighbours, but it falls off
somewhat for large numbers of neighbors. The best strategy appears to be to make the decision
based on the 5 to 10 closest neighbours.
d) Create the truth-normalised confusion matrix for your choice ofn_neighbors. Do you notice
anything different to the previous two confusion matrices?
[297]: neigh = KNeighborsClassifier(n_neighbors=6)
neigh.fit(X_train, y_train)
neigh_predictions = neigh.predict(X_test)
[298]: neigh_mat = confusion_matrix(y_test, neigh_predictions, normalize ="true")
sns.heatmap(neigh_mat.T, square =True, annot =True, cbar =False, \
xticklabels=label_encoder.classes_, yticklabels =label_encoder.
,→classes_, cmap ="Blues")
plt.xlabel('true label ')
plt.ylabel('predicted label ')
[298]: Text(89.18, 0.5, 'predicted label')
11

---

<!-- page:12 source:datsci-ex07-solution.pdf -->

This leads to a quite different picture from the previous two confusion matrices. The problematic
cases are clustered much less on certain pairs of macroareas, except that the number of perfectly
separable macroareas (0 entries) has decreased somewhat.
12

---
