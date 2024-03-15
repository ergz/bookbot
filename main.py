path_to_file = "./books/frankenstein.txt"


def count_chars(text: str):
    all_chars = [x.lower() for x in text if x.isalpha()]
    output = dict()
    for c in all_chars:
        if c in output:
            output[c] += 1
        else:
            output[c] = 1

    output = [{"name": k, "num": v} for k, v in output.items()]
    return sorted(output, key=lambda x: x["num"], reverse=True)


def count_lines(text: str) -> int:
    return len(text.split())


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        wc = count_lines(file_contents)
        print(f"--- Begin report of book {path_to_file} ---")
        print(f"Total lines in book: {wc}\n\n")
        char_count = count_chars(file_contents)
        for i in char_count:
            print(f"The '{i.get('name')}' character was found {i.get('num')} times")


if __name__ == "__main__":
    main()
