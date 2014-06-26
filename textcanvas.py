class TextCanvas(object):
	"""For composing character art by drawing in free order, instead of the line order imposed by just using print."""

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
 		return bounds[2] - bounds[0] + 1 

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
			x, y = [int(coord) for coord in key.split('_')]
			x += offset_x
			y += offset_y
			other_canvas.set(value, x, y)

