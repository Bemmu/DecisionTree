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
		x, y = int(x), int(y)
		"""Put a character or string on the canvas at a certain location, overwriting anything else there."""
		for i, ch in enumerate(str):
			key = '%s_%s' % (x + i, y)
			self.canvas[key] = ch

	def bounds(self):
		"""Return (min_x, min_y, max_x, max_y) tuple describing where the picture lies within the infinite canvas."""
		x_values = [int(key.split('_')[0]) for key in self.canvas.keys()]
		y_values = [int(key.split('_')[1]) for key in self.canvas.keys()]
		return (min(x_values), min(y_values), max(x_values), max(y_values))

	def width(self):
		bounds = self.bounds()
		return bounds[2] - bounds[0] 

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

	def blit_to(self, other_canvas, offset_x = 0, offset_y = 0):
		"""Blit the contents of this canvas to another canvas, possibly at different coordinates."""
		for key, value in self.canvas.items():
			x, y = key.split('_')
			x += offset_x
			y += offset_y
			other_canvas.set(value, x, y)

class TextTree(object):

	# Represent a tree such as
	#
	#	         root
	#	   _______|_______
	#      |              |
	#     foo            bar
	#      |              |
	#     leaf           node
	#	              ____|____
	#	              |         |
	#	             buz       boo
	#                 |         |
	#                yeah      what
	#
	# A tree is... the root and a list of subtrees with branch names.
	# Hmm... one simplification would be to just think that "foo" is not
	# the branch name to "leaf", but actually foo and bar are not special,
	# but they are the roots of new trees... but just happen to have only
	# one child.
	#
	# Yeah can't see any reason not to think of it like that! It simplifies
	# things. So a tree is the root name and list of subtrees, possibly none.
	#
	# ('root',
	#  ('foo',
	#   ('leaf')
	#  ),
	#  ('bar', (
	#   ('node', (
	#    ('buz', ('yeah')),
	#    ('boo', ('what'))
	#   ))
	#  ))
	# )
	def __init__(self, data = ('root', ('foo', 'leaf'), ('bar', ('node', (('buz', 'yeah'), ('boo', 'what')))))):
		self.data = data
		self.canvas = TextCanvas()
		self.draw()

	def draw(self):
		# To draw a tree, need to draw the subtrees. Then connect those subtree drawings with a stem and
		# put a label on top. Let's start with the label.

		# Here's how the label should be positioned relative to the stem below it for some example title widths.

		# t (0, 0)
		# | (0, 0)

		# ti (0, 0) 
		# |  (0, 0)

		# tit (-1, 0) 
		#  |  (0, 0)

		# titl (-1, 0)
		#  |   (0, 0)

		# title (-2, 0)
		#   |   (0, 0)

		# Set the title corresponding to the sketches above
		title = self.data[0]
		stem_x_position = 0 # always in center
		import math
		title_x_position = math.ceil((1.0-len(title))/2.0) # gradually goes more to the left
		self.canvas.set(title, title_x_position, 0)

		# Next the stem is only needed if there are some subtrees
		subtrees = self.data[1:]
		if len(subtrees) > 0:
			self.canvas.set('|', stem_x_position, 1)

		# Where to place those subtrees exactly isn't known until the width of subtree drawings is known.
		# So draw them all and then move them into place.
		canvases = []
		for subtree in subtrees:
			tree = TextTree(subtree)
			tree.draw()
			canvases.append(tree.get_canvas())

		# Now at this point we've drawn the title and the vertical bit of stem and know how big the subtrees
		# are. Lay them out next to each other.
		#
		#       title
		#         |
		#                
		# 1111112222223333333
		total_width = sum([canvas.width() for canvas in canvases])
		x = math.ceil((1.0-total_width)/2.0)

		# Wait this isn't right. The X calculated here would be the upper left of the block of subtrees.
		# But the offset given to blit_to is where the center of the tree should go.

		# So if I blit to 0, 0 then the stem part would end up 0, 1.

		# Things I know:
		#  - If there is an odd amount of boxes then the stem inside center has to align with the stem outside.
		#  - The solution will look like a formula involving ceil/floor most likely.
		#  - The outcome? At least the outcome needs to tell me at which X position to blit each box.
		#  - Inputs? Maybe just the total_width would be enough?
		# 
		# Can that really be enough? Consider these two cases:
		#
		#     title
		#       |
		#       |     
		#     1123
		#
		#     title
		#       |
		#       |
		#      1233
		#
		# Despite the total width being the same, actually the x-position is different!
		# So somehow the positioning DOES depend on the individual box size and total_width is not enough.
		#
		# What if I as a human being did this? How would I do it?
		# Well if I had an odd number of boxes, I would place the middle one right under the parent and then lay out the rest on the sides.
		# If I had an even number of boxes, I would just place them side by side and offset x so that they would be roughly in the center.
		#
		# It can't be so that the solution is different depending on the parity... solutions tend to be more clean than that.
		# Maybe if I write out the code, then the commonalities will become apparent.

		if (len(canvases)%2) == 0: # even
			pass
		else: # odd

			x_centers = []

			# Start at the leftmost point in the first canvas
			current_x = math.ceil((1.0-canvases[0].width())/2.0)

			for canvas in canvases:

				# Go to the center position of the current canvas
				current_x -= math.ceil((1.0-canvas.width())/2.0)

				x_centers.append(current_x)

				# Go to the leftmost position of the next canvas
				current_x += math.ceil((1.0-canvas.width())/2.0) + canvas.width()

			# Now the x_center of the centermost canvas should be 0. Adjust all so that it is.
			adjustment = -x_centers[len(x_centers)/2]
			x_centers = [x + adjustment for x in x_centers]

		# Finally connect stems to centers of each subtree.
		#
		#       title
		#    _____|_____
		#   |     |     |
		# 1111112222223333333
		#
		# How do I know what the "center point" of each subtree is. It has to be correct, otherwise
		# the stems in the subtree will look weird.
		#
		#   title
		#     |
		#   11111
		#   11111
		#   11111
		#
		# In the above case the subtree might be another single-child tree:
		#
		#   title
		#     |
		#   title
		#     |
		#   title


	def get_canvas(self):
		return self.canvas

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
# 	def draw_branches(self, midpoint, labels, subtree_widths):

# 		# For purposes of figuring out how to space the labels, imagine the label and subtree
# 		# inside a box. To hold them both, the boxes clearly need to be the maximum width of 
# 		# label & subtree.
# 		#
# 		# To draw them properly, lay out these boxes next to each other and make the stem
# 		# reach from the center of the leftmost box to the center of the rightmost one.
# 		#
# 		#         __________|__________
# 		#        /       /     \       \ 
# 		#    1________________________________
# 		#    |#label#|#label#|#label#|#label#|
# 		#    |   |       |       |       |   |
# 		#    |subtree|subtree|subtree|subtree|
# 		#    ''''''''''''''''''''''''''''''''' 

# 		box_padding = 4
# 		box_widths = [box_padding + max(i) for i in zip([len(l) for l in labels], subtree_widths)]

# 		# Figure out where the center points of each box fall.
# 		total_width = sum(box_widths)
# 		stem_length = total_width - box_widths[0]/2 - box_widths[-1]/2


# 		# What to do about not even?

# 		# |_

# 		# For example if stem_length is 2. Then it's just going to be on one side. Which side is that?
# 		# The side that needs it...

# 		first_box_leftmost_point = midpoint[0] - 

# 		# first_box_leftmost_point = -total_width/2 - midpoint[0]  # 1) in the picture
# 		# first_box_center_point = first_box_leftmost_point + box_widths[0]/2
# 		# last_box_rightmost_point = total_width/2 + midpoint[0]
# 		# last_box_center_point = last_box_rightmost_point - box_widths[-1]/2
# 		# stem_length = last_box_center_point - first_box_center_point

# 		# Draw horizontal stem to connect the farthest boxes.
# 		self.draw_horizontal_stem(midpoint, stem_length)

# 		# Draw the vertical stem parts that connect the horizontal stem to each box.
# 		x = first_box_leftmost_point
# 		for i, box_width in enumerate(box_widths):
# 			self.canvas.set(str(i) * box_width, x, midpoint[1] + 1)
# 			x += box_width

# #		label_line = "  ".join(labels)
# #		self.draw_stem(midpoint, len(label_line))
# #		self.canvas.set(label_line, midpoint[0] - len(label_line)/2, midpoint[1] + 2)

	# def __init__(self, data):
#		self.draw_branches((0, 0), ['yes', 'no'], [4, 10])

	def __str__(self):
		return str(self.canvas)

if __name__ == '__main__':
	text_tree = TextTree()
	print str(text_tree)