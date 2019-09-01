from ProgrammingLang import ProgrammingLang as PL


def main():
    ruby = PL("Ruby", "Dynamic", True, 1995)
    python = PL("Python", "Dynamic", True, 1991)
    visual_basic = PL("Visual Basic", "Static", False, 1991)

    mylang = [ruby, python, visual_basic]
    
    for i in range(len(mylang)):
        print(mylang[i])
    print("The Dynamically typed languages are:")
    for attributes in mylang:
        print(attributes.isdynamic())

if __name__ == "__main__":
    main()