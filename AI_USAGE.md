# AI Usage — Lab 2

## Tools used
Model used: Claude

## Where AI helped
I used AI for correcting my bash commands, any mistakes or errors I found
while creating the analysis scripts, and for questions about the analysis
for both python and R notebooks.

### Prompt  1
Prompt 1: "zsh: command not found: jupyter" why was jupyter not found? 

Claude's Response: "Prompt shows (base); Jupyter is in lab2. conda activate lab2 first, every new terminal. 
Check the yml's name: line to confirm which env is the right one."

once I ran this command it worked and I was able to create my Jupyter Notebook

### Prompt  2

Prompt 2: "/bin/sh: loading: command not found i got this error for both?"  and then 
/bin/sh: load-libraries: command not found im stil getting this error" "

Claude's Response: First word in {} is the engine; {loading libraries} made the shell run a command called loading. 
Use {r load-libraries} — lowercase r first, no spaces in the name.

The fix worked, I forgot that in R markdown you need to define the language being used 
in the code chunk.

###  Prompt 3

Prompt 3: "Error in UseMethod("filter") : no applicable method for 'filter' 
applied to an object of class "logical" — filter()"

Claude's Response: "filter() got no data frame, so R looked up stage as a global object. Use q1 %>% filter(!is.na(stage)) or filter(q1, ...). Rule: every 
dplyr verb takes a data frame first, from the pipe or explicitly, never both, never neither."

This made sense to me.

## Where AI was wrong or unhelpful

### Prompt 3
Prompt: "I am creating two boxplot graphs to compare bilirubin and albumin levels by PBC, 
why should the bilirubin graph be in log scale and albumin in linear?"

Claudes Response: "log does nothing for albumin's narrow range"

I decided to make both graphs log scale for consistency purposes so when looking at both graphs
it reflects the same analysis. 



