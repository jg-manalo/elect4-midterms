import cv2
import numpy as np
import os

def apply_vintage(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    vintage = cv2.transform(img, kernel)
    return np.clip(vintage, 0, 255).astype(np.uint8)

def main():
    input_dir = 'input'
    output_dir = 'output'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # images that are inside the input dir will be processed then on saved to outout dir
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(input_dir, filename)
            image = cv2.imread(path)
            
            if image is not None:
                # the image will have vintage filter effect applied to it
                processed = apply_vintage(image)
                output_path = os.path.join(output_dir, f"processed_{filename}")
                cv2.imwrite(output_path, processed)
                print(f"Successfully processed {filename}")

if __name__ == "__main__":
    main()