# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    Ans: When I first launched the game it looked normal until I started clicking.

- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").
    Ans: 1. At first I typed in the number 5 and pressed enter it looked like the game wasn't responding and even when I pressed the Enter key multiple times.

    2. When I typed in a numer that is  out of range the game did count it as an attempt. And sometimes, when I pressed start a new game, the program didn't behave like expected.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---- For this project I used Claude only. 
    One example of AI suggestion that worked was I to wrappe the input box and buttons inside a Streamlit form so that pressing Enter would submit a guess. And then, I refreshed the game in the browser to test the fix.

    There was a point the app crashed  when the show Hint checkbox wasn't working properly. Claude suggested to use both **key="show_hint"** and *value=st.session_state.show_hint* at the same time. It crashed the app.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I decided that a bug was fixed by launching the app and test it manually. After I fixed all the bugs I didn't know how to create the test bot, Claude did that entirely.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- I didn't know about streamlit until this project. But with my programming experienced I figured it was because of *random.randint()* kept running agin and again and picked a new number each time it ran. The simplest way I could explain streamlit to a person is that it is like a schoolboard that has something written on it and everytime a person enters the classroom streamlit erase the whole board and re-write what was on the board again. Claude save the secret number inside *st.session_state*

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
 

 ----- One habit that I want to reuse it Granularity: I always   
      test every fix one by one.
      Spend more time reading AI suggestion and think about it. many times the project crashed because there are suggestions that I didn't quite understand mostly because of limited technical skills. I also learned that AI generated code aren't always correct, then they are not a final answer. I know that my job is to assess it first, understand it, test it and intentionally breake it to cath mistakes it might contain. Also, using AI as my companinon help me work faster.
