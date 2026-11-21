
import os, shutil

R, W, G, B, X = "\033[91m", "\033[97m", "\033[90m", "\033[1m", "\033[0m"

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

def width():
    return min(64, shutil.get_terminal_size((80, 24)).columns)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    logo = ["ÆZ tool", "Database * OSINT * CSINT * Pentest"]
    for i, line in enumerate(logo):
        c = R if i == 0 else G
        print(f"{B}{c}{line.center(width())}{X}")
    print()

def box(title, content):
    w = width() - 2
    print(f"{R}╔{'═'*w}╗")
    print(f"║{B}{W}{title.center(w)}{X}{R}║")
    print(f"╠{'═'*w}╣")
    for line in content.splitlines():
        print(f"║{W}{line[:w].ljust(w)}{X}{R}║")
    print(f"╚{'═'*w}╝{X}")
    print(f"{GREEN}for + information write 99{X}")

if __name__ == "__main__":
    if os.name == "nt": os.system("")
    banner()
    box("MAIN MENU", "[01] OSINT\n[02] CSINT\n[03] ANALYZER\n[04] SETTINGS\n[00] EXIT")
    choice = int(input(f"{R}{B}M2VU > {X}"))
	if choice == 0:
        exit()
    if choice == 99:
        print(f"{CYAN}ÆZ multitool is create by a cyber professional , Create with not IA , The project ÆZ is a multitool for Csint * Database * Osint * Pentest{X}")
    else:
        print(f"{R}Dont work / no exist / in progress{X}")