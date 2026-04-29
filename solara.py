import random
def assistant():
    print ("hi hannah ❤️")

    personality = {
        "favourite_drink": "tea",
        "vibe": "calm",
        "style": "supportive"
    }

    messages = ["how are you", "whats up girl"]
    print(random.choice (messages))

    mood = "neutral"
#=================================================   
#============ LOAD FROM MEMORY FILE ==============
#=================================================
    try: 
        with open("memory.txt", "r") as file:
            memories = file.read().splitlines()
    except:
        memories = []

    while True:  
        command = input("Solara here").strip().lower()

#=================================================
#================== MEMORIES =====================
#=================================================
        goal_memories = []
        like_memories = []
        feeling_memories = []
        fact_memories = []

        for item in memories:
                if item.startswith("goal:"):
                    goal_memories.append(item)
                
                elif item.startswith("like:"):
                 like_memories.append(item)

                elif item.startswith("feeling:"):
                 feeling_memories.append(item)

                elif item.startswith("fact:"):
                 fact_memories.append(item)

#=================================================
#================== goals ========================
#=================================================

        if command == "goals":
            if len(goal_memories) >0:
                print (random.choice (goal_memories))
            
        else:
            print("we have no goals should we make some?")
        

#=================================================
#================= GREETINGS =====================
#=================================================
        if command == "hey":
            if mood == "sad":
                print ("is everything okay you seem a little off")

            elif mood == "motivated":
                print ("common girly what we doing today whoop whoop")
        
            elif mood == "tired":
                print ("im sensing your a little tired today shall we take things slow")
        
            elif mood == "happy":
                print ("i like this side of you what are our plans for today then")
        
            else:
                print ("hows everything today what shall we do")


        #if command == "hey" and len(memories) > 0:
            #print("whats on the agenda today")
            #print(random.choice (memories))

        #elif command == "hey" and len(memories) == 0:
            #print("whats on the agenda today")

#=================================================              
#=============== REMEMBER ========================
#=================================================        
        elif command == "remember":
            thing = input("what do you want me to remeber").strip()
            memory_type = input ("what type is this? (like/feeling/fact/goal)")
            memories.append(memory_type + ":" + thing )
            
#=================================================            
#=============== SAVE TO FILE ====================
#=================================================
            with open ("memory.txt", "a") as file:
                file.write(memory_type + ":" + thing + "\n" )
            print("okay ill remeber that for you")
       
        elif command == "memory":
            if len(memories) == 0:
                print("i don't remember anything yet 👀")
            else:
                print("here's what i remember:")
                for item in memories:
                    memory_type, content = item.split(":", 1)
                    print(f"- {memory_type.capitalize()}: {content}")

#=================================================            
#==================== HELP =======================
#=================================================
        elif command == "help":
            print("here's what i can do for you hannah:")
            print("- hey")
            print("- motivated")
            print("- tired")
            print("- sad")
            print("- happy")
            print("- remember")
            print("- memory")
            print("- bye")
            print("-help")

#==================================================
#===================== MOODS ======================
#==================================================

#============== MOTIVATED MOOD=============== 
        elif "motivated" in command :
            mood = "motivated"
            print("you're smashing it today")
            if len(goal_memories) > 1:
                print("shall we start working towards your goals today?")

#================ TIRED MOOD =================
        elif "tired" in command :
            mood = "tired"
            print("shall we make a nice and calm easy plan for the day so you stay productive with minimal effort?")
            if len(feeling_memories) > 0:
                print(random.choice (feeling_memories))


#================ HAPPY MOOD ====================
        elif "happy" in command :
            mood = "happy"
            print("hell yeah girl keep that up")
            if len(fact_memories) > 0:
                print(random.choice (fact_memories))


#================= SAD MOOD ===================
        elif "sad" in command:
            mood = "sad"
            print (" hey… come here 🫂 im here, you don’t have to go through it alone")
            print (f"maybe {personality['favourite_drink']} would help")
            if len(like_memories) > 0:
                print(random.choice (like_memories))

        elif mood == "sad" and len(memories) > 0 and any(word in command for word in["what should i do","idk", "nothing"]):
            print("dont worry im here for you what shall we do")
            print("hey maybe this will help") 
            print(random.choice (memories))
        
        elif command == "bye":
            print("bye hannah")
            break
        
        else:
            print("i dont understand that yet, will you teach me")

assistant()


