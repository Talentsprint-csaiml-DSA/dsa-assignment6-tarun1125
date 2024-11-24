def longest_box_sequence(boxes):
    boxes.sort(key = (lambda box: (box[0], box[1], box[2])))

    dp_array = [1] * len(boxes)

    for i in range(1,len(boxes)):
        for j in range(i):
            if (boxes[j][0] < boxes[i][0] and
                boxes[j][1] < boxes[i][1] and
                boxes[j][2] < boxes[i][2]):
                dp_array[i] = max(dp_array[i], dp_array[j] + 1)

    return max(dp_array)  
