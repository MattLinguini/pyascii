from PIL import Image, ImageColor

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

def create_pixel_matrix(image, width, height):
    image.thumbnail((width, height))
    # Gets the flat RGB data of the imag
    pixel_matrix = list(image.getdata())
    # Creates a new 2D array containing the RBG data of the image
    return [pixel_matrix[i:i+image.height] for i in range(0, len(pixel_matrix), image.width)]

def create_intensity_matrix(pixel_matrix):
    intensity_matrix = []
    for x in pixel_matrix:
        row = []
        for pixel in x:
            p_intensity = ((pixel[0] + pixel[1] + pixel[2]) / 3)
            row.append(p_intensity)
        intensity_matrix.append(row)
    return intensity_matrix

def convert_to_ascii(intensity_matrix):
    ascii_matrix = []
    for x in intensity_matrix:
        row = []
        for pixel in x:
            row.append(ASCII_CHARS[int(pixel/255 * len(ASCII_CHARS)) - 1])
        ascii_matrix.append(row)
    return ascii_matrix

def print_ascii_matrix(ascii_matrix):
    for x in ascii_matrix:
        # Repeat pixel 3 times to compensate for stretching 
        line = [pixel+pixel+pixel for pixel in x]
        print("".join(line))
    




def main():
    print('''
              ___   _____ _____ _____ _____ 
             / _ \ /  ___/  __ \_   _|_   _|
 _ __  _   _/ /_\ \\ `--.| /  \/ | |   | |  
| '_ \| | | |  _  | `--. \ |     | |   | |  
| |_) | |_| | | | |/\__/ / \__/\_| |_ _| |_ 
| .__/ \__, \_| |_/\____/ \____/\___/ \___/ 
| |     __/ |                               
|_|    |___/                                

Version: 1.0
Author: Matt Bennett

[i] Convert an image
[q] Quit
    ''')
    user_input = ''
    while user_input != 'q':
        user_input = input('Enter an option: ')
        # Image Conversion
        if user_input == 'i':
            image_input = input('Name of image: ')
            image = Image.open('images/' + image_input)
            width = ''
            height = ''
            while not width.isdigit():
                width = input('Desired Width: ')
            while not height.isdigit():
                height = input('Desired Height: ')
        
            p_matrix = create_pixel_matrix(image, int(width), int(height))
            i_matrix = create_intensity_matrix(p_matrix)
            a_matrix = convert_to_ascii(i_matrix)
            print_ascii_matrix(a_matrix)

        

if __name__ == '__main__':
    main()