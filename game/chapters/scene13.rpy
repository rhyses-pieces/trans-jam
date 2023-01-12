label scene13():
  
  scene bg backroom with wipedown
  with Pause(0.5)

  if li_truth:
    jump .truth
  elif li_desire:
    jump .desire
  else:
    jump .joke

  return

label .truth():
  
  show protag blush at left with dissolve:
    xzoom -1.0
  show li smile at right with dissolve

  protag "Who are you here for then?"
  li @ blush "It's silly, but I'm here for myself."
  li sad "Sorry for not being honest upfront."
  protag @ surprise "It's okay! I mean, I just, well--"
  protag @ closedeyes "*sigh*"
  protag "This is all new to me. And I'm your {i}boss{/i}, I don't wanna make you uncomfortable."
  li "... Am I making {i}you{/i} uncomfortable?"
  protag @ fear "Huh? No! No, you aren't. {nw}"
  show protag sad
  extend "It's the newness of it all, not you."
  show li surprise
  protag blush "Listen, I... wouldn't be opposed to trying us out if you're willing."
  li happy "Of course I'm willing. I wanna take you out on a date!"
  protag happy "Yeah, okay! Let's go on a date."

  return

label .desire():

  show protag smile at left with dissolve:
    xzoom -1.0
  show li blush at right with dissolve

  
  
  return

label .joke():

  show protag stubborn at left with dissolve:
    xzoom -1.0
  show li surprise at right with dissolve

  return