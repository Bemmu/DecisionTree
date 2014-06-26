from equations import *

training_set = [
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':3, 'BPV':0}},
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':59, 'BPV':0}},
	{'Hearing loss':'No', 'Injury':'No', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':1, 'BPV':55}},
	{'Hearing loss':'No', 'Injury':'Yes', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':21, 'BPV':1}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':63, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':28, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'No', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':234, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'Yes', 'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':1, 'BPV':0}},
	{'Hearing loss':'Yes', 'Injury':'Yes', 'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':30, 'BPV':0}},
]

def find_best_attribute_to_split_on(training_set):
	best_attr = None
	best_gain = None
	for attr in [key for key in training_set[0].keys() if key != 'classes']:
		information_gain = I(training_set, attr)
		if best_gain is None or information_gain > best_gain:
			best_gain = information_gain
			best_attr = attr
	return best_attr

print "Should split on attribute %s" % find_best_attribute_to_split_on(training_set)

