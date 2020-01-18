import sh

#call system commands
sh.pwd() #Get current Directory
sh.mkdir("files") #Make a new Directory
sh.touch("password.txt") #Make a new File
sh.whoami() #Get current user
sh.echo("Hello we are using 'sh' module")

