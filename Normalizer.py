import re


character_replacements = {
        '[ሁሂሃሄህሆ]': 'ሀ',
        '[ሉሊላሌልሎ]': 'ለ',
        '[ሱሲሳሴስሶ]':'ሰ',
        '[ሑሒሓሔሕሖ]':'ሐ',
        '[ሙሚማሜምሞ]':'መ',
        '[ሱሲሳሴስሶ]':'ሰ',
        '[ሩሪራሬርሮ]':'ረ',
        '[ሡሢሣሤሥሦ]':'ሠ',
        '[ሹሺሻሼሽሾ]':'ሸ',
        '[ቁቂቃቄቅቆ]':'ቀ',
        '[ቡቢባቤብቦ]':'በ',
        '[ቱቲታቴትቶ]':'ተ',
        '[ኁኂኃኄኅኆ]':'ኀ',
        '[ኑኒናኔንኖ]':'ነ',
        '[ኡኢኣኤእኦ]':'አ',
        '[ፉፊፋፌፍፎ]':'ፈ',
        '[ዩዪያዬይዮ]':'የ',
        '[ዑዒዓዔዕዖ]':'ዐ',
        '[ዱዲዳዴድዶ]':'ደ',
        '[ዙዚዛዜዝዞ]':'ዘ',
        '[ኩኪካኬክኮ]':'ከ',
        '[ፁፂፃፄፅፆ]':'ፀ',
        '[ጹጺጻጼጽጾ]':'ጸ',
        '[ጉጊጋጌግጎ]':'ገ',
        '[ጡጢጣጤጥጦ]':'ጠ',
        '[ዉዊዋውዎ]': 'ወ',
}

def charnorm(text_input: dict[str, int]):
    for term in list(text_input.keys()):
        term2 = term
        normText = term
        for char, replacement in character_replacements.items():
            normText = re.sub(char, replacement, term2)
            if(normText != term2):
                term2 = normText
                
        if normText in text_input.keys():
            text_input[normText] += text_input.pop(term)
        else:
            text_input[normText] = text_input.pop(term)
    return text_input



""" input_text = {"ወኮነ": 1, "ሶበ": 1, "ፄወዎሙ": 1, "ለደቂቀ": 1, "እስራኤል": 1, "ንጉሠ": 1 , "ከላዴዎን": 1, "ነበቦ": 1, "እግዚአብሔር": 1, "ኖጉሠ": 1}
normalized_text = charnorm(input_text, character_replacements)
print(normalized_text) """