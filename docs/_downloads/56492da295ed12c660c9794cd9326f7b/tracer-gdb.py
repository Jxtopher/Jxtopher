## https://stackoverflow.com/questions/17893554/how-to-print-the-current-line-of-source-at-breakpoint-in-gdb-and-nothing-else
# gdb --eval-command 'source gdb-trace.py' build/x64-unix-dbg/cvrp-main
# gdb -ex 'source gdb-trace.py' build/x64-unix-dbg/cvrp-main
import gdb

# Define the filename for trace output
trace_file = "step_trace.txt"

# Open the file for writing
with open(trace_file, 'w') as f:

  gdb.execute('break main')
  gdb.execute('set pagination off')
  gdb.execute('run')

  while True:
    # gdb.execute("next")
    gdb.execute('si')


    frame = gdb.selected_frame()
    sal = frame.find_sal()

    if sal.symtab:
      f.write(f"{sal.symtab.filename} {sal.line} {frame.function().name}\n")
    else:
      f.write(f"-\n")

# Print message to indicate trace completion  
print("Step-by-step trace saved to", trace_file)
gdb.execute('quit')