import sys
import pygfx as gfx

if len(sys.argv) == 1:
    sys.exit("missing STL or OBJ file") 

meshes = gfx.load_mesh(sys.argv[1])
display = gfx.Display()
display.show(meshes[0], up=(0, 0, 1))
