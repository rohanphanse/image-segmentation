# From Jackson Labratory's tutorial: https://www.youtube.com/watch?v=sFvZcUeShoo
from skimage import io
import napari
import numpy as np

viewer = napari.Viewer()
viewer.add_image(io.imread("./data/neuron_data.tif"))
points = np.array([[100, 100], [200, 200], [300, 100]])
viewer.add_points(points, size=30)
print(viewer.layers["points"].data)
napari.run()
