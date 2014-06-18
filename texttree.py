# Need to recurse to the end, otherwise cannot know how large a branch would be and would not
# know how much space to allocate for it.

#	         root
#	   _______|_______
#	  /               \
#	 leaf            branch
#                       \
#                      node
#	                 ____|____
#	                /         \
#	              leaf       leaf

#	        injury
#	     ______|_______
#       /              \
#     no               yes
#	  /                  \
#   not-BPV    frequency of vertigo attacks
#                _________|__________
#               /         |          \
#              0          1           2
#             /           |            \
#           not-BPV   hearing loss     BPV
#                         |
#                  _______|_______
#                 /               \
#               no                yes
#               /                   \
#             not-BPV               BPV

# Necessary width for a subtree is...
#   max(len(root), sum(len(subtrees)))

# For composing character art by drawing in free order, instead of the line order imposed by just using print.
class TextCanvas(object):
	def __init__(self):		
		self.canvas = {}

	def set(self, str, x, y):
		"""Put a character or string on the canvas at a certain location, overwriting anything else there."""
		for i, ch in enumerate(str):
			key = '%s_%s' % (x + i, y)
			self.canvas[key] = ch

	def bounds(self):
		"""Return (min_x, min_y, max_x, max_y) tuple describing where the picture lies within the infinite canvas."""
		x_values = [int(key.split('_')[0]) for key in self.canvas.keys()]
		y_values = [int(key.split('_')[1]) for key in self.canvas.keys()]
		return (min(x_values), min(y_values), max(x_values), max(y_values))

	def __str__(self):
		out = ""
		bounds = self.bounds()

		for i, y in enumerate(range(bounds[1], bounds[3] + 1)):
			if i > 0:
				out += "\n"

			for x in range(bounds[0], bounds[2] + 1):
				try:
					out += self.canvas['%s_%s' % (x, y)]
				except:
					out += ' '

		return out

if __name__ == '__main__':
	import random
	canvas = TextCanvas()
	for i in range(0, 10):
		canvas.set(':-)', random.randint(0, 100), random.randint(0, 20))

	print canvas