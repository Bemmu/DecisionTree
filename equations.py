# Python implementations of the equations given in Knowledge Discovery course material (http://www.uta.fi/sis/tie/timu/timu_eng.html).

memoize = False
debug = False

import math
pcalcs = ""

# Expected information needed to classify an arbitrary case in S
# https://github.com/Bemmu/DecisionTree/raw/master/img/hc.png
memo_h = {}
def H(S):
	if memoize and str(S) in memo_h:
		return memo_h[str(S)]

	s = sum([sum(_case['classes'].values()) for _case in S])

	def p(s, _class):
		global pcalcs
		su = 0
		for _case in S:
			su += _case['classes'][_class] 
		line = "p(%s) = %s/%s = %.2f\n" % (_class, su, s, su/float(s))
		if debug: print line

		return su/float(s)

	classes = S[0]['classes'].keys()

	result = -sum([p(s, Ci)*math.log(p(s, Ci),2) for Ci in classes if p(s, Ci) != 0])

	# Now just explain the result
	if debug: print "H(S) = -(",
	for i, Ci in enumerate(classes):
		if p(s, Ci) == 0: continue
		if i > 0 and debug: print "+", 
		if debug: print "%.2f * log2(%.2f)" % (p(s, Ci), p(s, Ci)),
	if debug: print ") = %.2f" % result

	memo_h[str(S)] = result

	return result

# Consider only those cases having the value Aj for attr A
# https://github.com/Bemmu/DecisionTree/raw/master/img/h_given_aj.png
memo_h_given_aj = {}
def H_given_Aj(S, A, Aj):
	memo_key = (str(S), A, Aj)
	if memoize and memo_key in memo_h_given_aj:
		return memo_h_given_aj[memo_key]

	S = [_case for _case in S if _case[A] == Aj]
	result = H(S)
	memo_h_given_aj[memo_key] = result
	if debug: print "H_given_Aj %s = %s is %.2f" % (A, Aj, result)

	return result

# https://github.com/Bemmu/DecisionTree/raw/master/img/h_for_attribute.png
memo = {}
def H_for_attribute(S, A):
	if memoize and (len(S), A) in memo:
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

	if debug: print "H_for_attribute %s = sum(" % A,
	result = 0

	for i, Aj in enumerate(vals):
		if i > 0 and debug: print "+",
		if debug: print "%.2f * %.2f" % (p(Aj), H_given_Aj(S, A, Aj)),
		part = p(Aj)*H_given_Aj(S, A, Aj)
		result += part

	if debug: print ")"

	memo[len(S), A] = result
	return result

# https://github.com/Bemmu/DecisionTree/raw/master/img/i.png
def I(S, A):
	if debug: print "I(C|%s) = %.2f - %.2f = %.2f" % (A, H(S), H_for_attribute(S, A), H(S) - H_for_attribute(S, A))
	return H(S) - H_for_attribute(S, A)

if debug: print pcalcs