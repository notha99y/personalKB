from pathlib import Path

import click
import cv2

cropping = False
reference_pts = []


def click_and_crop(event, x, y, flag, image):
    global reference_pts, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        reference_pts = [(x, y)]
        cropping = True
        print(cropping)

    elif event == cv2.EVENT_MOUSEMOVE:
        # user is moving the mouse within the window
        if cropping:
            # if we're in drawing mode, we'll draw a green rectangle
            # from the starting x,y coords to our current coords
            image_copy = image.copy()
            cv2.rectangle(image_copy, reference_pts[0], (x, y), (0, 255, 0), 2)

            cv2.imshow("Cropping", image_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        reference_pts.append((x, y))
        cropping = False
        print(cropping)
        print(len(reference_pts))


@click.command()
@click.argument("video_file", type=click.Path(exists=True))
@click.argument("save_dir")
def crop_video(video_file, save_dir):

    cap = cv2.VideoCapture(str(Path(video_file)))
    ret, image = cap.read()
    image_copy = image.copy()
    cv2.namedWindow("Cropping", cv2.WINDOW_NORMAL)
    cv2.imshow("Cropping", image)
    cv2.setMouseCallback("Cropping", click_and_crop, image)

    while cap:
        key = cv2.waitKey(0) & 0xFF
        if key == ord("q"):
            print(f"Image Cropped at {reference_pts}")
            break

    if len(reference_pts) == 2:
        roi = image_copy[
            reference_pts[0][1] : reference_pts[1][1],
            reference_pts[0][0] : reference_pts[1][0],
        ]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    cap.release()
    cap = cv2.VideoCapture(str(Path(video_file)))

    count = 0
    while cap:
        ret, image = cap.read()
        image_copy = image.copy()
        roi = image_copy[
            reference_pts[0][1] : reference_pts[1][1],
            reference_pts[0][0] : reference_pts[1][0],
        ]
        if count % 4 == 0:
            save_path = Path(save_dir) / f"img_{count}.jpg"
            cv2.imwrite(str(save_path), roi)
        cv2.imshow("ROI", roi)
        cv2.waitKey(1)
        count += 1


if __name__ == "__main__":
    # crop_video('/home/notha99y/Desktop/deploy_cv.mp4')
    crop_video()
