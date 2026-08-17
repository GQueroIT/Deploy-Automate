# Problem: String Manipulation and Formatting

## Scenario
Your monitoring tool spits out raw log lines like this, and you need to pull the useful pieces out by hand before you can do anything with them:

`2026-08-17 14:32:01 ERROR Disk usage at 95% on SERVER01`

## Your task
In solution.ps1:

1. Store that exact log line in a variable as a single string.
2. Use .Split() to break it into its pieces: date, time, level, and the rest of the message.
3. Pull out just the server name from the end of the message (SERVER01).
4. Pull out just the percentage number (95) as its own value.
5. Using the -f format operator, print a clean one-line summary like: [ERROR] SERVER01 is at 95% disk usage (logged 14:32:01).

## Hints
- Hint 1: .Split(" ") on the whole line gives you an array, but the message itself also contains spaces, so splitting on space alone gives you more pieces than just 4, think about how many pieces you actually need vs. how many you get, and consider .Split(" ", 4) which limits the number of resulting pieces.
- Hint 2: The percentage and server name are both embedded inside that last chunk of text, you'll need a second, smaller split or .Replace() on just that piece rather than trying to solve it in one split.
- Hint 3: -f uses positional placeholders like {0} and {1} that get replaced in order by whatever values you list after the -f, in the order you list them.
