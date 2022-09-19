typedef struct rectangle {
    float height, width;
} Rectangle;


float area(Rectangle rectangle) {
    return rectangle.height * rectangle.width;
}