## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    scene living_room

    "I find that if you stare at the ceiling long enough, you start to see patterns in the stipple of the ceiling."
    "It seems the mind has a way of finding patterns when really nothing is there."
    "I'm reminded of constalations; but at least those are actually useful."
    "My personally catalog of ceiling creatures serves the opposite purpose."
    "Instead of pushing me to explore new horizons, they keep me umoving and planted here on my couch."
    "The unfamilliar chime of my doorbell rings out into the dusty, trash ridden rooms of my lonely house."
    "I ignore it for a moment, thinking that it's my phone."
    "But when I realize my phone's been off for the entire week, save to order food, I know it must be something else."
    "Trying to remember if I ordered food recently, I slowly rise from the cold wet material of the couch."
    "My skin feels like it's peeling off, as my oily sweat has made for an effective adhesive."
    "I consider putting a shirt on, but after a while I realized it didn't matter."
    "No who one I cared about was coming over to my house, so it didn't matter if I greeted the strangers who delivered my food as a pale half-naked troll."
    "Standing up had called all my senses to attention."
    "My head began to throb from dehydration, and the smell of rotting pickles scraps invaded my nose."
    "I didn't like the pickeles, but I didn't have the energy to toss them in the bin."
    "Making my way to the front door, I squint my eyes as the sun shines though the glass at the top of the door."
    "I reach for the doorknob and lazily ween it open."

    scene resitential
    show yuri

    "..."

    y "Ah..."
    y "C-- Could you put on a shirt?"

    scene living_room
    play sound door_slam

    "My heart pounds in my aching chest and my face glows hot with embarassment."
    "I scramble to the sink to vomit, but the grim spattered steel is met only with a dry cough."
    "Must be because I haven't eaten in days."

    show mc_bedroom

    "I rush to my room and frantically pull a shirt over my head."
    "The fabric gets caught on my narrow elbows but I manage to finish while only bursting a few seams."
    "I then look in the mirror to see how unpresentable I just was and am horrified by the half-red half-pale, black eyed, shallow cheeked, bloodshot, tangle haired, animal staring back at me."
    "I can't go to her looking like this!"
    "Maybe she's already left."
    "Then I can die of embarassment alone."

    hide mc_bedroom

    "I peek through the windows adjacent to the front door and see a few stray strands of purple hair waiting patiently for me."
    "Trying to decide what to do, I opt to call her so at least she doesn't have to look at me again."
    "I pressed my thumb into my phone's power button and watch as an elaborate sequence of boot screens flash across the cracked glass."
    "Once I'm in, I hit Yuri's number at the top of my contacts and wait for her to respond."
    "It takes longer than I expected, but in a moment I hear her sweet sounding voice."

    y "Sorry to bother you... but..."

    mc "Yeah, I know I should just let you in but..."
    mc "Do you mind if we just call?"
    mc "I don't want you to see me like this."

    y "Not a worry [player]. I completely understand."
    y "You've been going through a lot."

    mc "Well... you could change that."

    "There is a pause and I see Yuri's head dop through the window curtains."

    mc "I'm sorry."

    y "Per... perhaps we could give it another chance."

    "I feel my head go faint and I have to sit down on the couch."

    y "But, I'll only consider it if you promise to come back to school."
    y "The club misses you and...{w} Well, I've missed you as well."
    y "We'll be having a clab meeting tomorrow, so I'll see you there."
    y "No need to push yourself, so you don't need to go back to class until the day after tomorrow."

    "I smile."

    mc "You're so thoughtful, I've always loved that about you."
    mc "So uh... do you want to come in?"

    y "Fufufu... I though you didn't want to be seen."

    mc "Oh uh... I can tidy up! Just sit tight."

    y "..."
    y "I'll see you at the club tomorrow."

    mc "I won't let you down."

    y "Of course."

    mc "I mean it! I don't know what I did wrong last time, but I promise to make it right."
    mc "I know I can be... uh...{w} but you'll see! I can change!"

    "Yuri doesn't say anything for a moment."

    y "I-It wasn't your fault."

    mc "Don't say that. Who else's fault could it have been?"
    mc "If I had just... I don't know... figured it out sooner!"
    mc "Was I not spending enough time with you?"
    mc "Should I read more? Study harder?"
    mc "Was I not good enough for you?"
    mc "Just tell me what it was so that at least I can try..."

    "Another long pause."

    y "Give me some time to think."
    y "I'll tell you tomorrow."

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
