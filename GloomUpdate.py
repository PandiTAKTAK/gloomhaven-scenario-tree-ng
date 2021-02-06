import tkinter as tk
import subprocess
import datetime

def submit_new_data():
    print("Setting scenarios to:\n%s (old)\n\nSetting scenarios to:\n%s (new)\n\nSetting shop to:\n%s\n\n" % (e1.get(), e2.get(), e3.get()))
    update_scenarios()
    create_new_scenarios()
    create_shop()
    master.destroy()
    print("\n\nAll actions complete...")

def update_scenarios():
    create_scenarios()
    print("Building scenarios and GitHub Pages...")
    p = subprocess.Popen('npm run build', stdout=subprocess.PIPE, shell=True)
    for line in p.stdout:
        print(line)
    p.wait()
    print("Building scenarios and GitHub Pages complete...")

def create_scenarios():
    print("Scenario creation started...")
    location = str("./src/assets/")
    print('Using location      : ' + location)

    filename ='{0}current.json'.format(location)
    print("Creating {0}...".format(filename))
    output_file = open(filename, "w+")

    output_file.write("{0}\n".format(e1.get()))
    output_file.close()

    print("Scenario creation finished...")

def create_new_scenarios():
    print("New style scenarios creation started...")
    location = str("./docs/")
    print('Using location      : ' + location)

    build_timestamp = datetime.datetime.now()
    current_day     = datetime.date.today().day
    current_month   = datetime.date.today().month
    current_year    = datetime.date.today().year

    filename ='{0}scenarios.html'.format(location)
    print("Creating {0}...".format(filename))
    output_file = open(filename, "w+")

    output_file.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
    output_file.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
    output_file.write("<head>\n<title>Updated {0}/{1}/{2}</title>\n".format(current_day, current_month, current_year))
    output_file.write("<style type=\"text/css\">\nbody, html{margin: 0; padding: 0; height: 100%; overflow: hidden;}\n</style>\n")
    output_file.write("</head>\n")
    output_file.write("<body>\n<iframe width=\"100%\" height=\"100%\"\"\n")
    output_file.write("src=\"{0}\"\n".format(e2.get()))
    output_file.write("/>\n</body>\n</html>\n")

    output_file.close()

    print("New style creation finished...")

def create_shop():
    print("Shop creation started...")
    location = str("./docs/")
    print('Using location      : ' + location)

    build_timestamp = datetime.datetime.now()
    current_day     = datetime.date.today().day
    current_month   = datetime.date.today().month
    current_year    = datetime.date.today().year

    filename ='{0}shop.html'.format(location)
    print("Creating {0}...".format(filename))
    output_file = open(filename, "w+")

    output_file.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
    output_file.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
    output_file.write("<head>\n<title>Updated {0}/{1}/{2}</title>\n".format(current_day, current_month, current_year))
    output_file.write("<style type=\"text/css\">\nbody, html{margin: 0; padding: 0; height: 100%; overflow: hidden;}\n</style>\n")
    output_file.write("</head>\n")
    output_file.write("<body>\n<iframe width=\"100%\" height=\"100%\"\"\n")
    output_file.write("src=\"{0}\"\n".format(e3.get()))
    output_file.write("/>\n</body>\n</html>\n")

    output_file.close()

    print("Shop creation finished...")


master = tk.Tk()
master.title("Gloomhaven Settings")
tk.Label(master, 
         text="Scenarios (old)").grid(row=0)
tk.Label(master, 
         text="Scenarios (new)").grid(row=1)
tk.Label(master, 
         text="Shop").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Close', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Submit', command=submit_new_data).grid(row=3, 
                                                  column=1, 
                                                  sticky=tk.W, 
                                                  pady=4)

tk.mainloop()