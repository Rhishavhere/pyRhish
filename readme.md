# pyRhish - A Simple Interpreted Language

pyRhish is a minimalistic interpreted language built in Python, designed for simple scripting and learning purposes. It provides basic programming constructs with an easy-to-understand syntax.

## Key Features

- **Simple Syntax**: Easy-to-read commands with natural language-like constructs
- **Basic Operations**:
  - Variable assignment: `x = 10`
  - Output: `rhish.say` and `rhish whisper`
  - Input: `rhish.listen`
- **Conditional Logic**:
  `rhish check` 
- **AI Integration** (if turned on):
  - Ask questions: `askRhish`

## Getting Started

1. Clone the repository
2. Write your Rhish scripts in `.rsv` file
2. Run :
   ```bash
   rhish script.rsv
   ```


## Syntax Guide

### Basic Syntax
1. **Variable Assignment**  
   ```rhish
   x = 10
   name = "Alice"
   ```

2. **Output**  
    - Normal output ( *newline and variable* ):  
      ```rhish
      rhish.say("Hello World")
      rhish.say("Answer", ans)
      ```
    - Inline output ( *statement print* ):  
      ```rhish
      rhish whisper This statement will be printed
      ```

3. **Input**  
   ```
   age = rhish.listen
   ```

4. **Conditional Logic**
    ```
    rhish check age > 18
    ha : rhish whisper You're an adult
    na : rhish whisper You're a minor
    ```

5. **AI Integration (if enabled)**
    ```
    askRhish What is the capital of France?
    ```


### Examples
1. Simple Calculator:
    ```
    x = rhish.listen
    y = rhish.listen
    rhish.say("Sum is", x + y)
    ```

2. Conditional Example:
    ```
    rhish whisper Enter age:
    age = rhish.listen
    rhish check age >= 21
    ha : rhish.say("You can drink")
    na : rhish.say("You're too young")
    ```

### Notes
- All statements must be on separate lines
- Strings can use either single or double quotes
- Basic math operations are supported: +, -, *, /

## Project Structure

- `interpreter.py`: Core interpreter implementation
- `rhish_run.py`: Script runner
- `rhish.bat`: Windows batch file for easy execution

