from PIL import Image

#NEED TO USE VECTOR OPPORATIONS INSTEAD OF FOR LOOPS
def crop(img):
    pix = img.load()
    width, height = img.size

#FIND TOP AND BOTTOM
    rowSums = []
    for i in range(0, height):
        currRowSum = 0
        for j in range(0, width):
            currRowSum += pix[j, i]
        rowSums.append(currRowSum)

    row_middle_val = rowSums[height//2]
    y_lowest_range = row_middle_val - (row_middle_val * .2)
    print(y_lowest_range)
    #loop through list of sums and find where the difference changes
    for i in range(0, len(rowSums)):
        if rowSums[i] >= y_lowest_range:
            y_top = i
            break
    for i in range(len(rowSums)//2, len(rowSums)):  #start halfway though
        if rowSums[i] <= y_lowest_range:
            y_bot = i
            break

    #FIND LEFT AND RIGHT
    colSums = []
    for i in range(0, width):
        currColSum = 0
        for j in range(0, height):
            currColSum += pix[i, j]
        colSums.append(currColSum)

    col_middle_val = colSums[width // 2]
    x_lowest_range = col_middle_val - (col_middle_val * .2)
    print(x_lowest_range)
    # loop through list of sums and find where the difference changes
    for i in range(0, len(colSums)):
        if colSums[i] >= x_lowest_range:
            x_left = i
            break
    for i in range(len(colSums) // 2, len(colSums)):  # start halfway though
        if colSums[i] <= x_lowest_range:
            x_right = i
            break

    #Crop to values found
    box = (x_left, y_top, x_right, y_bot)
    new_img = img.crop(box)

    return new_img
