# make a crop function for all images to use as side images
init -10 python:
    def sidecrop(s):
        return Transform(s, zoom=0.5)

    config.displayable_prefix["small"] = sidecrop

# define side images to only show when a character is not showing
define config.side_image_only_not_showing = True

# love interest
image li angry = At('li angry.png', sprite_highlight('li'))
image li blush = At('li blush.png', sprite_highlight('li'))
image li closedeyes = At('li closedeyes.png', sprite_highlight('li'))
image li default = At('li default.png', sprite_highlight('li'))
image li fear = At('li fear.png', sprite_highlight('li'))
image li happy = At('li happy.png', sprite_highlight('li'))
image li sad = At('li sad.png', sprite_highlight('li'))
image li smile = At('li smile.png', sprite_highlight('li'))
image li stubborn = At('li stubborn.png', sprite_highlight('li'))
image li surprise = At('li surprise.png', sprite_highlight('li'))
image li think = At('li think.png', sprite_highlight('li'))

image side li default = 'small:li default'

# protagonist
image protag angry = At('protag angry.png', sprite_highlight('protag'))
image protag blush = At('protag blush.png', sprite_highlight('protag'))
image protag closedeyes = At('protag closedeyes.png', sprite_highlight('protag'))
image protag default = At('protag default.png', sprite_highlight('protag'))
image protag fear = At('protag fear.png', sprite_highlight('protag'))
image protag happy = At('protag happy.png', sprite_highlight('protag'))
image protag sad = At('protag sad.png', sprite_highlight('protag'))
image protag smile = At('protag smile.png', sprite_highlight('protag'))
image protag stubborn = At('protag stubborn.png', sprite_highlight('protag'))
image protag surprise = At('protag surprise.png', sprite_highlight('protag'))
image protag think = At('protag think.png', sprite_highlight('protag'))

image side protag default = 'small:protag default'

# qirin
image qirin default = At('qirin default.png', sprite_highlight('qirin'))
image qirin happy = At('qirin happy.png', sprite_highlight('qirin'))
image qirin hooded = At('qirin hooded.png', sprite_highlight('qirin'))
image qirin sad = At('qirin sad.png', sprite_highlight('qirin'))
image qirin smile = At('qirin smile.png', sprite_highlight('qirin'))
image qirin think = At('qirin think.png', sprite_highlight('qirin'))

# reaper
image reaper default = At('reaper default.png', sprite_highlight('reaper'))
image reaper happy = At('reaper happy.png', sprite_highlight('reaper'))
image reaper sad = At('reaper sad.png', sprite_highlight('reaper'))
image reaper smile = At('reaper smile.png', sprite_highlight('reaper'))
image reaper think = At('reaper think.png', sprite_highlight('reaper'))