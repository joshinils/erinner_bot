from erinerrung import erinnerung

def main():
    e = erinnerung(["a"])
    e = erinnerung(["a", "b"])
    e = erinnerung(["a", "in", "5min"])
    e = erinnerung(["a", "in", "5", "min"])
    e = erinnerung(["a", "in", "5m"])
    e = erinnerung(["a", "in", "5", "m"])
    e = erinnerung(["a", "b"])

if __name__ == "__main__":
    main()
