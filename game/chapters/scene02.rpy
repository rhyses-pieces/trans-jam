label scene02:
    show protag surprise at right
    show li default at left

    show protag at hop
    protag "AAAH!!!"
    protag "EXCUSE ME HOW DID YOU GET IN MY HOUSE?" with hpunch
    li blush "Ahaha... magic?" (who_color="#575c69")
    protag angry "Get out!!"
    li surprise "Whoa, hang on, I know you're freaking out, but let me explain--" (who_color="#575c69")
    protag "What's there to explain?! I don't know you and I don't know how you got in!!"
    li blush "{i}O~kay{/i} I know it looks bad, but I promise I'm not here to hurt you or steal your stuff." (who_color="#575c69")
    protag think "Then what {i}are{/i} you here for?"

    $ liName = "Noel"
    li default "First of all, my name's [li]. I'm here to "

    protag default "Okay, [li]. Uh. Right."

    return