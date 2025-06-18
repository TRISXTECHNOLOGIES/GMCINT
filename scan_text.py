import pytesseract
from PIL import Image
import spacy
from pdf2image import convert_from_path

# SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Tesseract OCR
def image2text(image_path):
    try:
        #check if it's a pdf instead of image
        if image_path.endswith('.pdf'):
            pages = convert_from_path(image_path,300)

            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(pages[0])
            cleaned_text = ' '.join(text.split())
            return cleaned_text
        else:
            img = Image.open(image_path)
            # Use Tesseract
            text = pytesseract.image_to_string(img)
            # removing extra spaces and newlines
            cleaned_text = ' '.join(text.split())
            return cleaned_text
        
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

# Function to extract names and airport entities from text
def extract_entities(image_path):
    text = image2text(image_path)
    doc = nlp(text)
    # print(text)
    with open('Airlines_list.txt', 'r') as airlines:
        airlines_list = airlines.readlines()
    with open('Airports_list.txt', 'r') as airports:
        airports_list = airports.readlines()

    
    # Initialize lists for different entity types
    names = []
    airports = []
    organizations = []

    # Identify entities in the text
    for ent in doc.ents:
        # PERSON covers individual names
        if ent.label_ == "PERSON":
            names.append(ent.text)
        # GPE (Geo-Political Entity) includes countries, cities, airports, etc.
        elif ent.label_ == "GPE":
                airports.append(ent.text)
        # ORG (Organizations) could cover airline companies, airport authorities, etc.
        elif ent.label_ == "ORG":
            for airline in airlines_list:
                if 'air' in  ent.text.lower():
                    organizations.append(ent.text.strip())
    
    # Remove duplicates
    names = list(set(names))
    airports = [airport.strip() for airport in airports_list for item in list(set(airports)) if item in airport ]
    airline_company = list(set(organizations))

    #filter for requirments
    #first airline company (if multiple result fount)
    if airline_company:
        my_airline = ''
        for item in airline_company[0]:
            if not item.isalpha():
                my_airline+=' '
            else:
                my_airline+=item
        airline_company=my_airline
    #first two airports (if multiple result found)
    if airports:
        n=0
        my_airport = []
        for airport in airports:
            if n==2:
                airports = my_airport
                break
            my_airport.append(airport)
            n+=1

    #first two names (if multiple result found)
    if names:
        n=0
        my_name = []
        for name in names:
            if n==2:
                names = my_name
                break
            my_name.append(name)
            n+=1

    
    return names, airports, airline_company

# Example usage
# image_path = "ws/test_bp.png"
# # text = image2text(image_path)
# names, airports, organizations = extract_entities(image_path)
# print(names,airports,organizations)

