# Problem: Decompiling ARM to Bicep

## Scenario
You want to close the loop on this entire section by converting your own hand-written ARM JSON back into Bicep, and comparing it against the Bicep you originally hand-wrote for the same resource.

## Your task
1. Take the solution.json you hand-wrote back in module 1.
2. Run az bicep decompile solution.json against it.
3. Open the resulting .bicep file and compare it, property by property, against the solution.bicep you hand-wrote in module 2 for what should be the same storage account.
4. List at least two differences between the decompiled version and your hand-written version, naming conventions, extra comments, structural choices, anything that stands out.
5. Clean up the decompiled file so it matches your own coding style from module 2, this is the manual review step Microsoft's docs explicitly call out as expected.

## Hints
- Hint 1: Expect the decompiler to generate its own symbolic names for resources, often less readable than what you'd choose by hand, that's normal, rename them to match your own convention.
- Hint 2: Watch for warning comments the decompiler inserts directly into the output, these flag spots it wasn't fully confident about, read every one of them rather than deleting them without looking.
- Hint 3: If az bicep decompile errors out entirely instead of producing warnings, it usually means something in the source JSON doesn't have a known Bicep equivalent yet, note what triggered it rather than assuming you did something wrong.

## Expected Result
Your cleaned-up decompiled file should compile successfully with az bicep build and produce JSON substantively equivalent to your module 1 and module 2 versions.
