import facefinder
import util

def find_and_process_faces(
        input_dir, 
        output_dir,
        ):
    """
    Given the input path, find faces and write to the output path
    """

    for image_file in util.next_file(input_dir, '.jpg'):
        print image_file
        rects, img =  facefinder.detect(image_file)
        # drop the file name extenion
        file_name = util.file_name_from_path(image_file).split('.')[0]
        output_file = output_dir + '/' + file_name 
        facefinder.crop(rects,img,output_file)
        print len(rects)


