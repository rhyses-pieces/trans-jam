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
  
  show protag smile at left with dissolve:
    xzoom -1.0
  show li blush at right with dissolve

  li "Well, uh, that's... that gives me a lot to think about, at least."
  protag think "?"
  protag "Yes, I'm sure it's a lot to think about. Your {i}friend{/i} seems like they have a lot on their plate."
  show li surprise at hop
  li "!"
  li blush "Eheh... yeah, that's right, they do. Poor guy."
  protag "(I wonder what his deal is?)"
  protag neutral @ closedeyes "(Ah, oh well. Maybe he's just really concerned for his friend.)"
  protag "Hopefully your friend will find someone who gets them."
  li smile @ sad "..."
  li "Yeah, thanks. I'll pass that along to them."

  return

label .desire():

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

label .joke():

  show protag stubborn at left with dissolve:
    xzoom -1.0
  show li surprise at right with dissolve

  li ""

  return