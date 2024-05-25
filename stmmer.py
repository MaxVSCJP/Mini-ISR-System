import re

# Define the lists of prefixes and suffixes
prefixes = [
    "ወዖኢይት", "ወኢይትት", "ዖኢይትት", "ወዖኢትት", "ሇአስተ", "ወአስተ", "ዖኢይት", "ዖናስተ", "ዖያስተ", "በአስተ",
    "ወዖኢይ", "ወኢትት", "ወናስተ", "ወመስተ", "ሇዖይት", "ወኢይት", "እምዖ", "እምነ", "በአስ", "ዖኢይ", "ዖይት",
    "በዖይ", "እምዝ", "ሇዖኢ", "መስተ", "ወኢት", "እምኢ", "ዖኢተ", "ዖንት", "ወኢይ", "ኢይት", "ሇዖያ", "ሇዖይ",
    "ኢያስ", "ወእም", "ዖትት", "ያስተ", "አስተ", "ኢትት", "ወሇዖ", "ሇዖበ", "ሇዖአ", "ሇይት", "እምበ", "ወበመ",
    "ወትት", "ወዖይ", "ወዖኢ", "በዖአ", "ወእት", "ይት", "አን", "አስ", "እም", "ዖተ", "ወይ", "ወሇ", "ወየ", "ሇዖ",
    "ኢይ", "ወኢ", "ዖይ", "በተ", "በዖ", "ወበ", "ወዖ", "ዖኢ", "ኢተ", "ዖያ", "ዖን", "ወን", "ዖየ", "ወተ", "ዖት",
    "በበ", "ሇሇ", "ሇዖ", "ዖበ", "ወወ", "እት", "ትት", "ወይ", "ኢየ", "ወያ", "ወእ", "ወታ", "ወመ", "ሇይ", "ሇአ",
    "አ", "ኡ", "ኢ", "መ", "ሙ", "ሚ", "ተ", "ቱ", "ቲ", "ታ", "ት", "ኣ", "እ", "የ", "ያ", "ይ", "ኑ", "ና", "ን", "ወ",
    "ነ", "በ", "ዖ", "ሇ", "ም"
]
suffixes = [
    "ውንቲክሙ", "ውንቲክን", "ውንቲሆሙ", "ውንቲሆን", "ክምዎሙ", "ክምዎን", "ክናሆሙ", "ክናሆን", "ያኒክሙ", "ያኒክን",
    "ያኒሆን", "ያኒሆሙ", "ያቲሆሙ", "ያቲሆን", "ውንቲከ", "ውንቲሃ", "ውንትኪ", "ዋቲሃኒ", "ዋቲሆሙ", "ዋቲሆን",
    "ውያን", "ውያት", "ትክን", "ትክሙ", "ክምዎ", "ክምዋ", "ክሙኒ", "ክሙነ", "ኪዮሙ", "ኪዮን", "ክናሃ", "ክናኒ",
    "ኪናነ", "ክዎሙ", "ኩክሙ", "ኩክን", "ናሆሙ", "ናክሙ", "ያኒከ", "ያንከ", "ንክሙ", "ኒክሙ", "ንክን", "ኒሆን",
    "ያኒየ", "ያኒነ", "ያኖሙ", "ያኖን", "ያንነ", "ያትኪ", "ያቶን", "ቲሆን", "ያትያ", "ያቲየ", "ያትነ", "ያንኪ",
    "ተክሙ", "ተክን", "ውያት", "ውያን", "ቲሆሙ", "ያቲሁ", "ትየሰ", "ቲክሙ", "ቲሁኒ", "ሆሙኒ", "ኒሃኒ", "ናቲሃ",
    "ውንተ", "ውንት", "ያኒሃ", "ያኒከ", "ያኒሁ", "ተኒ", "ያት", "ሆሙ", "ሆን", "ክን", "ዋት", "ተነ", "ተከ", "ተኪ",
    "ቶሙ", "ቶን", "ኣት", "ኣን", "ክሙ", "ዊት", "ዋን", "ያን", "ዎሙ", "ትየ", "ትነ", "ኮን", "ዎን", "ተኒ", "ኪዮ",
    "ዮሙ", "ዮን", "ኪያ", "ኪኒ", "ካሁ", "ክዎ", "ኩከ", "ኩኪ", "ኪዋ", "ናሁ", "ናሃ", "ናኪ", "ትከ", "ትኪ", "ኒሁ",
    "ያነ", "ኒከ", "ንየ", "ኒየ", "ኒነ", "ንነ", "ያኑ", "ኖሙ", "ያና", "ኖን", "ቲሃ", "ቲየ", "ንከ", "ንኪ", "ሁኒ",
    "ክሙ", "ሆሙ", "ሆን", "ሙነ", "ሙኒ", "ቲነ", "ከኒ", "ታተ", "ታት", "ናት", "ኮሙ", "የኑ", "ትሰ", "ትኒ", "የኒ",
    "ዊተ", "ሁ", "ይ", "ነ", "ዮ", "ዎ", "የ", "ዋ", "ዊ", "ከ", "ኩ", "ኪ", "ነ", "ኒ", "ና", "ን", "ቱ", "ታ", "ት", "ቶ",
    "ሃ", "ሁ", "ሙ", "ሂ"
]

### Geez Stemmer Implementation


import re

# Recording rules and exceptions
def apply_recording_rules(word):
    # Implement the recording rules based on the document
    # Example rules:
    if len(word) == 2:
        return word
    if word.startswith("ተ") and word[1] == "ን":
        return word
    if len(word) == 3 and word.startswith("ወ") and word[1] == "ን":
        return word
    if len(word) == 3 and word.startswith("መ"):
        return word
    if word.startswith("አ") and (word[1] == "ፍ" or word[1] == "ፋ"):
        return word
    if word.startswith("ኢት") or word.startswith("ኢየ") and (word[2] == "ዮ" or word[2] == "ሩ"):
        return word
    return None

# Check infixes
def handle_infixes(word):
    if len(word) == 3 and ("ወ" in word or "የ" in word):
        word = word.replace("ወ", "").replace("የ", "")
        if word.startswith("መ"):
            word = "ሞ" + word[1:]
        elif word.startswith("ሠ"):
            word = "ሤ" + word[1:]
        elif word.startswith("ቀ"):
            word = "ቆ" + word[1:]
        return word
    return word

# Main stemmer function
def geez_stemmer(word_list):
    stemmed_words = {}
    for word,freq in word_list.items():
        if len(word) <= 3:
            ok = word
            if ok in stemmed_words:
                stemmed_words[ok] += freq
            else:
                stemmed_words[ok] = freq
            continue
        
        ok = apply_recording_rules(word)
        if ok:
            if ok in stemmed_words:
                stemmed_words[ok] += freq
            else:
                stemmed_words[ok] = freq
            continue
        
        # Remove prefixes
        for prefix in prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]
                break
        
        # Remove suffixes
        if len(word) > 3:
            for suffix in suffixes:
                if word.endswith(suffix):
                    word = word[:-len(suffix)]
                    break
        
        # Handle infixes
        word = handle_infixes(word)
        
        # Use n-gram if necessary
        if len(word) >= 5:
            ok = word[:4]
            if ok in stemmed_words:
                stemmed_words[ok] += freq
            else:
                stemmed_words[ok] = freq
        else:
            ok = word[:3]
            if ok in stemmed_words:
                stemmed_words[ok] += freq
            else:
                stemmed_words[ok] = freq
    
    
    return stemmed_words
