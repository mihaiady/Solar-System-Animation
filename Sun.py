class Sun:
    def __init__(self, canvas, xCenter, yCenter, image, anchor):
        canvas.create_image(
            xCenter - image.width() / 2,
            yCenter - image.height() / 2,
            image=image,
            anchor=anchor,
        )
