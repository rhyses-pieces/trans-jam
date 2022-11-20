label scene12():

  scene bg zodiac_covered with wipeup
  with Pause(0.5)

  protag smile left "Can I ask what zodiac sign you are?"
  li surprise right "Oh! Yeah, I can."
  li neutral @ smile "I was born under the {b}rooster{/b} sign."
  protag neutral @ surprise "!"
  protag @ happy "Nice, okay! That's great info."
  protag @ think "(Huh, that's kinda funny since I'm a {b}dragon{/b} sign.)"
  protag smile "(Oh well, I'm just here to do a love reading.)"
  protag neutral "Let's see..."

  play sound "audio/clink.mp3"

  window hide

  scene bg zodiac_li with dissolve
  with Pause(0.5)

  protag neutral "(There's a lot of leaves in the {b}spring{/b} season. {nw}"
  show protag think 
  extend "That {i}could{/i} symbolize change and hope.)"
  protag neutral "(It's also a romantic season in some ways.)"
  protag @ stubborn "(It also seems like it's overlapping over a lot of signs...)"
  protag @ surprise "({b}Rabbit{/b}, {b}snake{/b}... even {b}dragon{/b} are all touched by the leaves.)"
  protag @ blush "(In fact, there's a lot on the {b}dragon{/b} sign... That's weird.)"
  protag @ closedeyes "(Feels like there could be a lot of conflict in this person's love life.)"
  protag "(There's enough on {b}winter{/b} that it seems like maybe this person will need some patience...)"
  protag @ think "(What should I tell him?)"

  stop music fadeout 1.0

  menu li_choice:
    "What kind of interpretation do you want to convey?"

    "Talk about the possible matches.":
      jump scene12.truth
    "Make his friend seem popular.":
      jump scene12.desire
    "His prospects are going to be wild.":
      jump scene12.joke

  return

label .truth():

  protag closedeyes "..."
  protag @ blush "..."
  protag "Ahem."
  protag neutral "Your friend seems like they might find a potential match in many signs."
  protag "Among them are those born under the {b}rabbit{/b}, {b}dragon{/b}, and {b}snake{/b} signs."
  li @ fear "That's a lot..."
  li "(Wait...)"
  show li surprise with hop
  with Pause(0.25)
  li neutral @ think "Can I ask what sign you are?"
  show protag surprise with hpunch
  with Pause(0.25)
  protag "Huh? Me?"
  protag neutral @ think "No one's ever asked that of me before..."
  protag "I was born under the {b}dragon{/b} sign."
  li "..."
  li smile @ happy "I heard that they pair well with {b}roosters{/b}."
  show protag surprise with hop
  with Pause(0.25)
  protag "!"
  protag blush "Y-yeah? What does that have to do with anything?"
  li @ closedeyes "I have to be honest-- I'm not here for my friend."
  protag "... {i}Oh{/i}."
  
  $ truthEnding += 1
  $ li_truth = True

  return


label .desire():

  protag "I have good news {i}or{/i} bad news, depending on how you view it."
  li think @ fear "Huh? Okay..."
  protag "Your friend's prospects are bountiful-- {nw}"
  show protag smile
  extend "they'll be pretty popular when it comes to their love life."
  show li surprise with hop
  with Pause(0.25)
  li "!"
  li think "..."
  li neutral "Huh, that sounds... cool...?"
  protag @ happy "Yeah! It seems like they'll be popular, especially during {b}spring{/b}."
  protag "Many people will find them charming and love them, I'm sure."
  li @ blush "You think so?"
  protag @ happy "Of course!"
  
  $ desireEnding += 1
  $ li_desire = True

  return

label .joke():

  protag @ closedeyes "..."
  protag @ stubborn "..."
  protag closedeyes @ sad "..."
  li fear "?"
  li "What's wrong?"
  protag "..."
  protag neutral "There's a lot of bad luck involving birds."
  li surprise "... Huh??"
  protag @ stubborn "Your friend {i}needs{/i} to avoid birds, especially chickens."
  protag "It's imperative for their survival."
  li "{b}Huh?{/b}"
  protag stubborn "Avoid pigeons too. Apparently those are also incredibly dangerous."
  protag "I once had a client who came to me because there were pigeons mating in front of their window everyday."
  li "What?"
  protag "(Two pigeons have found more action than I have, damn.)"
  protag "Anyway your friend is going to attract a lot of danger in their life. They need to be careful."
  
  $ jokeEnding += 1
  $ li_joke = True

  return