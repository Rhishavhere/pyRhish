# import os
# import google.generativeai as genai
# from dotenv import load_dotenv


class RhishInterpreter:
  def __init__(self):
    self.variables = {}
    self.current_line = 0

    # load_dotenv()
    # genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    # self.model = genai.GenerativeModel(
    #   model_name="gemini-2.0-flash-exp",
    #   system_instruction="provide only simple and small answers within one or two lines",
    # )

  def execute(self,code):
    lines = code.split("\n")

    while self.current_line < len(lines):
      line = lines[self.current_line].strip()
      self.current_line += 1
      
      if not line:
        continue
      if line.startswith("rhish.say("):
        self._execute_print(line)
      elif line.startswith("rhish whisper "):
        self._execute_whisper(line)
      elif "rhish.listen" in line:
        self._execute_input(line)
      elif line.startswith("rhish check "):
        self._execute_check(lines)
      elif line.startswith("askRhish "):
        self._execute_ask(line)
      elif "=" in line:
        self._execute_assign(line)
      elif line in ["{", "}", "na"]:
        continue
      else:
        print(f"Rhish Language Doesn't Understand: {line}")
  
  def _execute_assign(self,line):
    var_name, expression = line.split("=", 1)
    var_name = var_name.strip()
    expression = expression.strip()
    value = eval(expression, {}, self.variables)
    self.variables[var_name] = value

  def _execute_print(self, line):
    content = line[line.index("(") + 1:line.rindex(")")]
    args = [arg.strip() for arg in content.split(",")]
    
    result = []
    for arg in args:
      if '"' in arg or "'" in arg:
        value = arg.strip('"').strip("'")
        result.append(value)
      else:
        try:
            value = eval(arg, {}, self.variables)
            result.append(str(value))
        except:
            result.append("Undefined variable")
    print(" ".join(result))

  def _execute_whisper(self,line):
    content = line[len("rhish whisper "):].strip()
    print(content.replace("\\n", "\n"), end=" ")
  
  def _execute_input(self, line):
    var_name = line.split("=")[0].strip()
    user_input = input()
    try:
        value = int(user_input)
    except:
      try:
        value = float(user_input)
      except:
        value = user_input
    self.variables[var_name] = value
  
  def _execute_check(self, lines):
    # Get the condition line
    check_line = lines[self.current_line - 1]
    condition = check_line[len("rhish check "):].strip()
    
    ha_statements = []
    na_statements = []
    
    # Current state: collecting ha or na statements
    collecting_ha = True
    
    # Look for ha and na statements
    while self.current_line < len(lines):
        line = lines[self.current_line].strip()
        if not line:  # Skip empty lines
            self.current_line += 1
            continue
            
        if line.startswith("ha :"):
            statement = line[len("ha :"):].strip()
            ha_statements.append(statement)
        elif line.startswith("na :"):
            collecting_ha = False
            statement = line[len("na :"):].strip()
            na_statements.append(statement)
        elif collecting_ha:
            if line.startswith("  "):  # Check for indentation
                ha_statements.append(line.strip())
            else:
                break
        else:
            if line.startswith("  "):  # Check for indentation
                na_statements.append(line.strip())
            else:
                break
            
        self.current_line += 1
    
    # Evaluate condition
    try:
        result = eval(condition, {}, self.variables)
    except:
        print(f"Invalid condition: {condition}")
        return
    
    # Execute appropriate statements
    statements = ha_statements if result else na_statements
    for statement in statements:
        if statement.startswith("rhish.say("):
            self._execute_print(statement)
        elif statement.startswith("rhish whisper"):
            self._execute_whisper(statement)
        elif "rhish.listen" in statement:
            self._execute_input(statement)
        elif "=" in statement:
            self._execute_assign(statement)

  def _execute_ask(self, line):
    # Extract the question from the line
    question = line[len("askRhish "):].strip()
    try:
        # Get response from Gemini
        response = self.model.generate_content(question)
        # Print the response
        print(response.text)
    except Exception as e:
        print(f"Error getting response: {str(e)}")
