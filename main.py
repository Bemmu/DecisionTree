from decisiontree import make_decision_tree
from texttree import TextTree

training_set = [
	{'Rank' : 'Assistant Prof', 	'Years' : '3', 'classes' : {'Tenured' : 0, 'not-Tenured' : 1} },
	{'Rank' : 'Assistant Prof', 	'Years' : '7', 'classes' : {'Tenured' : 1, 'not-Tenured' : 0} },
	{'Rank' : 'Professor', 			'Years' : '2', 'classes' : {'Tenured' : 1, 'not-Tenured' : 0} },
	{'Rank' : 'Associate Prof', 	'Years' : '7', 'classes' : {'Tenured' : 1, 'not-Tenured' : 0} },
	{'Rank' : 'Assistant Prof', 	'Years' : '6', 'classes' : {'Tenured' : 0, 'not-Tenured' : 1} },
	{'Rank' : 'Associate Prof', 	'Years' : '3', 'classes' : {'Tenured' : 0, 'not-Tenured' : 1} },
]

decision_tree = make_decision_tree(training_set)
print str(TextTree(decision_tree))
print

training_set = [
	{'Outlook' : 'sunny', 		'Temperature' : 'hot', 		'Humidity' : 'high', 	'Windy' : 'false', 	'classes' : {'N' : 1, 'P' : 0}},
	{'Outlook' : 'sunny', 		'Temperature' : 'hot', 		'Humidity' : 'high', 	'Windy' : 'true', 	'classes' : {'N' : 1, 'P' : 0}},
	{'Outlook' : 'overcast', 	'Temperature' : 'hot', 		'Humidity' : 'high', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'rain', 		'Temperature' : 'mild', 	'Humidity' : 'high', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'rain', 		'Temperature' : 'cool', 	'Humidity' : 'normal', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'rain', 		'Temperature' : 'cool', 	'Humidity' : 'normal', 	'Windy' : 'true', 	'classes' : {'N' : 1, 'P' : 0}},
	{'Outlook' : 'overcast', 	'Temperature' : 'cool', 	'Humidity' : 'normal', 	'Windy' : 'true', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'sunny', 		'Temperature' : 'mild', 	'Humidity' : 'high', 	'Windy' : 'false', 	'classes' : {'N' : 1, 'P' : 0}},
	{'Outlook' : 'sunny', 		'Temperature' : 'cool', 	'Humidity' : 'normal', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'rain', 		'Temperature' : 'mild', 	'Humidity' : 'normal', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'sunny', 		'Temperature' : 'mild', 	'Humidity' : 'normal', 	'Windy' : 'true', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'overcast', 	'Temperature' : 'mild', 	'Humidity' : 'high', 	'Windy' : 'true', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'overcast', 	'Temperature' : 'hot', 		'Humidity' : 'normal', 	'Windy' : 'false', 	'classes' : {'N' : 0, 'P' : 1}},
	{'Outlook' : 'rain', 		'Temperature' : 'mild', 	'Humidity' : 'high', 	'Windy' : 'true', 	'classes' : {'N' : 1, 'P' : 0}},
]

decision_tree = make_decision_tree(training_set)
print str(TextTree(decision_tree))
print

training_set = [
	{'Hearing loss':'No', 	'Injury':'No', 		'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':3, 'BPV':0}},
	{'Hearing loss':'No', 	'Injury':'No', 		'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':59, 'BPV':0}},
	{'Hearing loss':'No', 	'Injury':'No', 		'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':1, 'BPV':55}},
	{'Hearing loss':'No', 	'Injury':'Yes', 	'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':21, 'BPV':1}},
	{'Hearing loss':'Yes', 	'Injury':'No', 		'Frequency of vertigo attacks':'0', 'classes' : {'not-BPV':63, 'BPV':0}},
	{'Hearing loss':'Yes', 	'Injury':'No', 		'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':28, 'BPV':0}},
	{'Hearing loss':'Yes', 	'Injury':'No', 		'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':234, 'BPV':0}},
	{'Hearing loss':'Yes', 	'Injury':'Yes', 	'Frequency of vertigo attacks':'1', 'classes' : {'not-BPV':1, 'BPV':0}},
	{'Hearing loss':'Yes', 	'Injury':'Yes', 	'Frequency of vertigo attacks':'2', 'classes' : {'not-BPV':30, 'BPV':0}},
]

decision_tree = make_decision_tree(training_set)
print str(TextTree(decision_tree))
