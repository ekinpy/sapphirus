import os
import sapphirus

if os.name == "nt":
    os.system("")

print(sapphirus.Text("Sapphirus", fg="dodgerblue3", style="b").stylize())
print(sapphirus.Text("Transform your terminal into a canvas of colors with", fg="grey50").stylize(),
      sapphirus.Text("Sapphirus", fg="dodgerblue3", style="b").stylize())
print("")
print(sapphirus.Text("GitHub:", style="b").stylize())
print(sapphirus.Text("https://github.com/ekinpy/sapphirus", fg="dodgerblue3", style="u").stylize())