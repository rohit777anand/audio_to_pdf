# Importing Libraries
from gtts import gTTS
import PyPDF2

# Input
a = input("Enter the Pdf File Name: ")
b = input("Enter the Audio File Name: ")
c = input("Enter the Language: ")

# Create PDF Reader Object Using Imported Module
pdf_reader = PyPDF2.PdfReader(open(a, 'rb'))
count = len(pdf_reader.pages) # counts number of pages in pdf
print("The number of pages in the pdf: ",count)

# Extracting text data from each page of the pdf file
text = ''
for i in range(count):
    page = pdf_reader.pages[i]
    text += page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# Call GTTS
myAudio = gTTS(text=clean_text, lang=c, slow=False)

# Save as mp3 file
myAudio.save(b +".mp3")
