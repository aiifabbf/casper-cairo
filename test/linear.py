import sys
sys.path.append("..")
try:
    from cairo import *
except:
    raise Exception("failed to import cairo")

s = ImageSurface(FORMAT_RGB24, 400, 400)
c = Context(s)
linear = LinearGradient(0, 0, 400, 400)
linear.add_color_stop_rgb(0, 0, 0.3, 0.8)
linear.add_color_stop_rgb(1, 0, 0.8, 0.3)
c.set_source(linear)
c.paint()

with open("linear.png", "wb+") as f:
    s.write_to_png(f)

s.finish()