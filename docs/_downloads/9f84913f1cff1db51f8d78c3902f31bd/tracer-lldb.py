# apt install liblldb-16 liblldb-16-dev  python3-lldb-16 lldb-16
# lldb-16 -f build/x64-unix-dbg/cvrp-main -- tracer-lldb.py 

import lldb


# Check if a frame is available
if frame:
# Get filename and line number
filename = frame.source_file.basename
line_number = frame.line

print(f"Source File: {filename}, Line: {line_number}")
# Implement logic to access the source code file and retrieve the instruction at that line
else:
print("No frame selected.")