import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, GObject, Vte, GLib
import os, subprocess, time, threading, sys

print(sys.argv[1])
nvgpuname = subprocess.check_output(["/home/ward/Downloads/test3/gpu-utils getname"], stderr=subprocess.STDOUT, shell=True)
        
column_names = False
drop_nan = False
df = None
application_id="cosmo.nvidia.wizard"
        
builder = Gtk.Builder()
builder.add_from_file("/home/ward/projects/nobara/cosmo-nvidia-wizard/process.ui")
#builder.connect_signals(obj)
        
window = builder.get_object("main_window")
window.show()
        
main_box = builder.get_object("main_box")
top_box = builder.get_object("top_box")
buttom_box = builder.get_object("buttom_box")
action_text = builder.get_object("action_text")
progress_bar = builder.get_object("progess_bar")
nvidia_logo = builder.get_object("nvidia_logo")
topbar_text = builder.get_object("topbar_text")
        
terminal=Vte.Terminal()
#terminal.set_input_enabled(False)
terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ['HOME'],
    ["/bin/bash"],
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )
main_box.pack_start(terminal, True, True, 10)
        
### Action Window
action_window = builder.get_object("action_window")
action_accept = builder.get_object("action_accept")
action_decline = builder.get_object("action_decline")
        
action_window.connect("destroy", Gtk.main_quit)
action_decline.connect("pressed", Gtk.main_quit)
        
###
        
win = builder.get_object("main_window")
win.connect("destroy", Gtk.main_quit)
win.show_all()
        
topbar_text.set_label(f"Installing driver for {nvgpuname.decode('ascii')}")
        
if (sys.argv[1]) == "install": 
    def install():
        progress_bar.pulse()
        progress_bar.set_pulse_step(100.0)
        def install_cmd6():  
            command6 = "echo \"Sending this command 6 to a virtual terminal.\"\n"
            terminal.feed_child(command6.encode("utf-8")):
            action_window.show_all()
        def install_cmd5():  
            command5 = "neofetch\n"
            terminal.feed_child(command5.encode("utf-8"))
        def install_cmd4():   
            command4 = "neofetch \n"
            terminal.feed_child(command4.encode("utf-8"))
        def install_cmd3():    
            command3 = "echo \"Sending this command 3 to a virtual terminal.\"\n"
            terminal.feed_child(command3.encode("utf-8"))
        def install_cmd2():    
            command2 = "echo \"Sending this command 2 to a virtual terminal.\"\n"
            terminal.feed_child(command2.encode("utf-8"))
        def install_cmd1():
            command1 = "echo \"Sending this command 1 to a virtual terminal.\"\n"
            terminal.feed_child(command1.encode("utf-8"))
        install_cmd5()
        install_cmd6()
    install()
            
Gtk.main()
