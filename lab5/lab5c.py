from lab5b import *

def test_pixel_constraint():
    """
    Test for pixel_constraint
    """
    test_constraint = pixel_constraint(10, 250, 10, 250, 10, 250) #the constraints
    test_cases = [(10, 50, 100), (150, 249, 20), (125, 250, 150)] #our cases
    test_answers = [0, 1, 0] #correct answers

    for i in range(len(test_cases)):
        print(test_constraint(test_cases[i]))
        print(test_answers[i])


        assert test_constraint(test_cases[i]) == test_answers[i], "Not within parameters"
    print("Test succsessful")


def test_generator_from_image():
    """
    Test for generator_from_image
    """
    pixel_list = [(255, 255, 255), (0, 0, 0), (178, 229, 21)]
    test_generator = generator_from_image(pixel_list)

    for tries in range(len(pixel_list)):
        assert test_generator(tries) == pixel_list[tries], "Value, not equal"
    print("Test succsessful")


def test_combine_images():
    """
    Test for combine_images
    """
    results = [[(0, 0, 0), (100, 0, 52), (255, 255, 255)], [(255, 255, 255), (0, 13, 52), (20, 42, 99)]]

    list_src = [[(200, 254, 100), (0, 0, 0), (200, 254, 100)], [(255, 255, 255), (54, 54, 55), (255, 255, 255)]]

    list_cond = pixel_constraint(0, 210, 0, 255, 0, 110)

    list_gen1 = generator_from_image([(0, 0, 0), (0, 13, 52), (255, 255, 255)])

    list_gen2 = generator_from_image([(255, 255, 255), (100, 0, 52), (20, 42, 99)])

    for tries in range(len(list_src)):
        print(combine_images(list_src[tries], list_cond, list_gen1, list_gen2))
        assert combine_images(list_src[tries], list_cond, list_gen1, list_gen2) == results[tries], "Incorrect choice of pixels"
    print("Test succsessful")


def generator_from_image(img):
    """
    Generates the color scheme from an image, in a list format.
    """
    def getColor(i):

        try:
            return img[i]
        except IndexError:
            raise IndexError("Incorrect input parameter")
        except TypeError:
            raise TypeError("Wrong format for list")
    return getColor


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Gives us the specified input values that .
    Checks if the HSV "color" is within the given, specified input values in pixel_constraint. 
    """
    def constraint(color):
        (h,s,v) = color
        if not isinstance(color, tuple) or len(color) !=3:
            raise TypeError("Only accept tuples with 3 integers")
        
        elif h > hlow and h < hhigh and \
            s > slow and s < shigh and \
            v > vlow and v < vhigh:
            return 1
        return 0
    return constraint


def combine_images(mask_source, condition, generator1, generator2):
    """
    Uses three different images/generators and combines them depending on the given condition.
    """
    new_list = []
    mask = [condition(i) for i in mask_source]
    try:
        for index in range(len(mask)):
            if mask[index] == 1:
                new_list.append(generator1(index))
            elif mask[index] == 0:
                new_list.append(generator2(index))
            else:
                new_list.append(add_tuples( \
                    multiply_tuple(generator1(index), mask[index]), 
                    multiply_tuple(generator2(index), 1 - mask[index])))
    except (ValueError, IndexError):
        print("Error in genrator_from_image or condition")
        raise
    return new_list
    
     
