wiremon = lambda : ''.join([f"""
      .wps-{typ}{bus}:has(.wps-{typ}{bus}-i{wire}[checked]) .wps-{typ}{bus}-o{wire} {{
        animation: makeCheck 0.1ms;
      }}

      .wps-{typ}{bus}:has(.wps-{typ}{bus}-i{wire}:not([checked])) .wps-{typ}{bus}-o{wire} {{
        animation: makeUncheck 0.1ms;
      }}
""" for wire in range(15) for bus in range(15) for typ in "wp"])[:-1]


with open("wiremon.txt", "w") as fp: fp.write(wiremon())