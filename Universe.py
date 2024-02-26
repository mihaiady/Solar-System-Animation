class Universe:
    def __init__(self, canvas, x, y, image, anchor):
        canvas.create_image(
            x,
            y,
            image=image,
            anchor=anchor,
        )
