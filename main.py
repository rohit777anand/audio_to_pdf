#Importing PDF reader PyPDF2
import PyPDF2
#Importing Google Text to Speech library
from gtts import gTTS



def pdf_to_audio(pdf_path) -> None:
    """
    Converts a PDF file to an audio file using text-to-speech technology.

    Parameters:
    pdf_path (str): The path to the PDF file.
    audio_path (str): The path to save the audio file.

    Returns:
    None
    """

    # Initialize the PDF reader and text-to-speech engine
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    count = pdf_reader.numPages  # counts number of pages in pdf

    # Loop through each page in the PDF file and extract the text
    text = ''
    for page_num in range(count):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()

    # Clean the text: Remove leading/trailing spaces, and replace newlines with spaces
    clean_text = text.strip().replace('\n', ' ')

    #Set language to english (en)
    language = 'en' 

    # Convert the cleaned text to audio
    #Call GTTS
    myAudio = gTTS(text=clean_text, lang=language, slow=False)
    #Save as mp3 file
    myAudio.save("Audio.mp3")   

# Example usage
pdf_file_path = 'example.pdf'
pdf_to_audio(pdf_file_path)
