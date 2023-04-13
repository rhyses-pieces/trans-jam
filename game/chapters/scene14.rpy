label scene14():

  play_music(cafe, fadein=1.0, fadeout=2.0, loop=True)
  scene bg cafe with Fade(0.5, 1, 0.5)

  narrator "The store opens again to another day, filled with drinks, snacks, and fortunes."

  show protag smile at center with fade
  with Pause(0.25)

  protag @ happy "Order up!"

  return
  