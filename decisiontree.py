# Functions for constructing a top-down decision tree (TDIDT).

# Need to add a "stopping criterion" here.

from equations import *
from texttree import TextTree

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

def stopping_criterion_met(training_set):

	# Split recursively until all cases in same class.

	# Find if all in same class...

	# So at least will need to look at each training set
	# And attributes don't matter, just looking at classes so...

	# All are in same class if... ?

	class_memberships = [x['classes'] for x in training_set]
	classes_with_members = [[k for k,v in single.items() if v > 0] for single in class_memberships]
	flattened = reduce(lambda a,b:a+b, classes_with_members)
	uniqued = list(set(flattened))
	return len(uniqued) == 1

	# Ugh I'm feeling stupid today :-/

	# Approach: count for each class how many members it has.
	# Then if all except one have zero membership then true.

	return False

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
   	if stopping_criterion_met(training_set) or attr is None:

   		# If there are no more attributes to split on, pick class based on majority.
   		likeliest_class = sorted(training_set[0]['classes'].items(), cmp=lambda a,b:b[1]-a[1])[0][0]
   		return (likeliest_class,)

   	# Nodes are all the possible values of the picked attribute, sorted to alphabetical order.
	values = sorted(unique_values(training_set, attr))
	child_nodes = tuple([(value,make_decision_tree(branch_on_attribute(training_set, attr, value))) for value in values])
	return (attr,) + child_nodes
