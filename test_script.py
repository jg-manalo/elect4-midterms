import os
import cv2

def test_outputs_exist():
    """Check if the output folder contains files."""
    output_files = [f for f in os.listdir('output') if not f.startswith('.')]
    assert len(output_files) > 0, "Test Failed: No images were generated in output folder."
    print("Test Passed: Output files found.")

def test_image_validity():
    """Check if the generated files are actually readable images."""
    for filename in os.listdir('output'):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = cv2.imread(os.path.join('output', filename))
            assert img is not None, f"Test Failed: {filename} is corrupted."
    print("Test Passed: All output images are valid.")

if __name__ == "__main__":
    test_outputs_exist()
    test_image_validity()
