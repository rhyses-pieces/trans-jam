label scene13():
  
  scene bg backroom with wipedown
  with Pause(0.5)

  show protag neutral at left with dissolve:
    xzoom -1.0
  show reaper neutral at right with dissolve

  if li_truth:
    jump .truth
  elif li_desire:
    jump .desire
  else:
    jump .joke

  return

label .truth():
  
  return

label .desire():
  
  return

label .joke():

  return