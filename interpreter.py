class RhishInterpreter:
  def __init__(self):
    self.variables = {}
    self.current_line = 0
  
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
      elif line.startswith("agar "):
        self._execute_if(lines)
      elif "=" in line:
        self._execute_assign(line)
      elif line in ["{", "}", "toh"]:
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
  
  def _execute_if(self, lines):
    # Get condition from if statement
    line = lines[self.current_line - 1]
    condition = line[5:].strip()  # Remove 'agar ' from start
    
    # Check if condition has a brace - invalid syntax
    if "{" in condition:
        print("Error: Opening brace must be on a new line")
        return
    
    # Evaluate condition
    try:
        result = eval(condition, {}, self.variables)
    except:
        print(f"Invalid condition: {condition}")
        return

    # Find matching blocks
    if_block = []
    else_block = []
    current_block = if_block
    brace_count = 0
    waiting_for_brace = True
    
    while self.current_line < len(lines):
        line = lines[self.current_line].strip()
        self.current_line += 1
        
        if waiting_for_brace:
            if line == "{":
                waiting_for_brace = False
                continue
            elif line == "toh":
                current_block = else_block
                continue
            else:
                print("Error: Expected {")
                return
          
        if line == "{":
            brace_count += 1
        elif line == "}":
            if brace_count > 0:
                brace_count -= 1
            else:
                if current_block == else_block:
                    break
                current_block = else_block
                waiting_for_brace = True
                continue
        elif line == "toh":
            current_block = else_block
            waiting_for_brace = True
            continue
        else:
            current_block.append(line)

    # Execute appropriate block
    block_to_execute = if_block if result else else_block
    for line in block_to_execute:
        if line.startswith("rhish.say("):
            self._execute_print(line)
        elif line.startswith("rhish whisper"):
            self._execute_whisper(line)
        elif "rhish.listen" in line:
            self._execute_input(line)
        elif "=" in line:
            self._execute_assign(line)
