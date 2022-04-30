Debug=False
def DebugEnable():
    print("[DEBUG] Debugging started")
    print("[DEBUG] Importing 'datetime'")
    global datetime
    from datetime import datetime
    print('[DEBUG '+str(datetime.now())+"] Imported 'datetime'")
    global Debug
    Debug=True

def DebugLog(log=str):
    if Debug==True:
        print('[DEBUG '+str(datetime.now())+'] '+str(log))

#Uncomment to enable debug
#DebugEnable()

DebugLog("Importing library 'random'")
import random
DebugLog("Imported 'random'")

def GenerateName(nametype="random"):
    if str(type(nametype))!="<class 'str'>":
        DebugLog("'nametype' is not a string")
        raise TypeError
    DebugLog(f"Generating a name with type '{nametype}'")

    def dsmp():
        DebugLog("Generating a type 'dsmp' name...")
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        character=['Dream','TommyInnit','GeorgeNotFound','Sapnap','BadBoyHalo','Fundy','Wilbur','Skeppy','Technoblade','Ranboo']
        like=['ILike','ILIKE','ILove','ILY','ily','Ily','ILOVE']
        cool=['IsCool','ISCOOL','Iscool','IsAwesome','IsAWESOME','ISAWESOME','IsGreat','isCOOL']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        character=character[random.randint(0,len(character)-1)]
        like=like[random.randint(0,len(like)-1)]
        cool=cool[random.randint(0,len(cool)-1)]
        if random.randint(1,2)==1:
            part1=character
            part2=cool
        else:
            part1=like
            part2=character
        if random.randint(1,5)==3:
            subfinal=f'{part1}_{part2}'
        else:
            subfinal=part1+part2
        if "ily" not in subfinal.lower():
            if random.randint(1,3)==2:
                subfinal=f'{x}{subfinal}{x2}'
        if "ILY" in subfinal:
            subfinal=subfinal.upper()
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        DebugLog("Finished generating name")
        return str(subfinal)


    def weird():
        DebugLog("Generating a type 'weird' name...")
        wP1=['Fart','Poop','You','Hand','Arm','Mouse','Leg','Foot','Eye','Finger','Cat','Dog','Kitten','Puppy','Chair','Lamp','Bed','Anime','Human','Joe','Goop']
        wP2=['Licker','Eater','Maker','Shaker','Hater','Creator','Lover','Liker','User','Abuser']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        wP1=wP1[random.randint(0,len(wP1)-1)]
        wP2=wP2[random.randint(0,len(wP2)-1)]

        if random.randint(1,5)==3:
            subfinal=f'{wP1}_{wP2}'
        else:
            subfinal=wP1+wP2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,3)==2:
            subfinal=f'{x}{subfinal}{x2}'
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        DebugLog("Finished generating name")
        return subfinal

    def sus():
        DebugLog("Generating a type 'sus' name...")
        sP1=['AmongUs','Amongus','Amogus','Gus','Mogus','Emogus']
        sP2=['IsSussy','IsSus','IsWeird','IsCool','IsAwesome','IsGreat','IsBad']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        sP1=sP1[random.randint(0,len(sP1)-1)]
        sP2=sP2[random.randint(0,len(sP2)-1)]
        if random.randint(1,5)==3:
            subfinal=f'{sP1}_{sP2}'
        else:
            subfinal=sP1+sP2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,3)==2:
            subfinal=f'{x}{subfinal}{x2}'
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        DebugLog("Finished generating name")
        return subfinal

    def hypixel():
        DebugLog("Generating a type 'hypixel' name...")
        P1=['0H','0h','Oh','x','Ohhhhh','0hhhhh','ily','Ily','ILY','Best','Poggers','Pog']
        P2=['Duck','Ducks','Cat','Cats','Kat','Katz','Kats','Ducc','Duccs','Capybara','Capybaras','Puppy','Kitten','Kittens','Strong','Cool','Great','Sweaty','Insane','Amazing','Glue','Puff','Puffy','Poof','Fox','Foxxy','Doggy','Dog','Kitty','Apple','Pear','Orange','Velocity','Reach','Aura']
        x=['xx','Xx','XX','Oo']
        x2=['xx','xX','XX','oO']
        xsel=random.randint(0,len(x)-1)
        x=x[xsel]
        x2=x2[xsel]
        P1=P1[random.randint(0,len(P1)-1)]
        P2=P2[random.randint(0,len(P2)-1)]
        if random.randint(1,5)==3:
            subfinal=f'{P1}_{P2}'
        else:
            subfinal=P1+P2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()

        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')

        if random.randint(1,20)==10:
            if random.randint(1,5)==1:
                ms="MS"
            else:
                ms="ms"
            subfinal=str(random.randint(0,999))+ms
        DebugLog("Finished generating name")
        return subfinal

    def weird2():
        DebugLog("Generating a type 'weird2' name...")
        P1=['dex','slu','sla','pluh','ploo','bu','bo','blo','bla','zlu','plu','pla','pa','za','boo']
        P2=['muh','uh','guh','gen','n','gan','gon','slun','lun','blun','dun','gloo','ploo','pluh','oo','a']
        P1=P1[random.randint(0,len(P1)-1)]
        P2=P2[random.randint(0,len(P2)-1)]
        subfinal=P1+P2
        if random.randint(1,5)==4:
            subfinal=subfinal.upper()
        elif random.randint(1,5)==4:
            subfinal=subfinal.lower()
        if random.randint(1,20)==11:
            subfinal==subfinal.replace('o','0').replace('O','0').replace('s','5').replace('S','5').replace('e','3').replace('E','3')
        DebugLog("Finished generating name")
        return subfinal
    
    nametype=nametype.lower()
    if nametype=="dsmp":
        return str(dsmp())
    elif nametype=="sus":
        return str(sus())
    elif nametype=="weird":
        return str(weird())
    elif nametype=="hypixel":
        return str(hypixel())
    elif nametype=="weird2":
        return str(weird2())
    elif nametype=="random":
        DebugLog("nametype='random', choosing random name type")
        rand1=random.randint(1,5)
        if rand1==1:
            final=dsmp()
        elif rand1==2:
            final=sus()
        elif rand1==3:
            final=weird()
        elif rand1==4:
            final=hypixel()
        elif rand1==5:
            final=weird2()
    else:
        DebugLog("'"+str(nametype)+"' is not a valid nametype")
        raise ValueError
    return str(final)

def GenerateMessage(messagetype="random"):
    DebugLog("Generating random message")
    if str(type(messagetype))!="<class 'str'>":
        DebugLog("'messagetype' is not a string")
        raise TypeError

    def cringe():
        DebugLog("Generating a type 'cringe' message")
        cringe = ['mogus','cring','cringey','cringe']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        emoji = [":pensive:",""]
        cringe=cringe[random.randint(0,3)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]
        emoji=emoji[random.randint(0,1)]
        final = str(thats+" "+cringe)
        pos=random.randint(1,4)
        if pos==1:
            final = str(emoji+" "+bro+" "+final)
        elif pos==2:
            final = str(emoji+" "+final+" "+bro)
        elif pos==3:
            final = str(bro+" "+final+" "+emoji)
        elif pos==4:
            final = str(final+" "+bro+" "+emoji)
        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def sus():
        DebugLog("Generating a type 'sus' message")
        sus = ['mogus','sussy','sus','amogus','weird','wacky']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        emoji = [":flushed:",":face_with_raised_eyebrow:",":hot_face:",""]
        sus=sus[random.randint(0,3)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]
        emoji=emoji[random.randint(0,3)]
        final = str(thats+" "+sus)
        if random.randint(1,10)==7:
            sus=sus.upper()
        pos=random.randint(1,4)
        if pos==1:
            final = str(emoji+" "+bro+" "+final)
        elif pos==2:
            final = str(emoji+" "+final+" "+bro)
        elif pos==3:
            final = str(bro+" "+final+" "+emoji)
        elif pos==4:
            final = str(final+" "+bro+" "+emoji)
        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def twitter():
        DebugLog("Generating a type 'twitter' message")
        twitterphrases = ["cope harder","cope","L","dont care","ratio","blocked","touch grass","climb a tree","take a dump",":clown:"]
        loops=0
        final = twitterphrase=twitterphrases[random.randint(0,9)]
        while loops<3:
            if random.randint(1,30)==9:
                twitterphrase=twitterphrases[random.randint(0,9)].upper()
            else:
                twitterphrase=twitterphrases[random.randint(0,9)]
            final = final+" + "+twitterphrase
            loops=loops+1
        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def funny():
        DebugLog("Generating a type 'funny' message")
        funny = ['LOL','LUL','LOOOOOL','loool','lol','lul','funny']
        final=funny[random.randint(0,6)]
        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def good():
        DebugLog("Generating a type 'good' message")
        good = ['pog','poggers','pogggggg','good','awesome','amazing','insane','cool','not cap']
        thats = ["that's","thats","that is"]
        bro = ["broski","bro","man","brother"]
        good=good[random.randint(0,8)]
        thats=thats[random.randint(0,2)]
        bro=bro[random.randint(0,3)]

        final = str(thats+" "+good)
        if random.randint(1,10)==7:
            good=good.upper()
        pos=random.randint(1,2)
        if pos==1:
            final = str(bro+" "+final)
        elif pos==2:
            final = str(final+" "+bro)

        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def dsmp():
        DebugLog("Generating a type 'dsmp' message")
        love = ['i love','anyone else love','I LOVE','ANYONEEEEE LOVE','I LIKE','i like','any1 else like','anyone else really love']
        emojis= [':hot_face:',':smiling_face_with_3_hearts:',':drooling_face:',':two_hearts:',':heart_eyes_cat:',':heart_eyes:']
        dsmpchar = ['dream','tommyinnit','ranboo','sapnap','georgenotfound','badboyhalo','tubbo','wilbur','quackity']
        love=love[random.randint(0,7)]
        emoji=emojis[random.randint(0,5)]
        dsmpchar=dsmpchar[random.randint(0,8)]
        final = str(love+" "+dsmpchar)

        pos=random.randint(1,2)
        if pos==1:
            final = str(emoji+" "+final)
        elif pos==2:
            final = str(final+" "+emoji)

        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def poop():
        DebugLog("Generating a type 'poop' message")
        ims = ['anyone else','im really','any1 else really','im so','bro im so','why am i so','why am i','help im really']
        emojis= [':stuck_out_tongue:',':confounded:',':weary:',':tired_face:',':persevere:',':worried:',':face_with_symbols_over_mouth:',':grimacing:']
        thing = ['constipated','gassy rn','gassy','full of gas','runny','constipated rn','constipated right now','gassy right now']
        im=ims[random.randint(0,7)]
        emoji=emojis[random.randint(0,7)]
        thing=thing[random.randint(0,7)]
        final = str(im+" "+thing)
        if random.randint(1,20)==19:
            final=final.upper()

        if random.randint(1,3)==3:
            final=final+str("?"*random.randint(1,8))

        pos=random.randint(1,2)
        if pos==1:
            final = str(emoji+" "+final)
        elif pos==2:
            final = str(final+" "+emoji)

        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    def game():
        DebugLog("Generating a type 'game' message")
        love = ['i love playin','i love','i love playing','i like','i really like','i really like playing','i really really love']
        game = ['roblox','fortnite','among us','fall guys']
        love=love[random.randint(0,6)]

        game=game[random.randint(0,3)]
        final = str(love+" "+game)
        if random.randint(1,10)==6:
            final=final.upper()
        if random.randint(1,10)==5:
            final=str(final+final[len(final)-1:]*random.randint(1,11))
        if random.randint(1,3)==3:
            final=final+str("!"*random.randint(1,16))

        if final[0]==" ":
            final=final[1:]
        DebugLog("Generated message")
        return final

    messagetype=messagetype.lower()
    if messagetype=="cringe":
        return str(cringe())
    elif messagetype=="sus":
        return str(sus())
    elif messagetype=="twitter":
        return str(twitter())
    elif messagetype=="funny":
        return str(funny())
    elif messagetype=="good":
        return str(good())
    elif messagetype=="dsmp":
        return str(dsmp())
    elif messagetype=="poop":
        return str(poop())
    elif messagetype=="game":
        return str(game())
    elif messagetype=="random":
        DebugLog("messagetype='random', choosing random message type")
        rand1=random.randint(1,8)
        if rand1==1:
            return str(cringe())
        elif rand1==2:
            return str(sus())
        elif rand1==3:
            return str(twitter())
        elif rand1==4:
            return str(funny())
        elif rand1==5:
            return str(good())
        elif rand1==6:
            return str(dsmp())
        elif rand1==7:
            return str(poop())
        elif rand1==8:
            return str(game())
    else:
        DebugLog("'"+str(messagetype)+"' is not a valid messagetype")
        raise ValueError