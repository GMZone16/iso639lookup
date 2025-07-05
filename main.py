from search import ISO639Lookup

if __name__ == "__main__":
    isoLookUpObject = ISO639Lookup()

    print(isoLookUpObject.get_iso_part1("aar"))
    print(isoLookUpObject.iso_lookup("aao"))
