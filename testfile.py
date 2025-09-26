def CountPopularChars():
    if len(sys.argv) >= 2:
        s = sys.argv[1]
    else:
        s = sys.stdin.read().strip()
    print("DEBUG: got input ->", s)
