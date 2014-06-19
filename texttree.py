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
#
#
#	        injury
#	     ______|_______
#       /   /     \    \
#    lol  what  really  cool
#
#
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
		if len(self.canvas.keys()) == 0:
			return ""

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

class TextTree(object):

	# Draw part that looks like          ______|_______
	#
	def draw_horizontal_stem(self, midpoint, stem_length):
		for i in range(0, stem_length):
			x = midpoint[0] + i - stem_length/2 
			ch = '|' if x == midpoint[0] else '_'
			self.canvas.set(ch, x, midpoint[1])

	# Draw part that looks like        ________|_________
	#                                 /      /    \      \
	#                              label  label  label  label
	#                                |      |      |      |
	#
	def draw_branches(self, midpoint, labels, subtree_widths):

		# For purposes of figuring out how to space the labels, imagine the label and subtree
		# inside a box. To hold them both, the boxes clearly need to be the maximum width of 
		# label & subtree.
		#
		# To draw them properly, lay out these boxes next to each other and make the stem
		# reach from the center of the leftmost box to the center of the rightmost one.
		#
		#         __________|__________
		#        /       /     \       \ 
		#    1________________________________
		#    |#label#|#label#|#label#|#label#|
		#    |   |       |       |       |   |
		#    |subtree|subtree|subtree|subtree|
		#    ''''''''''''''''''''''''''''''''' 

		box_padding = 4
		box_widths = [box_padding + max(i) for i in zip([len(l) for l in labels], subtree_widths)]

		# Figure out where the center points of each box fall.
		total_width = sum(box_widths)
		first_box_leftmost_point = -total_width/2 - midpoint[0]  # 1) in the picture
		first_box_center_point = first_box_leftmost_point + box_widths[0]/2
		last_box_rightmost_point = total_width/2 + midpoint[0]
		last_box_center_point = last_box_rightmost_point - box_widths[-1]/2
		stem_length = last_box_center_point - first_box_center_point

		# Draw horizontal stem to connect the farthest boxes.
		self.draw_horizontal_stem(midpoint, stem_length)

#		label_line = "  ".join(labels)
#		self.draw_stem(midpoint, len(label_line))
#		self.canvas.set(label_line, midpoint[0] - len(label_line)/2, midpoint[1] + 2)

	def __init__(self, data):
		self.canvas = TextCanvas()
		self.draw_branches((0, 0), ['yes', 'no'], [4, 10])

	def __str__(self):
		return str(self.canvas)

if __name__ == '__main__':
	data = None
	text_tree = TextTree(data)
	print str(text_tree)