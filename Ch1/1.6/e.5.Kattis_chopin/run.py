import sys

def main():
    lines = sys.stdin.read().splitlines()

    mapping = {
        "A#": "Bb",
        "C#": "Db",
        "D#": "Eb",
        "F#": "Gb",
        "G#": "Ab"
    }

    for key in list(mapping.keys()):
        mapping[mapping[key]] = key

    for n, line in enumerate(lines):
        note, tonality = line.split()
        if note in mapping:
            note = mapping[note]
            print(f"Case {n+1}:", note, tonality)
        else:
            print(f"Case {n+1}: UNIQUE")


if __name__ == "__main__":
    main()
