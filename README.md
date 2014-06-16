DecisionTree
============

This is a work in progress study project related to the University of Tampere course 'Knowledge Discovery'.
The aim of this project is for me to learn how to generate decision trees from training data in Python.

# Input

The program takes as input a list of case data. Each list item can represent multiple
training cases that all have the same attributes.

	S = [
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':3, 'BPV':0}},
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':59, 'BPV':0}},
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':1, 'BPV':55}},
	{'Hearing loss':'No', 'Injury':'Yes', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':21, 'BPV':1}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':63, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':28, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':234, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'Yes', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':1, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'Yes', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':30, 'BPV':0}}
	]

The above is an example of possible input. For instance the first item in the list means that there are three training cases
classified as 'not-BPM', all having the attributes 'Hearing loss' = 'No', 'Injury' = 'No' and 'Frequency of vertigo attacks' = 0.

# Output

The program produces a text visualization that shows the resulting tree.

# What the program does

## Equations

The function "H(S)" in the python code implements the equation
![Expected information needed to classify an arbitrary case in S](img/hc.png)