#river: str = "mmmmmississippi"
words: str = "<!---das das das---!>"

print(
    #"m" + river.lstrip("m")
    words.strip('<!>-').split()
)