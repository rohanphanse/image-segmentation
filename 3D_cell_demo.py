# Demo from: https://github.com/napari/napari
from skimage import data
import napari

viewer = napari.view_image(data.cells3d(), channel_axis=1, ndisplay=3)
napari.run()