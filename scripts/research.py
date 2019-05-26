"""A DRW research toolkit library.
"""


def categorize(source, theme, subtheme=None):
    """Categorize sources by theme and optionally subtheme.
    """
    if subtheme:
        return f"{source} classified as {theme}:{subtheme}"
    else:
        return f"{source} classified as {theme}"
    
    
if __name__ == "__main__":
    print("Running as an APP, NOT imported as a library!")