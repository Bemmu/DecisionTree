import math
from textcanvas import TextCanvas

class TextTree(object):
	""" 
	Draws an ASCII art representation of a tree:
	
		         root                  
		   _______|_______             
		  |               |            
		 foo             bar           
		  |               |            
		  |               |            
		 leaf            node          
		           _______|_______     
		          |       |       |    
		         buz     boo     hoo   
		          |       |       |    
		          |       |       |    
		         yeah    what    ever  
	
	
	The above example was drawn from the following tuple structure:	
		(
			'root', 
			(
				'foo', 
				(
					'leaf', 
				)
			), 
			(
				'bar', 
				(
					'node', 
					(
						'buz', 
						(
							'yeah', 
						)
					), 
					(
						'boo', 
						(
							'what', 
						)
					),
					(
						'hoo', 
						(
							'ever', 
						)
					)
				)
			)
		)

	Example usage:
		print str(TextTree())

	"""

	def __init__(self, data = 
		(
			'root', 
			(
				'foo', 
				(
					'leaf', 
				)
			), 
			(
				'bar', 
				(
					'node', 
					(
						'buz', 
						(
							'yeah', 
						)
					), 
					(
						'boo', 
						(
							'what', 
						)
					),
					(
						'hoo', 
						(
							'ever', 
						)
					)
				)
			)
		)
	):
		self._data = data
		self._canvas = TextCanvas()
		self._draw()

	def get_canvas(self):
		"""Get the TextCanvas the tree was drawn on"""
		return self._canvas

	# From http://stackoverflow.com/questions/10482339/how-to-find-median
	@classmethod
	def median(cls, lst):
	    even = (0 if len(lst) % 2 else 1) + 1
	    half = (len(lst) - 1) / 2
	    return sum(sorted(lst)[half:half + even]) / float(even)

	def _draw_title(self, title, padding = 2):
		# Here's how the title should be positioned relative to the stem below it for some example title widths.

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
		title = " "*padding + title + " "*padding
		title_x_position = math.ceil((1.0-len(title))/2.0) # gradually goes more to the left
		self._canvas.set(title, title_x_position, 0)

	def _x_centers(self, canvases):
		x_centers = []

		# Start at the leftmost point in the first canvas
		current_x = math.ceil((1.0-canvases[0].width())/2.0)

		for i, canvas in enumerate(canvases):

			# Go to the center position of the current canvas
			current_x -= math.ceil((1.0-canvas.width())/2.0)

			x_centers.append(current_x)

			# Go to the leftmost position of the next canvas
			current_x += math.ceil((1.0-canvas.width())/2.0) + canvas.width()

		return x_centers

	def _draw(self):
		title, subtrees = self._data[0], self._data[1:]

		self._draw_title(title)

		# Stem and drawing of subtrees is only needed if there are some.
		if not subtrees:
			return
		self._canvas.set('|', 0, 1)

		# Where to place those subtrees exactly isn't known until the width of subtree drawings is known.
		# So draw them all and then move them into place.
		canvases = []
		for subtree in subtrees:
			tree = TextTree(subtree)
			#tree.draw()
			canvases.append(tree.get_canvas())

		# Now at this point we've drawn the title and the vertical bit of stem and know how big the subtrees
		# are. Lay them out next to each other.
		#
		#       title
		#         |
		#                
		# 1111112222223333333
		#
		# This layout problem is a bit hairier than just centering the blocks, as we would prefer the box below 
		# to align with the stem | under the label.
		#
		# Consider these two cases:
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
		# Despite the total width being the same, actually they are placed differently! Turns out the solution
		# is to place them according to the median point of the box centers. That way the middle one will end up
		# at 0 or if there is no middle, then the midpoint ends up at 0.
		#
		x_centers = self._x_centers(canvases)
		adjustment = math.floor(-self.median(x_centers))
		x_centers = [x + adjustment for x in x_centers]

		# Draw each canvas in the computed center
		for canvas, x_center in zip(canvases, x_centers):
			canvas.blit_to(self._canvas, x_center, 3)

		# Finally connect stems to centers of each subtree.
		#
		#       title
		#    _____|_____
		#   |     |     |
		# 1111112222223333333
		for x_center in x_centers:
			self._canvas.set('|', x_center, 2)
		self._draw_horizontal_stem((0, 1), int(x_centers[-1] - x_centers[0]))

	# Draw part that looks like          ______|_______
	#
	def _draw_horizontal_stem(self, midpoint, stem_length):
		for i in range(1, stem_length):
			x = midpoint[0] + i - stem_length/2 
			if x != midpoint[0]:
				self._canvas.set('_', x, midpoint[1])

	def __str__(self):
		return str(self._canvas)

if __name__ == '__main__':
	print "\n" + str(TextTree()) + "\n"