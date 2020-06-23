
def personal_meme(value):
    if 0 <= value <= 20:
        return  '/static/images/happycat.jpeg'
    elif 21 <= value <=40:
        return '/static/images/gooddaycat.jpg'
    elif 41 <= value <=60:
        return '/static/images/mehcat.jpg'
    elif 61 <= value <=80:
        return '/static/images/donecat.jpg'
    elif 81 <= value <=100:
        return '/static/images/angrycat.jpg'
