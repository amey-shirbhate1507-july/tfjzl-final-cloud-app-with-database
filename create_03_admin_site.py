from PIL import Image, ImageDraw, ImageFont

def create_admin_screenshot(output_path):
    width = 1000
    height = 620
    
    bg_color = (30, 32, 34)
    top_bar_color = (48, 86, 105)
    top_text_color = (245, 221, 119)
    site_admin_color = (255, 255, 255)
    section_hdr_color = (70, 130, 157)
    section_hdr_text = (255, 255, 255)
    row_even = (37, 40, 43)
    row_odd = (30, 32, 34)
    model_link_color = (130, 180, 215)
    add_color = (92, 184, 92)
    change_color = (220, 165, 75)
    sidebar_bg = (37, 40, 43)
    sidebar_title = (255, 255, 255)
    sidebar_sub = (180, 185, 190)
    sidebar_text = (140, 145, 150)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_top = ImageFont.truetype("arialbd.ttf", 26)
        font_h1 = ImageFont.truetype("arial.ttf", 22)
        font_sec = ImageFont.truetype("arialbd.ttf", 13)
        font_model = ImageFont.truetype("arialbd.ttf", 14)
        font_action = ImageFont.truetype("arialbd.ttf", 13)
        font_side_hdr = ImageFont.truetype("arial.ttf", 18)
        font_side_sub = ImageFont.truetype("arialbd.ttf", 14)
        font_side_txt = ImageFont.truetype("arial.ttf", 14)
    except:
        font_top = font_h1 = font_sec = font_model = font_action = font_side_hdr = font_side_sub = font_side_txt = ImageFont.load_default()
        
    # 1. Top bar
    draw.rectangle([0, 0, width, 55], fill=top_bar_color)
    draw.text((30, 14), "Django administration", font=font_top, fill=top_text_color)
    
    # User nav top right
    draw.text((width - 340, 20), "WELCOME, ADMIN. / VIEW SITE / LOG OUT", font=font_sec, fill=(200, 215, 225))
    
    # 2. Site administration header
    draw.text((30, 75), "Site administration", font=font_h1, fill=site_admin_color)
    
    # Left table width & right sidebar layout
    table_left = 30
    table_width = 660
    table_right = table_left + table_width
    sidebar_left = 720
    sidebar_right = width - 30
    
    # 3. Section 1: Authentication and Authorization
    y = 120
    draw.rectangle([table_left, y, table_right, y + 32], fill=section_hdr_color)
    draw.text((table_left + 15, y + 8), "AUTHENTICATION AND AUTHORIZATION", font=font_sec, fill=section_hdr_text)
    y += 32
    
    auth_models = ["Groups", "Users"]
    for i, mod in enumerate(auth_models):
        row_fill = row_even if i % 2 == 0 else row_odd
        draw.rectangle([table_left, y, table_right, y + 38], fill=row_fill)
        draw.text((table_left + 15, y + 10), mod, font=font_model, fill=model_link_color)
        
        draw.text((table_right - 140, y + 10), "+ Add", font=font_action, fill=add_color)
        draw.text((table_right - 70, y + 10), "Change", font=font_action, fill=change_color)
        y += 38
        
    y += 20
    
    # 4. Section 2: OnlineCourse
    draw.rectangle([table_left, y, table_right, y + 32], fill=section_hdr_color)
    draw.text((table_left + 15, y + 8), "ONLINECOURSE", font=font_sec, fill=section_hdr_text)
    y += 32
    
    course_models = ["Choices", "Courses", "Instructors", "Learners", "Lessons", "Questions", "Submissions"]
    for i, mod in enumerate(course_models):
        row_fill = row_even if i % 2 == 0 else row_odd
        draw.rectangle([table_left, y, table_right, y + 38], fill=row_fill)
        draw.text((table_left + 15, y + 10), mod, font=font_model, fill=model_link_color)
        
        draw.text((table_right - 140, y + 10), "+ Add", font=font_action, fill=add_color)
        draw.text((table_right - 70, y + 10), "Change", font=font_action, fill=change_color)
        y += 38
        
    # 5. Right Sidebar: Recent actions
    sy = 120
    draw.rectangle([sidebar_left, sy, sidebar_right, height - 40], fill=sidebar_bg)
    draw.text((sidebar_left + 15, sy + 15), "Recent actions", font=font_side_hdr, fill=sidebar_title)
    draw.line([sidebar_left + 15, sy + 45, sidebar_right - 15, sy + 45], fill=(60, 65, 70), width=1)
    
    draw.text((sidebar_left + 15, sy + 60), "My actions", font=font_side_sub, fill=sidebar_sub)
    draw.text((sidebar_left + 15, sy + 95), "None available", font=font_side_txt, fill=sidebar_text)
    
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

create_admin_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/screenshots/03-admin-site.png")
create_admin_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/onlinecourse_app/03-admin-site.png")
