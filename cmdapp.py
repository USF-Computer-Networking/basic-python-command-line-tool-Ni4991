import cmd
import subprocess
import sys

class CLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        # define cmd 
        self.prompt = "> "
        # define program banner
        self.intr = ""

    def help_run(self, args):
        print "run a sub shell"

    def do_help(self, args):
        if args == "exit":
            print "exit this program"
        elif args == "quit":
            print "quit this program"
        elif args == "shell":
            print "run a shell commad"
        elif args == "run":
            print "run a sub shell"
        else:
            print "unknown command"

    def do_run(self, args):
        this.shell("cmd")

    def do_exit(self, args):
        "exit this program"

        sys.exit()

    def do_quit(self, args):
        "quit this program"

        return True

    def do_shell(self, args):
        "run a shell commad"

        subshell = subprocess.Popen(args, shell=True, stdin=None, stdout=None)
        subshell.communicate()
        subshell.terminate()

        print("")

    # define shortcuts for quit and run and help
    do_q = do_quit
    do_r = do_run
    do_h = do_help
