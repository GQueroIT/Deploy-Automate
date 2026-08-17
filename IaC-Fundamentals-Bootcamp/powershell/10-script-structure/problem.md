# Problem: Script Structure: Params Blocks, Comment-Based Help

## Scenario
The Get-DiskSpaceStatus function you wrote back in module 3 works fine, but it's stuck inside your head as "that function I wrote once," it's not a real, documented, callable script yet.

## Your task
Turn it into a proper standalone script:

1. In solution.ps1, add a script-level param() block at the very top (before any other code) exposing DriveLetter and WarningThresholdPercent, same as the function's parameters from module 3.
2. Add [CmdletBinding()] above the param block.
3. Add a full comment-based help block (.SYNOPSIS, .DESCRIPTION, .PARAMETER for each parameter, and at least one .EXAMPLE) either immediately above or immediately below the param block.
4. Move the actual disk-checking logic from module 3's function into the body of this script, using the script's own $DriveLetter and $WarningThresholdPercent instead of function parameters.
5. Confirm it works by mentally running Get-Help .\solution.ps1 -Full, does everything you'd expect to see actually show up based on what you wrote?

## Hints
- Hint 1: The param() block must be the first executable line, comments and blank lines above it are fine, but no other code, not even a variable assignment, can come before it.
- Hint 2: Comment-based help has to be a single contiguous <# ... #> block, formatted exactly with .SYNOPSIS, .DESCRIPTION etc. each on their own line, not scattered as separate # comments.
- Hint 3: [CmdletBinding()] goes directly above param(), with nothing in between.

## Expected Result
Get-Help .\solution.ps1 -Full should display a synopsis, a description, and a parameter entry for each parameter you defined, plus at least one example, not an empty or generic help page.
