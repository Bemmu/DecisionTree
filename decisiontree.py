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

import math

memo_h = {}
pcalcs = ""

# Expected information needed to classify an arbitrary case in S
def H(S):
	if str(S) in memo_h:
		return memo_h[str(S)]

	s = sum([sum(_case['classes'].values()) for _case in S])

	def p(s, _class):
		global pcalcs
		su = 0
		for _case in S:
			su += _case['classes'][_class] 
		line = "p(%s) = %s/%s = %.2f\n" % (_class, su, s, su/float(s))
		print line

		return su/float(s)

	classes = S[0]['classes'].keys()

	result = -sum([p(s, Ci)*math.log(p(s, Ci),2) for Ci in classes if p(s, Ci) != 0])

	# Now just explain the result
	print "H(S) = -(",
	for i, Ci in enumerate(classes):
		if p(s, Ci) == 0: continue
		if i > 0: print "+", 
		print "%.2f * log2(%.2f)" % (p(s, Ci), p(s, Ci)),
	print ") = %.2f" % result

	memo_h[str(S)] = result

	return result

# OK, so I can compute H(S) now and it even matches my previous calculation.

memo_h_given_aj = {}

# Consider only those cases having the value Aj for attr A
def H_given_Aj(S, A, Aj):
	memo_key = (str(S), A, Aj)
	if memo_key in memo_h_given_aj:
		return memo_h_given_aj[memo_key]

	S = [_case for _case in S if _case[A] == Aj]
	result = H(S)
	memo_h_given_aj[memo_key] = result
	print "H_given_Aj %s = %s is %.2f" % (A, Aj, result)

	return result

memo = {}

def H_for_attribute(S, A):
	if (len(S), A) in memo:
		return memo[len(S), A]

	s = sum([sum(_case['classes'].values()) for _case in S])
	s_for_Aj = lambda Aj: sum([sum(_case['classes'].values()) for _case in S if _case[A] == Aj])

	# p(Aj) is the relative frequency of the cases having
	# value Aj for the attribute A in the set S
	p = lambda Aj:s_for_Aj(Aj) / float(s)

	# All the different values attribute A could have
	vals = set([_case[A] for _case in S])

	# Pre-memoize
	for Aj in vals:
		p(Aj)*H_given_Aj(S, A, Aj)

	print "H_for_attribute %s = sum(" % A,
	result = 0

	for i, Aj in enumerate(vals):
		if i > 0: print "+",
		print "%.2f * %.2f" % (p(Aj), H_given_Aj(S, A, Aj)),
		part = p(Aj)*H_given_Aj(S, A, Aj)
		result += part

	print ")"

	memo[len(S), A] = result
	return result

def I(S, A):
	print "I(C|%s) = %.2f - %.2f = %.2f" % (A, H(S), H_for_attribute(S, A), H(S) - H_for_attribute(S, A))
	return H(S) - H_for_attribute(S, A)

print H(S)

for attr in [key for key in S[0].keys() if key != 'classes']:
	print I(S, attr)

print pcalcs