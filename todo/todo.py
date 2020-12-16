import sys
from datetime import date


def write_to_file(task):
	file=open("/home/ruthra/plans/todo.txt",'r')
	li=file.read()
	li=li.split("\n")
	if task not in li :	
		with open("/home/ruthra/plans/todo.txt",'a',encoding='utf-8') as file:
			file.write(task)
			file.write("\n")
			file.close()

def display_help():
	print("Usage :-")
	help=open("/home/ruthra/plans/help.txt")
	print(help.read())
	help.close()

def add_task():
	if len(sys.argv) == 2 :
		print("Error: Missing todo string. Nothing added!")
	else :
		task = sys.argv[2]
		write_to_file(task)
		print("Added todo: \""+task+"\"")

def display_task():
	file=open("/home/ruthra/plans/todo.txt")
	todo_list=file.readlines()
	if len(todo_list) == 0 : print("There are no pending todos!")
	i=liness()-1
	for line in reversed(todo_list) :
		line=str(line)
		line=line.strip("\n")
		i=str(i)
		print("["+i+"]",line)
		i=int(i)
		i-=1
	file.close()

def liness():
	file=open("/home/ruthra/plans/todo.txt")
	todo_list=file.readlines()
	i=1
	for line in todo_list :
		i+=1
	file.close()
	return i

def mark_done():
	if len(sys.argv) == 2 :
		st="Error: Missing NUMBER for marking todo as done."
		print(st)
		sys.exit()
	task_no = sys.argv[2]
	task_no = int(task_no)
	line_no = liness()
	
	if task_no < 1  :
		print("Error: todo #0 does not exist.")
		sys.exit()
	file=open("/home/ruthra/plans/todo.txt",'r')
	temp=file.readlines()
	task=temp[task_no-1]
	file.close()
	done_msg="x "
	datee=date.today()
	datee=str(datee)
	done_msg+=datee+" "+task
	file=open("/home/ruthra/plans/done.txt",'r')
	li=file.read()
	
	if done_msg not in li :	
		with open("/home/ruthra/plans/done.txt",'a',encoding='utf-8') as file:
			file.write(done_msg)		
			file.close()
		
		with open("/home/ruthra/plans/todo.txt",'r') as file:
			lsi=list(file)
		del lsi[task_no-1]
		with open("/home/ruthra/plans/todo.txt",'w',encoding='utf-8') as file:
			for n in lsi:
				file.write(n)
			file.close() 
	task_no = str(task_no)
	print("Marked todo #"+task_no,"as done.")
		
def delete_task():
	if len(sys.argv) == 2 :
		print("Error: Missing NUMBER for deleting todo.")
	else :
		task_no = sys.argv[2]
		task_no = int(task_no)
		if task_no < 0 : 
			print("Error: todo #0 does not exist. Nothing deleted.")
			sys.exit()
		else :
			with open("/home/ruthra/plans/todo.txt",'r') as file:
				lsi=list(file)
			del lsi[task_no-1]
			with open("/home/ruthra/plans/todo.txt",'w',encoding='utf-8') as file:
				for n in lsi:
					file.write(n)
				file.close() 
			task_no = str(task_no)
			print("Deleted todo #"+task_no)

    
	 

           
def report():
	file=open("/home/ruthra/plans/todo.txt",'r')
	temp=file.read()
	todo_list=temp.split("\n")
	pending=0 
	for i in todo_list:
		if i:
			pending+=1
	file=open("/home/ruthra/plans/done.txt",'r')
	temp=file.read()
	done_list=temp.split("\n")
	done=0
	for i in done_list:
		if i:
			done+=1
	datee=date.today()
	datee=str(datee)
	print(datee,"Pending :",pending,"Completed :",done)
def cmd(req):
	
	if req == "help" : display_help() 
	elif req == "add" : add_task() 
	elif req == "ls" : display_task()
	elif req == "del" : delete_task()
	elif req == "done" : mark_done()
	elif req == "report" : report()
	else : print("try again")

if len(sys.argv) == 1 :
	display_help()
	sys.exit()

req = sys.argv[1] # req


cmd(req)
