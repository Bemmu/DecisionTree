from equations import *
from texttree import TextTree

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
	"""Which attribute has the highest information gain?"""
	best_attr = None
	best_gain = None
	for attr in [key for key in training_set[0].keys() if key != 'classes']:
		information_gain = I(training_set, attr)
		if best_gain is None or information_gain > best_gain:
			best_gain = information_gain
			best_attr = attr
	return best_attr

def unique_values(training_set, attribute):
	"""Return all the different values that the given attribute has in the given training data"""
	values = [x[attribute] for x in training_set]
	return dict([(a, '') for a in values]).keys()

def branch_on_attribute(training_set, attr, value):

	# Only include cases where attribute has the given value
	training_set = [c for c in training_set if c[attr] == value]

	# Remove the attribute from the cases
	training_set = [dict([(a,v) for a,v in x.items() if a != attr]) for x in training_set]

	return training_set

def make_decision_tree(training_set):
	# The tree is the attribute to split on and subtrees have the different values of the attribute, under which are the next splits.
	#
	#  Attribute  
	#    __|__      
	#   |     |     
	# Value  Value 
	#   |     |
	#   |     |
	#  next  next
 	#  attr  attr
	#  tree  tree
	#
   	attr = find_best_attribute_to_split_on(training_set)
   	if attr is None:
   		likeliest_class = sorted(training_set[0]['classes'].items(), cmp=lambda a,b:b[1]-a[1])[0][0]
   		return (likeliest_class,)

	values = sorted(unique_values(training_set, attr))
	return (attr,) + tuple([(value,make_decision_tree(branch_on_attribute(training_set, attr, value))) for value in values])
