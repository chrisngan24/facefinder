import facefinder
import image_processing

if __name__ == '__main__':
    path = 'data/in'
    facefinder.find_and_process_faces(
            path, 
            'data/out',
            processors=[
                ('cell shading', image_processing.cell_shade)
                ]
            )
