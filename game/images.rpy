# define transforms and configs for side images
# mipmap dissolve since the side image is scaled down
transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True, mipmap=True)

transform change_transform(old, new):
    contains:
        old
        yalign 1.0
        xanchor 0.0
        alpha 1.0
        ease 0.3 alpha 0.0
    contains:
        new
        yalign 1.0
        xanchor 0.0
        alpha 0.0
        ease 0.3 alpha 1.0

define config.side_image_same_transform = same_transform
define config.side_image_change_transform = change_transform
define config.side_image_only_not_showing = True

# love interest
layeredimage li:
    at sprite_highlight('li')
    group emote auto:
        attribute neutral default

image side li left = LayeredImageProxy('li', Transform(xalign = 0.0, zoom = 0.8, xzoom = -1.0))
image side li right = LayeredImageProxy('li', Transform(xalign = 1.0, zoom = 0.8, xzoom = 1.0))

# protagonist
layeredimage protag:
    at sprite_highlight('protag')
    group emote auto:
        attribute neutral default

image side protag left = LayeredImageProxy('protag',Transform(xalign = 0.0, zoom = 0.8, xzoom = -1.0))
image side protag right = LayeredImageProxy('protag',Transform(xalign = 1.0,zoom = 0.8, xzoom = 1.0))

# qirin
layeredimage qirin:
    at sprite_highlight('qirin')
    group emote auto:
        attribute neutral default

image side qirin left = LayeredImageProxy('qirin', Transform(xalign = 0.0, zoom = 0.8))
image side qirin right = LayeredImageProxy('qirin', Transform(xalign = 1.0, zoom = 0.8, xzoom = -1.0))

# reaper
layeredimage reaper:
    at sprite_highlight('reaper')
    group emote auto:
        attribute neutral default

image side reaper left = LayeredImageProxy('reaper', Transform(xalign = 0.0, zoom = 0.8))
image side reaper right = LayeredImageProxy('reaper', Transform(xalign = 1.0, zoom = 0.8))