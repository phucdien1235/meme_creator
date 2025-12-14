from guizero import App, Text, TextBox, Combo, ButtonGroup, Slider, Drawing, ListBox, Box

def change_image():
    draw_image.clear()
    draw_image.image(100, 100, image = image_name.value, width = 250, height = 250)
    draw_image.text(0,0, text = what_text.value, color = what_text_color.value, font = what_text_font.value, size = what_text_size.value)
    draw_image.image(what_X.value, what_Y.value, image = f"{what_sticker.value}.png", width = 50, height = 50)
app = App(title = "Meme Creator", width = 750, height = 700)
box_change_text = Box(app, height = 200, width = 500, border = True, align = "top", layout = "grid")
box_change_text.bg = "lightblue"
Text(box_change_text, grid = [0,0], text = "Enter text: ", size = 15)
what_text = TextBox(box_change_text, grid = [1,0], width = 50, command = change_image)
Text(box_change_text, grid = [0,1], text = "Select text color: ", size = 15)
what_text_color = Combo(box_change_text, grid = [1,1], options = ["black", "red", "green", "purple"], command = change_image)
what_text_color.bg = "pink"
Text(box_change_text, grid = [0,2], text = "Select font: ", size = 15)
what_text_font = ButtonGroup(box_change_text, grid = [1,2], options = ["Arial", "Times New Roman", "Courier"], command = change_image)
what_text_font.bg = "yellow"
Text(box_change_text, grid = [0,3], text = "Select size: ", size = 15)
what_text_size = Slider(box_change_text, grid = [1,3], command = change_image, end = 50, start = 10, width = 300)
what_text_size.bg = "lightblue"
box_sticker = Box(app, height = 150, width = 400, align = "top", layout = "grid")
Text(box_sticker, text = "Select stcker: ", size = 15, grid = [0,0])
what_sticker = Combo(box_sticker, grid = [1,0], options = ["star", "oval", "square"], command = change_image)
what_sticker.bg = "orange"
Text(box_sticker, text = "X: ", size = 15, grid = [0,1])
what_X = Slider(box_sticker, grid = [1,1], width = 250, end = 400, command = change_image)
Text(box_sticker, text = "Y: ", size = 15, grid = [0,2])
what_Y = Slider(box_sticker, grid = [1,2], width = 250, end = 400, command = change_image)
box_image = Box(app, height = 350, width = 750, align = "top")
image_name = ListBox(box_image, items = ["cat.png", "bird.png", "dog.png"], selected = "cat.png", height = 300, width = 300, align = "left", command = change_image)
image_name.bg = "lightyellow"
draw_image = Drawing(box_image, height = 350, width = 450)
draw_image.bg = "lightblue"
draw_image.image(100, 100, image = image_name.value, width = 250, height = 250)
draw_image.text(0,0, text = "", color = what_text_color.value, font = what_text_font.value, size = what_text_size.value)
draw_image.image(what_X.value, what_Y.value, image = f"{what_sticker.value}.png", width = 50, height = 50)

app.display()
