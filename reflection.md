# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---Pressing enter doesn't sumbit the response when the text says it should. The program is suppose to give you a certain amount of attempts but only gives you 6 attempts. When you press new game button, it gives you 8 attempts when the page originally reads 7 attempts and it doesnt actually restart the game. It also seems the program will randomly tell you to go higher or lower regardless of the actual secret number, even when your inputs pass the range of 1-100, until runs out of attempts. The secret number also doesnt follow the range of the diffulcty level. Also not an error but when click on the submit guess button, there is no user friendly indication that the guess is correct or wrong other than the attemps left going down.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used Claude Code. After I identified bugs during my first run at the game I gave the bugs to the AI to see where the logic fault was. It correctly provided the lines and reasoning, I looked at the code and confirmed. I have yet to see an AI suggession that is incorrect or misleading. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---I looked at the test cases and then manually ran the app again and see if the bug was fixed. I ran the test it gave me and passed but then I noticed the original test cases failed, it was because the orignial test cases was written wrong. It compared the return of check_guess(guess, secret) with a string when its a tuple. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

"Move the parse_guess function to logic_utils.py, and update the import in app.py.