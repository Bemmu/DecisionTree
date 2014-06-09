DecisionTree
============

This is a work in progress study project. The aim is for me to learn how to generate decision trees from training data in Python.

The program takes as input a list of cases. Each list item can represent multiple
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

