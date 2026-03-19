# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This is a number guessing game built with where the player tries to guess a secret number within a limited number of attempts. The game gives hints after each guess and tracks a score based on how quickly and accurately the player guesses. 

Bugs Found                                                               
  1. The secret number changed every time you clicked submit.                   
  2. The hints were backwards — "Too High" told you to go higher and "Too Low"  
  told you to go lower.                                                         
  3. The game could not compare the guess to the secret on even attempts because
   the secret was treated as text instead of a number.                          
  4. The attempt counter started at 1 instead of 0, so the first guess was    
  counted as the second.                                                        
  5. Easy mode only gave 6 attempts while Normal gave 8, making Easy harder than
   Normal.                                                                      
  6. The submit button had to be clicked twice for the guess to register.     
  7. The debug history did not show the latest guess until you clicked submit   
  again.   

  Fixes included  adding a session state guard so the secret number stays stable, correcting the swapped hint messages, 
  and removing a string cast that broke number comparisons. The attempt counter was also fixed to start at 0, and Easy mode was 
  given 10 attempts instead of 6 so it is actually easier than Normal. Finally, the submit button was wrapped in aform so one click registers correctly, and the debug expander was moved to after the submit block so history update first.                            


## 📸 Demo

![Gameplay screenshot](Screenshot%202026-03-19%20at%2011.01.55%20AM.png)  
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
