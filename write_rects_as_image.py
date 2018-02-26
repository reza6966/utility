def write_rects_as_image(img, rect_list, out_dir, prefix="", word_indices=[]):
    """
    Writes rectangle areas listed in rect_list as a new image.
    :param img: the main image that rectangle areas are extracted from it.
    :param rect_list: list of rectangle areas that must be extracted from img.
    :param out_dir: the path of writing the extracted rectangle images.
    :param prefix: the prefix name of extracted rectangle images.
    :param word_indices: list of word indices of subwords rectangles passed to the function as rect_list.
            If the word_indices be empty, no another extra prefix will be added to the
            extracted rectangle image file name.
    :return:
    """
    counter = 0
    word_index_str = ''
    for rect in rect_list:
        temp_img = img[rect[1]:rect[3], rect[0]:rect[2]]

        if word_indices.__len__() != 0:
            word_index_str = str(word_indices[counter]) + '.'

        cv2.imwrite(
            out_dir + prefix + word_index_str + str(rect[0]) + "." + str(rect[1]) + "." + str(rect[2]) + "." + str(
                rect[3]) + ".jpg",
            temp_img)
        counter = counter + 1
