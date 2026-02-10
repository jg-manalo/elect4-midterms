import cv2
import numpy as np
import os

def apply_vintage(img):
    #It adds vintage effects on the image
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    vintage = cv2.transform(img, kernel)
    return np.clip(vintage, 0, 255).astype(np.uint8)

def apply_pencil_sketch(img):
    # In this process the image will be converted into a pencil sketch
    sketch_gray, _ = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return sketch_gray

def adjust_saturation(img, scale=1.5):
    #It manipulates the saturation of the image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * scale, 0, 255)
    return cv2.cvtColor(hsv.astype("uint8"), cv2.COLOR_HSV2BGR)

def inject_noise(img):
    #The output of the image will have pepper like design
    row, col, ch = img.shape
    gauss = np.random.normal(0, 30, (row, col, ch))
    noisy = img + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def motion_blur(img, kernel_size=15):
    #This process add a motion blur effect to the image
    kernel = np.zeros((kernel_size, kernel_size))
    kernel[int((kernel_size - 1)/2), :] = np.ones(kernel_size)
    kernel /= kernel_size
    return cv2.filter2D(img, -1, kernel)

def main():
    input_dir = 'input'
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Supported formats
    valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')

    # images that are inside the input dir will be processed then on saved to outout dir
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(valid_extensions):
            path = os.path.join(input_dir, filename)
            image = cv2.imread(path)

            if image is not None:
                name_only = os.path.splitext(filename)[0]

                # Vintage
                vintage_res = apply_vintage(image)
                cv2.imwrite(os.path.join(output_dir, f"{name_only}_vintage.jpg"), vintage_res)

                # Pencil Sketch
                sketch_res = apply_pencil_sketch(image)
                cv2.imwrite(os.path.join(output_dir, f"{name_only}_sketch.jpg"), sketch_res)

                # Color Saturation
                sat_res = adjust_saturation(image)
                cv2.imwrite(os.path.join(output_dir, f"{name_only}_saturated.jpg"), sat_res)

                # Noise Injection
                noise_res = inject_noise(image)
                cv2.imwrite(os.path.join(output_dir, f"{name_only}_noisy.jpg"), noise_res)

                # Motion Blur
                blur_res = motion_blur(image)
                cv2.imwrite(os.path.join(output_dir, f"{name_only}_blur.jpg"), blur_res)

                print(f" Successfully processed 5 versions of {filename}")


if __name__ == "__main__":
    main()