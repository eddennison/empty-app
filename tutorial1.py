from ggame import App
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
brectangle = RectangleAsset(50, 20, thinline, blue)
rrectangle = RectangleAsset(50, 20, thinline, red)
bellipse = EllipseAsset(500,250,thinline, blue)
rpolygon = PolygonAsset([(0,250),
                        (0,50),
                        (50,0),
                        (950,0),
                        (1000,50),
                        (1000,250),
                        (1000,450),
                        (950,50),
                        (50,500),
                        (0,250)],thinline, red)


# Now display a rectangle
Sprite(brectangle,(100,100))
Sprite(rrectangle,(110,110))
Sprite(bellipse,(500,250))
Sprite(rpolygon(500,250))

myapp = App()
myapp.run()