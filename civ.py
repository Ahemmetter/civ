"""
Civ
"""
import arcade as a

# Window constants
screen_width = 1280
screen_height = 720
screen_title = "Civ"

# Sprite and map constants
tile_scale = 1
sprite_size = 64
grid_size = (sprite_size * tile_scale)
scroll_speed = 10

class Civ(a.Window):
	"""Main application class"""

	def __init__(self):
		"""Defines the class"""
		# inherits from Window class
		super().__init__(screen_width, screen_height, screen_title)

		# sets up the windows dimensions
		self.tile_list = None
		self.left_boundary = 0
		self.right_boundary = screen_width
		self.top_boundary = screen_height
		self.bottom_boundary = 0
		self.dx = 0
		self.dy = 0

		# sets background color
		a.set_background_color(a.color.WHITE)

	def setup(self):
		"""Runs once on startup"""
		# create a list of tiles
		self.tile_list = a.SpriteList()
		self.score = 0
		# self.zoom_levels = [1, 2, 3]
		# self.zoom = zoom_levels[2]

		# import the map
		map_name = "/Users/nitrox/Code/civ/assets/world.tmx"
		tile_layer_name = "Tile Layer 1"
		my_map = a.read_tiled_map(map_name, tile_scale)
		map_array = my_map.layers_int_data[tile_layer_name]
		self.end_of_map = len(map_array[0]) * grid_size - grid_size
		self.tile_list = a.generate_sprites(my_map, tile_layer_name, tile_scale)

	def on_draw(self):
		"""Draws the map"""
		a.start_render()
		self.tile_list.draw()

	def on_key_press(self, key, modifiers):
		"""Runs when a key is pressed"""
		if key == a.key.LEFT or key == a.key.A:
			self.dx = -scroll_speed
		elif key == a.key.RIGHT or key == a.key.D:
			self.dx = scroll_speed
		elif key == a.key.UP or key == a.key.W:
			self.dy = scroll_speed
		elif key == a.key.DOWN or key == a.key.S:
			self.dy = -scroll_speed

	def on_key_release(self, key, modifiers):
		"""Runs when a key is released"""
		if key in [a.key.LEFT, a.key.RIGHT, a.key.UP, a.key.DOWN, a.key.A, a.key.D, a.key.W, a.key.S]:
			self.dx = 0
			self.dy = 0

	# def on_mouse_press(self, x, y, button, key_modifiers):
		"""
        # Called when the user presses a mouse button.
		"""
		# pass

	def update(self, delta_time):
		"""Moves the map"""
		if (self.top_boundary + self.dy >= self.end_of_map) or (self.bottom_boundary + self.dy <= 0):
			self.dy = 0
		if (self.right_boundary + self.dx >= self.end_of_map) or (self.left_boundary + self.dx <= 0):
			self.dx = 0

		self.top_boundary += self.dy
		self.bottom_boundary += self.dy
		self.left_boundary += self.dx
		self.right_boundary += self.dx

		# set the viewport
		a.set_viewport(self.left_boundary, self.right_boundary, self.bottom_boundary, self.top_boundary)

def main():
	""" Main method """
	game = Civ()
	game.setup()
	a.run()


if __name__ == "__main__":
	main()
