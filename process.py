import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, GObject, Vte, GLib
import os, subprocess, time, threading, sys

print(sys.argv[1])
nvgpuname = subprocess.check_output(["/home/ward/Downloads/test3/gpu-utils getname"], stderr=subprocess.STDOUT, shell=True)

def run_after(f_after):
    def wrapper(f):
        def wrapped(*args, **kwargs):
            ret = f(*args, **kwargs)
            f_after()
            return ret
        return wrapped
    return wrapper

class Application:
    ### MAIN WINDOW ###
    def __init__(self):
        
        self.column_names = False
        self.drop_nan = False
        self.df = None
        application_id="cosmo.nvidia.wizard"
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/ward/Downloads/test3/process.ui")
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object("main_window")
        self.window.show()
        
        self.main_box = self.builder.get_object("main_box")
        self.top_box = self.builder.get_object("top_box")
        self.buttom_box = self.builder.get_object("buttom_box")
        self.action_text = self.builder.get_object("action_text")
        self.progress_bar = self.builder.get_object("progess_bar")
        self.nvidia_logo = self.builder.get_object("nvidia_logo")
        self.topbar_text = self.builder.get_object("topbar_text")
        
        self.terminal=Vte.Terminal()
        #self.terminal.set_input_enabled(False)
        self.terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/bash"],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )
        self.main_box.pack_start(self.terminal, True, True, 10)


        win = self.builder.get_object("main_window")
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        
        self.topbar_text.set_label(f"Installing driver for {nvgpuname.decode('ascii')}")
        
        if (sys.argv[1]) == "install":
            def install():
                self.progress_bar.pulse()
                self.progress_bar.set_pulse_step(100.0)
                self.command1 = "echo \"Sending this command to a virtual terminal.\"\n"
                self.terminal.feed_child(self.command1.encode("utf-8"))
                self.command2 = "echo \"Sending this command to a virtual terminal.\"\n"
                self.terminal.feed_child(self.command2.encode("utf-8"))
                self.command3 = "echo \"Sending this command to a virtual terminal.\"\n"
                self.terminal.feed_child(self.command3.encode("utf-8"))
                self.command4 = "echo \"Sending this command to a virtual terminal.\"\n"
                self.terminal.feed_child(self.command4.encode("utf-8"))
                self.command5 = "echo \"Sending this command to a virtual terminal.\"\n"
                self.terminal.feed_child(self.command5.encode("utf-8"))      
            install()
            def finished():
                os.system("/home/ward/projects/nobara/cosmo-nvidia-wizard/reboot.sh")
            finished()
 
Application()
Gtk.main()
