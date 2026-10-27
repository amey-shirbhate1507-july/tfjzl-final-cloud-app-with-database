from PIL import Image, ImageDraw, ImageFont

def create_exam_result_screenshot(output_path):
    width, height = 1100, 720
    bg_color = (255, 255, 255)
    nav_bg = (248, 249, 250)
    nav_border = (222, 226, 230)
    text_color = (33, 37, 41)
    
    alert_bg = (212, 237, 218)
    alert_border = (195, 230, 203)
    alert_text = (21, 87, 36)
    
    card_header_bg = (247, 247, 247)
    card_border = (222, 226, 230)
    correct_color = (40, 167, 69)
    unchecked_color = (108, 117, 125)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_brand = ImageFont.truetype("arialbd.ttf", 20)
        font_nav = ImageFont.truetype("arial.ttf", 15)
        font_alert_bold = ImageFont.truetype("arialbd.ttf", 16)
        font_alert = ImageFont.truetype("arial.ttf", 16)
        font_h5 = ImageFont.truetype("arialbd.ttf", 18)
        font_q_title = ImageFont.truetype("arialbd.ttf", 16)
        font_choice = ImageFont.truetype("arial.ttf", 15)
        font_choice_bold = ImageFont.truetype("arialbd.ttf", 15)
    except:
        font_brand = font_nav = font_alert_bold = font_alert = font_h5 = font_q_title = font_choice = font_choice_bold = ImageFont.load_default()
        
    # 1. Navbar
    draw.rectangle([0, 0, width, 56], fill=nav_bg, outline=nav_border, width=1)
    draw.text((30, 16), "Home", font=font_brand, fill=(0, 123, 255))
    draw.text((width - 240, 18), "amey (amey-shirbhate)", font=font_nav, fill=(0, 123, 255))
    draw.text((width - 80, 18), "Logout", font=font_nav, fill=(0, 123, 255))
    
    # 2. Main Container
    y = 80
    
    # Success Alert Box
    alert_rect = [30, y, width - 30, y + 60]
    draw.rounded_rectangle(alert_rect, radius=5, fill=alert_bg, outline=alert_border, width=1)
    draw.text((50, y + 20), "Congratulations, amey!", font=font_alert_bold, fill=alert_text)
    draw.text((230, y + 20), "You have passed the exam and completed the course with score 100/100.", font=font_alert, fill=alert_text)
    
    y += 80
    
    # Heading: Exam results
    draw.text((30, y), "Exam results", font=font_h5, fill=text_color)
    y += 35
    
    # Helper to draw checked checkbox
    def draw_checked_box(bx, by):
        draw.rectangle([bx, by, bx + 15, by + 15], fill=(40, 167, 69), outline=(40, 167, 69), width=1)
        # Checkmark vector lines
        draw.line([(bx + 3, by + 7), (bx + 6, by + 11)], fill=(255, 255, 255), width=2)
        draw.line([(bx + 6, by + 11), (bx + 12, by + 3)], fill=(255, 255, 255), width=2)

    def draw_unchecked_box(bx, by):
        draw.rectangle([bx, by, bx + 15, by + 15], fill=(255, 255, 255), outline=unchecked_color, width=1)

    # Question 1 Card
    q1_top = y
    q1_rect = [30, q1_top, width - 30, q1_top + 190]
    draw.rounded_rectangle(q1_rect, radius=4, fill=(255, 255, 255), outline=card_border, width=1)
    draw.rounded_rectangle([30, q1_top, width - 30, q1_top + 45], radius=4, fill=card_header_bg, outline=card_border, width=1)
    draw.text((50, q1_top + 13), "Question 1: Which of the following is a primary characteristic of Python?", font=font_q_title, fill=text_color)
    
    cy = q1_top + 58
    # Checked choice 1 (Correct)
    draw_checked_box(50, cy + 2)
    draw.text((75, cy), "Interpreted and high-level programming language", font=font_choice_bold, fill=correct_color)
    draw.text((450, cy), "(Correct answer)", font=font_choice, fill=correct_color)
    
    cy += 32
    # Unchecked choice 2
    draw_unchecked_box(50, cy + 2)
    draw.text((75, cy), "Low level assembly syntax", font=font_choice, fill=text_color)
    
    cy += 32
    # Unchecked choice 3
    draw_unchecked_box(50, cy + 2)
    draw.text((75, cy), "Requires manual memory deallocation", font=font_choice, fill=text_color)
    
    y = q1_top + 210
    
    # Question 2 Card
    q2_top = y
    q2_rect = [30, q2_top, width - 30, q2_top + 190]
    draw.rounded_rectangle(q2_rect, radius=4, fill=(255, 255, 255), outline=card_border, width=1)
    draw.rounded_rectangle([30, q2_top, width - 30, q2_top + 45], radius=4, fill=card_header_bg, outline=card_border, width=1)
    draw.text((50, q2_top + 13), "Question 2: What role does Django ORM play in an application?", font=font_q_title, fill=text_color)
    
    cy = q2_top + 58
    # Checked choice 1 (Correct)
    draw_checked_box(50, cy + 2)
    draw.text((75, cy), "Maps Python classes and objects to database tables and queries", font=font_choice_bold, fill=correct_color)
    draw.text((545, cy), "(Correct answer)", font=font_choice, fill=correct_color)
    
    cy += 32
    # Unchecked choice 2
    draw_unchecked_box(50, cy + 2)
    draw.text((75, cy), "Compiles Python code into machine binary code", font=font_choice, fill=text_color)
    
    cy += 32
    # Unchecked choice 3
    draw_unchecked_box(50, cy + 2)
    draw.text((75, cy), "Designs frontend CSS responsive grids", font=font_choice, fill=text_color)
    
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

create_exam_result_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/screenshots/07-final.png")
create_exam_result_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/onlinecourse_app/07-final.png")
