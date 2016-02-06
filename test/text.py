import sys
sys.path.append("..")
try:
    from cairo import *
except:
    raise Exception("failed to import cairo")

s = ImageSurface(FORMAT_RGB24, 400, 400)
c = Context(s)
c.select_font_face("ubuntu")
c.set_font_size(100)
c.set_source_rgb(1, 1, 1)
c.paint()
c.set_source_rgb(0, 0, 0)
print("Font extents: ", c.font_extents())
xb, yb, width, height = c.text_extents("hi")[:4]
c.move_to(200 - width / 2 - xb, 200 - height / 2 - yb)
c.show_text("hi")

with open("text.png", "wb+") as f:
    s.write_to_png(f)

s.finish()