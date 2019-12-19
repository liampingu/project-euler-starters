#! /usr/bin/python3

# to time how long it takes your code to run, enter the problem number here
# and then run this file

problem_num = 1




import time, sys, os

if len(sys.argv) == 2:
    problem_num = int(sys.argv[1])
    
module_name = "problem{:03}".format(problem_num)
file_name = module_name + '.py'
if not os.path.isfile(file_name):
    print("[!] file '{}' doesn't exist!".format(file_name))
    exit()

print("[*] running {}...".format(module_name))
start_time = time.time()
__import__(module_name)
end_time = time.time()
print("[*] code finished!")

elapsed_time = end_time - start_time
milliseconds = int(elapsed_time*1000)

print("[*] time taken: {}s {:03}ms".format(int(milliseconds/1000), milliseconds%1000))
