to read process id and name i used psutil library in python
the same library could be used to read cpu usage and memory usage too

the terminal updation could be done by curses to update the data in realtime

i stored all the processes and their details in a dictionary

then using curses stdscr
i printed the header and i printed out each and every process
then i used keyup and keydown to scroll using simple dictionary traversal
:)