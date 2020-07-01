for i in range(10):
    filename = f"input{i}.dat"
    print(filename)
    with open(filename,"w") as f:
        f.write(f"{i}\n")
