import os 

def full_reset():
    print("Resetting launchpad icon size and order...\n")
    os.system("defaults write com.apple.dock ResetLaunchPad -bool TRUE;killall Dock")
    return

def size_reset():
    print("Resetting launchpad icon size... \n")
    os.system("defaults delete com.apple.dock springboard-rows")
    os.system("defaults delete com.apple.dock springboard-columns;killall Dock")
    return

def change_size(rows, cols):
    print(f"Changing launchpad layout to {rows} rows and {cols} columns... \n")
    os.system("defaults write com.apple.dock springboard-rows -int "+rows)
    os.system("defaults write com.apple.dock springboard-columns -int "+cols)
    os.system("killall Dock")
    return

if __name__ == "__main__":
    os.system("clear")

    ans = input("Options: \n 1.) Adjust rows and columns \n 2.) Reset icon size only \n 3.) Reset icon size and order \n \n")

    if int(ans) == 1:
        rows = input("Number of rows? \n")
        cols = input("Number of coloums? \n")
        change_size(rows, cols)
    elif int(ans) == 2:
        size_reset()
    elif int(ans)== 3:
        full_reset()
    else:
        print("Wrong option, exiting")

