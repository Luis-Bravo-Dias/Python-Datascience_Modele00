def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    bar_len = 61
    for i, item in enumerate(lst, 1):
        percent = int(i / total * 100)
        filled = (percent * bar_len) // 100
        bar = "=" * (filled - 1) + ">" + " " * (bar_len - filled)
        print(f"\r{percent}%[{bar}] {i}/{total}", end="", flush=True)
        yield item
    print()
