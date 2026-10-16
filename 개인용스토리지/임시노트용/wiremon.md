wiremon = lambda : ''.join([f"""
  .wps-{typ}{bus}:has(.wps-{typ}{bus}-i{wire}[checked]) .wps-{typ}{bus}-o{wire} {{
    animation: var(--anime-on) !important;
  }}

  .wps-{typ}{bus}:has(.wps-{typ}{bus}-i{wire}:not([checked])) .wps-{typ}{bus}-o{wire} {{
    animation: var(--anime-off) !important;
  }}
""" for wire in range(16) for bus in range(16) for typ in "wp"])[:-1]

doraemon = lambda : f"""\
@import url("https://xunr3.github.io/bugccore.css");

@layer usingBugccore {{
  /* begin, 16 wirebut16bit bus and 16 wirebus16bit port, 512bit */
{wiremon()}
  /* end, 16 wirebut16bit bus and 16 wirebus16bit port, 512bit */
}}\
"""

with open("wiremon.txt", "w") as fp: fp.write(doraemon())
