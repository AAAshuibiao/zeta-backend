def log(username, filename, link, time):
    with open("userlist.csv", "a+") as f:
        f.write('\n')
        f.write(f'{time},{username},{filename},{link}')
