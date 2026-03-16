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

- [ ] The purpose of the game is to find a hidden number by using clues.

----The computer is keeping a secret number, and your job is a detective —you make guesses, and the computer gives you hints to help you get closer and closer until you find it.

----The game also teaches you how to think smart. Instead of guessing randomly, you use the hints to cut the possibilities in half each time. For example, if the range is 1 to 100 and your first guess is 50, the computer tells you to go higher or lower — now you already know 50 numbers you can skip!

----It's like playing "I'm thinking of a number" with a friend, but the computer is your friend.




- [ ] Here are the bugs found in the game:

----The hints were backwards. When your guess was too high, the game told you to go higher. That made no sense!

----The score was broken. Sometimes the game gave you points for a wrong guess, which is not fair.

----The game forgot to reset properly. After you won, clicking "New Game" did not fully restart — the game still thought you already won.

----The counter was wrong. The game started counting at 1 instead of 0, so you always lost one guess for free.

----Wrong guesses still counted. If you typed a letter or a number outside the range, the game still took away one of your attempts.

----The difficulty did not change. When you switched from Easy to Hard, the game kept using the same range of numbers.

----The input box kept your old guess. When you started a new game, your last guess was still sitting in the box.

----The hint checkbox kept turning itself back on. Even if you turned off hints, the game turned them back on every time you guessed.

----The attempts counter was always one step behind. It showed the old number instead of the updated one.

----The Enter key did not work. You had to click the button every time — pressing Enter did nothing.

----The buttons disappeared when the game ended. Once you won or lost, the input box and buttons vanished and you could not do anything.


- [ ] Fixes applied

- Fix swapped hint directions in check_guess (Too High/Too Low)
- Fix update_score: remove arbitrary even/odd condition, symmetric      
   penalties, score floor
- Fix new game button not resetting game status, score, and history
- Fix attempts counter starting at 1 instead of 0 (game ended too early)
- Fix invalid/out-of-range guesses consuming an attempt
- Fix difficulty change not resetting the game or secret range
- Fix input field retaining last guess after new game
- Fix show hint checkbox resetting on every submit
- Fix attempts display always one step behind due to render order
- Fix Enter key not submitting a guess
- Fix controls disappearing when game ends (removed st.stop())
- Refactor: extract reset_game() helper, consolidate session state init,
  remove duplicate parse_guess, move helpers to top of file,
  replace difficulty maps with DIFFICULTY_CONFIG dict

## 📸 Demo

- [ ] [images/winning_game_screenshot.png]
- [ ] [images/passed_tests.png]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
