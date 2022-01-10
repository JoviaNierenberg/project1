# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # replacement function
    def replace_all(text, dictionary):
        for key, val in dictionary.items():
            text = text.replace(key, val)
        return text
    # create dictionary with text and replacement text, use interim letters P & Q so that C and G are properly replaced
    d = { "A":"U", "T":"A", "G":"P", "C":"Q", "P":"C", "Q":"G" }
    # return result of running replace_all on the sequence and the dictionary
    return replace_all(seq, d)

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    transcribed = transcribe(seq)
    return transcribed[::-1] # use slicing to reverse string
