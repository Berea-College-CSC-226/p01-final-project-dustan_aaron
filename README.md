# CSC226 Final Project

## Instructions

**Author(s)**: Stephen Aaron Robinson & Dustan Webb

**Google Doc Link**: https://docs.google.com/document/d/1hF_YyhnfbonXv3Gwq11vM1z6Taylc1I5qp7h2871Wzk/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

️**Title**: 3 in 1, Games of the Year Edition

**Purpose**: The user will get to choose between 3 games to play, including The Game of Nim, Rock Paper Scissors,
and Mastermind. The 3 games will have a main menu, the main menu is going to have a one sentence slight description of 
how the game is going to work and what the user will be doing. The main menu will be a seperate file and the master for 
all the games. All the games will be separated in files and will be short and sweet but with this being a final project
all the games together would take some time to play but all in all should be a blast. 

**Source Assignment(s)**: HW06: The Game of Nim (game_of_nim.py)

**CRC Card(s)**:
  
![](image/MM_CRC.png)
![](image/RPS_CRC.png)
![](image/GON_CRC.png)

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: Robinson_Main
        Branch 1 assignments: Mastermind, Game of Nim, Game Selection
    Branch 2 starting name: Dwebb28
        Branch 2 assignments: Rock Paper Scissors, Game of Nim, Game Selection
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

The Game of Nim, Rock Paper Scissors, and Mastermind games are not our ideas, but the code is ours.

---Command lambda is something I found on google in tkinter explorations that is different
buttons that calls to the same function but has can produce a different output. With Rock paper scissors being
same function but different output I needed to find something.
"tkinter button that calls the same function but can produce two different outputs" (what I searched) google output:You
can make a Tkinter button call the same function but produce different outputs by passing an argument to the function when creating the button.
This is typically done using lambda or functools.partial.


Using a button to open a window in Tkinter: https://stackoverflow.com/questions/27639298/tkinter-open-a-new-window-with-a-button-prompt
Closing a Tkinter window: https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
Updating a Tkinter window: https://pythonexamples.org/python-tkinter-refresh-window/
Read only text widget: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
Label Text changing: https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    Stephen Aaron Robinson: 11/17/2025 
        I've ran into a few issues so far, but ultimately feel good about how the project is going.
```
    Dustan M. Webb 11/23/2025
        I've gotten mojority of the code done, I have one massive bug that I need to fix and can't really figure it
        out so I think I'm going to head to the TA lab and get some help with it. But ultimately feel good on how 
        everything is going as a whole. 
---

## Milestone 3: Virtual Check-In

❗Indicate what percentage of the project you have left to complete and how confident you feel. 

❗️**Completion Percentage**: `0 - 100%`

❗️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    Aaron: I am pretty confident about completing the project. (Mainly because it is done already as I forgot to do this
    during milestone 3's time.
    
    Dustan: **Everything is going very smooth, we have officially started on the Game of Nim and the Main menu. 
    Looking at about probably a 70-80 ish percent done. Once break is all the way over and were able to get back to it
    probably going to be pretty close to done once were back. Speaking for both of us, I feel like we are very cofident.
    everything is going just as good if not better as we planned it to go. We like how everything is turning out. 
    The programs are looking good no bugs or anything what so ever. **
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

```
The user starts with a window with a window allowing them to select a game from the three choices of Rock Paper Scissors, 
Game of Nim, and Mastermind. They then get to play the game they selected. Instructions for these games are below.

Rock Paper Scissors: The user plays against an AI that taunts them constantly. They have 3 choices, Rock, Paper, and Scissors.
    The user will click one of the buttons to try and beat the AI, using the classic rules of Rock beats Scissors, Scissors beats Paper,
    and Paper beats Rock.
   
Game of Nim: The user is given some instructions, given the option to change the number of balls, and then starts the game.
    In the game they get 4 buttons to choose how many balls to take out. They repeat this until they either lose or win.


Mastermind: The user is brought to a menu for Mastermind, with 2 buttons, "Play" and "Settings". If they choose settings,
    they can change the number of pegs (buttons) they have to guess the color of, and the number of guesses they get. If they
    don't change these settings, the default number for both is 4. When hitting play, the user is met with 2 windows, one with 4 blank pegs (Or whatever number they put in the settings),
    and the other with 4 buttons that are colored. They can use these color buttons to input a guess, that is showed to them as
    they input it, of the blank pegs in the other window. After inputing a guess of colors, the pegs on the other window updates
    to show which, if any, of the colors matched with the blank pegs' hidden colors. If the user guesses the correct pattern, they win,
    but if they use all of their guesses, they lose. 
```

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1:  Aaron
    I suggested this idea, as I thought it'd be fun and that we could complete it in time. I got it from the 100 in One
    plug and play consoles.In the end, it turned out to be more difficult than I thought, but still fun in my opinion. 
    The project came out to be what I expected, 3 games in one program. I learnt a lot about Tkinter and how to use it to make GUI's.
    This was the most difficult part, as Tkinter is pretty confusing at first glance, but over time I believe it became easier to add to.
    Next time though, I think it'd be better to devote more time into one thing than less time into multiple things. 
    
    I think me and my partner worked well together. We were able to communicate easily, meet up at planned times, and execute 
    the plans we made. I think it went as well as any teamwork could go. There may have been things that could be better, like
    our communication when we actually met up, but otherwise it went great.
```

```
    Partner 2: **We selected it because we were both intrugued on tkinter and were really wondering on how that would turn
    out for us. He knew a lot about mastermind, both of our games of nims were flawless on our homework assignment code.
    Then rock, paper sciccors just stuck out to me and thought would've been a lot of fun to try and man handle for the class 
    to enjoy. 
    Honestly pretty close to the tea, everything went exactly as we planned and imagnined in my opinion. Now the only thing
    was time wise, one week we got too far ahead (which is obviously better than being behind, then one week we were behind.
    To be 100% honest, I did worse being far ahead than I did being behind, when I'm behind I'm very by the book, get to the point
    type of person. When we were ahead, I overthought every line of code I produced, my research wasn't how I wanted it to go
    , I thought that rock paper sciccors could've looked better that kind of stuff. I learned that you need to be patient and 
    learn how to take breaks away from your partner and even with your partner. Espeically getting caught up in errors, 
    that made me the angriest. 
    The hardest part was honestly just being patient, I kept getting caught up in something, it wouldn't work and I'd forget 
    how to reset and take a deep breath. At the end of the day, thats the world of being a computer scientist. I had one error,
    where it would just print the cpu winning statment, all because in the list I made all 3 capitalized and in the function
    of calling from the list in lower case. I ended up getting some help for it because I was so lost on why just that print 
    statement was working in the elif loop. 
    The thing I would do different, is planning wise, honestly I would have a better on paper in thought process of planning it.
    Because we had the classes, the function and everything planned. But the long process of 3 games and a main menu, it
    was extremely hard to plan for all 4 while trying to focus on one thing at a time so you wouldn't get caught up on the 
    long run of it all. We worked pretty well, I have nothing to complain about, we split up but worked together perfectly,
    communication was always on point. There was nothing challenging, besides one time my ac broke and we had to rescedule 
    but also find time to finish it all up. 
```

---