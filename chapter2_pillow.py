from PIL import Image, ImageFilter

def main():
    # Load the image
    try:
        image = Image.open('example.jpeg')
        print("✅ Image successfully loaded.")
    except Exception as e:
        print(f"❌ An error occurred while opening the image: {e}")
        return

    # Save the image
    try:
        image.save('result.jpg')
        print("✅ Image successfully saved as result.jpg.")
    except Exception as e:
        print(f"❌ An error occurred while saving the image: {e}")
        return

    # Crop the image
    try:
        cropped_image = image.crop((10, 10, 200, 200))
        cropped_image.save('cropped_result.jpg')
        print("✅ Image successfully cropped and saved as cropped_result.jpg.")
    except Exception as e:
        print(f"❌ An error occurred while cropping the image: {e}")
        return

    # Resize the image
    try:
        resized_image = cropped_image.resize((100, 100))
        resized_image.save('resized_result.jpg')
        print("✅ Image successfully resized and saved as resized_result.jpg.")
    except Exception as e:
        print(f"❌ An error occurred while resizing the image: {e}")
        return

    # Filter the image
    try:
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image.save('filtered_result.jpg')
        print("✅ Image successfully filtered and saved as filtered_result.jpg.")
    except Exception as e:
        print(f"❌ An error occurred while filtering the image: {e}")

if __name__ == "__main__":
    main()