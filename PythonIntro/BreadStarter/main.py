import os
from bread import readImage, outputGrid, firstPass, secondPass, thirdPass


def main():
    # file_path = input("Enter the path to the image file: ")
    # while not os.path.exists(file_path):
    #     print("File not found. Please try again.")
    #     file_path = input("Enter the path to the image file: ")

    grid = readImage("PythonIntro/BreadStarter/SimpleImage.txt")
    print("Initial Image:")
    outputGrid(grid)

    labeled_grid, label_relationships = firstPass(grid)
    print("\nAfter First Pass (Labeled Image):")
    outputGrid(labeled_grid)

    unified_grid = secondPass(labeled_grid, label_relationships)
    print("\nAfter Second Pass (Unified Labels):")
    outputGrid(unified_grid)

    object_count = thirdPass(unified_grid)
    print(f"\nNumber of unique objects: {object_count}")

    print("\nLabel Relationships:")
    print(label_relationships)


if __name__ == "__main__":
    main()
