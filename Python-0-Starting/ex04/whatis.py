import sys

def main():
    if len(sys.argv) == 1:
        return
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    arg = sys.argv[1]
    
    try:
        num = int(arg)
    except ValueError:
        # Arg n'est pas un int
        print("AssertionError: argument is not an integer")
        return
    
    # modulo si off ou even
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
