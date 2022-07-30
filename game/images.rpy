# define transforms and configs for side images
# mipmap dissolve since the side image is scaled down
transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True, mipmap=True)

define config.side_image_same_transform = same_transform
define config.side_image_only_not_showing = True

# love interest
layeredimage li:
    at sprite_highlight('li')
    group emote auto:
        attribute neutral default

image side li left = LayeredImageProxy('li', Transform(xalign = 0.0, xzoom = -1.0))
image side li right = LayeredImageProxy('li', Transform(xalign = 1.0, xzoom = 1.0))

# protagonist
layeredimage protag:
    at sprite_highlight('protag')
    group emote auto:
        attribute neutral default

image side protag left = LayeredImageProxy('protag',Transform(xalign = 0.0, xzoom = -1.0))
image side protag right = LayeredImageProxy('protag',Transform(xalign = 1.0, xzoom = 1.0))

# qirin
layeredimage qirin:
    at sprite_highlight('qirin')
    group emote auto:
        attribute neutral default

image side qirin left = LayeredImageProxy('qirin', Transform(xalign = 0.0))
image side qirin right = LayeredImageProxy('qirin', Transform(xalign = 1.0, xzoom = -1.0))

# reaper
layeredimage reaper:
    at sprite_highlight('reaper')
    group emote auto:
        attribute neutral default

image side reaper = LayeredImageProxy('reaper')