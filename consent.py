from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

#func for dynamic consent form
def consent_form(user_id,username,booking_num,airline,signature,flight_id):
    from datetime import date
    today_date = date.today().strftime("%d day of %B, %Y")
    username = username.upper()
    airline = airline.upper()


    # Formulate the consent form text
    consent_form = f'''                                 SPECIAL POWER OF ATTORNEY

KNOW ALL MEN BY THESE PRESENTS THAT I, {username}, in relation to flight booking number {booking_num} of {airline} airline ("Airline"), do hereby appoint and constitute GETMYCLAIMS including its nominees ("Company"), having its registered office at [office address], as my true, irrevocable and lawful legal representative and authorized agent, on my behalf and in my name, execute to do all or any of the acts, deeds, or things including to collect compensation from the Airline, monetary or otherwise, in relation to the claim, in accordance with Regulation (EC) No. 261/2004, Air Passenger Rights and Air Travel Organisers Licensing (Amendment) (EU Exit) Regulations 2019. GETMYCLAIMS.
AND NOW THEREFORE BY THESE PRESENTS I hereby authorize and empower the Company, as my lawful and valid representative for me and on my behalf to exercise, execute and perform all or any of the following acts, deeds and things, namely:
    1. To represent and act legally before the Airline in relation to the claim, inquires and/or any
        investigation undertaken by the Company's representatives.
    2. To submit, re-submit, withdraw and/or rectify the claim with the Airline.
    3. To obtain any and all information required in relation to the claim.
    4. To file, execute, examine, enforce, defend, answer or oppose any and all documents and
        conduct negotiations with the Airline and/or any third parties.
    5. To enter into any settlement in kind, upon written request by me, in relation to the claim and to
        sign, declare and/or affirm any other document in any way connected herewith.
    6. To receive and collect all claim amounts from the Airline on my behalf in the bank account of
        the Company.
    7. To retain such amounts equivalent to 25% (twenty-five percent) of the compensation, plus all
        applicable taxes (direct and indirect, both), received by the Company from the Airline, on
        behalf of me, as fee for the services provided by the Company ("Service Fee").
    8. To deposit the claim amount in my bank account after deducting the requisite Service Fee
        upon receipt of such claim amount from the Airline.

AND WHEREAS I hereby authorize the Company to do all acts, deeds and things omitted with respect to the claim mentioned above, as it deems fit.

AND I hereby for myself, my heirs, executors, administrators of acts done and legal representatives agree that all such acts, deeds and things lawfully done by the Company shall be constructed as acts, deeds and things done by me and I undertake to RATIFY AND CONFIRM all and whatsoever that the Company shall lawfully do or cause to be done for me by virtue of the power conferred and these presents hereby.

AND I agree with the terms and conditions of the Company.
IN WITNESS WHEREOF, I, {username}, have hereunto set my hand this {today_date}, in the presence of the following witnesses.

Signed and delivered by the within named                    I accept:
    
    {username}                                                                  GET MY CLAIMS
    '''
    from os import makedirs
    makedirs(f'./uploads/{user_id}',exist_ok=True)
    text_to_image(consent_form,signature, f'./uploads/{user_id}/consent_form_{flight_id}')
    

# Function to convert text to an image for an A4 sheet
def text_to_image(text,signature, image_path):
    # Define A4 size in pixels (at 300 dpi)
    width, height = 2480, 3508  # A4 at 300 dpi

    # Create a blank image with a white background
    image = Image.new('RGB', (width, height), color=(255, 255, 255))

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font = ImageFont.load_default()

    # Define text padding and starting position
    padding = 100
    y = padding

    # Split the text into lines based on word wrapping
    lines = []
    for line in text.splitlines():
        words = line.split(' ')
        line_text = ""
        for word in words:
            test_line = f"{line_text} {word}"
            if draw.textlength(test_line, font=font) < width - 2 * padding:
                line_text = test_line
            else:
                lines.append(line_text)
                line_text = word
        lines.append(line_text)

    # Draw each line of text on the image
    for line in lines:
        draw.text((padding, y), line, fill=(0, 0, 0), font=font)
        y += font.getbbox(line)[3] + 10  # Add line height + some spacing

    # Open the base image that created
    base_image = image.convert("RGBA")

    # Open the image to paste
    # Decode the base64 string
    overlay_image = base64.b64decode(signature) #signature is image in utf-8 string
    
    # Convert binary data to image
    overlay_image = Image.open(BytesIO(overlay_image))
    #resize it
    overlay_image = overlay_image.resize((500,200),Image.LANCZOS)
    overlay_image = overlay_image.convert("RGBA")

    position = (200, 3050)  # Position where the overlay image will be pasted
    
    # Paste the overlay image onto the base image at the specified position
    base_image.paste(overlay_image, position, overlay_image)

    # Save the resulting image
    base_image.save(image_path+'.png',optimize=True)
    bw_img = base_image.convert('L')
    bw_img.save(image_path+'.pdf',optimize=True)
