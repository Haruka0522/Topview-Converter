import mouse
import cv2
import argparse
import glob
import numpy as np


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", default="images", type=str,
                        help="Image / Directory containing images to convert")
    parser.add_argument("--img_size", default=(300, 600))

    return parser.parse_args()


def calc_homography(points_list, result_size):
    pts1 = np.float32(points_list)
    w, h = result_size
    pts2 = np.float32([[w, h], [w, 0], [0, 0], [0, h]])
    M = cv2.getPerspectiveTransform(pts1, pts2)

    return M


def get_mouse_points(window_name):
    points_list = list()
    mouse_data = mouse.MouseParam(window_name)
    print("click LR->TR->TL->LL")
    while len(points_list) < 4:
        cv2.waitKey(100)  # chattering eliminator
        if mouse_data.get_event() == cv2.EVENT_LBUTTONDOWN:
            xy = mouse_data.get_xy()
            if xy not in points_list:
                points_list.append(xy)
                print(xy)

    return points_list


if __name__ == "__main__":
    options = get_options()
    result_size = options.img_size

    # input images
    dir_path = options.images
    if dir_path[-4:] in [".png", ".jpg"]:
        files_list = [dir_path, ]
    else:
        files_list = glob.glob("{}/*.*".format(dir_path))

    for idx, image_path in enumerate(files_list):
        window_name = "image {}".format(idx)
        image = cv2.imread(image_path)
        row, col = image.shape[:2]
        image = cv2.resize(image, (int(row*0.5), int(col*0.5)))
        cv2.imshow(window_name, image)
        points_list = list(get_mouse_points(window_name))
        cv2.destroyAllWindows()

        # transform matrix
        M = calc_homography(points_list, result_size)

        result = cv2.warpPerspective(image, M, result_size)

        cv2.imwrite("{}.jpg".format(idx), result)
