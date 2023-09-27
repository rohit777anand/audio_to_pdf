import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path, audio_path):
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
    speaker = pyttsx3.init()

    # Loop through each page in the PDF file and extract the text
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()

    # Clean the text: Remove leading/trailing spaces, and replace newlines with spaces
    clean_text = text.strip().replace('\n', ' ')

    # Convert the cleaned text to audio
    speaker.save_to_file(clean_text, audio_path)
    speaker.runAndWait()
    speaker.stop()

# Example usage
pdf_file_path = 'example.pdf'
audio_output_path = 'output_audio.mp3'
pdf_to_audio(pdf_file_path, audio_output_path)
