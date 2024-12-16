class RhishInterpreter:
  def __init__(self):
    self.variables = {}
  
  def execute(self,code):
    lines = code.split("\n")
    for line in lines:
      line = line.strip()
      if not line:
        continue
      if line.startswith("rhish.say("):
        self._execute_print(line)
      elif line.startswith("rhish whispers"):
        self._execute_whisper(line)
      elif "=" in line:
        self._execute_assign(line)
      else:
        print(f"Rhish Languages Doesn't Understand: {line}")
  
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
    content = line[len("rhish whispers"):].strip()
    print(content)
  
  def _execute_assign(self,line):
    var_name, expression = line.split("=", 1)
    var_name = var_name.strip()
    expression = expression.strip()
    value = eval(expression, {}, self.variables)
    self.variables[var_name] = value
