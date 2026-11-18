from jeu import *

assert formater_temps(125) == "02:05"
assert formater_temps(0) == "00:00"
assert formater_temps(3599) == "59:59"
print("formater_temps : OK")