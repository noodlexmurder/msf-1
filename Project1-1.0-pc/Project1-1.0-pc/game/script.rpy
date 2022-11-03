define a = Character("Aurora") #the player character
define s = Character("Stella") #the love interest

define config.default_text_cps = 45

define x = [0, 0, 0, 0]
define fantasypoints = 0
define realitypoints = 0



label start:
    scene bcstart
    show aurora_test
    #menu:
        #"play the first version of this game":
       #     jump start2
      #  "play the newest version of this game":
     #       "going forward is the new version of the game"

    """
    I wake up from that familiar dream, fluttering my eyelashes as the speckles of 
    sunlight dance on my face.

    My eyes open and I look at a figure sitting on the ledge of the window, 
    sorting through books and pages and little knick-knacks.
    """
    s "Finally you're awake. I was starting to get worried."

    "So she says, with an all-too-obviously sarcastic grin on her face."

    a "You sound like someone who's still mad about always losing to me in Spell Duel."
    s """
    Spell Dual? That silly childhood game?

    Why are you bringing this up all of a sudden. Did that nap mess with your cognitive function?

    Haha, you're still the same as when we were kids.
    """
    "Stella softly chuckles, glancing away."

    a "Was it really that long ago?"
    "That vivid dream made it seem like it was yesterday. A strange feeling is burning in my chest."
    
    s "Seriously, Aurora. That was so long ago. Move on and get a life"
    """
    She comes closer and reaches out to playfully hit me on the shoulder.

    The small physical contact shocks me back into reality.

    I can hear the comforting bubbling, fizzling, and whistling of pots, potions, and cauldrons
    in the humble cabin. In every nook and cranny there is some kind of whimsical device. every
    shelf is full of large spell books and every bottle is teeming with all kinds of colorful
    and strange liquids. Two witch hats hang on the wall.

    Stella stands by the door, putting garden pruners and some elixir bottles into her bag.
    """

    a "Those bottles... are you going to collect the ingredients for that potion today?"

    "Stella's gaze stays on her bag."

    s "Yeah, I can't just wait here all day for you to get ready."

    a "What are the garden pruners for?"

    s "I'm going to do some work in the rose garden later in the afternoon."

    "This means Stella's going to be out all day, and I won't be able to spend as much time with her"

    menu ("", screen = "option"):
        "Let me come with you!":
            a "I want to go with you!"
            s "Are you sure?" #SHOW HER SMIRKING
            s "You seemed pretty tired earlier."
            a "I'm not! I want to go with you. Let's go!"
            jump gettingReadyForPotion
            

        "You're going to leave me here all day?":
            a "You're not going to leave me here all day by myself are you?"
            s "You're free to go out whenever you want! Haha, don't act like I own you or anything."
            s "You realize you can go out and do things without me, right? We're not kids anymore."
            "She gives me a symathetic smile"
            a "Its not I can't go out without you or anything... I just like spending time with you."
            s "Haha, alright. Come on then!"
            jump gettingReadyForPotion

label gettingReadyForPotion:
    "I get up quickly and brush off my dress before rushing to Stella's side by the door." #SHES WEARING A DRESS,, MAKE SURE TO UPDATE

    """
    Stella doesn't seem as enthusiastic as I would like her to be. Instead, she looks a little torn.

    But that expression only lasts a few seconds before she looks at me and smiles.
    """

    s "You really can't live without me can you, Aurora? You don't to follow me around all day like a pet."
    """
    She lightly taps my nose with the tip of her finger.

    She teases me, but I don't think she really understands the extent of my feelings for her.

    Perhaps today I can make those feelings clear to her.
    """
    a "I'm coming with you."
    """
    I repeat my intent in a firmer tone. 
            
    Stella and I have known each other since we were very young, 
    and even though she can appear dismissive sometimes, she's usually just shy.

    Or perhaps there is some other reason why she's so anxious about our relationship.

    We walk out the door.
    """
    jump pomegranatePotion

label pomegranatePotion:
    scene bcevent1
    """
    We walk on the small dirt path through the woods that surrounds our humble cabin,
    making light conversation and laughing like normal.

    The lush green grass pads the ground along the path. Piles of fallen fruits sink into the cushiony foliage and the air smells deep and natural with a hint of sweetness from the fruits.

    Stella's heels make small clouds of dirt as she walks forward with a clear destination in mind.

    We walk along countless trees, their overextending branches and strong trunks providing a protective
    presence, making me feel safe and comfortable within this large and unpredictable forest.

    The fluffy grass climbs up the bases of the trees, and some fallen fruits lay nested in the nooks of the branches.

    Small animals scurry around as if dancing along to the birds' songs. I've always been engrossed in the
    complexity and beauty of this forest.

    I stop my eyes from wandering around at the beautiful environment and focus my attention on Stella once more.
    """

    a "So, what was this potion for again?"
    s "I don't know... that's what we're here to find out."
    a "What do you mean you don't know?"

    s "It's a new innovation I wanted to try. I drew some inspiration from an old mythology book."

    "Stella was always such a bookworm. She's always reading mythology or poetry of some kind or another. I wonder why she didn't just become a literature professor."

    s """
    You know that story about the goddess of spring, Persephone, who was kidnapped and taken to Hades' palace in the underworld where they got married.

    Her absence caused a famine and eternal winter in the world above, but she couldn't return because she had consumed a few pomegranate seeds. Once you consume the fruit of the underworld you are trapped there.

    Eventually, Hades agreed to let her revisit her home above once every nine months.
    """

    a "That... is a really twisted love story."

    s """
    Exactly! I want to find out more about this dark and powerful fruit.
    
    What will happen if I make a potion with pomegranate extract as the main ingredient?

    Aren't you excited to see what will happen if someone drinks that kind of potion?
    """

    a "Wouldn't that just be a less concentrated pomegranate juice?"

    s """
    I knew you would say something like that. Sometimes you can be uncharacteristically realistic...

    I dare you to try it!
    """

    """
    Stella is clearly ecstatic about her new idea. A mischevious smile overtakes her face.

    She has already grabbed a ripe pomegranate off of one of the many fruit trees surrounding us.

    Without waiting for me to agree she slices the fruit in half and starts squeezing the pomegranate juice into an exilir bottle that she had brought from the cabin.
    """

    menu ("", screen = "option"):
        "Are we seriously doing this?":
            s "Are you backing out?"

    """
    Once Stella becomes set on something, it's very hard to convince her any other way.

    The extract is mixed with a few other strange ingredients from Stella's bag and the liquid inside the glass bottle turns into a deep crimson color. It glistens in the sunlight like a rare jewel.

    The way Stella holds it up makes the potion look beautiful and tempting, fleeting and temporary.
    """

    a "Are you trying to trick me into drinking a potion that will also bind me to you forever?"

    "Stella's previously elated expression dims down just slightly, as if trying to hide something."
    
    "Her emotions are so hard to understand. We tease each other all the time, so what's wrong?"

    menu ("", screen = "option"):
        "...":
            "Stella notices your concern and quickly shakes her dimmed expression off of her face. She laughs off the tension."

            s "Haha, of course you shouldn't want to spend eternity with me. Persephone also fell into that fate by accident, what sane person would make that kind of choice?"
             
        "What's wrong?":
            a "What's wrong?"
            "Stella looks away and pouts."
            s "Nothing! I guess you wouldn't want to spend eternity with me, and I wouldn't want to do that with you either!"
        
    "I look into Stella's eyes, her gaze is deep and confusing. Specks glimmer in her cosmic-latte-colored irises, applying even more complexity."

    "It's like I can see galaxies swirling in her eyes, silver clouds spinning in a vast universe of secrets. Her cheeks are flushed, though hardly noticeable under her dark skin."
    "Even after all these years, her emotions can be so difficult to understand."

    menu:
        "Should I drink Stella's underworld potion?"
        "Drink the potion":
            #$ fantasypoints += 1
            jump drinkThePotion
            
        "'Miss-Worst-Cook'":
            #$ realitypoints += 1
            jump dontDrinkThePotion

label drinkThePotion:
    
    #start drinking potion
    $ fantasypoints += 1
    """
    Without another second to delay, I snatch up the bottle from her hand and start chugging away.

    With each gulp the potion becomes harder to swallow, but I am determined to finish every last drop.

    I pull my lips away from the bottle, a burning sensation in my throat. The aftertaste is even more bitter, something I didn't even think was possible.
    """
    a "*COUGH* *COUGH* *COUGH*"
    s "Aurora! What's wrong with you! I didn't expect you to actually drink it!"

    """
    As I continue with my coughing fit Stella hits me on the back repeatedly with a shy rage, trying to coax out the rest of the liquid trapped in my throat.

    I finally calm down, wiping away the tears that built up on my eyelashes and clearing my throat.

    Stella's eyes, worried and attentive, stare into mine. She's holding her breath waiting for what happens next.

    But apart from the horrible taste in my mouth, I don't feel any different. 
    """

    menu ("", screen = "option"):
        "That was awful!":
            a "Yuck! That tasted awful..."
            s "Why did you drink it! Anyone in their right mind wouldn't try something like that!"
            s "We're lucky it didn't actually do anything... what if you grew a tail or something?"
            a "Then it would've been worth it to aid you in your experiments."
            s "Oh, be serious! You're still so childish." #show her smiling

        "Lie and say it tasted good":
            a "Yummm... this is definetely one of your better potions."
            s "Don't lie to me! You almost just choked to death!"
            a "Hahaha. I would drink it all over again just for you!"
            s "Don't say things like that! It's embarassing..."

    """
    Stella launches herself into my arms, trapping me in a tight embrace.

    I must have really worried her, but judging by the way her usually calm self holds me close, I can tell our bond is even deeper than before.
    """
    jump roseGarden

label dontDrinkThePotion:
    #start of not drinking the potion
    $ realitypoints += 1
    a "I'm not eating or drinking anything Miss-Worst-Cook makes."
    s "..."
    "There is an unbearable silence for a few moments. Stella looks at me blankly, as if I have somehow stopped time and frozen her in this moment."
    "Why did I say that?"
    "Where did that come from?"
    a "Stella... I-"
    "The usual soft whistles of the wind traveling through the trees' branches suddenly turns harsh and loud."
    "The strange winds create an almost omniscient resonation within the pomegranate trees. Leaves fall down from the treetops and swirl like strange musical notes falling off the staff. The foliage dances a strange waltz mid air."
    "I look around, unsure of what caused this interruption. Nothing like this ever happens in this peaceful, quiet world that Stella and I live in. It's unnerving, and I feel myself getting cold and clammy."
    "I turn to Stella, wanting to see her reaction to this strange event... but she just stands there, smiling."
    "Her smile is a familiar one: the kind of smile she gives me when I correctly guess the next ingredient in a potion, or when I bring her something she needs before she asks for it. The same smile that she would give me as kids when we had a good round of Spell Duals."
    "Her reaction confuses me, it's as if she's completely unfazed by the sudden change in our environment."
    "But before I can say anything else, she is already walking away, her wild silver waves bouncing slightly behind her."
    "The wind has stopped."
    jump roseGarden

    #a "No way! No matter how much I love you, I'm not drinking that..."
    #a "I don't even know what it's supposed to do."
    #s "I thought so! You've been a bit of a coward ever since we were kids. Haha"
    #"Her concerning expression goes away, and she has immediately gone back to teasing me."
    #a "On second thought, maybe I will take a sip! You'll feel sorry when I become invisible or start to grow extra limbs."

label roseGarden:
    scene bcevent2
    #start of rose garden/ event 2
    #INCLUDE TRANSITION FROM EVENT 1 TO EVENT 2
    """
    We walk back to the cabin toward the rose garden that Stella has grown and tended to for years.

    Neither of us speak of what happened in the forest. She hasn't looked back at me.

    The silence is bearable. It's a small walk and we reach the garden in no time. I'm just happy to be by her side.

    The sunlight reflects off of the pure-white roses and hits me in the eye. Without realizing it, a single tear streams down my face.
    """
    s "What's wrong? Is the state of my garden that bad?" #shes smiling
    "I wipe away the tear and laugh. The usual Stella is back."
    a "It's nothing. It's probably just the pollen."
    s "If you're allergic to the pollen you should just go inside. Don't put yourself in uncomfortable situations for me."
    menu ("", screen = "option"):
        #"What should I do?"
        "Grab the watering can":
            "I grab the nearby watering can and start watering the rose bushes without missing another beat."
            a "It's fine, see? I can still work."
            s "Okay then, as long as you're useful." #smiling
    "I keep watering the bushes, watching the clear dew form on top of the rose petals. The drops of water catch the light beautifully, absorbing the subtle tones of the sky."
    "Stella only grows red and white roses. She doesn't even grow any other flowers unless she needs something for a specific spell or potion. She likes to keep her garden simple, which I find ironic considering the complexity of her emotions."
    "While I water the roses, Stella mixes some of her potions in the soil. A while ago she figured out a way to make a potion that replaces fertilizer."
    "I watch as she takes a loose chunk of her silver hair and swipes it elegantly behind her ear. She looks so natural in a sea of roses, each flower enhancing her natural beauty."
    "The deep floral scent and the classic beauty of the roses combined with incoming sunset make for such a romantic environment."
    "I'll take advantage of this opportunity."
    menu ("", screen = "option"): #COME BACK TO THIS AND FIX IT
        "You look beautiful":
            a "Even among this sea of roses you manage to be the most beautiful."
    "I pluck a rose from its bush and hold it out toward Stella, motioning her to accept it."
    s "Why are you saying things like this all of a sudden..."
    a "Sorry, but it's true. I can't help myself."
    "She looks away shyly, embarassed by my boldness."
    s "No... it's not true. I don't fit in with these roses."
    a "How come? I think you match their beauty perfectly."
    "She looks down at the rose in my fingers: A vibrant red rose in full bloom."
    s "Haha, the red roses are so bright and full of life. They're bold and their meaning is never questioned."
    s "Meanwhile I'm dull and insecure. And I have a hard time dealing with the kind of passion a red rose brings."
    menu ("", screen = "option"):
        "I like you the way you are.":
            a "I like you exactly the way you are. You don't need to change anything."
        "Good thing I prefer white roses.":
            a "It's a good thing I prefer white roses to red ones, then."
            #stella blushing
    s "Stop that...you're just trying to make me feel better."
    a "Either way, as long as it's working."
    "I watch her as she presses the backs of her hands to her face, trying to cool down her flushed cheeks."
    a """
    Each rose has it's own charm.

    Actually, I remember since we were younger you've always preferred white roses.

    Remember that time we had a fight over which color rose was prettier? Hahah, things used to be so much simpler.
    """
    "Stella brings her face away from her hands and chuckles fondly at the memory."
    s "Yup, you really wanted to be right back then."
    a "I take back what I said back then, white roses are definetely prettier. They look better on you."
    s "Stoppp all you do is tease me. It's like you enjoy seeing me embarassed."
    "Her smile is much brighter than it was just a few moments before as she pushes me on the shoulder gently."
    a """
    Not only that, but white roses are more elegant, more delicate, harder to care for.
    
    You have to be more careful with them, because the smallest actions can blemish their petals.
    """
    s "Alright, alright, I get it. You can stop teasing me now."
    a """
    Plus, their color reminds me of you.
    
    When I look at a white rose I can only see you, your hair, and your eyes. It makes me smile.
    """
    s "Stop it already!"
    "She finally takes the red rose from my hand and glances away quickly as if trying to shake the blush away from her cheeks."
    "She bends down briefly and plucks a white rose, holding both of our cut flowers in her hand."

    s "Tell me... If you were to pick just one of these flowers, which one would you choose?"
    """
    Intrigued by her question, I take another look at the flowers held within her palms.

    The red rose is being held in her left. It looks fresh, vibrant, lively, and ... oddly familiar despite it being one of hundreds.

    The white rose is being held in her right palm. As my eyes come across it that blinding light stings me once more. It's the same 
    glare that caused me to shed a tear as Stella and I arrived at the garden earlier.

    It's strange. By now the sun's light, which would have been reflected, has dimmed.

    Involuntarily my breathing speeds up, my heart trembling within my chest. My thoughts are suddenly cloudy. My head is spinning.

    Was that blinding light earlier just a coincidence? Either way, something about this white rose unnerves me deeply, although I can't even begin to understand why.

    But there's no time to worry about myself and my racing thoughts, right now all that matters is Stella.
    """

    menu:
        "Which of the roses should I take from Stella's hands?"
        "Take the white rose":
            jump takeWhiteRose
        "I want to- put this ... red rose here":
            jump takeRedRose

label takeWhiteRose:
    "I wrap my fingers around hers, taking the white rose in my hand."
    a "What kind of question is that? Of course I'd pick the white rose. The one that reminds me the most of you."
    "The flush in Stella's cheeks comes back in a sharp wave. Her affectionate eyes soften, yet there is a sense of subtle complicated emotions behind her silver irises that I can't quite read."
    "We stand in silence for only a few moments, my hands still wrapped around hers, until she drops her head on my shoulder and whispers."
    s "I'm happy... that you're choosing me like this. But..."
    "But?"
    s "But you shouldn't act like this anymore. When will you understand..."
    "Her soft voice trails off in defeat. I can barely make out what she says."
    "Her strange habit of suddenly speaking in riddles always comes at the worst time. How am I supposed to decipher what she means? How am I supposed to decipher her heart?"
    menu ("", screen = "option"):
        "I choose you.":
            a "I chose the white rose, and I chose you."
    "Her head is still hanging on my shoulder. Her hands are uncharacteristically cold."
    s "Stop talking. You really haven't changed a bit since then..."
    "Among the rose-filled pasture, she is still the only thing I can see."

label takeRedRose:
    #JKLFDLJDSF
    "My vision blurs, a throbbing headache appears. I can't think."
    a "I know it's not appropriate... but I want to- this red rose here."
    "I don't feel my mouth move, but words come out. With my fists I attempt to rub out whatever has overtaken my vision."
    "When I open my eyes I see Stella staring back at me, a dumbfounded expression on her delicate face."
    s "What did you just say?"
    "Wait... was that voice me? Did I say that? I don't know what came over me, or why my head still throbs."
    "Stella's expression softens. She gives me an understanding smile."
    if realitypoints >= 1:
        #CHOSE REALITY OPTION BEFORE
        "She is smiling warmly again. That familiar, comforting smile."
        "Neither of us say anything more."
        "That same tune that appeared in the forest appears again, the strange wind moving away the clouds from the sky."
        "The harsh light from the sky reflects off of the white roses, blinding me again."
        "The light gets brighter and brighter. I instinctively cover my eyes with my hand. I tear up again, the headache worsening, throbbing even worse than before."
        "The landscape around us seems to distort. The strange song emerges from the previously meek wind as it pushes the clouds away, casting a bright light onto the white rose petals."
        "The harsh light blinds me again and I instincively bring up my hands to shield my eyes. I tear up again. The headache worsens."
        "The landscape around me seems to distort: rose stems growing and thinning, curling around each other, cutting each other with their thorns."
        "I'm overwhelmed, afraid. Was this all triggered by a single red rose? What does this have to do with the previous event in the forest?"
        "Through blurry and wavering eyes I look at Stella, who has already turned and started walking toward the cabin."
        "She turns her head over her shoulder, silver hair swaying gently, and smiles at me."
    elif realitypoints= 0:
        #FIRST TIME CHOOSING REALITY OPTION
        "Her smile is a familiar one: the kind of smile she gives me when I correctly guess the next ingredient in a potion, or when I bring her something she needs before she asks for it. The same smile that she would give me as kids after a good round of Spell Dual."
        "The harsh light from the sky reflects off of the white roses, blinding me again."
        "The light gets brighter and brighter. I instinctively cover my eyes with my hand. I tear up again, the headache worsening, throbbing even worse than before."
        "A strange song emerges from the previously meek wind as it pushes the clouds away, casting a bright light onto the white rose petals."
        "The harsh light blinds me again and I instincively bring up my hands to shield my eyes. I tear up again. The headache worsens."
        "The landscape around me seems to distort: rose stems growing and thinning, curling around each other, cutting each other with their thorns."
        "I hear sounds and see things I've never experienced before in Stella and I's quiet world."
        "I'm overwhelmed, afraid. Was this all triggered by a single red rose?"
        "Through blurry and wavering eyes I look at Stella, who has already turned and started walking toward the cabin."
        "She turns her head over her shoulder, silver hair swaying gently, and smiles at me."

    "Did I make her upset? Should I have chosen the white rose instead? What triggers her strange behavior?"
    "There are too many feelings... too many questions. The wind has gone and the distortion has ceased: reverting back to the world I'm used to"
    "I go back inside after Stella, deciding to lie down for a while."
    jump event3

label event3:
    scene bcevent3
    "..."
    "I don't know how long I slept, but the window displays the somber darkness outside. It must\'ve been a considerate amount."
    "Today's events completely exhausted me."
    "The cabin is completely dark except for the flickering flame of a single white candle."
    "I can barely make out Stella's face: one side cast in a warm light, the other completely hidden in the darkness."
    "Stella sits at the windowsill, her nose in yet another book: a small hardcover collection of existing poems that she bound together herself."

    s "You're awake. I have something to tell you."
    "She closes the book and leaves it on the windowsill."
    s "I... have to leave now."
    menu:
        "Where are you going?":
            a "Where are you going?"
        "This late?":
            a "You're going out now? It's so dark outside."
    "She doesn't answer. Instead, she looks out the window into the dark night. Her eyes scan the barely recognizable woods and the white stars in the sky."
    a "It's really dangerous to leave at this time... When are you planning on coming back?"
    "Still silent. Now her gaze is fixed onto a specific point, unwavering."
    menu:
        "Are you okay?":
            a "Stella? Is everything alright?"
            s "I'm okay."
            "She has already decided what she wants to do. There's nothing I can say to convince her to stay."
            a "I don't know where you're going... but I want to come with you."
            "I have to go with her. Wherever she goes I have to be by her side. The thought of her leaving gives me a desperate ache in my chest."
        "Can I come with you?":
            a "Stella? Can I at least come with you?"
    s "No... I know you need me. I know it's just been us for a long time. But... I have to do this."
    "She continues staring into the starry night, and I can spot moisture on her cheek."
    if fantasypoints = 2:
        jump goAfterHer
    elif realitypoints > 1:
        jump dontGoAfterHer

label goAfterHer:
    #go after her
    s "Goodbye."
    "Without another word she rushes out the door, her long skirt swaying behind her."
    "Panicking, I pick up the candle that's burning on the windowsill and run out after her."
    "She's always been fast and elusive. I sprint after her as best as I can, but it takes me a while before I reach out for her shoulder and force her to stop running."
    #FINISH LATER

    jump fantasyEnding

label dontGoAfterHer:
    "I dont go after her"
    menu:
        "Do not go gentle into that good night.":
            a "i am saying somethign!!!WW!!E!E!E!E!"
        #FINISH LATER
    jump true

label fantasyEnding:
    #THIS IS WHERE THE FANTASY ENDING GOES
    #FINISH LATER
    jump endCredits

label endCredits:
    scene bgEnd1
    "You have finished the game."

label oldThing:
    #a "Oh..."
    #a "Is it already this late...?"
    #"It's a normal day, but it's not normal that I wake up when the sun is already going down."
    #a "Stella"
    #"..."
    #a "Stella?"
    #"......"
    #s "Stella!"
    #"........."
    #"It's so slient. She doesn't seem to be here."
    #"............."
    #"Stella is not home."
    #"Looking aroud, you realize there is a photo of Stella in your pocket."
    #"You took it out and lifted up to your vision."
    #menu:
     #   "She's beautiful":
      #      a "I should head out to look for her. It's getting late."
       # "WHERE IS SHE":
        #    a "I should head out to look for her. It's getting late."
    
    #a "There is just one path stretching out from my home."
    #a "I just need to follow along -- there's no other way Stella could go."
    #"..."
    #"......"
    #"........."
    #"........................"
    #"You have no idea how long it has been."
    #"It's always the same path."
    #"It's leading me to nowhere."
    #a "Why can I still see my house...?"
    #a "Why is still dusk...?"
    "You sit down paralyzed on the dirt ground."
    "..."
    s "Aurora"
    "!!!"
    a "Is that you?!"
    "......"
    "I turn around, and around, and Stella is just in front of me."
    s "Hey Aurora."
    "Her voice sounds unfamiliar."
    a "What do you mean \"hey\"? Where have you been? It\'s late!"
    s "I think this should be the end."
    a "...?"
    s "Like anything, including life, there's the end of you and me."
    a "Wait... what on earth are you talking about?"
    "In a blink of an eye. Stella disappeared."
    "Her soft voice remained and echoed profoundly."
    
    menu:
        "No. Our story is IMMORTAL.":
            jump bad
        "What's this end... Is it really the end?":
            if fantasypoints >= 2:
                jump bad
            else: 
                jump true

label bad:
    scene bcend1
    """
    .....

    


    """

    "......"
    "Birds are chirping."
    "It's dawn."
    "......"
    a "So... that was a dream."
    a "What a dream..."
    "You managed to get up from the soft pillow."
    "(Szzzzzzzzz~)"
    "The familiar and appetizing sound of Stella frying eggs comes from the kitchen."
    "It's just another day."
    a "And there'll be infinitely many other days just like today."
    "Stella comes over, taking off the warm-colored apron."
    s "Breakfast's ready!"
    a "You looks happier than normal."
    "And you don't know why -- she also looks sadder than ever before."
    "Stella makes a puzzled face to your words, and then smiles and moves away, which tells you to hurry up."
    a "Yeah, I'm not letting her go. NEVER"
    "......"
    "Bad Ending: Forever and Ever"

    return

label true:
    "......"

    a """
    Where am I?

    My head hurts...
    """
    jump find

label find:
    scene bcend2
    menu :
        "There's something over there..."
        "Garnet earrings":
            a """
            A pair of earrings with inlaid garnet stones. The dark red color looks almost black.

            These aren\'t mine...

            These are...
            """
            $ x[0] = 1

        "A notebook":
            a """
            One of those small hardcover bound notebooks with a ribbon bookmark.

            I open it up to the bookmarked page, revealing a pressed white rose.

            The fragrance of the rose has almost worn off.

            There\'s... someone\'s funeral...
            """
            $ x[1] = 1
            
        "A poem":
            a """
            A poem from an author called Dylan Thomas.

            The title reads... \"Do not go gentle into that good night\".

            She used to love this poem.
            """
            $ x[2] = 1
        
        "Old Card Deck":
            a """
            An old hand-made card deck. The title of the game is written in water-based marker on the back of every card.
            
            \"Spell Dual\".

            ...

            \"Spell Dual\"...

            ...
            """
            $ x[3] = 1
        
    if x[0] == 1 and x[1] == 1 and x[2] == 1 and x[3] == 1:
        jump found
    else:
        jump find

label found:
    a """
    I remember now...

    Stella, my one and only friend...

    I didn't... get to tell you...

    I used to play pretend in a treehouse with Stella.

    We would dress up as little witches, and play that card game together...

    In retrospect, my love started to grow away back then...

    Then, that night, the prom...

    The funeral...

    The day I had to sort out her things...
    """

    "Stella shows up in her prom dress."

    s """
    It has been too long since then, Aurora...

    You know our fantasy world is not real.

    You know you are no longer 17.

    You can't live like this anymore.

    Daydreaming is fun when we were together. But you should not throw away your life like this.
    """

    menu:
        "I didn't get to tell you how I feel about you.":
            s """
            I know. I always know.

            That is why it hurts so much for me to see you like this.

            Go back to school.

            Find a job...

            For me, please?

            I am your memory.

            Stella would have wanted you to move on.

            And deep down in your heart, you know that.

            She wouldn't want you to escape from reality. She doesn't wnat you to escape from anything!

            I am distant because you knew deep down that she would want this for you.
            """
        
        
        "Is that why you were so distant to me?":
            s """
            I am your memory.

            Stella would have wanted you to move on.

            And deep down in your heart, you know that.

            She wouldn't want you to escape from reality. She doesn't wnat you to escape from anything!

            I am distant because you knew deep down that she would want this for you.
            
            I know. I always know.

            That is why it hurts so much for me to see you like this.

            Go back to school.

            Find a job...

            For me, please?
            """
    
    a """
    It's scary to live in a reality without you.

    I don't want to leave you...
    """

    s """
    You have to venture on.

    Without me.

    Be brave, Aurora!

    I'm always with you.

    In the fantasy we made together, in the worlds we built together.

    In those silly witch stories we wrote together
    """

    a "I love you."
    s "I love you too."

    "True Ending: Venture On"

    jump endCredits
    
##UNUSED EVENT.. i just didnt want to erase it lol
#label pickRedRose:
    #picking a red rose for stella
 ##  "Red roses... the classic symbol of love."
   # "I hold the rose and approach Stella, holding it out for her, expecting her to accept my gift the way she has always accepted my gifts."
    #a "This is for you."
    #s "..." #blushing expression ???
    #a "What's wrong?"
    #"She has never rejected me this way before..."
    #s "Ah... to be honest I'm not too fond of red roses recently."
    #a "How come?"
    #s "They're just... so cliche don't you think?"
    #menu:
     #   "They're not cliche":
      #      a "I don't think they're cliche. They're timeless and romantic."
       #     s "Haha, don't talk about romance with me!"
        #    s "I prefer the white roses. They're less...concrete."
#too vibrant, too alive, nake it obvious that she feels like it doesnt fit her
        #"You're right. White roses are better":
         #   a "Now that I think about it, you're right! The white ones are even more beautiful."
          #  s "Exactly! They're pure and can hold so much meaning beyond just love or romance or passion."

####################################################END OF NEW VERSION
####################################################THE OLD VERSION!!!!
label start2:

    scene background

    show aurora_test

    "You wake up in a lush green field, unfamiliar flowers and scents surrounding you. The gentle sunlight, speckled by the trees, dances on your face."
    "You blink awake, and as you turn your head to the side you spot a girl sitting next to you. She looks uninterested, spacing out, she traces the horizon with her eyes."

    "She notices your subtle movements and turns to look at you."

    s "You're awake. You usually sleep for a little longer."
    "She looks at you blankly as she tucks a strand of her thick hair behind her long pointed ears."

    menu:
        "Who are you?":
            s "Did you forget my name again? (She says with a sympathetic smile)."
            s "It's Stella."
            "Before you have time to ask any other questions, Stella gets up, brushing off her legs."
            s "Come on, it'll get dark soon. You said you would help me gather the ingredients for that potion I wanted to make."
            menu:
                "Right...":
                    jump goToGrove
                "Of course.":
                    jump goToGrove

label goToGrove:
    "You get up, but before you meet her eyes she turns over her shoulder and starts walking toward the crowd of fruit trees."
    "She walks proudly and quickly, her hair swinging back and forth, her shoulders rolled back."
    s "Come on, slowpoke (she says with a teasing grin)"
    "You jog a few steps to catch up until you are walking with her side by side"
    menu:
        #"You try and talk to her some more"
        "What kind of potion are you going to make?":
            s "Hmm..... now you care? When I first told you about it you didn't seem that interested."
            a "Well I want to know now."
            s "I forgot the name, it's just this thing I wanted to try. It's not like you're doing anything else today, so I made you come along."
        "Your hair looks nice today":
            s "Ughhh...(she groans)"
            s "If you're going to compliment me at least make it better than /that/."
            menu:
                "I'm taking it back then!":
                    "She lets out a laugh, raising her hand to ever so slightly cover her lips"
                "Sorry":
                    a "I'm sorry, I guess I run out of words when I'm around such a pretty girl."
                    #show stella blushing
                    "She nudges you on the arm playfully"
            s "Stop messing around, we're almost at the orchard."

#insert transition to orchard
s "Here, take this"
"She hands you a redish-orange fruit, then another, and another."
a "Do you really need this many?"
s "Hey, why did you come along if you're just going to complain?"
s "Obviosly I don't need this many for just one potion (she rolls her eyes)"
"She sets another fruit on top of your hands"
s "Pick one! The best one!"
menu:
    "Which one should Stella use for her potion?"
    "First fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Yup! This is a good one."
        jump makePotion
    "Second fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Yuck! This one has a weird... gushy spot."
        s "Pick another one..."
        menu:
            "First fruit":
                "You hand her the first fruit and she looks at it very carefully."
                s "Yup! This is a good one"
                jump makePotion
            "Third fruit":
                "She holds the fruit up to her face and sniffs it."
                s "Perfect! This is exactly what I needed."
                jump makePotion
            "Fourth fruit":
                "She holds the fruit up to her face and sniffs it."
                s "Ew! This one's rotten... what is it doing with the rest of these?"
                s "Pick a different one."
                menu:
                    "First fruit":
                        s "Yup! This is a good one."
                        jump makePotion
                    "Third fruit":
                        s "Perfect! This is exactly what I needed."
                        jump makePotion
    "Third fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        s "Perfect! This is exactly what I needed."
        jump makePotion
    "Fourth fruit":
        "Stella takes it from your stack and palms the fruit in her hands, looking at it from all sides with the gaze of a connosieur"
        "She holds it up to her face and sniffs it."
        s "Ew! This one's rotten... what is it doing with the rest of these?"
        s "Pick a different one."
        menu:
            "First fruit":
                "You hand her the first fruit and she looks at it very carefully."
                s "Yup! This is a good one"
                jump makePotion
            "Second fruit":
                s "Yuck! This one has a weird... gushy spot."
                s "Pick another one..."
                menu:
                    "First fruit":
                        s "Yup! This is a good one"
                        jump makePotion
            "Third fruit":
                s "Perfect! This is exactly what I needed."
                jump makePotion  

label makePotion:
    #make potion in here.... onl y happens after first or third fruit is chosen.
    "Stella crouches on the floor and pulls out an assortment of containers"
    "She rips open the fruit with her hands, pomegranate seeds pouring out and sprawling all over her lap, a few small drops of red forming on her clothes."
    "She takes three small pomegranete seeds out of the hundreds and drops them one at a time inside the bottle. With a small pestle from her bag she crushes the seeds into a hard pulp inside the bottle, then takes out a small powder satchet and pours it in as well."
    "It turns an ominous, dark-red and murky color, and the sweet smell of the fruit is gone. Then she takes another container and pours its liquid inside the bottle, swirling the mixture around gently."
    "She smells it and makes a face, but hides her disgust with a mischevious smile."
    s "Here!"
    s "Drink it!"
    a "What? You want me to drink that?"
    s "Yeah that's what I just said."
    "She pushes the bottle right in front of your face, her smile bright. You haven't seen her smile like that before. She looks at you with pleading eyes"
    s "Come on, drink it! Be my test subject."
    menu:
        "Will you drink Stella's potion?"
        "Drink it":
            jump drinkPotion
        "Don't drink it":
            jump dontDrinkPotion

label drinkPotion:
    $ fantasypoints += 1
    "You take the bottle and bravely chug it as Stella watches with wide eyes."
    a "*Burp*"
    s "Hahahaha"
    "You try and ignore that burning sensation in your throat as Stella laughs, rolling around in the dirt with amusement."
    "It takes her a while to calm down as you chug water that she conveniently laid out before you drank the potion."
    s "I can't believe you actually did it! You're crazy."
    menu:
        "Crazy for you":
            #show stella flushed
            s "Hey! Stop that!"
            s "You better not expect anything out of complimenting me, you got that?"
            s "Geez..."
        "I regret everything":
            "She continues laughing."
            s "Aw man, I knew it was gonna be bad, but I didn't know it would be *that* bad!"
            a "The things I do for you..."
            "Stella gives you a solemn look and a slight smile."
        "That tasted awful!":
            "She continues laughing."
            s "Aw man, I knew it was gonna be bad, but I didn't know it would be *that* bad!"
            a "The things I do for you..."
            "Stella gives you a solemn look and a slight smile."
    s "Come on!"
    "She stands up, throwing all her leftover containers halfhazardly back into her bag."
    s "There's another place I want to check out today before it gets dark!"
    menu:
        "What place?":
            s "The rose garden!"
    s "You know how much I like roses. I keep walking by this garden on my way back to town, but I never have time to go inside and take a closer look."
    s "That's why I'm dragging you with me today!"
    menu:
        "Stella wants you to go to the rose garden with her"
        "With pleasure":
            "She rolls her eyes at you and pulls you up."
            s "Ok, Cassanova, let me lead the way!"
        "Fine...":
            s "It seems like you're getting a little tired of me, but that's fine!"
            s "It's not like you're my only friend around here anyway."
    "The two of you gather yourselves and make your way to town to view the rose garden"
    jump event2

label dontDrinkPotion:
    $ realitypoints += 1
    a "No way! I'm not drinking that! What is it supposed to do anyway?"
    s "Tch..."
    s "Come onnnn you're no fun."
    menu:
        "Never in a million years!":
            s "Tch..."
        "Don't even think about it":
            s "Tch..."
    "Stella scoffs, but doesn't try to convince you any more."
    s "You never really liked my cooking anyway."
    a "Is this considered cooking?"
    "She frowns but only for a second before She takes the potion bottle and throws it a few feet away. You watch the glass shatter and the suspicious-looking liquid seep into the dry dirt."
    s "Well, I wasn't gonna drink it."
    "She stands up, throwing all her leftover containers halfhazardly back into her bag."
    s "There's another place I want to check out today before it gets dark!"
    menu:
        "What place?":
            s "The rose garden!"
    s "You know how much I like roses. I keep walking by this garden on my way back to town, but I never have time to go inside and take a closer look."
    s "That's why I'm dragging you with me today!"
    menu:
        "Stella wants you to go to the rose garden with her"
        "With pleasure":
            "She rolls her eyes at you and pulls you up."
            s "Ok, Cassanova, let me lead the way!"
        "Fine...":
            s "It seems like you're getting a little tired of me, but that's fine!"
            s "It's not like you're my only friend around here anyway."
    "The two of you gather yourselves and make your way to town to view the rose garden"
    jump event2

label event2:
    #scene rose garden
    "You both walk into the garden, the sweet floral smells almost overwhelming your senses, stinging your eyes."
    s "Wow! It's so much prettier than I imagined."
    "You watch by her side as she skips around the enclosed area, walking beneath floral arches and in between small fountains and benches. The entire garden is made up of only two colors of roses: red and white. "
    "She picks a white rose off of one of the bushes, cutting the thick stem with her long, dagger-like nails."
    
    "She presses her thumb firmly on one of the rose's thorns, her gaze low and uninterrupted. She looks lost in thought, as if she's forgotten that you are there too."
    s "I prefer the white ones over the red. I think red roses are too cliche..."
    "She continues gripping the thorns, twirling the untamed rose in her bare hand."
    s "These flowers are beautiful."
    menu:
        "I think you're more beautiful":
            #show stella flushed
            s "How can you say things like that with a straight face?"
            s "Stop it..."
            a "It's true."
            "She glances at you, her grip on the rose weakening."
            s "Geez... hahah"
        "Yes they are":
            s "I'm glad we're agreeing on something!"
    s "Which ones do you think are better? The red or white roses?"
    menu:
        "Which roses do you prefer?"
        "Red":
            jump redRoses
        "White":
            jump whiteRoses
        "Pink":
            jump pinkRoses

    label redRoses:
        s "The red ones?" #show stella disgusted
        s "Ugh, I bet you don't even have a preference, you just want to go against what I say."
        a "No, I love red roses. They're the classic symbol of romantic love."
        s "Gross! Don't talk about romance with me!"
        s "White roses are so much better! They're pure and simple. Plus, they're not purely romantic. They're about remembrance and respect. Something that you should
        have for me!"
        menu:
            "I respect you":
                $ fantasypoints += 1
                a "Oh, beautiful Stella, I have so much respect for you. You have made me see the error of my ways."
                a "You're right, white roses are much better."
                #show stella happy
                s "Mhm! That's what I thought."
                jump event2End
            "Let's agree to disagree":
                $ realitypoints += 1
                a "Let's agree to disagree."
                s "Fine by me... If you're fine with being wrong!"
                "You both laugh and continue to look around the garden together, Stella now loosely holding the white rose between her reddened fingers."
                jump event2End
            "Red roses are more popular for a reason":
                $ realitypoints += 1
                a "Well, the red ones are more popular for a reason."
                s "Yeah... you would think that."
                "She laughs and you both continue to look around the garden together. Stella's white rose now being loosely grasped between her reddened fingers."
                jump event2End
    label whiteRoses:
        $ fantasypoints += 1
        a "Of course I agree with you. The red roses are too cliche, white ones are much better. It's not even a competition."
        s "Exactly!"
        s "Wait..."
        s "You're not just agreeing with me right?"
        menu:
            "Of course not!":
                a "No not at all! Your opinion is simply the correct one."
                s "Hahaha, good to know."
                jump event2End
            "Yes I am":
                a "Yeah, I am. I don't care too much about roses, I just like seeing you happy."
                "Her cheeks flush as red as the flowers around her."
                s "You shouldn't try so hard... It's not going to get you anywhere!"
                a "Sorry, sorry. I can't help myself."
                jump event2End
                

    label pinkRoses:
        s "Oh come one! Be serious. There's no pink roses here."
        a "You didn't say I had to choose a rose that was in this garden."
        s "Nooo, I asked you if red or white roses were better."
        a "Well I like them both, and I think they can coexist in one rose."
        s "Tch... Come on. You have to pick one!"
        menu:
            "Which roses do you prefer?"
            "White roses":
                jump whiteRoses
            "Red roses":
                jump redRoses

    label event2End:
        #end event 2
        "The sun is starting to set, turning the white roses into a light orange. It feels like hardly any time had gone by, but its already dawn."
        "Stella notices this and turns to make her way toward the exit."
        "She lets go of the white rose she was holding, letting fall onto the dirt."
        a "You're not taking it with you?"
        s "Nope... Everything must go back to where it came from , right?"
        "You notice the sun setting far behind the arch of roses."
        "Stella continues walking forward, a small skip in her step. You both have seen all there is to see at the rose garden, and make your way back to town to rest."


screen option_e(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in range(0, 2):
                button:
                    if i == 0:
                        background Frame("gui/button/choice1_idle_background.png")
                        hover_background Frame("gui/button/choice1_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    elif i == 1:
                        background Frame("gui/button/choice2_idle_background.png")
                        hover_background Frame("gui/button/choice2_hover_background.png")
                        xysize(1920,150)
                        action items[i].action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text items[i].caption

screen option(ch, items):
        text _(ch):
            size 80
            color "#000"

        vbox:
            align (0.5,0.5)
            spacing 30
            for i in items:
                button:
                    background Frame("gui/button/choice_idle_background.png")
                    hover_background Frame("gui/button/choice_hover_background.png")
                    xysize(1920,150)
                    action i.action

                    hbox:
                        spacing 20
                        align (0.5, 0.5)
                        text i.caption